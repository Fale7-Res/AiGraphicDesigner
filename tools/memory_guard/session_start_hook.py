#!/usr/bin/env python3
"""Antigravity SessionStart Hook: Injects External Brain startup instructions."""
import json
import sys


def main() -> None:
    """Read SessionStart payload from stdin and output systemMessage reminder on stdout."""
    _ = sys.stdin.read()
    response = {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": (
                        "MANDATORY STARTUP PROTOCOL: Read memory/MEMORY_INDEX.md, "
                        "memory/session/CURRENT_TASK_CHECKPOINT.md, and memory/session/ACTIVE_SESSION_WAL.md "
                        "before executing any task. Always read source files in full (Line 1 to end) "
                        "and check memory/FUNCTION_REGISTRY.md before writing functions."
                    )
                }
            }
        ]
    }
    print(json.dumps(response, ensure_ascii=False))


if __name__ == "__main__":
    main()
