<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:52:17Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:57:50Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:52:17Z"}
END_DOC_PROVENANCE -->
# Real Groq Burger pilot — preparation and capability decision

Prepared 2026-10-31T15:47:36.113591+00:00. Geometry NOT_ACCEPTED; production architecture NOT_APPROVED.

## Verified publication and preservation

Local and remote main both verified at `eea0acc8c6b1c9f00710a24ba7165a438eab6bf1`, commit `[AGD-CODEX-RESEARCH] Evaluate restricted geometry tools replay and Groq dry-run readiness`. Working tree was clean. EXP_AI_GUIDED_GEOMETRY_01 is published in this commit. All 839 prior manifest file hashes verified. No offline session, detector or fitting experiment was rerun, and no historical output was overwritten.

## Live status: STOPPED_AT_LIVE_GATE

Actual Groq inference requests 0, image uploads 0, cost USD 0. Model decisions, accepted/rejected model edits and final AI geometry are NOT_AVAILABLE; AI performance NOT_TESTED, not FAILED/SUCCESSFUL. Prior B/M figures are deterministic/mock evidence only.

Official [vision documentation](https://console.groq.com/docs/vision) currently lists qwen/qwen3.8-27b with image input and tool use. Images count 2048 input tokens each, up to 3 per request. [Local function calling](https://console.groq.com/docs/tool-use/local-tool-calling) executes tools in the host application. [Published free limits](https://console.groq.com/docs/rate-limits) list 30 RPM / 1000 RPD / 8000 TPM / 200000 TPD, but explicitly defer exact quota to the organization's console. These statements establish public model capability, not this account's model permission, remaining quota or billing tier. No authenticated account evidence has been supplied. No exposed key was used to probe the account.

### Exact owner approvals/information required

1. Revoke the previously exposed key, install a replacement locally in GROQ_API_KEY, and confirm rotation. Do not post it in chat. A variable being present would not prove rotation; no credential value was inspected.
2. Confirm/provide redacted current Groq console evidence of Free-only plan/no paid fallback, qwen/qwen3.8-27b model access, and remaining quota sufficient for two requests / 15000 conservatively reserved tokens, paced at least 61 seconds apart. Do not include any key or payment details. A token limit or successful request is not proof of no charges.
3. Authorize transmission to Groq of the exact first contact sheet below: the published Burger raster and current geometry only. No evaluator annotations, masks, unrelated files or private Arena assets.
4. Review the newly generated second preview and approve its exact hash before request 2. The second preview cannot be named/hash-approved before request 1's edit. Current CLI has no supported step/resume with persisted budgets; first-preview approval alone is insufficient for the complete pilot. Do not silently broaden permission to all future images.
5. Confirm the matched pilot cap: two inference requests, twelve local tool calls, two commits, two candidate IDs/edit, unchanged 0.6 px gate, at most 1024 completion tokens total, 15000 reserved tokens, USD 0 maximum and no paid fallback. Stop on missing proof, quota/permission failure, invalid geometry or budget exhaustion; no automatic transport retry.

First preview: `C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01\results\A03_burger\C_dry_run_final_validation\planner_preview_02.png`

SHA256: `8bbe920df13f689cd65b25ba60a3bcd1c2ad7665626e35a4c7daf3dee6fd98fa`; 143915 bytes. The first frozen dry-run reservation was 6303 tokens; both image appearances would account for 4096 tokens, not including text/tool schemas. Costs remain zero only under verified free-only access; a local token budget cannot make a paid account free. Review [Groq data handling](https://console.groq.com/docs/your-data) before authorizing transmission: this would be cloud processing.

## Frozen proposed pilot and measurement rubric

Use original Burger A geometry and saved deterministic B, unchanged source/candidate pool, same renderer/coordinates and the common 12-call / 2-commit / 2-ID limits. B queried 16 candidates; the optional driver bootstraps 8, but both tools expose the same underlying bounded pool and eligible-first rank. Record any ROI/query differences and compare actual calls/compute, not just request count. No extra detector run or new geometry tool is allowed within the planning-effect comparison.

Request1 should identify source-visible forms and distinguish observations from uncertainty: bun outline, filling/cheese/lettuce interfaces, seeds and gaps. It should inspect current geometry and choose an admissible existing-candidate action or explicitly report an unavailable capability. No category coordinates/templates or evaluator guides are supplied.

After local execution, preserve accepted/rejected/rollback records, render the actual SVG and source overlay, report source-fit/crossing/complexity diagnostics and inspect the resulting preview. Request2 should explain which deficiency remains, interpret any rejection, choose a different useful supported action or stop/declare a capability gap. Repeating the same unavailable operation is negative planning evidence. Recognition is not credited as geometry recovery.

Score separately: (a) grounded visual observations with uncertainty; (b) useful tool selection; (c) interpretation of diagnostics; (d) recognizing capability limits; (e) actual per-component/source-supported SVG change; (f) false joins/edges and microgeometry. Two requests are feasibility evidence only; no universal claim. Source-based recall is not semantic precision and no exact Burger geometry truth is available.

### Additional pilot instrumentation gap

Current groq_pilot.py replaces assistant content with None in its next exchange and does not retain a descriptive planning/abstention record. Tool decisions are journaled, but missing logs cannot establish what the model understood. Before interpreting those questions, add a bounded, sanitized structured observation/capability-gap record (ROI, observation, uncertainty, requested capability, stop reason), treated strictly as untrusted data and never geometric truth. Also add audited single-step/resume with persisted request/tool/spending budgets so request 2 can wait for exact image approval without resetting limits. These are pilot control/observability changes, not a new geometry engine. They are proposed here; no historical driver has been silently edited.

## Capability gap and smallest useful extension order

Current tools can crop a source, query excluded trace IDs, fit/append those traces, validate counters and render/rollback. They cannot create a boundary absent from the frozen pool, move/refine accepted curves, infer missing junctions, edit region ownership or complete closed faces. The optional planner additionally exposes only get_candidates/stage_candidates/rollback_change; source inspection/rendering/validation are host operations. Calling this a professional drawing engine today would be incorrect.

|Priority|Small extension|Reuse and constraints|Independent evidence required|
|---|---|---|---|
|0|Structured planner observations + step/resume ledger|Existing provider/transaction journals; bounded text/ROI/confidence; no geometry authority; persist budgets across the approval pause|No secret/GT leakage; complete tool replies; restart does not refund budget; missing capability explicitly observable|
|1|ROI-local source-supported boundary proposals|Existing multiscale Lab evidence and curve fitter; new proposals derived from raster rather than only frozen IDs; retain confidence/rejection evidence, no model control-point emission|Recover a deliberately absent boundary on independent controls while limiting reflection/texture false positives; same policy across Burger/Arabic/logo/holdout|
|2|Network-aware contour-group assembly before per-trace filtering|Prior endpoint graph diagnostics and shared-reference integrator; short source-supported connectors become graph relationships, not pixel fallback paths|Thin connectivity/closure improves without false joins, tiny-face proliferation or corner loss. Cycle count alone cannot pass|
|3|Local accepted-curve refinement|Existing constrained refit/rollback, fixed accepted endpoints/junctions/corners and source-deviation gate; validated alternative replaces a specific curve ID transactionally|Real contour/coherence improvement, not merely fewer segments; no adjacent-region/crossing regression|
|4|Region/junction edits|Reuse atomic face traversal and corrected exporter; explicit split/merge/connect proposals with containment/ownership evidence and adjacent-face revalidation|Correct holes and shared interfaces; no silent component deletion, gap hiding or invented occlusion|
|5|Error-guided local repair orchestrator|Combine independently validated tools and local source residuals in a bounded accept/reject loop; soft-lock accepted structure|Local benefit plus preserved neighboring detail across categories; measured convergence and rollback stability|

Prior network diagnostics remain core evidence: Shield abstract cycle potential 714→2 after>=6px filtering and→0 under P selection; these are not 714 real regions. A planner cannot repair that by selecting long traces alone. Network assembly is needed, but indiscriminately restoring every short pixel edge would recreate a mosaic. ROI-local discovery and network assembly must first be tested as separate interventions before combining them. Do not couple new tools with a new planner and attribute all gains to AI.

Recommended next geometry experiment after approval: test ONE bounded ROI-local source-proposal tool, with the controller fixed and independent hidden controls for absent boundaries, thin curves and lighting false positives. Include a separate network-grouping control only if budget permits a matched ablation. Keep current source-ID planner as baseline. Do not start region editing or a universal engine rewrite in the pilot.

## Existing Burger evidence and unavailable live outputs

Original A: 128 paths / 950 cubics, source-trace recall≈0.1841. Deterministic B: 132 paths / 974 cubics, recall≈0.1860. Both yield 18 evaluator atomic faces; the small support gain does not establish complete buns/fillings/lettuce/cheese or semantic regions. These already-published outputs remain the comparison controls; they were not rerun.

Original SVG: `C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01\results\A03_burger\A.svg`
Deterministic SVG: `C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01\results\A03_burger\B.svg`
Live final SVG, model decisions, live usage and accepted/rejected model edits: NOT_AVAILABLE because no live request was authorized/executed. Do not relabel B or M as a Groq result. Final live structural metrics cannot be fabricated.

## Decision

**VERIFIED:** offline package published/intact; public Groq vision/tool support; exact first preview and existing controls available.
**SUPPORTED BUT LIMITED:** transactional tools and small deterministic source-support additions work; no completed Burger geometry.
**HYPOTHESIS:** visual planning can prioritize better edits if suitable geometry operations exist.
**NOT_ESTABLISHED:** account free quota/billing, real model understanding, useful model edits, universal reconstruction or completed geometry.

GO recommendation: prepare audited observation and step/resume controls, then execute only after the owner satisfies all live gates. NO-GO now for live requests, a paid fallback, a capability upgrade hidden inside the planner comparison, or production integration. No new major geometry-tool implementation was begun. Stop at the live gate for explicit owner decisions.

## Independent QA and preparation validation

Independent preparation audit passed; live readiness remains BLOCKED. QA independently checked the exact preview hash/143915 bytes, all seven dashboard file links, absence of credential-shaped tokens in new documents, and honest NOT_TESTED labeling. No API, credential environment or offline session was accessed by QA. See reports/qa/FINAL_QA.md and GATE_AUDIT.json. The publisher -CheckOnly passed branch/remote/identity/index checks; no Git mutation was performed by that check. These document checks establish preparation integrity, not model performance or geometry acceptance.

The ROI-discovery-before-network-grouping ranking is an engineering hypothesis, not an established experimental winner. Network filtering already has direct loss evidence; ROI proposals may still retain false lighting edges or fail to integrate. Test independently before combination.

## Ending publication state

The new preparation package is UNCOMMITTED / UNPUBLISHED. One scoped git-add attempt failed creating .git/index.lock with Permission denied. This is a filesystem/sandbox metadata restriction, not an authentication failure. No retry, ACL change or bypass was attempted. Earlier EXP_AI_GUIDED_GEOMETRY_01 remains published at eea0acc8c6b1c9f00710a24ba7165a438eab6bf1.

Owner-run PowerShell command:

```powershell
& 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\outputs\groq_burger_pilot_review\Publish-Research.ps1'
```

The script verifies actual repository/main/origin and identities, rejects unrelated staged files, fetches and stops on remote divergence, stages only experiments/EXP_GROQ_BURGER_PILOT_01, commits if needed, pushes without force and verifies the remote SHA. It does not create duplicate commits. The artifact manifest lists exact scoped files and hashes.
