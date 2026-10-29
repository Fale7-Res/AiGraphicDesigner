<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:50:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Independent reference review — pre-candidate draft

Reviewed protocol, shield JSON/SVG overlay evidence, known-control manifest, real-case ROIs and REFERENCE_AUDIT.md before any benchmark candidate observations. Inspected original shield independently, then both full and crown 4× reference overlays. No engine fitting, segmentation or candidate experiment was run by QA.

## Verified coverage and integrity

- Independently verified source SHA256 and dimensions for shield, Tux, Arabic and Cat. Shield source matches `900b7ee76d9428ab30b654e584a6dd72ea924c55cc116420edfa387527a134f1`,369×249. Shield points lie within the source bounds.
- Thirteen declared critical components cover the shield exterior, metallic bevels/red interface, complete five-tip crown, two interior tips, flanks, central tip/lobes, fold and both band edges. Four negative-space valleys and major band/lobe joins are explicitly listed. Source-only overlay review found no major omitted crown component within this declared scope.
- Alignment is approximate, particularly curved valleys, central lobe transitions and the band edges; polylines visibly approximate smooth source transitions. This is adequate as a declared visual reference, not exact contour ground truth.
- References clearly identify AI authorship, no human/exact ground truth, subjective uncertainty and evaluator-only use. Known vector controls remain in their original locations; unresolved-rights fine-feature assets and their derived renders remain external. Real-case boxes explicitly do not invent precision/recall ground truth.

## Required pre-freeze clarification

`central_ornament_internal_fold` has `critical:true` but is described as an uncertain appearance edge with no outline/hole implication. The similarly appearance-derived red shading axis is excluded. Resolve this ambiguity before freezing: either retain the fold as a mandatory **visible-feature review with UNKNOWN geometric interpretation**, explicitly without requiring an added closed boundary/face, or classify it appearance-only. This is not a request to alter coordinates or thresholds based on candidates.

All thirteen critical contour uncertainties are1.2–2px, exceeding the frozen1px test tolerance. Report strict distances/matching as diagnostics, with uncertainty-band results separately. These annotations cannot certify95% precision/recall at1px or yield a complete geometry acceptance. Missing/uncertain evidence must remain UNKNOWN/INCOMPLETE; numerical proximity to an uncertain trace cannot become a PASS. Exact known controls can support their separately justified geometry gates.

Other guardrails: global boundary aggregates must deduplicate repeated full-outline/subcomponent samples; per-component presence remains mandatory. Broad fine-detail exemption boxes must not exempt every background island or grid cell within a box: exemptions need correspondence to the predeclared genuine thin feature. Feature boxes for Tux/Arabic/Cat are visual review locations, not automated component-presence proofs. No claim of independent human validation is warranted by this second AI review.

## Freeze recommendation

Recommend freezing the source-only approximate references **after the fold interpretation is recorded**, without silently loosening any quality threshold. Freeze hashes before benchmark candidates, keep engine workers free of reference/ROI inputs, and retain the evidence limitations in all final case decisions. This approves a stable evaluator reference set for the bounded diagnostic study; it does not approve source geometry, a new engine or production architecture, which remains NOT_APPROVED.
