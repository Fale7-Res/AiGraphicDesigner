<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T06:53:54Z", "last_action": "CREATED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:53:54Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:53:54Z"}
END_DOC_PROVENANCE -->
# Code Change Regions & Documentation Provenance (Mandatory)

**Scope:** Every newly created or edited first-party source-code region and every human-maintained Markdown document. This policy is part of the AI Graphic Designer governance system; it does not imply any prior project history.

## 1. Source code: START / END for every logical change region

- Before writing a new logical block (function, class, substantial calculation, interface, bug fix, or coherent edit), put a language-appropriate **comment immediately above the changed region** and a matching **comment immediately after it**. This applies to additions *and* edits. Do not pepper each statement with markers. Instead, use the smallest complete coherent change. The marker boundaries may surround entire functions where that is the narrowest safe unit.
- Record the real time of the edit in UTC ISO-8601 (`YYYY-MM-DDTHH:MM:SSZ`). Never invent an earlier original creation time for existing code. Use `CREATED` for new code; `EDITED` for existing code changed now. Keep prior change markers only when they still correctly identify preserved regions; archive/historize old records if replacing them.
- Every marker must contain an actual task/change ID and responsible agent ID. If no task exists, create an authorized task entry first. An edit by a subagent must cite its parent task and owning agent in a matching task/commit handoff. The code comment cannot be used as a substitute for Git history and review evidence.
- Example, Python:

```python
# START CHANGE TASK-0042 | 2026-10-17T07:20:30Z | CREATED | Author: vector-and-typography-agent
def compose_group(children):
    return list(children)
# END CHANGE TASK-0042 | 2026-10-17T07:20:30Z | CREATED
```

- Example, TypeScript:

```ts
// START CHANGE TASK-0043 | 2026-10-17T07:22:11Z | EDITED | Author: fullstack-canvas-agent
export function mapLayerIds(ids: string[]): string[] {
  return [...ids];
}
// END CHANGE TASK-0043 | 2026-10-17T07:22:11Z | EDITED
```

- For JSX, CSS, HTML, SVG, JSON, SQL, or generated files, choose the **language's valid comment format** and do not invalidate parsers. JSON does not support comments: use a versioned sidecar change record and Git diff instead of inserting invalid JSON comments. Never write comments inside immutable snapshots, hashes, source vision, lockfiles, or third-party/generated code.
- When editing a long-lived function, record the new edit in its smallest safe enclosing scope. `Start` and `End` record the time of the **change**, not the claimed authorship of unchanged legacy code. No nested/overlapping confusing markers unless supported explicitly; prefer adjacent segments.
- Check matching ID, UTC time, CREATED/EDITED status and ordering using `python tools/governance/change_tracking.py verify`. It checks marker structure but **does not prove** every changed line is covered; independent Diff/PR review is mandatory for that.

## 2. Markdown docs: creation and modification tracking

- Every mutable human-authored Markdown file has a `DOC_PROVENANCE` comment containing `created_at_utc`, `last_edited_at_utc`, `tracking_started_at_utc`, `last_action` (`CREATED`, `EDITED`, `IMPORTED_LEGACY`), `last_change_id`, and `last_editor`.
- Existing documents imported into provenance use `created_at_utc: null` and `last_edited_at_utc: null` if the historical date is unverified. `tracking_started_at_utc` is **NOT** a claim about the original creation date. After an actual edit, set `last_action: EDITED` and a real timestamp.
- Append an event to `memory/DOCUMENT_PROVENANCE.json`, and update the in-document marker in the **same controlled change**. Use:
  - `python tools/governance/change_tracking.py edit-document --file docs/...md --kind EDITED --change-id TASK-0042 --editor vector-and-typography-agent`
  - `--kind CREATED` for a new document not previously recorded.
  - `python tools/governance/change_tracking.py verify` before delivery.
- `DOC_PROVENANCE` is metadata rather than visible content. Preserve document headings, YAML frontmatter, and original prose. Historical append-only WAL, derived code mirrors, generated indexes, historical promotion snapshots, and the owner verbatim vision have their **own provenance**. Never inject annotations into immutable owner content or generated sources.
- If a mutable Markdown file is also a promoted Findings target, use `manage_findings.py record-doc-revision` (or verified supersession) before closing the task. A document header alone does not authorize changing approved promoted text.
- When the user asks which data was last created or edited, read these records, verify the change ID against the task ledger/Git revision, and distinguish imported historical unknowns from verified timestamps.

## 3. Integration / QA requirements

1. The owner and parent agent may approve task scope; subagents may capture evidence but must not self-approve reserved decisions.
2. Before editing code, search `memory/FUNCTION_REGISTRY.md`, existing interfaces, callers, and tests. Do not add duplicate behavior merely because its old name differs.
3. Put markers in the actual source, not only the Markdown code mirror; regenerate mirrors and catalog after source changes.
4. Refresh human-document provenance after every intentional Markdown edit, then verify with the change tracker. Don't modify generated indexes manually.
5. Run: `python tools/memory_guard/sync_rules.py --write`, `python tools/memory_guard/sync_code_mirrors.py --write`, `python tools/project_catalog/build_catalog.py --write`, `python tools/governance/change_tracking.py verify`, `python tools/memory_guard/verify_brain_sync.py`, `python tools/project_catalog/verify_catalog.py`, and relevant tests.
6. Provenance timestamps are evidence for traceability, not a cryptographic proof that a human edited the content. For tamper resistance use Git commits, reviews, branch protection, and ideally external signed approvals.

## 4. Platform & permission limitations

- `tools/findings_guard/file_lock.py` uses POSIX `flock` or Windows `msvcrt.locking` to serialize cooperative commands; it cannot defend against a process intentionally bypassing the CLI. Always test native Windows locking and actual Antigravity Hook loading before claiming full Windows integration.
- In `.agents/hooks.json`, `python` must resolve to Python 3 with project prerequisites installed. On Windows, validate `python --version` and, if missing, configure an actual interpreter path or supported launcher (`py -3`) locally; do not silently assume `python3` exists.
- Owner approval cannot be cryptographically established by `--confirm-owner-authorized` or IDE hook JSON alone. When genuine owner authentication is required, use human-reviewed protected Git authorization or an external signed consent process. Current P0 is NOT_APPROVED; no agent is authorized to approve it by itself.
