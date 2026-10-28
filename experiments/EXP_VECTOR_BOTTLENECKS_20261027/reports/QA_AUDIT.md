<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T03:30:09Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T03:39:50Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T03:30:09Z"}
END_DOC_PROVENANCE -->
# Independent QA — vector reconstruction bottlenecks

AUDIT_RESULT: PASSED for bounded experimental execution and principal saved evidence. This is not approval of production architecture, general vector fidelity, semantic editability, typography reconstruction, Clean SVG or Magic Layers. Global architecture remains **NOT_APPROVED**.

Auditor: `/root/ablation_qa`. Verified baseline: `ec4849376f2bcc74339175e4bd991de83e7dfe0a`. Scope: isolated `EXP_VECTOR_BOTTLENECKS_20261027`; historical implementations, prior 140-candidate searches, saved appearance experiment and owner vision are preserved.

## Independent verification performed

1. Read complete owner vision and inspected baseline Git status, current experimental sources and tests. Read `bottlenecks.py`, `oracle.py`, `coverage.py`, `correct_bottlenecks.py`, `safe_monitor.py` and the dedicated test modules. No feature implementation was authored by this auditor.
2. Independently executed all 14 dedicated tests: five granularity/visibility/monitor tests, six coverage tests and three oracle tests. All passed without skips. Real renderer-dependent tests include visible versus occluded 1x1 cells, so erosion does not silently hide the microgeometry artifact.
3. Independently verified 21 granularity conditions across seven cases, including 63 B/C/D principal SVGs. Frozen source/reference/geometry/previous-result hashes, strict ordered B/C/D geometry and mask identity, gradient capacity and raster/filter/script exclusions pass. White-background SSIM and MSE independently recompute exactly from saved rasters. Seven detail128 conditions reuse prior saved fits; no historical search rerun was needed.
4. Independently verified all seven detail192 matching-paint stroke corrections. Baseline SVG hashes and corrected hashes match; deleting only the explicitly added stroke attributes gives identical SVG trees, including geometry, paint, gradients and alpha masks. Native white/black/bluegray SSIM, MSE and paired deltas independently recompute exactly. This is paint-coverage overlap, not unchanged effective painted geometry.
5. Independently verified all 816 coverage inventory hashes and the coverage dashboard's local links. Recomputed 36 control alpha-deficit counts/areas across three partition fixtures, three render scales and four paint conditions; saved metrics match. Exact shared-edge diagonal/curved partitions and real-gap/exterior negatives are retained.
6. Oracle tests verify source-geometry invariance, legal gradient capacity, actual native metrics, source hashes and fresh source-SVG renders with zero native MSE. All oracle output regions were refitted; no initialization paint fallback remains. Exact geometry is privileged diagnostic information, not an inferred reconstruction engine.
7. A separate actual child-process timeout check passed after a bounded Windows termination drain. The initial immediate check observed asynchronous child termination; the monitor now waits up to two seconds and reports unverified PIDs. This does not guarantee observation or termination of every very short-lived descendant.

## Findings and corrections

| Severity | Finding | Disposition |
|---|---|---|
| HIGH for performance interpretation | Coffee/dice already had complete fit/evaluation artifacts when historical contextual rendering and process supervision stalled. Outer timing and termination failed, including access/PID handling errors. | Recover principal results from saved valid evaluations without refitting. Preserve failures and mark those whole-case timings invalid; do not report them as algorithm cost or successful enforcement of the original wall-time guard. |
| MEDIUM | A correction dashboard label initially said D256 while the paired corrective experiment used uniform detail192. | Corrected label inspected visually: D192 stroke.25. Metrics explicitly identify baseline_detail192. Prior D128 coverage diagnostics are a separate comparison. |
| MEDIUM | Immediate process cleanup did not wait for Windows child termination. | Bounded identity-checked drain and cleanup_unverified reporting added; actual short timeout test passes. Avoid absolute cleanup guarantees. |
| Interpretation risk | Compound nonzero paths are not a general Boolean union; thresholded per-region samples are not analytic topology. | Explicitly disclosed. Actual exact-partition controls support source-over AA seams, while arbitrary real-image compound differences remain conditional. |
| Interpretation risk | Path bounding boxes can overstate invisible cells, and interior-only sampling can erase 1x1 cells. | Un-eroded crisp pixel-center ownership with source-alpha weights, assigned-area fraction and occlusion tests implemented. Masks are separated; the metric remains sampled, not exact continuous vector area. |

