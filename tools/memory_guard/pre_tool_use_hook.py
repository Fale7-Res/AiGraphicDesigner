#!/usr/bin/env python3
"""Antigravity PreToolUse Hook: Gates sensitive owner-only approval/acknowledgment commands."""
import json
import sys


def main() -> None:
    """Inspect run_command tool calls and require explicit user confirmation on owner-only gates."""
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        payload = {}
    tool_call = payload.get("toolCall", {})
    args = tool_call.get("args", {})
    cmd_line = str(args.get("CommandLine") or args.get("command") or "")

    if "manage_approvals.py" in cmd_line and "authorize" in cmd_line:
        print(json.dumps({
            "decision": "force_ask",
            "reason": "Owner-only governance gate: AI agents cannot self-approve architecture transitions without explicit interactive owner authorization.",
        }, ensure_ascii=False))
        return
    if "export_updates.py" in cmd_line and "acknowledge" in cmd_line:
        print(json.dumps({
            "decision": "force_ask",
            "reason": "Owner-only review gate: AI agents cannot self-acknowledge review packages.",
        }, ensure_ascii=False))
        return

    print(json.dumps({"decision": "allow"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
