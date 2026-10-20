#!/usr/bin/env python3
"""Git-free Incremental Review Update Exporter for AI Graphic Designer.

Supports: export, validate --update UPDATE-NNNN, status, acknowledge.
"""
# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED | Author: Governance maintainer
from pathlib import Path
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED
from datetime import datetime, timezone
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
UPDATES_DIR = ROOT / "updates"
BASELINES_DIR = UPDATES_DIR / "baselines"
PACKAGES_DIR = UPDATES_DIR / "packages"
LATEST_DIR = UPDATES_DIR / "latest"
STATE_FILE = BASELINES_DIR / "state.json"

EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "updates"}


def compute_sha256(file_path: Path) -> str:
    """Compute hex SHA-256 digest of a file."""
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def scan_workspace_files() -> dict[str, dict]:
    """Scan all first-party tracked files and return path -> {sha256, size}."""
    records: dict[str, dict] = {}
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts[:-1]):
            continue
        rel = p.relative_to(ROOT).as_posix()
        records[rel] = {"sha256": compute_sha256(p), "size": p.stat().st_size}
    return records


def export_package() -> dict:
    """Generate a numbered incremental update package in updates/packages/."""
    for d in [BASELINES_DIR, PACKAGES_DIR, LATEST_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    state = json.loads(STATE_FILE.read_text(encoding="utf-8")) if STATE_FILE.exists() else {
        "local_scan_baseline": None,
        "exported_update": None,
        "reviewer_acknowledged_baseline": None,
        "history": [],
    }
    next_num = len(state.get("history", [])) + 1
    update_id = f"UPDATE-{next_num:04d}"
    pkg_dir = PACKAGES_DIR / update_id
    pkg_files_dir = pkg_dir / "files"
    pkg_files_dir.mkdir(parents=True, exist_ok=True)

    current_scan = scan_workspace_files()
    for rel in current_scan:
        src = ROOT / rel
        dst = pkg_files_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    manifest = {
        "update_id": update_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_acknowledged": state.get("reviewer_acknowledged_baseline"),
        "file_count": len(current_scan),
        "files": current_scan,
    }
    (pkg_dir / "UPDATE_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    zip_path = PACKAGES_DIR / f"{update_id}.zip"
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zf:
        for f in sorted(pkg_dir.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(pkg_dir))

    latest_zip = LATEST_DIR / "AI_DESIGNER_LATEST.zip"
    shutil.copy2(zip_path, latest_zip)

    state["local_scan_baseline"] = update_id
    state["exported_update"] = update_id
    state.setdefault("history", []).append({
        "update_id": update_id,
        "generated_at": manifest["generated_at"],
        "file_count": len(current_scan),
    })
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "EXPORTED", "update_id": update_id, "zip_path": str(zip_path.relative_to(ROOT))}


def validate_package(update_id: str) -> dict:
    """Validate that all files in the numbered package match their manifest SHA-256 hashes."""
    pkg_dir = PACKAGES_DIR / update_id
    manifest_path = pkg_dir / "UPDATE_MANIFEST.json"
    if not manifest_path.exists():
        raise SystemExit(f"Missing manifest for {update_id}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mismatches: list[str] = []
    for rel, info in manifest.get("files", {}).items():
        copied = pkg_dir / "files" / rel
        if not copied.exists() or compute_sha256(copied) != info["sha256"]:
            mismatches.append(rel)
    return {"status": "VALID" if not mismatches else "INVALID", "update_id": update_id, "mismatches": mismatches}


def acknowledge_package(update_id: str, reviewer: str, note: str) -> dict:
    """Record explicit user-confirmed reviewer acknowledgment."""
    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    state["reviewer_acknowledged_baseline"] = {
        "update_id": update_id,
        "acknowledged_by": reviewer,
        "note": note,
        "acknowledged_at": datetime.now(timezone.utc).isoformat(),
    }
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "ACKNOWLEDGED", "update_id": update_id, "by": reviewer}


def main() -> None:
    """CLI entrypoint for export_updates.py."""
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "export":
        print(json.dumps(export_package(), ensure_ascii=False))
    elif cmd == "validate":
        uid = sys.argv[sys.argv.index("--update") + 1] if "--update" in sys.argv else "UPDATE-0001"
        res = validate_package(uid)
        print(json.dumps(res, ensure_ascii=False))
        if res["status"] != "VALID":
            raise SystemExit(1)
    elif cmd == "acknowledge":
        if "--confirm-reviewed" not in sys.argv:
            raise SystemExit("Refusing automatic acknowledgment without --confirm-reviewed")
        uid = sys.argv[sys.argv.index("--update") + 1]
        by = sys.argv[sys.argv.index("--by") + 1] if "--by" in sys.argv else "Owner"
        note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else "Reviewed"
        print(json.dumps(acknowledge_package(uid, by, note), ensure_ascii=False))
    else:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8")) if STATE_FILE.exists() else {"status": "UNINITIALIZED"}
        print(json.dumps(state, ensure_ascii=False))


if __name__ == "__main__":
    main()
