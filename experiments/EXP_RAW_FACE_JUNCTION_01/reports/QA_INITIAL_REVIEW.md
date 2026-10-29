<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T12:20:20Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T12:20:20Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T12:20:20Z"}
END_DOC_PROVENANCE -->
# Independent initial QA — raw face/junction representation

Reviewer: /root/raw_face_qa. This is a read-only diagnostic and protocol challenge, not constructor implementation or candidate execution.

## Verified inherited data

`inspect_baselines.py` reads the four saved `baseline.json` graphs from EXP_THIN_STRUCTURE_TOPOLOGY_01 (fine_features local-only work path), reconstructs original crack walks using inherited geometry_eval functions, and independently applies Shapely Polygon validity and exact repeated-coordinate counting. It writes `baseline_face_audit.json`.

| Case | Chains | Invalid raw walks | Walks with repeated chain endpoints | Walks with repeated points only internal to chains |
|---|---:|---:|---:|---:|
| Shield | 809 | 18 | 18 | 0 |
| Arabic | 539 | 7 | 7 | 0 |
| K01 | 93 | 0 | 0 | 0 |
| Fine | 22 | 1 | 1 | 0 |

These figures support testing repeated-endpoint walk decomposition. They do not yet establish that all invalid walks can be decomposed into valid and correctly nested faces, that existing segmentation is correct, or that visual detail improves.

## Defensible matched comparison

Split only a closed face walk at repeated chain-endpoint vertices. Retain each original directed chain occurrence exactly once for its original label. Preserve chain IDs, crack vertices, fitted segments, adjacency labels, source dimensions and segmentation labels. No make_valid/buffer/polygon union may modify construction geometry. They can only diagnose.

Compare both raw and fitted per-label evenodd fill coverage. Global foreground union equality alone can conceal a material-boundary reassignment. Prefer exact raw polygon symmetric-difference area plus independent native/zoom SVG renders. Renderer antialiasing may vary by contour grouping at point contacts; any observed difference must be reported separately from geometric equivalence.

A simple loop need not itself be an entire connected material region: a label can validly comprise multiple faces, holes, and point contacts. OGC Polygon.is_valid is not equivalent to SVG fill correctness or physical artwork topology. Independent label connectivity must distinguish 4-connected cells and 8-connected point contacts; splitting face walks is not a legitimate way to claim repaired fragmented segmentation.

## Scientific and safety challenges

1. Splitting increases ring counts and changes ring-level denominators. Report original-to-result walk mapping, per-label area, directed-edge multiset, nonzero area preserved, and chain-level crossings; do not compare raw ring counters as if objects were unchanged.
2. Self-touch validity can improve while all curves, actual SVG pixels, and critical internal detail remain unchanged. Call this representation repair, not reconstruction improvement.
3. Raw crack walks are source-grid diagnostics. Their exact SVGs must not be promoted as accepted final vector geometry or a pixel-grid fallback.
4. Apply the inherited B correction in matched original/corrected face references while preserving its thresholds and raw-chain eligibility. Decomposition may change incidence groups and therefore the number of jointly proposed cubics; expose this rather than attributing every difference solely to removal of one guard.
5. Safeguard whole-face hole relationships, not merely individual ring validity. Even valid simple loops can overlap improperly or have incorrect containment. Record winding, shell/hole parity, point-contact identities and per-label topology.
6. K01 has no raw-invalid walk and is a necessary unchanged negative control for decomposition. Fine has upstream thirteen-vs-four fragmentation, which face splitting cannot reconnect without changing fixed labels.
7. Shield uncertain AI reference cannot certify strict 1 px crown accuracy. Count no new crown component without independent spatial evidence; unchanged geometry cannot improve missing-boundary recall.
8. Exact labels/chains plus changed face walks do not remove inherited curve crossings. Verify each crossing identity and distinguish intentional common endpoints, point contacts, interior crossings and overlaps.

## Conditions for an honest conclusion

Representation hypothesis supported only if invalid raw walks become defensible simple cycles without any lost edge/area/support or mislabeled holes. Safe-fitting-unblock hypothesis supported only if matched guarded proposals are newly accepted and preserve all safety invariants. Visible geometry progress requires independent rendered contour/detail evidence beyond counters. Complete geometry remains NOT_ACCEPTED unless every inherited gate passes; production NOT_APPROVED.

Candidate protocol and outputs have not yet been supplied to QA. This review is not final artifact acceptance.
