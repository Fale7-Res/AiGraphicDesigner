<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T15:21:31Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T15:23:52Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T15:21:31Z"}
END_DOC_PROVENANCE -->
# Loss-accounted contour construction and closed-loop geometry

**Geometry NOT_ACCEPTED. Production architecture NOT_APPROVED.**

## Decision

**VERIFIED:** a large part of the previous contour loss was construction-related. Partitioning restores all selected raw contour length in 17 of 18 case/evidence sets, while preserving explicit accounting of the remainder. K01 goes from zero accepted curves to three closed contours in each evidence arm. Arabic and Fine Features gain substantial boundary support. No detection, model inference, training, source threshold or evaluator construction input changed.

**SUPPORTED BUT LIMITED:** these are meaningful contour-retention improvements, not complete professional reconstruction. The Shield crown barely improves, much detected evidence is still excluded by selection, and retained contours include lighting, texture and pixel-scale staircases. Closed contour nesting is not filled-region ownership. The periodic variant is not a consistent improvement and loses one Arabic loop.

**Next recommendation:** one controlled region/junction integration experiment, using the retained contours and the explicitly excluded short/junction traces. Test whether source-supported graph assembly and component-aware selection can recover the omitted crown/band structure without false joins, crossing conflicts or hidden grid fallback. Preserve partitioned P as the construction control; do not adopt Q globally. Include a multiscale geometric-coherence gate so retaining a raster staircase is not mistaken for a professional curve. Do not begin a new detector/model search merely to recover evidence already present but discarded by selection. Where the frozen evidence genuinely lacks a required contour, mark it unresolved and propose targeted discovery separately.

No new integration experiment is implemented here. Stop for owner review.

## 1. Baseline, scope and preservation

Starting local HEAD, tracking main and independently queried remote main all matched `3922fc393cd7fbb3675cae9cfec21d097e74fcbd`; the working tree was clean. The complete owner vision and previous report, code, QA, source predictions, SVGs and rejected traces were read/inspected. All historical files and negative evidence remain unchanged.

The authoritative vision still includes planned image generation, professional editable SVG, semantic objects, advanced Magic Layers and Arabic typography. This experiment implements none of those downstream features or final appearance. No new model, dependency, training, detector, threshold, source preprocessing or production engine was introduced.

Scope: six saved cases × three frozen evidence arms. The 18 saved stable SVGs are condition **O**, copied byte-for-byte. New conditions **P** and **Q** produce 36 matched candidates. The previous 140-search, 24-condition and pretrained-inference matrices were not rerun.

## 2. Frozen protocol and integrity

`protocol.json` pins 74 source/prediction/trace/code/reference files before candidates. The implementation agent added periodic-join diagnostic fields after the initial freeze but before any benchmark. `PRE_EXECUTION_SOURCE_FREEZE.json` explicitly records the final implementation hash and three harness/monitor hashes. The scientific constants and historical inputs did not change. QA verified the original pins with that explicit pre-execution amendment and all four final source hashes. This amendment is preserved rather than hidden.

The constructors receive only saved `source_points_xy`, fixed parameters and budgets. Case names route files; no image-specific geometry or evaluator annotations construct candidates. Original predictions and the corrected serializer remain pinned. References are read only by the separate evaluator.

The initial freeze/code checkpoint could not be published because Git metadata writes were denied. Source snapshots, protocol, logs and manifests remain local. The usage interruption occurred after the main runs; resumption did not restart them.

## 3. Loss ledger: every trace and every source edge

There are **13,094 saved traces** across the 18 evidence sets. Every trace retains its ID, old selection/rejection reason and raw edge intervals. Each source edge belongs to exactly one half-open interval `[lo, hi)`; shared anchors do not duplicate edges. Accepted plus rejected/skipped source arc length equals the original length within numerical tolerance. Post-guard vetoes update the ledger rather than silently deleting output.

Stages are separate:

