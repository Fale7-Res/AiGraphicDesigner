#!/usr/bin/env python3
"""Independent Working-Tree & Catalog Completeness Validator for AI Graphic Designer.

Verifies 100% first-party file coverage, zero uncataloged files, zero stale paths,
complete field presence, and valid relationship endpoints.
"""
from pathlib import Path
from datetime import date
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools" / "memory_guard"))
import verify_brain_sync as vbs

# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:54:00Z | EDITED | Author: orchestrator-planner
EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "packages", "baselines", "latest", "versions"}
VERSIONS_DIR = ROOT / "versions"
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:54:00Z | EDITED
REQUIRED_LABELS = [
    "Path",
    "Type",
    "Purpose",
    "Contents summary",
    "Why it exists",
    "Current status",
    "Source of truth / authority",
    "Update trigger",
    "Related Files",
]


# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:54:00Z | CREATED | Author: orchestrator-planner
def verify_version_catalog(version_id: str) -> list[str]:
    """Verify PROJECT_FILE_CATALOG.md for a specific version against its actual files."""
    errors: list[str] = []
    vdir = VERSIONS_DIR / version_id
    if not vdir.is_dir():
        return [f"Version directory not found: {vdir}"]

    actual_files: set[str] = set()
    for p in vdir.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(vdir).as_posix()
        if any(part in EXCLUDED_DIRS for part in p.relative_to(vdir).parts[:-1]):
            continue
        actual_files.add(rel)

    cat_path = vdir / "PROJECT_FILE_CATALOG.md"
    if not cat_path.exists():
        return [f"Missing {version_id}/PROJECT_FILE_CATALOG.md"]

    cat_text = cat_path.read_text(encoding="utf-8")
    entries = re.findall(r"^### `([^`]+)`$", cat_text, re.M)
    cataloged = set(entries)

    missing = sorted(actual_files - cataloged)
    stale = sorted(cataloged - actual_files)

    if len(entries) != len(cataloged):
        errors.append(f"Duplicate file entries in {version_id}/PROJECT_FILE_CATALOG.md")

    for chunk in re.split(r"^### `[^`]+`\s*$", cat_text, flags=re.M)[1:]:
        for label in REQUIRED_LABELS:
            if f"**{label}:**" not in chunk:
                errors.append(f"Incomplete file-entry field in {version_id} catalog: {label}")
        if "**Related Files:** No" in chunk and "**Related Files:** None currently identified." not in chunk:
            errors.append(f"Missing explicit no-relationship statement in {version_id} catalog")
        if "**Related Files:** Yes" in chunk and not re.search(r"^#### `[^`]+`", chunk, re.M):
            errors.append(f"Missing related file detail block in {version_id} catalog")

    if cat_text.count("```") % 2 != 0:
        errors.append(f"Unbalanced Markdown code fences in {version_id}/PROJECT_FILE_CATALOG.md")

    if missing:
        errors.append(f"Uncataloged files in {version_id}: {missing}")
    if stale:
        errors.append(f"Stale catalog paths in {version_id}: {stale}")

    return errors


def verify_all_version_catalogs() -> list[str]:
    """Verify all version file catalogs under versions/."""
    errors: list[str] = []
    if not VERSIONS_DIR.is_dir():
        return errors
    for vid in sorted([d.name for d in VERSIONS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]):
        errors.extend(verify_version_catalog(vid))
    return errors
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:54:00Z | CREATED


def main() -> None:
    """Validate PROJECT_FILE_CATALOG.md against the actual repository tree."""
    actual: set[str] = set()
    excluded: list[str] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        # START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED | Author: Governance maintainer
        if rel == "memory/decisions/.approval_tx_journal.json":
            continue  # transient recovery journal; never an authoritative catalog entry
        # END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED
        # START CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:35:00Z | EDITED | Author: orchestrator-planner
        if rel.startswith("tools/update_packages/registry/") or rel.startswith("exports/updates/"):
            continue  # update packaging runtime state and generated archives; not source code
        # END CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:35:00Z | EDITED
        # START CHANGE TASK-V01-PORTABILITY-01 | 2026-10-17T17:48:00Z | EDITED | Author: orchestrator-planner
        if rel.endswith((".zip", ".tar.gz", ".tar")):
            continue  # archive distributions are transport packages, not source code
        # END CHANGE TASK-V01-PORTABILITY-01 | 2026-10-17T17:48:00Z | EDITED
        if any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts[:-1]):
            excluded.append(rel)
        else:
            actual.add(rel)

    catalog_path = ROOT / "PROJECT_FILE_CATALOG.md"
    catalog_text = catalog_path.read_text(encoding="utf-8") if catalog_path.exists() else ""
    entries = re.findall(r"^### `([^`]+)`$", catalog_text, re.M)
    cataloged = set(entries)

    missing = sorted(actual - cataloged)
    stale = sorted(cataloged - actual)
    errors: list[str] = []
    errors.extend(vbs.verify_owner_approval_provenance())
    # START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED | Author: Governance maintainer
    errors.extend(vbs.ct.verify())
    # END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED

    # START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:54:00Z | EDITED | Author: orchestrator-planner
    version_arg = None
    for idx, arg in enumerate(sys.argv):
        if arg == "--version" and idx + 1 < len(sys.argv):
            version_arg = sys.argv[idx + 1]

    if version_arg:
        errors.extend(verify_version_catalog(version_arg))
    else:
        errors.extend(verify_all_version_catalogs())
    # END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:54:00Z | EDITED

    if len(entries) != len(cataloged):
        errors.append("Duplicate file entries in PROJECT_FILE_CATALOG.md")

    metadata_path = HERE / "file_metadata.json"
    edges_path = HERE / "relationships.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.exists() else {}
    edges = json.loads(edges_path.read_text(encoding="utf-8")) if edges_path.exists() else []

    if set(metadata) != actual:
        errors.append("file_metadata.json path set differs from actual first-party tree")

    for e in edges:
        if e.get("source") not in actual or e.get("target") not in actual:
            errors.append(f"Stale relationship endpoint: {e}")
        for key in ["relationship", "direction", "change_impact", "evidence"]:
            if not e.get(key):
                errors.append(f"Missing relationship attribute {key} in {e}")

    for chunk in re.split(r"^### `[^`]+`\s*$", catalog_text, flags=re.M)[1:]:
        for label in REQUIRED_LABELS:
            if f"**{label}:**" not in chunk:
                errors.append(f"Incomplete file-entry field: {label}")
        if "**Related Files:** No" in chunk and "**Related Files:** None currently identified." not in chunk:
            errors.append("Missing explicit no-relationship statement")
        if "**Related Files:** Yes" in chunk and not re.search(r"^#### `[^`]+`", chunk, re.M):
            errors.append("Missing related file detail block")

    if catalog_text.count("```") % 2 != 0:
        errors.append("Unbalanced Markdown code fences in PROJECT_FILE_CATALOG.md")

    if missing:
        errors.append(f"Uncataloged first-party files: {missing}")
    if stale:
        errors.append(f"Stale catalog file paths: {stale}")

    result = {
        "date": date.today().isoformat(),
        "total_first_party_files_discovered": len(actual),
        "total_files_cataloged": len(cataloged),
        "uncataloged_files": missing,
        "stale_catalog_paths": stale,
        "excluded_count": len(excluded),
        "catalog_coverage_percentage": round(100 * len(actual & cataloged) / len(actual), 6) if actual else 100.0,
        "relationship_count": len(edges),
        "errors": errors,
    }
    (HERE / "validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
