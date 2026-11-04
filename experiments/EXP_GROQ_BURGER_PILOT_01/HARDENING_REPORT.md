<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T16:26:24Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-11-04T15:43:21Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T16:26:24Z"}
END_DOC_PROVENANCE -->
# Hardened Groq pilot controls — completed offline validation

Geometry NOT_ACCEPTED. Architecture NOT_APPROVED. Real Groq performance NOT_TESTED.

## Scope and verified baseline

Local and actual remote main matched `9f298a77df991829fe5249f993faed90f1fe702c`. Prior experiment/preparation artifacts remain intact; the original reports describe their historical state. No completed baseline sessions or detector/model experiments were rerun. New synthetic sessions test only the approved control changes with existing Burger inputs, tools, fit gates and exporter. No API keys/environment secrets were inspected and no live provider calls were made.

## Implementation

`pilot_control.py` records a strict six-field observation (missing components, normalized ROI, uncertainty, chosen action, unavailable capabilities, stop reason), sanitizes credential-shaped strings and labels it UNTRUSTED_PLANNER_OBSERVATION. Unknown fields, nonfinite numbers, degenerate ROIs, duplicate JSON keys and overlong strings fail closed. All model tool proposals are validated before any edit. Observations cannot change geometry, approve previews or override guards.

An exclusive session lock and append-only hash-linked JSON state records persist identity, source and implementation pins, exact preview hash, separate per-request owner approvals, tool events, accepted/rejected actions, geometry snapshot, request/token counters and commit counts. A durable REQUEST_RESERVED record precedes transport. A crash/unknown result cannot be retried automatically: RESERVED, HALTED and stale locks require manual audit; counters are never refunded. Valid provider usage is preserved before validating observations; absent/invalid usage is marked unknown with reservation retained, not reported as zero.

Restart validates the frozen source, implementation files, accepted curves and every persisted geometry event file before transport. The unchanged engine restores accepted/pending/history/events/commit state; no reconstructive algorithm is replaced. Every attempted request retains its reservation even when invalid output halts processing. Same-session repeated call IDs are rejected. No silent tool budget refill or extra source candidate query occurs during feedback.

Each step executes exactly one request at most. Request two requires new approval binding the current identity, index=1 and exact freshly rendered preview hash. Approval for index=0 cannot authorize it, even if pixels happen to be identical. Payload image hashes must match exactly. Free-account proof is checked fresh on each live step; provider counters/cadence are restored from the durable journal. Caps remain 2 requests / 15000 reserved tokens / 512 completion tokens per request / 1024 total / 12 tools / 2 commits / 2 candidate IDs per edit / USD0.

## Actual validation and limits

14 parent adversarial tests pass. Independent QA findings/tests are preserved alongside the final report. Synthetic Burger v4 completed two steps with a new controller/engine instance between steps: 11609 reserved tokens, 100 synthetic completion tokens, 10 tool calls, two commits and 132 final paths. A second fresh replay matched the full sanitized summary, exact final geometry hash and preview PNG hash. This is control/transaction evidence, not AI performance or a new geometric completeness result. Native SVGs and preview PNGs are in each session's initial_engine folder and session root.

The v1/v2/v3 sessions and replays are preserved as superseded control evidence; v4 adds usage-first accounting, implementation pins, strict usage-field allowlisting and rejection of credential-shaped tool-call IDs. An initial fixture attempt failed before session creation because its parent directory was absent; mkdir was corrected. Parent tamper test initially changed a field to its existing value; the assertion was corrected to perform an actual edit. QA also caused corrections for duplicate-key parsing, pretransport event consistency and removal of an unmetered candidate query. No guard or geometric tolerance was weakened.

Journal hashes/locks defend against accidental corruption and cooperative duplicate processes, not a hostile filesystem owner rewriting/deleting the entire history. Owner approvals and billing proof are trusted local host attestations, not cryptographic proof of provider billing. Do not delete records/locks to restart ambiguous work. Local secret-pattern sanitization cannot prove that arbitrary free text contains no previously unknown private data; only the bounded source/geometry context is transmitted. Model response content=null during tool calling will halt as an observation-contract incompatibility, not establish bad geometry reasoning. That compatibility remains untested until an authorized live pilot.

## Owner instructions — no live authorization supplied yet

1. Revoke the exposed key in Groq Console. Set a replacement only in your local PowerShell process using a secure prompt; do not paste it into chat or a file:

```powershell
$secure = Read-Host 'Replacement Groq API key' -AsSecureString
$env:GROQ_API_KEY = [System.Net.NetworkCredential]::new('', $secure).Password
Remove-Variable secure
```

2. Review current organization model access, free-only plan/no paid fallback and available quota. Public rate tables and a working key do not prove free-only access. Keep the redacted account evidence and private proof JSON OUTSIDE the repository. The existing FreeAccountVerification fields are unchanged: verified_by=owner_console, record_sha256=SHA256 of reviewed redacted evidence, checked_at_unix=current Unix seconds, free_plan/zero_charge_verified/model_available=true, requests_remaining>=2, tokens_remaining>=15000, permitted_image_sha256 containing only exact reviewed preview hashes. Proof expires after 24h and does not override local limits. Recheck free-only status before each request. Do not create a false proof merely to satisfy the CLI.