1. Frozen thresholded evidence → skeleton → stored source traces.
2. Minimum-length and top-128 selection.
3. Partition fitting and deviation/complexity checks.
4. Closed-loop handling and safety guards.
5. Actual SVG serialization and rendering.

The earlier tracer omitted six isolated skeleton vertices: Shield Classical one, Astronaut Classical five. All other sets have zero untraced skeleton vertices. These zero-length omissions are recorded as stage-0 evidence losses, not fitting losses; no point geometry was invented to hide them.

The existing minimum raw length **6 px** and length-ranked **128-trace cap** remain fixed. This is scientific isolation, not an endorsement of those selection rules. Explicit CSV/JSON ledgers preserve short-chain, proposal-budget, per-trace cubic-budget, periodic-deviation and other loss reasons.

## 4. Compared methods and safety

**O — inherited stable construction:** saved outputs, no refitting. Old whole-trace capacity was 64 cubics and at most eight refinements.

**P — partitioned construction:** derive corner/curvature evidence from source-only RDP support at epsilon 0.35 px, avoiding direct use of every raster staircase turn as a corner. Partition at significant corners >=60°, accumulated turn >=35°, or before source arc length exceeds 32 px. Cuts use exact original source indices. Fit each interval with the inherited stable fitter and unchanged **0.6 px** bidirectional numerical envelope. Limits: 64 cubics per partition, 512 per original trace, 4096 per arm/condition, and eight local subdivisions. Valid contiguous intervals reassemble into chains with exact shared endpoints. Rejected intervals remain visible in the ledger. No raw-grid, rectangle, image or polyline fallback is exported.

**Q — closed-loop periodic handling:** use exactly the same partitions. For genuinely source-closed traces, reconcile bounded tangent handles at smooth partition joins, including the seam; retain intentional corners. Revalidate every affected interval. Unsafe modifications are rejected explicitly, without quietly substituting P and calling it a periodic success. A source loop is marked closed only when all its intervals survive with the correct nonzero signed-area orientation. Partial cyclic runs remain open.

Open-trace local fitting is the same in P/Q. Global budget/conflict guards may nevertheless affect later retention, so final output identity is not assumed without inspection. Full C1 smoothness at all source corners is neither desirable nor claimed.

Both methods preserve source endpoints and junction coordinates. Global checks reject newly introduced proper crossings/overlaps relative to the corresponding frozen source trace pairs, duplicate curves and newly self-intersecting traces. Numerical flattening and a bounded intersection displacement tolerance are not exact continuous topology certification. Inherited source defects and missing incidence remain possible.

Partitioning and increased per-original-trace capacity form a coupled intervention. The study does not attribute all gains to a single formula. The separate K01 cap-only control below helps distinguish capacity from construction behavior.

## 5. Quantitative results

Recall uses the unchanged 1.25 px known-mask/proxy tolerance. Shield rows use the approximate full-crown guide's declared uncertainty band instead; they are not directly comparable with the other rows. Arabic and horse references are source-threshold proxies, not independent glyph/vector truth. The photograph has no exact physical-contour reference. Per-guide precision, recall, selected-stage support and full resource/complexity measurements are in `reports/METRICS.json`.

