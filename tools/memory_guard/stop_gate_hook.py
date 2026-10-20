#!/usr/bin/env python3
"""Antigravity Stop Hook: Verifies External Brain & Code Mirrors are in sync before stopping."""
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def main() -> None:
    """Run verify_brain_sync.py on Stop event; force agent to continue if out of sync."""
    _ = sys.stdin.read()
    proc = subprocess.run(
        [sys.executable, str(HERE / "verify_brain_sync.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print(json.dumps({
            "decision": "continue",
            "reason": (
                "External Brain Sync Check Failed! Run `python tools/memory_guard/sync_code_mirrors.py --write` "
                "and update memory/code_mirrors/ and memory/session/ACTIVE_SESSION_WAL.md before stopping. "
                f"Details: {proc.stdout.strip()}"
            ),
        }, ensure_ascii=False))
    else:
        print(json.dumps({"decision": "allow"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
