<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:13:29Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:13:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:13:29Z"}
END_DOC_PROVENANCE -->
# Independent QA — exporter/discovery cycle, prereview

Reviewer: /root/export_discovery_qa. Reviewed historical raw-face report, protocol, final QA; preceding thin/isolation reports and actual geometry_eval.py, face_cycles.py, track_b.py. Read-only; no benchmark reruns or construction changes.

## Verified inherited defect

geometry_eval.svg_graph.data appends `Z` to each fitted closed chain. Region assembly removes later chains' initial `M` but retains their `Z`. SVG closepath closes to the enclosing subpath's most recent move, not the logical chain start. The command subsequently changes the active current point, so damage can propagate beyond the unintended closing edge. Native VTracer exporter and production application are not implicated by this source evidence.

## Required independent serializer checks

- Parse actual SVG command state, including move origin/current position and each implicit closing segment; inspect against independent directed chain traversal.
- Explicitly test a closed chain with noncoincident terminal endpoint (native implicit closure), embedded after an open chain and followed by another open chain; reverse this closed occurrence as well.
- Preserve reversed cubic control order, open-chain behavior, sharp corners, evenodd compound contour/hole parity and shared incidence.
- Avoid comparing only one foreground mask: per-label output and geometric segment state must agree. A palette or opacity collision can hide ownership changes.
- Compare old/corrected serializer only with identical graphs; compare O/R only after expected renderer-equivalence gate passes. Serialize historical graphs into new directories; never overwrite original evidence.

## Matched safe-fitting review

Track B inputs must differ only in face-walk decomposition; constants and actual safety guards must remain unchanged. Eligibility counts can change because newly separated cycles become independent targets. Report original and decomposed ring denominators together, and distinguish new accepted chain IDs from changes in counting. Repaired signed area is not silhouette improvement. No invalid surrounding-face or crossing guard may be weakened to obtain acceptance.

## Discovery review

Constructor must consume source RGB/alpha and uniform fixed parameters without case-specific ROI, evaluator guide, truth mask or known-vector geometry. A stronger method must output actual curves/strokes/regions, not merely edge maps. New evidence near source contrast is not proof of physical boundary or crown recovery. Keep integration status separate from proposal plausibility, and report false details, junction/width failures, shading ambiguity and inherited microgeometry explicitly.

This prereview is not final correctness certification, accepted geometry or publication confirmation.