3. Initialize a new session (local rendering only), inspect its preview and status, and send the owner GO with the exact displayed hash. Do not approve unseen pixels. The commands below use the existing isolated interpreter; no package installation is required:

```powershell
$python = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\agd-native\Scripts\python.exe'
$pilot = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_GROQ_BURGER_PILOT_01\hardened_pilot.py'
& $python $pilot init --session burger_owner_01 --identity burger_owner_01
& $python $pilot status --session burger_owner_01
# After reviewing private_sessions/burger_owner_01/preview_00.png:
& $python $pilot approve --session burger_owner_01 --identity burger_owner_01 --index 0 --sha256 '<exact-reviewed-first-hash>'
# This command remains blocked without explicit live/rotation flags, current private proof and exact image approval:
& $python $pilot step --session burger_owner_01
# ONLY after owner GO, rotated-key setup and verified free-only access:
& $python $pilot step --session burger_owner_01 --live --rotation-confirmed --account-proof 'C:\Users\Mohamed\Documents\GroqPilotPrivate\account-proof.json'
```

4. Stop after request one. Inspect newly generated preview_01.png and sanitized diagnostics. Update permitted_image_sha256 in the reviewed private proof for that exact preview; approve index=1 with its actual hash. Then, after at least61seconds and explicit owner approval, execute the same step command once. A failed/ambiguous request halts the session, not an automatic retry. Do not rerun init or invent another session to replenish budgets. Remove GROQ_API_KEY from the local process when finished. Private sessions are Git-ignored; synthetic evidence is separately versioned.

## Reproduction and decision

Run test_pilot_control.py for control tests. Run synthetic_session.py --name NEW_UNIQUE_NAME for a new synthetic two-step session using saved source/predictions. Existing output names are never overwritten. To audit a saved session without executing anything, instantiate PilotSession(path).read(); inspect the immutable record chain, observation/action records and matching event files. Resume is not inference replay: no provider call is repeated from a journal.

VERIFIED: offline control tests, synthetic restart/replay and actual SVG serialization/rendering. SUPPORTED BUT LIMITED: fail-closed controller readiness under the tested cooperative filesystem conditions. NOT ESTABLISHED: real model observation/tool compatibility, account entitlement, live planning or geometry gains. No new geometry tools, detector policies, acceptance criteria or production interfaces were added.

Recommendation: GO for owner review of the live gate; no live execution until key rotation, free-only proof and exact preview approval. Stop for owner decision. Never interpret a successful synthetic fixture as successful Groq geometry reconstruction.

## Final independent QA and current gate

Independent adversarial tests and findings are included under reports/hardening/qa. QA discovered that arbitrary extra provider usage fields could enter the journal; the final boundary now persists only three validated integer counters. The failed synthetic usage audit is preserved with the passing rerun. Valid usage on malformed observations is retained; unknown transport usage remains explicitly unknown. No real credential appeared in this audit.

The CLI owner_review_pending_v4 session is initialized locally with zero requests, WAITING_APPROVAL. Its exact preview remains SHA256 8bbe920df13f689cd65b25ba60a3bcd1c2ad7665626e35a4c7daf3dee6fd98fa (143915 bytes). A real --live command without account proof/rotation confirmation was refused before any provider/key access; counters remained zero. No human approval was manufactured for this live-mode session. It is Git-ignored.

The current status is HARDENING_GATE.json. Earlier LIVE_GATE.json/REPORT.md are preserved historical preparation records. Use Publish-Hardening.ps1 for this checkpoint, not the earlier preparation message.

Final QA: 15 independent adversarial tests pass in addition to 14 implementation tests. The saved v4 sessions match the current implementation pin and actual SVG/preview output hashes. See reports/hardening/qa/FINAL_QA.md. The v3 mismatch is explicitly superseded, not hidden. No Groq requests or secret access occurred.

## Publication outcome — November 4, 2026

The final hardening checkpoint is UNCOMMITTED / UNPUBLISHED. One scoped staging attempt was denied creating .git/index.lock. This is a filesystem/sandbox metadata restriction, not an authentication failure. No retries or ACL changes were attempted. Starting/published main remains 9f298a77df991829fe5249f993faed90f1fe702c; no new commit SHA is claimed. The scoped publisher CheckOnly passed. Private live sessions are Git-ignored, and the release scan found no credential-shaped values. The size-aware manifest includes approximately26MB of source, tests and full synthetic journals with each file below0.4MB; no model weights/environments are included.

Owner-run publication:

```powershell
& 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\outputs\groq_burger_pilot_review\Publish-Hardening.ps1'
```

It checks the exact repository, main branch, expected GitHub origin, identities and unrelated staged files, fetches safely, stops on remote divergence, stages only experiments/EXP_GROQ_BURGER_PILOT_01, commits with [AGD-CODEX-RESEARCH] if required, pushes without force and independently verifies remote HEAD. Existing commits are never duplicated.