| Case / evidence | Old recall | Partitioned recall | Periodic recall | Selected length retained, P |
|---|---:|---:|---:|---:|
| A01_shield / Classical | 0.3023 | 0.3036 | 0.3036 | 100.0% |
| A01_shield / ML | 0.4886 | 0.4987 | 0.4987 | 100.0% |
| A01_shield / Hybrid | 0.4729 | 0.5076 | 0.5085 | 100.0% |
| G06_arabic / Classical | 0.0421 | 0.9730 | 0.9712 | 100.0% |
| G06_arabic / ML | 0.5227 | 0.9162 | 0.9158 | 100.0% |
| G06_arabic / Hybrid | 0.4471 | 0.9167 | 0.9167 | 100.0% |
| K01_linear_corner_hole / Classical | 0.0000 | 0.9994 | 0.9994 | 100.0% |
| K01_linear_corner_hole / ML | 0.0000 | 0.9953 | 0.9922 | 100.0% |
| K01_linear_corner_hole / Hybrid | 0.0000 | 0.9953 | 0.9922 | 100.0% |
| fine_features / Classical | 0.2876 | 0.8495 | 0.8495 | 100.0% |
| fine_features / ML | 0.4612 | 0.9784 | 0.9784 | 100.0% |
| fine_features / Hybrid | 0.4612 | 0.9784 | 0.9784 | 100.0% |
| H01_horse / Classical | 0.0077 | 0.7108 | 0.7108 | 71.2% |
| H01_horse / ML | 0.0948 | 0.7635 | 0.7635 | 100.0% |
| H01_horse / Hybrid | 0.1412 | 0.9033 | 0.9033 | 100.0% |
| H02_astronaut / Classical | No exact reference | No exact reference | No exact reference | 100.0% |
| H02_astronaut / ML | No exact reference | No exact reference | No exact reference | 100.0% |
| H02_astronaut / Hybrid | No exact reference | No exact reference | No exact reference | 100.0% |


P retains 100% of selected length in 17 of 18 sets. Horse Classical retains about 71.2%; its long trace reaches the frozen 512-cubic limit and explicitly loses 655.56 px of source length. Q additionally rejects 8.24 px in Arabic Classical, reducing retained closed loops from seven to six. No resource threshold or geometric tolerance was relaxed to manufacture a pass.

## 6. K01: the critical closed-loop failure

The frozen input has three closed contours per arm: outer form, oval boundary and internal quadrilateral decoration. O accepted none: two traces hit the 64-cubic limit and one failed deviation/refinement. P and Q retain all three closed contours in every arm, with exact closure and preserved source winding/nesting. Classical uses 239 cubics; ML and Hybrid each use 240. P known foreground-boundary recall is approximately **0.9994 / 0.9953 / 0.9953**. The hole-boundary support measurement is reported separately.

The quadrilateral is an internal material/decorative boundary, not automatically another hole. Foreground-only mask precision penalizes this legitimate interior edge, so its roughly 0.75–0.78 precision cannot be treated as semantic false-positive truth. No filled face, occlusion ordering or correct region ownership is inferred from three closed strokes. Actual SVGs visibly recover the drawing, but stair-step jitter remains.

### Separately frozen cap-only diagnostic

After the main matrix, one narrow K01 diagnostic was frozen in `CAP512_DIAGNOSTIC_FREEZE.json` before execution: call the old stable fitter on the identical traces with **only** its maximum cubic count increased from 64 to 512. Keep RDP, deviation 0.6 px and eight refinement rounds unchanged; no partition or periodic handles.

All nine attempts (three contours × three arms) still failed with `deviation_budget`, and the diagnostic SVGs remain empty. This rejects the explanation that increasing capacity alone, under the old bounded refinement procedure, reproduces the K01 repair. It supports partition/refinement behavior as part of the mechanism, without proving that periodic smoothing caused the recovery. Each arm completed in approximately 40–42 seconds, sampled peak about 124 MiB.

## 7. Shield: complete interior artwork remains unresolved

Classical crown guide recall changes only **0.3023 → 0.3036** in P, despite retaining all selected length. Its raw-all crown support is about 0.850, but selected support is about 0.302. Most of this gap is therefore selection-related, not a remaining wholesale fitting loss. Approximately 4,998.63 px of its total raw contour length remains excluded by the unchanged short/trace-count rules. Some excluded evidence is lighting/texture; it cannot all be promoted to structural geometry.

ML crown support changes **0.4886 → 0.4987**; Hybrid **0.4729 → 0.5076**. These are modest changes, not crown reconstruction. ML outer-silhouette support improves from zero fitted support to about **0.984**, and Hybrid to **0.988**, after long contour retention. That exterior improvement cannot override missing crown ornament and interior forms.

