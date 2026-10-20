#!/usr/bin/env python3
"""Deterministic Context Recovery Engine after Interruption or Compaction.

Reads CURRENT_TASK_CHECKPOINT.md, ACTIVE_SESSION_WAL.md, isolated subagent WALs,
subagent ownership locks, and subagent findings to build a complete recovery packet.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SESSION_DIR = ROOT / "memory" / "session"
SUBAGENT_WALS_DIR = SESSION_DIR / "subagent_wals"
FINDINGS_ENTRIES_DIR = ROOT / "memory" / "findings" / "entries"
LOCKS_PATH = ROOT / "memory" / "findings" / "subagent_ownership_locks.json"
RECOVERY_OUT = SESSION_DIR / "RECOVERY_PACKET.json"


def build_recovery_packet() -> dict:
    """Reconstruct complete session and subagent state after interruption or compaction."""
    checkpoint_path = SESSION_DIR / "CURRENT_TASK_CHECKPOINT.md"
    wal_path = SESSION_DIR / "ACTIVE_SESSION_WAL.md"
    decisions_path = ROOT / "memory" / "decisions" / "DECISION_LOG.md"

    checkpoint_text = checkpoint_path.read_text(encoding="utf-8") if checkpoint_path.exists() else ""
    wal_text = wal_path.read_text(encoding="utf-8") if wal_path.exists() else ""
    decisions_text = decisions_path.read_text(encoding="utf-8") if decisions_path.exists() else ""

    wal_entries = re.findall(r"^### `\[(WAL-[0-9]+)\]\s*—\s*([^`]+)`", wal_text, re.M)
    subagent_wals: list[dict] = []
    if SUBAGENT_WALS_DIR.exists():
        for p in sorted(SUBAGENT_WALS_DIR.glob("*.wal.md")):
            txt = p.read_text(encoding="utf-8")
            steps = re.findall(r"`\[(STEP-[0-9]+)\]`", txt)
            subagent_wals.append({
                "file": p.relative_to(ROOT).as_posix(),
                "step_count": len(steps),
                "last_step": steps[-1] if steps else None,
            })

    findings_summary: list[dict] = []
    if FINDINGS_ENTRIES_DIR.exists():
        for p in sorted(FINDINGS_ENTRIES_DIR.glob("*.json")):
            data = json.loads(p.read_text(encoding="utf-8"))
            findings_summary.append({
                "finding_id": data.get("finding_id"),
                "subagent_id": data.get("subagent_id"),
                "state": data.get("current_approval_state"),
            })

    active_locks: list[dict] = []
    if LOCKS_PATH.exists():
        ldata = json.loads(LOCKS_PATH.read_text(encoding="utf-8"))
        active_locks = [lk for lk in ldata.get("locks", []) if lk.get("status") == "ACTIVE"]

    arch_not_approved = "ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED`" in decisions_text
    packet = {
        "recovered_at": datetime.now(timezone.utc).isoformat(),
        "status": "RECOVERED_CLEAN" if (checkpoint_text and wal_text) else "INCOMPLETE_SESSION_FILES",
        "architecture_approval_status": "NOT_APPROVED" if arch_not_approved else "UNKNOWN",
        "main_wal_entry_count": len(wal_entries),
        "latest_main_wal_id": wal_entries[-1][0] if wal_entries else None,
        "isolated_subagent_wals": subagent_wals,
        "active_subagent_locks": active_locks,
        "findings": findings_summary,
    }
    if "--write" in sys.argv:
        RECOVERY_OUT.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return packet


def main() -> None:
    """CLI entrypoint for context recovery."""
    packet = build_recovery_packet()
    print(json.dumps(packet, ensure_ascii=False))
    if packet["status"] != "RECOVERED_CLEAN":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