No unresolved blocking principal-artifact correctness defect was found. Final documentation, provenance and inventory integration should preserve these distinctions.

## Scientific conclusions supported by checked evidence

**Coverage:** exact shared boundary coordinates can still yield source-over antialiasing seams. Native diagonal and curved exact partitions have alpha deficits, whereas their known-union compound controls do not. The deliberately missing strip remains a true-gap negative. Matching-paint strokes reduce some deficits but expand exterior paint and can damage color/contour accuracy. They do not repair topology or prove crack-free interoperable SVG rendering.

**Oracle:** known source geometry materially improves the current fitter's result compared with reconstructed geometry on the two analytic controls. The remaining oracle error demonstrates restricted appearance family/optimization and rendering limitations still matter. Equally spaced stops and sample-derived radial extent do not exactly reproduce all original source gradient parameters. These findings do not permit additive percentages of error attributed to geometry, appearance or coverage.

**Granularity:** greater detail is not uniformly better. Shield SSIM peaks at detail192 before decreasing at256 despite lower MSE. Coffee has the same SSIM reversal. Cat has higher256 SSIM but worse MSE than192. The radial control deteriorates from SSIM0.913501 at128 to0.811491 at192 and0.764463 at256. All settings and metrics must remain visible; this is a frontier, not a monotonic success story.

**Correction:** uniform detail192 strokes improve several measured outputs, but Arabic white MSE increases by approximately0.449797 even while SSIM has a tiny positive delta. This is an explicit negative result. Corrected alpha is still imperfect. On opaque sources, zero new support outside source alpha says little about object silhouette accuracy because the entire source canvas is opaque.

**Visual inspection:** actual cat and radial comparison sheets show more local features at higher detail but conspicuous artificial, texture-derived or shading-contour divisions. The radial gradient develops rings and seams at higher granularities. D192 strokes reduce some seam visibility but do not recover correct continuous appearance. Textured images remain materially below the strongest saved pixel-equivalent reference. Arabic appearance remains heavily carried by the fixed source-derived alpha run mask.

## Limits and approval boundary

- Five reused real inputs and two existing analytic controls are a bounded diagnostic set, not new independent generalization evidence. Original high-resolution performance and other domains remain untested.
- Alpha-weighted sampled RGB microgeometry statistics do not certify coherent geometry; source-derived alpha masks remain grid dependent. Low visible microcell fraction, cubic commands and shared coordinates are individually insufficient for acceptance.
- Spatial boundary/interior error partitions describe reconstructed-region locations, not physical object ground truth or independent causes.
- One working renderer, bounded parameter configurations, restricted <=4-stop appearance models and same-image interpolation splits limit conclusions. No guarantee of globally optimal appearance or professional editability is supported.
- Whole-case performance affected by interruption/process failures is invalid for cost comparison. Valid local trace/fit/render records and newly monitored jobs should be identified separately; RSS limits are sampled soft guards.
- Historical source/owner vision preservation is checked against tracked Git state. No commit or remote publication is certified without actual Git confirmation.
- Scoped mirrors, document provenance and final packaging are the parent's final integration gate; repository-wide historical governance failures must not be called globally passing based on this research audit.

Recommendation: preserve the gradient fitter and current engine as experimental components. Evidence justifies further bounded work on coherent region discovery, appearance capacity and boundary-aware coverage, rather than adopting blanket stroke correction, universally increasing detail, or replacing VTracer outright. A materially different experiment requires the owner's next decision.


Final parent verification: added artifact-inventory missing/modified regression test; all15 tests pass (3oracle+6coverage+6parent). Independent QA reviewed report calibration and fresh-phase reuse guard fixes. No new image fitting/tracing was performed during packaging.


Final independent closure review: report calibration and bounded reproduction instructions passed; complete-oracle and coverage hash guards now verify expected cases and inventory. Four focused temporary-file guard checks passed, including tamper/outside-root rejection. No further image experiments were requested.


Final independent mirror closure: all9source hashes,51verbatimmirrorblocks and51ASTdeclarationranges match, including the unchanged oracle metadata helper hoisted from a loop. Reproduction guards resolved; no blocking findings remain. Runtime/scientific results unchanged; no image rerun requested.
