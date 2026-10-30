<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T15:21:31Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T15:21:31Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T15:21:31Z"}
END_DOC_PROVENANCE -->
<!-- DOC_PROVENANCE {"created_at_utc":"2026-10-30T08:38:16Z","last_edited_at_utc":"2026-10-30T08:38:16Z","tracking_started_at_utc":"2026-10-30T08:38:16Z","last_action":"CREATED","last_change_id":"AGD-CONTOUR-QA-PREFLIGHT","last_editor":"contour_qa"} -->
# Independent preflight QA

Reviewer: contour_qa. Read full owner vision, AGENTS, prior ML study REPORT/QA_FINAL, complete construct_geometry.py and stable_fit.py. No features, detector predictions, reference data or construction outputs changed by reviewer.

## Frozen source and loss accounting requirements

1. Reuse all eighteen original construction.json trace lists by trace_id and point coordinates. Do not retrace skeletons or alter hysteresis. Retain hashes of source predictions, discovery.npz, construction.json, fitter and corrected exporter. File-routing case names are admissible; geometric answer coordinates are not.
2. Raw edge occurrences define the conservation unit. For each original trace, segment intervals must cover every consecutive source edge exactly once, either accepted, rejected or explicitly budget-skipped. Split endpoints may be repeated, edge spans may not. Arc-length totals must match within numerical tolerance; rounded display lengths are insufficient evidence.
3. For cyclic source traces, preserve the original closing edge. Do not synthesize an extra zero-length edge or classify open contours as closed. A split cyclic path remains a loop only if every interval is retained, joins close exactly, and no topology conflict is present. Open strokes do not establish filled components, counters, regions or holes.
4. Record source length, selection status, partition boundaries/reasons, fit invocation, refinement counts, cubic counts, deviation, acceptance/rejection and all unattempted-budget reasons. Every trace must appear, including <6px and beyond rank128.

## Expected mechanisms and caveats

Old losses include minimum6px, top128, 64cubics per trace, <=8 refinement rounds and whole-chain rejection. The inherited fitter uses open approxPolyDP and endpoint handles even for closed loops. Its acceptance checks deviation; is_simple is only diagnostic. A good fit score therefore does not imply topology safety.

Comparing new versus old changes construction capacity/partition policy as approved, not detection. Report added compute/cubics and whether recovered evidence was excluded by budget versus rejected by deviation. Do not claim restored structure where mere extra false-positive texture/reflection strokes were retained.

## Safety assertions to freeze

- Finite controls; exact fixed source endpoints at segment joins; closed-loop endpoint equality; no independently shifted source coordinate systems.
- Symmetric measured deviation remains <=0.6px including flatten/sample numerical envelope. Threshold never relaxed. Report numerical rather than exact certification.
- Detect duplicates in undirected source edge occurrence coverage and fitted curve geometric proximity. Distinguish intended shared endpoint/junction contact from a new proper crossing.
- Intersections and adjacency are compared to the frozen source graph. Source trace indices alone do not validate intended region ownership.
- Fit corners remain explicit when source turning angle warrants it. Closure continuity may be C0 at an intentional corner; do not force global smoothness.
- Do not preserve every source-grid turn as a cubic. Record short curve/path scales, integer alignment, axis-aligned/staircase length and added complexity; no raster/image/rect fallback.
- Independent evaluator masks/guides may score saved outputs only; no evaluator imports/ROI-driven construction or thresholds selected after results.
- Known K01 loops receive separate closure and hole-relation diagnostics; open-stroke boundary recall is not hole correctness.
- Process-tree monitoring must be tested with a child allocating memory. Summed RSS is sampled shared-page-inclusive process RSS, not an exact unique or instantaneous peak.

## Claim boundaries

Shield guides have1.2–2px uncertainty and cannot certify strict1px crown reconstruction. Arabic threshold references are raster proxies. Fine Features derivatives remain owner-local pending rights clarification. Raw/fitted drawings and per-component support must remain visible even if all numerical checks improve. Geometry NOT_ACCEPTED; architecture NOT_APPROVED.
