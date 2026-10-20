#!/usr/bin/env python3
"""Automated Rule Synchronizer (.agent_rules/ -> .agents/rules/).

Eliminates manual rule duplication by treating .agent_rules/*.md as the single
canonical authoring source and automatically generating/verifying .agents/rules/*.md.
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
CANONICAL_DIR = ROOT / ".agent_rules"
ANTIGRAVITY_DIR = ROOT / ".agents" / "rules"


def sha256_bytes(data: bytes) -> str:
    """Return hex SHA-256 of raw bytes."""
    return hashlib.sha256(data).hexdigest()


def sync_or_check(write_mode: bool) -> dict:
    """Synchronize or verify parity between .agent_rules/ and .agents/rules/."""
    ANTIGRAVITY_DIR.mkdir(parents=True, exist_ok=True)
    canonical_files = {p.name: p for p in sorted(CANONICAL_DIR.glob("*.md"))}
    target_files = {p.name: p for p in sorted(ANTIGRAVITY_DIR.glob("*.md"))}

    drifted: list[str] = []
    missing_in_target: list[str] = []
    orphan_in_target: list[str] = []

    for name, src_path in canonical_files.items():
        dst_path = ANTIGRAVITY_DIR / name
        if not dst_path.exists():
            if write_mode:
                shutil.copy2(src_path, dst_path)
            else:
                missing_in_target.append(name)
        else:
            if sha256_bytes(src_path.read_bytes()) != sha256_bytes(dst_path.read_bytes()):
                if write_mode:
                    shutil.copy2(src_path, dst_path)
                else:
                    drifted.append(name)

    for name, dst_path in target_files.items():
        if name not in canonical_files:
            if write_mode:
                dst_path.unlink()
            else:
                orphan_in_target.append(name)

    ok = not (drifted or missing_in_target or orphan_in_target)
    return {
        "status": "SYNCHRONIZED" if ok else "OUT_OF_SYNC",
        "canonical_count": len(canonical_files),
        "drifted": drifted,
        "missing_in_target": missing_in_target,
        "orphan_in_target": orphan_in_target,
        "write_mode": write_mode,
    }


def main() -> None:
    """CLI entrypoint for sync_rules.py."""
    write_mode = "--write" in sys.argv
    res = sync_or_check(write_mode=write_mode)
    print(json.dumps(res, ensure_ascii=False))
    if res["status"] != "SYNCHRONIZED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