Named checks cover all tips/flanks/valleys, central ornament/fold, upper/lower bands, metallic frame boundaries and red/gold material separation. ML's central ornament/fold remains around 0.122 fitted guide support, while its outer metallic ridge has no support. The Classical material interface remains poor despite many retained lighting traces. Dedicated crown SVG close-ups and per-component tables expose these failures.

“Absent upstream” means absent from the frozen thresholded evidence or trace graph, not proof the original model could never detect it. The Shield guides have 1.2–2 px uncertainty, no qualified human-independent exact truth, and some illumination ambiguity. No strict one-pixel crown or complete physical-boundary claim is justified.

## 8. Arabic, Fine Features and holdouts

**Arabic:** P raises Classical boundary-proxy recall **0.0421 → 0.9730**, ML **0.5227 → 0.9162**, Hybrid **0.4471 → 0.9167**. P Classical preserves all seven source-closed traces; Q loses one through its unchanged deviation gate. P proxy precision remains approximately 1.000/0.986/0.994. These are meaningful source-contour construction gains. They do not establish independently correct glyph outlines, counters or semantic letter connections. Incorrect source connectivity cannot be fixed merely by retaining it.

**Fine Features:** P recall rises Classical **0.2876 → 0.8495**, ML/Hybrid **0.4612 → 0.9784**. P retains all selected lengths, but the Classical raw-all versus selected gap remains. Closed boundary-network loops are not the four source foreground objects. Exact four-object topology/width reconstruction is not established. The unknown-rights Arena fixture and all derived geometry/images remain owner-local, with public hashes and retrieval information.

**Horse:** Classical improves from 0.0077 to 0.7108 but hits the 512-cubic original-trace cap; ML improves 0.0948→0.7635, Hybrid 0.1412→0.9033. Frozen source traces are open; no arbitrary closing edges are invented. Source closure/connection defects remain upstream of fitting. No clean filled silhouette is claimed.

**Astronaut:** all selected source length is retained by P/Q, but the Classical selection retains only a small part of total detected contour length. Lighting, texture and background evidence remain ambiguous. No exact photographic structure ground truth or complete drawing claim exists.

## 9. Geometry quality, false contours and anti-grid limits

Independent numerical checks found no newly introduced self or mutual proper crossing conflicts relative to the matched raw traces. Exact source endpoints, accepted interval mapping, command/control-point serialization and source loop nesting were checked. This validates bounded construction behavior, not a complete planar arrangement or professional topology.

More retention can preserve more false evidence. Shield lighting traces and the learned Horse false edges remain. The latter's P proxy precision is about 0.821, versus Hybrid about 0.953 and Classical about 0.999. Do not label all newly retained length “valid structural artwork.” Shading-only Shield guides are reported separately, not mandatory geometric components.

No embedded raster, rectangle mosaic or grid fallback was found. Nevertheless, **short cubic microgeometry remains substantial**: approximately 23.8% of K01 Classical P curve length and 37.4% of Arabic Classical P curve length lies in cubics whose sampled span is <=2 px. Long-path bounding boxes alone would conceal this. Axis/lattice alignment, control-hull scale, segment count, length-weighted microgeometry and real 16× views remain negative vector-quality evidence. Length×width is a proxy, not exact visible painted area. The RDP/deviation settings preserve staircases; closed curves alone do not meet the owner's Pen Tool objective.

## 10. Resource validation and execution

The Windows venv launcher issue was corrected before benchmarking. A controlled child allocated and touched 64 MiB: the monitor saw approximately **96.27 MiB tree RSS versus 3.91 MiB launcher RSS**, and a separate 48 MiB limit test stopped the owned worker tree. `MONITOR_VALIDATION.json` records PIDs and samples. All benchmark workers observed descendant PIDs.

All 18 main workers completed. Summed monitored wall time was **661.18 seconds**, maximum sampled process-tree RSS **159.875 MiB**. The longest worker was 141.61 seconds for both Arabic Classical conditions together; the longest individual condition was approximately 117.81 seconds. This respects the 120-second condition and 300-second worker bounds. Cap-only diagnostic time/resources are separate. Evaluation, rendering, QA and packaging are not included in constructor timing.

