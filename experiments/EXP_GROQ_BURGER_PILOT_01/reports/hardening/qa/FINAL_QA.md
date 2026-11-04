<!-- DOC_PROVENANCE
{"created_at_utc": "2026-11-04T15:42:25Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-11-04T15:43:21Z", "last_editor": "root", "tracking_started_at_utc": "2026-11-04T15:42:25Z"}
END_DOC_PROVENANCE -->
# Independent QA — hardened observation and pause/resume controls

**AUDIT_RESULT: PASSED for the tested offline control implementation and saved synthetic v4 evidence. Real Groq performance NOT_TESTED. Live authorization/account prerequisites remain outstanding. Geometry NOT_ACCEPTED. Architecture NOT_APPROVED.**

Reviewer read the complete `pilot_control.py`, `hardened_pilot.py`, synthetic fixture and parent tests, and inspected the existing reports. QA wrote independent tests and read-only saved-record audits only. No provider/network request, environment/key inspection, old benchmark rerun, or geometry feature implementation was performed. Parent separately owns final source mirrors, manifests, publication and owner gate checks.

## Independent controls

All **15 independent adversarial tests pass** on the current implementation. They verify no-approval/source mismatch rejection before transport; bool/stale image approvals; all tool proposals validated before any effect; duplicate call identities; durable ambiguous-failure reservation with no retry; restart request/token/tool persistence; exact payload-image binding; journal gaps and duplicate-key refusal; proof duplicate-key refusal; missing geometry event refusal before reservation; untrusted redacted observations; usage allowlisting and known usage retained on invalid observations; implementation drift refusal; and credential-shaped call-ID rejection without journaling the rejected identifier.

The model cannot supply host paths, approve images, reset counters, change arbitrary code, invoke Git/network/shell, or overrule geometry validation. A separate per-request local approval binds session identity, request index and exact current PNG hash. The next preview is generated locally and waits for separate approval. Restarts restore accepted geometry, pending/history/event state, commits and provider-side accounting rather than starting a fresh budget.

An exclusive lock blocks cooperating concurrent processes. Append-only records are written exclusively and fsynced before transport reservation/effects. RESERVED/HALTED/stale-lock cases do not trigger automatic retry; unknown provider completion remains ambiguous and requires manual audit. Journal integrity and implementation/source pins are checked, and persisted engine event files must match the restored snapshot before transport. Duplicate JSON keys are rejected rather than relying on last-key semantics.

These controls protect against accidental corruption, normal restart and cooperating clients. Hash chains and local OWNER_LOCAL_CLI attestations do not cryptographically authenticate the human or defeat a hostile OS user rewriting/deleting the whole history. Session limits are per-session: users must not create new sessions to replenish an ambiguous pilot's quota. Provider/account verification remains trusted host evidence backed by actual owner-reviewed console information.

## Findings corrected during review

Initial journal/proof readers accepted duplicate keys. Missing persisted engine files could also have caused a request before output failure. Both were corrected and tested. An unmetered candidate query in feedback was removed; the host now reuses bootstrapped/dispatched candidates. No geometry gate or source threshold was relaxed.

Usage initially arrived after observation parsing, losing known token usage when the observation contract failed. Usage is now validated and durably recorded before observation validation; absent/invalid usage receives an explicit unknown-usage count while its full reservation stays spent. A further test found that otherwise-valid usage dictionaries could carry unvalidated extra text into the journal. The corrected implementation persists only the three validated nonnegative integer token counts. The synthetic-only failing test output is retained as `FAILED_USAGE_AUDIT.txt`; no real credential was involved.

A credential-shaped function-call identity could bypass observation-text redaction under an injected transport. Current control rejects IDs with the provider-key prefix before storing proposals/effects. The independent test confirms the synthetic identifier never enters the journal. Strict observation fields are bounded, sanitized and marked UNTRUSTED_PLANNER_OBSERVATION; they are not evaluated geometric truth.

## Saved synthetic evidence, independently checked without replay execution

`SAVED_V4_AUDIT.json` independently verifies both existing `synthetic_two_step_v4` and `synthetic_two_step_replay_v4`:

- Eleven linked records each; two durable request reservations, two usage receipts and two separate index0/index1 approvals.
- Two synthetic requests,11609 reserved tokens,100 synthetic completion tokens, ten local tool events and two commits.
-132 final geometry paths; exact summary equality, final geometry hash `a0fb8f0fb28356f02b90c5e7f0783c352e4343959b1c51e59681e5b184442a50`, and final preview SHA256 `2e013575ff178e70a87bb2e9518189c47ec2623e7a8a4781ac041fa4c74d4b54`.
- Every saved record/hash/sequence and engine event file matches; counters do not refund between stages; each usage entry contains exactly the validated integer fields.
- Every referenced preview matches its recorded bytes. The final real SVG has132 paths and contains no image, rectangle mosaic, script or foreign object; its actual renderer PNG decodes.
- Current inspected controller/CLI/engine/partition/serializer bytes match v4's implementation pin `ee778d216cfcb87a9d88a97ec289bc805fb013fd681d1a2007fce3372b9c2c4c`.

The earlier v3 evidence is intact and internally consistent, but its aggregate implementation pin differs from current bytes after the additional call-ID guard/provenance update. It is superseded for current implementation readiness; the mismatch was explicitly reported, not silently erased. V4 is the matched current control evidence. QA did not rerun v1-v4 sessions; it only read them. The audit helper's historical filename is `audit_saved_v3.py`, but its final explicitly selected inputs and JSON output identify v4.

This exact geometry already matches the deterministic source-ID additions. It is not a model-driven improvement, a new boundary discovery result, or evidence that Burger components are complete. Synthetic planner observations are fixtures, not learned visual understanding.

## CLI/live gate and remaining limits

`init` renders locally without reading a key; `approve` only records the exact reviewed preview. CLI `step` requires explicit live and rotation-confirmation flags plus private account proof outside the repository. The existing provider adapter must independently pass fresh free-only account/model/quota/zero-charge and image-hash checks before reading GROQ_API_KEY or transmitting. No live request was executed in these tests. An initialized pending session is not live approval.

The controller now records missing components, ROI, uncertainty, chosen action, unavailable capabilities and stop reason. It still cannot turn an unsupported model request into a new geometry capability. A real tool-calling response with null assistant content will stop as an observation-contract incompatibility; synthetic tests do not prove this model will satisfy both JSON-content and tool-call requirements. Such a failure must not be labeled inferior geometric reasoning or silently bypassed.

The implementation pin covers the explicit controller/CLI/engine/partition/serializer set, not every transitive dependency or provider file. Preserve the published source/runtime manifests and revalidate them when preparing live execution. Pattern-based free-text sanitization cannot certify that arbitrary unknown private data is absent; only the bounded authorized source and geometry context should be sent.

**VERIFIED:** bounded offline restart/approval/accounting/redaction controls, preserved negative test evidence and matching saved v4 SVG/PNG/state evidence.

**SUPPORTED BUT LIMITED:** fail-closed pilot control readiness within the documented cooperative-host model.

**NOT ESTABLISHED:** free-account entitlement/quota/no-charge status, actual Groq observation/tool compatibility, real model understanding, AI geometry gains, universal reconstruction or accepted geometry.

Recommendation: preserve/publish this validated hardening checkpoint, then stop at owner review. GO for live execution only after the existing exact preview, rotated-key and independently verified free-only account prerequisites are satisfied. No production or appearance work follows from these tests.
