<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:50:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Independent source/interface review — initialization isolation

Read `isolation.py`, `run_matrix.py`, `geometry_eval.py`, `test_isolation.py` and adapter Rust source. No benchmark candidates, engine calls or construction/evaluation changes were performed by QA. References frozen separately; architecture NOT_APPROVED.

## Findings requiring resolution or explicit restriction

1. **Graph construction is part of the initializer condition.** Arena uses its legacy crack builder/face walker; the Rust comparator uses VTracer graph extraction plus a newly authored right-turn walker and8-connected patch grouping. Identical labels and reversed shared references do not alone establish equivalent faces. Verify exact canonical raw unit edges and raw face-fill recovery of input labels for both implementations, including checkerboards, same-label disconnected islands, holes, frame touches and narrow pinches. If graph semantics differ, report combined graph-construction/initialization effects rather than an isolated spline-fitter effect. Adapter validation checks raw edge coverage/adjacency, which is valuable; its unit tests currently check incidence rather than full face raster equivalence.

2. **Current evaluator is diagnostic, not the complete frozen topology gate.** `ring_points` measures gaps but unconditionally drops each subsequent chain's first point; Shapely then implicitly closes a ring. Polygon metrics can therefore incorporate an artificial bridge when endpoints disagree. `geometry_acceptance` omits the measured max gap and self-intersecting-chain count. Pair checks exclude frame chains, and `touches` can include endpoint-to-interior contacts that may be unintended. Ring validity does not establish correct shell/hole containment, face coverage or nonoverlap. No candidate can receive complete PASS in this version, but obvious invalidity could be labeled merely NOT_ESTABLISHED. Retain explicit unresolved/failed categories and do not claim full topology certification.

3. **Resume guards trust existence.** Driver skips saved segment/fit files without validating frozen input, adapter/source hashes, completion and provenance. A partially written or adapter-output target from an interrupted run can bypass normal validation/label echo processing. Arena fit records label hash but not the exact external source hashes associated with that execution. Frozen protocol must remain unchanged, but robust reuse checks and provenance are needed before declaring reproduction reliable. No failed/reused candidate was assumed valid by this review.

4. **Budgets are not identical to execution organization.** Whole Arena batch is supervised with600s rather than one600s worker per condition; total observed CPU budget is not accumulated by this driver. End-of-stage Arena RSS is not a peak, although the outer monitor samples process-tree memory. Report these distinctions and actual termination causes, never interpret interruption as algorithmic failure without evidence.

## Measurement and test limitations

- Adaptive convex-hull cubic flattening bounds point-to-chord deviation by.01px, a sound approximation building block; double-precision polyline predicates still do not certify continuous intersections at near contacts. Explicit unresolved cases are necessary.
- `compare_samples` computes pooled bidirectional mean, weighted by sample counts, whereas Arena audit used equal mean of two directed means. They differ with unequal contour lengths; preserve both directed fields and do not compare the pooled number as the identical historical Chamfer definition.
- Ring-absolute-area microgeometry double-counts holes and is explicitly labeled diagnostic. Frozen visible-area-weighted anti-mosaic tests and1/2/4px repeated diagnostics are not implemented here. No full anti-mosaic acceptance is justified.
- Reference local-box precision includes unrelated nearby valid boundaries and is correctly disclaimed. Approximate reference bands cannot certify1px completeness. Fold gate-role fields must remain respected by any later aggregate gate rather than treating every `critical:true` as required topology.
- Test named `test_svg_preserves_shared_reversal_hole` actually constructs one outer square: it checks evenodd and raster absence, not shared reversal or a hole. Add meaningful multi-chain/reversed cubic/compound-hole export coverage before relying on its name. Export currently preserves all candidates and uses real SVG primitives; no raster embedding is introduced.
- Uniform/empty internal-boundary maps cause `np.concatenate([])` in evaluate. This is an evaluator robustness limitation for arbitrary partitions, not proof a selected benchmark fails.
- Common opaque white-composited working PNGs are fair for this bounded RGB geometry comparison only when canonical sRGB source and saved-label pixel equality are frozen and verified. This is not a continuous-alpha test. Positive labels with0exterior are appropriate; Rust accepts interior0 as outside, so wrapper rejection is important. The Rust dense-label validation checks an upper bound, not actual density/zero absence.

## Provisional disposition

Proceed only as an explicitly diagnostic matrix while preserving all outputs and validating raw graph equivalence. No complete reconstruction/production acceptance follows from the current diagnostic evaluator. Source-only references must not be imported by either construction worker; current imports/requests keep those stages separate. Await saved matrix and full evaluation before a final research claim. No engine replacement or new geometry architecture was approved by this QA review.
