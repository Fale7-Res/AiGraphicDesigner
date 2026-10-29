<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T11:43:19Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T11:43:19Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T11:43:19Z"}
END_DOC_PROVENANCE -->
# Independent implementation review — pre-execution

Read track_a.py, track_b.py, run_study.py, study.py and all three test modules. **No critical construction-scope or reference-isolation blocker found** for the approved bounded ablation. This is permission to assess the frozen experiment scientifically, not approval of candidate geometry or architecture. QA did not run benchmark candidates or alter construction/evaluation/reference code.

## Contracts checked

- TrackA accepts RGB, positive label array and uniform config only. It imports no reference, mask, truth or case-specific geometry; candidate names enter only the outer path/manifest worker. The worker checks inherited file hashes but does not use baseline metric contents for construction.
- Skeleton endpoint connectivity is8; Dijkstra routes are explicitly4-neighbor with at most12unit steps, so the clarified arc budget holds. Tangent/width/color/corridor/background/mixture gates and deterministic proposal ordering are present. Constructor never adds an arbitrary region or cell array; accepted edits merge existing endpoint labels and add a narrow source-supported connector. New IDs are dense renumberings of memberships, not new shapes.
- Frozen worker config mapping correctly translates radius_floor to radius_floor_px and max_pair_proposals to max_endpoint_pairs. Other default algorithm constants match the frozen descriptive method. No per-benchmark hardcoded settings or reference ROI exceptions were found.
- TrackB starts saved geometry, preserving exact labels/faces/incidence/raw vertices/shared IDs/endpoints. Eligibility is exactly two orthogonal unit cracks with collapsed chord controls and an incident raw-valid degenerate ring. It proposes one fixed cubic with repeated raw bend control point, not a search or raw-grid fallback.
- Local B guards compare exact signed area/winding, affected ring validity, raw shell/hole relations, frame containment and typed pair-defect identities. Existing defects remain visible and unresolved; rejection preserves originals. Exact area helper is extracted from inherited code as a pure function; geometry evaluator imports do not load reference files in this construction path.

## Independent tests

Independently ran `python -B -m unittest discover -s <experiment> -p test*.py -v`: **13passed,0skips**, reported test time0.087s (command wall1.879s). These are abstract controls, not benchmark reruns. Controls cover supported/missing evidence, blank legitimate gap, offset/adjacent strokes, deterministic bounded proposals, unchanged input, unitL hole/T-junction preservation, new collision rejection, unsupported nonunit shape rejection, false joins/splits and empty reference rejection. Existing inherited NumPy2D-cross deprecation warnings remain; no historical helper was edited.

## Limits to preserve in results

TrackA is specifically endpoint reconnection, not arbitrary missing-boundary discovery. A wholly absent band or region cannot be recovered. Whole endpoint-label merges may connect unrelated same-colored objects; source color mixtures are heuristic, clipped Lab-line support, not physical compositing truth. Prototype averages may fail on shaded/gradient regions. The512closest-pair cap occurs before many eligibility filters and can consume budget on same-label pairs; disclose truncation rather than interpreting zero accepted proposals as universal algorithm incapability. Greedy edits use frozen source hypotheses and cannot guarantee correct topology.

TrackB only repairs eligible unitL degeneration. Area>=.1 of raw is a bounded safety criterion, not fidelity or meaningful-region correctness. Existing1px cells remain and are not promoted to professional artwork. Adaptive flattening/Shapely local guards cannot certify continuous global topology or repair unrelated invalid raw arrangements. The outer worker must enforce wall/memory budgets even if one geometry-validation call exceeds the internal elapsed-time checkpoint.

TrackA config contains frozen boolean/version descriptors whose behavior is implemented unconditionally; alternative config values should not be interpreted as supported algorithm variants. The approved frozen values match source. Runtime worker status/frozen input checks do not alone prove executable-source immutability: parent should preserve source/config hashes and PROTOCOL_FREEZE verification before execution, especially on resume. No source variation or benchmark outcomes were assumed by this review.

Per-target conditional combined scheduling remains evaluator research branching, not deployed winner selection or independent held-out generalization. Shield strict1px stays NOT_ESTABLISHED and Arabic remains a source proxy. All failures, false joins, width/coverage errors and nonimproving outputs must remain. Global architecture **NOT_APPROVED**.