Polling can miss short peaks, and summed RSS can double-count shared pages. These are sampled measurements, not certified maximum allocation or energy measurements. No GPU inference or model load occurred. The usage-limit pause is not compute runtime.

## 11. Tests, independent QA and reproducibility

Nine construction tests cover periodic circles, intentional corners, long contours, nested opposite-winding loops, shared junction endpoints, open P/Q equivalence, explicit budget/deadline losses, duplicate-input and short-trace rejection. The corrected exporter remains imported from the prior verified implementation.

Independent QA verified the frozen inputs/amendment, all 36 new candidate ledgers, exact SVG controls/endpoints/closures, 18 byte-identical saved baselines, sampled bidirectional deviation and no new crossing conflicts. It independently rendered the Q outputs and inspected K01/Shield comparisons. Final dashboard/report/cap-control review is recorded separately in the final QA artifact; a successful unit test is not complete geometric acceptance.

Source, tests, frozen policy, original input hashes, interval-level JSON/CSV, actual SVGs, native/full4×/detail16× renders, loss overlays and resource records are retained. The local dashboard includes restricted Fine Features; the repository dashboard excludes those derivatives. No model weights, virtual environments, caches or unknown-rights assets should be staged. Reproduction instructions describe the inherited dependencies and safe scratch outputs.

## 12. Git state and publication

Starting remote was verified as `3922fc393cd7fbb3675cae9cfec21d097e74fcbd`. Scoped staging failed once with `.git/index.lock: Permission denied`. No ACL changes, sandbox bypass, repeated prohibited writes, force push or history rewrite occurred. No new commit/push is claimed. The owner-run scoped `Publish-Research.ps1` checks the repository, main branch, origin, staged scope and ancestry; commits only if needed; pushes normally; verifies remote HEAD. Exact inventory and ending state accompany delivery.

## Claim ledger and next decision

- **VERIFIED:** substantial old construction losses, exact per-edge accounting, K01 closed-contour recovery, Arabic/Fine contour-support gains, failure of the cap-only K01 control, and the periodic Arabic regression.
- **SUPPORTED BUT LIMITED:** partitioning is a useful construction control, with bounded topology-safety evidence and meaningful internal-contour progress in the known/Arabic cases.
- **HYPOTHESIS:** source-supported junction/region integration and content-aware trace selection can turn retained and excluded evidence into a more complete drawing without false joins or pixel-scale proliferation.
- **NOT ESTABLISHED:** complete Shield crown/ornament, correct semantic regions/holes, independent Arabic typography, professional smooth geometry, complete photographic artwork, final appearance fidelity or production readiness.

Approve no production default from this experiment. Recommended next owner decision: bounded region/junction integration with retained-source evidence and explicit microgeometry/coherence vetoes. Geometry remains NOT_ACCEPTED; architecture remains NOT_APPROVED.

## Final independent QA closure

`qa/QA_FINAL.md` accepts the **bounded research evidence only**. It verified all 36 candidate ledgers and SVG command/control-point roundtrips, 74 original pins with the explicit pre-execution amendment plus four final source pins, all 18 byte-identical baselines and prior metric equivalence, bidirectional numerical samples, K01 source-containment preservation, process-tree telemetry, nine tests and actual renderer outputs. All nine cap-only attempts remain rejected. Both dashboards resolve their local references. Reviewer renders derived from Fine Features remain local-only and are not packaged into Git.

The final package gives the cap-only diagnostic a distinct entrypoint name (`execute_cap_only`) to satisfy the scoped function registry; this is a packaging-only rename with its call site updated. The executed source and its frozen hash remain unchanged. Constructor geometry and all measured outputs are preserved.

## Governance limitation

Scoped experiment provenance and code mirrors pass. Root-wide provenance verification returns exit 1 with 280 reported registry/metadata issues; full output is retained. Historical/global governance was not rewritten to manufacture a pass. This package does not certify repository-wide governance.
