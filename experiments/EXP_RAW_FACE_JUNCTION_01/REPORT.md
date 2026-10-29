<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T12:39:52Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T12:39:52Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T12:39:52Z"}
END_DOC_PROVENANCE -->
# Raw-face and junction validity — bounded geometry research

Geometry milestone: **NOT_ACCEPTED**. Production architecture: **NOT_APPROVED**.

## Technical decision

**VERIFIED:** Pinched raw face walks can be decomposed into simple cycles while preserving segmentation, shared boundaries, every fitted control point, directed chain occurrences, signed raw area and actual native/8x raw region-ID renders. The four-case raw-invalid-ring counts become zero.

**VERIFIED:** This does not reconstruct missing artwork. O/R curve-only SVG and PNG bytes are identical. Fine-feature fragmentation, crown distortion and Shield's seven crossing/overlap pairs remain. Ring counts change, so lower invalidity counts are not a fidelity result.

**VERIFIED:** The matched-control test exposed an inherited research SVG exporter defect: embedded closed chains in compound face walks emit `Z` after their initial `M` has been removed, closing to the wrong containing subpath origin. Actual graph endpoint gaps are zero. Face decomposition changes these erroneous fitted fills despite unchanged geometry.

**NOT ESTABLISHED:** Whether the raw-face correction unblocks safe fitting in fine_features, Arabic or Shield. Their frozen fitted-render equality checks fail, so all three follow-on RB runs were stopped. The unchanged K01 control passes and exactly reproduces saved B; this is not a new repair benefit.

Recommendation: retain the representation and export diagnosis, fix/validate the export contract in a narrowly scoped control, and move the next substantial geometry effort toward source-driven structural discovery. Do not run another broad face-count or endpoint-threshold tuning cycle. No current candidate passes complete internal geometry or final visual-fidelity gates.

## 1. Repository, recovery and preservation

Starting local HEAD, origin/main tracking and independently queried remote main all matched `29c7ea331f82c5274392421b2bec8a5213d2e08c`; the working tree was clean. This includes all three previous thin-study checkpoints published by the owner. The complete original owner vision, previous isolation/thin reports, frozen policies and independent QA were read. Historical artifacts and approved assets were preserved. The 24-condition isolation and 140-candidate search were not rerun.

All new work is confined to EXP_RAW_FACE_JUNCTION_01. Final appearance, image generation, intelligent Arabic typography, semantic groups, Magic Layers and professional editing remain full product requirements; none was implemented or abandoned. Source color was used only for geometric evidence.

The attempted checkpoint publication failed: `git add -- experiments/EXP_RAW_FACE_JUNCTION_01` returned `fatal: Unable to create .../.git/index.lock: Permission denied`. A supported grant for the repository and then the exact .git path did not resolve it. No stale index.lock file exists. Authentication independently failed through wincredman (`unable to get password from user`). No ACL/security bypass, force-push, history rewrite or unrelated staging was performed. No new commit or upload is claimed. The owner-run scoped publication script and exact inventory are delivered; research continued without further retries.

## 2. Hypotheses, frozen controls and budgets

The protocol and inputs were frozen in FREEZE.json before any new benchmark candidates. Independent QA verified all three frozen file hashes before execution. Baseline O is the byte-preserved saved S_A/F_A common-face graph; B is the previous saved guarded graph. Neither segmentation nor original initialization was rerun.

- **R:** recursively split closed face walks only at repeated exact chain endpoints. Preserve every chain, its raw vertices and controls, incidence, labels, region identity and per-label directed occurrence multiset. No chain splitting, interpolation, pruning, new region or point motion.
- **RB:** unchanged historical Track B on R, only if whole-case invariants and exact O/R raw native/8x plus fitted8x render equality hold. This gate was not weakened after discovering the exporter problem.
- **Independent evidence probe:** fixed multiscale Lab Canny and dual-polarity luminance Sato on native RGB only. No candidate topology or segmenter was constructed from those maps.

Four cases; at most four representation candidates, four follow-on guards, one source probe per case. Per principal worker 600s/4096MiB; probe90s/1024MiB; total7200CPU-second budget, active engineering6h. No parameter search, paid API, hosted AI or neural dependency. The primary branch stops if equivalence fails; subsequent code is evaluator/presentation only.

Known-control gates remain IoU>=0.97, thin area recall>=0.95, exact sampled components/holes, mean boundary<=0.45px and p95<=1.25px, with critical-component vetoes. Shield's existing1.2–2px uncertain AI guide cannot certify strict1px accuracy; no new human reference was invented. Arabic proxy metrics are not font-outline truth. Photographic boundary generalization is outside these four controls.

## 3. Implementation and earliest supported root cause

`face_cycles.py` performs exact closed-walk decomposition. Each occurrence belongs to exactly one resulting cycle; original-to-cycle mapping, signed areas, zero/invalid cycles and rejected operations are recorded. It never infers a semantic foreground connection or edits a label pixel. `run_case.py` enforces baseline/freeze hashes and renders matched controls before any guard call.

The read-only baseline audit found all raw-invalid walks in this bounded set also contain repeated chain-endpoint visits: fine1, Arabic7, Shield18, K010. There were no internal-only repeated raw vertices. Junction diagnostics include the source-label2x2 neighborhood at each repeated endpoint; point-contacting/diagonal cells permit weakly simple face walks even when their filled raster ownership is well defined. This is a representation incompatibility with strict simple-ring predicates, not proof that the segmentation itself is erroneous or that the original SVG fill is necessarily wrong.

Exact cycle decomposition is preferred over buffer(0), make_valid or morphological relabeling: those can move/remove boundaries, alter ownership or hide collapsed faces. Mature planar arrangements are a broader future option but cannot infer missing source boundaries. Here a full DCEL or graph rebuild would add variables without being necessary to test the pinched-walk hypothesis.

## 4. Results, ring denominators and matched comparison

| Case | Condition | Rings | Raw invalid | Fitted invalid | Raw-nonzero/fit-zero | Chains / cubics | Crossing/overlap pairs |
|---|---|---:|---:|---:|---:|---:|---:|
| fine_features | O | 18 | 1 | 4 | 3 | 22 / 36 | 0 |
| fine_features | R | 27 | 0 | 6 | 6 | 22 / 36 | 0 |
| fine_features | B | 18 | 1 | 4 | 3 | 22 / 36 | 0 |
| G06_arabic | O | 226 | 7 | 78 | 69 | 539 / 514 | 0 |
| G06_arabic | R | 235 | 0 | 71 | 69 | 539 / 514 | 0 |
| G06_arabic | B | 226 | 7 | 76 | 67 | 539 / 514 | 0 |
| A01_shield | O | 464 | 18 | 153 | 131 | 809 / 737 | 7 |
| A01_shield | R | 500 | 0 | 139 | 133 | 809 / 737 | 7 |
| A01_shield | B | 464 | 18 | 153 | 131 | 809 / 737 | 7 |
| K01_linear_corner_hole | O | 45 | 0 | 3 | 3 | 93 / 88 | 0 |
| K01_linear_corner_hole | R | 45 | 0 | 3 | 3 | 93 / 88 | 0 |
| K01_linear_corner_hole | B | 45 | 0 | 0 | 0 | 93 / 88 | 0 |
| K01_linear_corner_hole | RB | 45 | 0 | 0 | 0 | 93 / 88 | 0 |

Fine split9 times (18→27 rings), Arabic9 (226→235), Shield36 (464→500), K010 (45 unchanged). Every original directed occurrence and signed area is retained. Fine collapsed3→6 and Shield131→133 under R expose separately enumerated cycles; no control point moved or newly destroyed feature is inferred from these counts. Arabic invalid78→71 is likewise a different ring partition, not seven recovered letter components.

O/R raw native and8x ID renders differ in zero RGBA pixels on all cases. O/R fitted8x differs fine8,735; Arabic19,070; Shield78,232; K010. Therefore **RB is SKIPPED**, not failed or successful, in the first three. The saved B comparison remains visible but is not substituted for those missing runs. K01 RB equals the prior B graph exactly.

## 5. Exporter defect and limits of attribution

The affected helper is the historical geometry research exporter `EXP_COMPLETE_GEOMETRY_ISOLATION_01/geometry_eval.py`, not evidence that every VTracer or production SVG exporter has this defect. At line87 it appends `Z` to a closed chain. At line97 later chain `M` commands are removed when assembling one face subpath; line99 adds the final ring closure. An embedded chain's `Z` can therefore close to the containing walk's origin and change where the next command starts.

Independent passive command-state tracing identifies wrong embedded closes in O: fine1, Arabic7, Shield24, K010. R has zero in this diagnostic. The actual graph ring endpoint gap remains zero throughout. Fine's concrete example closes embedded chain13, whose start is(110,32), to containing origin(35,19), a76.118px unintended jump. See reports/exporter_audit.json for exact cases and independent scripts.

**VERIFIED:** this command-semantic defect exists and the failed cases contain it. **SUPPORTED BUT LIMITED:** it explains why an apparently equivalent fitted export comparison can fail. **NOT ESTABLISHED:** quantitative attribution of every changed pixel or corrected-export equivalence, which requires its own matched exporter control. Historical exporter code was left unchanged and the primary frozen gate remains binding. No replacement exporter was quietly used to permit more guard runs.

## 6. Structural and visual outcomes

### Fine features

R has zero raw-invalid simple rings, but raw foreground remains13 components versus known4. Fitted IoU stays0.8202433464578585; fitted12 components, area recall0.870523, and the1.25px curve remains incompletely recovered. Source evidence cannot change that without a new geometry proposal mechanism. No thin connection or missing region was recovered. Unchanged actual boundary drawing at1x/4x/16x is shown next to decomposed raw cycles and label ownership.

### Arabic

The actual boundary drawing is unchanged. Source-threshold fitted IoU changes0.920244959→0.931811351 after R solely through the regrouped region export, not new glyph contours. R proxy fit topology becomes6 components/1hole, matching the raw proxy but not source-threshold40/9. These threshold counts include antialiasing/noise and are not independent outline correctness. Prior B has69→67 collapsed rings but remains structurally unresolved. No correct typography/counter reconstruction is claimed.

### Shield: complete crown and interior review

Outer and inner metallic contours, material interface, five crown tips/valleys, central ornament, flanks and both band edges are included in the dashboard and retained frozen guide table below. O/R curve bytes are identical, so no missing crown component can have been discovered by this operation. All seven measured crossing/overlap pairs persist. Apparent region-fill changes must be separated from genuine curve accuracy.

Guide recall within the declared uncertainty band (not certified semantic correspondence or1pxaccuracy):

| Component | Uncertainty px | Raw O/R | Fit O | Fit R |
|---|---:|---:|---:|---:|
| shield_outer_silhouette | 1.8 | 0.9358 | 0.8886 | 0.8886 |
| metallic_outer_bevel_ridge | 1.8 | 0.2076 | 0.1588 | 0.1588 |
| metallic_inner_bevel_ridge | 1.5 | 0.8226 | 0.7603 | 0.7603 |
| red_gold_material_interface | 1.2 | 0.7155 | 0.6343 | 0.6343 |
| crown_complete_visible_outline | 1.7 | 0.7215 | 0.6970 | 0.6970 |
| crown_left_tip_and_flank | 1.5 | 0.6995 | 0.6919 | 0.6919 |
| crown_left_inner_tip | 1.5 | 0.6737 | 0.6632 | 0.6632 |
| crown_center_tip_and_lobes | 1.7 | 0.9348 | 0.9078 | 0.9078 |
| crown_right_inner_tip | 1.5 | 0.7266 | 0.6629 | 0.6629 |
| crown_right_tip_and_flank | 1.7 | 0.6638 | 0.5971 | 0.5971 |
| central_ornament_internal_fold | 2.0 | 0.8288 | 0.7740 | 0.7740 |
| lower_band_upper_edge | 1.2 | 0.3515 | 0.3324 | 0.3324 |
| lower_band_lower_edge | 1.5 | 0.2975 | 0.2890 | 0.2890 |

The recognizable crown still has distorted/uncertain contours and incomplete internal support. Band, ornament and frame guide coverage must not be hidden behind silhouette metrics. Central fold/light transition remains ambiguous; it is not forced into a physical closed region. **NOT ESTABLISHED:** complete crown geometry or strict1pxacceptance. No improved human-reviewed reference was available.

### K01 control

R makes zero changes. Its RB reproduces the saved B six-chain repair exactly: three collapsed rings become zero, valid foreground component/hole counts remain1/1, numerical flattened coverage reports zero gaps/overlap/exterior area, yet silhouette IoU stays0.950661647273557, below0.97. The known boundary mean/p95 remain above policy. This reconfirms topology safety without visible silhouette improvement; it provides no evidence that decomposing raw faces unblocked anything.

## 7. Coverage, shared boundaries, intersections and anti-mosaic

No source preprocessing, alpha, region ownership, curve control, adjacency or incidence changed between O/R. Exact shared references and measured gaps are retained. Raw region-ID coverage at two resolutions is identical, supported independently by algebraic parity/occurrence invariants. This does not prove all hidden overlap or final renderer antialiasing/compositing correctness. Filled-region numerical coverage remains NOT_ESTABLISHED where fitted rings are invalid; no hidden polygon repair was applied.

No new path or chain geometry, source-grid fallback, tiny rectangle, raster underlay, stroke patch or hardcoded artwork was inserted. Face subpath counts increase because existing occurrences are separated, not because new cell geometry was created. Existing tiny regions remain and are not automatically meaningful. Per-case1/2/4px source-owned and actual4xvisible microgeometry, lattice fractions, curve counts and raw-to-fitted displacement are retained. No10%2px-area alarm is triggered; this does not certify coherent professional geometry, and long thin strips can escape tiny-bounding-box tests. O/R final staircase/corner behavior is identical because controls are identical; there is no smoothness improvement to claim.

## 8. Independent source-discovery feasibility assessment and probe

The preceding endpoint operator is not retuned. `source_evidence_probe.extract` receives only native uint8 RGB and fixed constants. On normalized Lab it unions per-channel Canny at sigma0.6/1.2 with thresholds0.04/0.10 and1pxcross-scale persistence. It separately saves luminance Sato response maps at scales0.7/1.2/2, both polarities. No labels, reference curves, case ROI, region construction, contour linking or source-grid SVG export enters that constructor. Per-image ridge normalization is display-only, not confidence. No source map is a recovered shape.

The evaluator subsequently compares source-edge pixel centers(x+.5,y+.5) to the complete original raw crack segments at integer corner coordinates; >2pxis a fixed evidence-distance diagnostic, not an omitted-structure classifier.

| Case | Persistent source edge pixels | Image density | Farther than2pxfrom raw graph |
|---|---:|---:|---:|
| fine_features | 637 | 5.1839% | 0 |
| G06_arabic | 2615 | 3.8914% | 0 |
| A01_shield | 12634 | 13.7504% | 3428 |
| K01_linear_corner_hole | 1287 | 4.1895% | 0 |

All densities remain below the frozen15%clutter warning; Shield is close at13.75%. Its magenta far-evidence overlay includes extensive red/gold texture, shading/reflections and some internal contrast. **NOT ESTABLISHED:** which3428pixels are genuine missing material contours, their precision/recall, or complete crown recovery. Fine/Arabic/K01 zero beyond2pxdoes not exclude missing sub2pxconnections, incorrect widths or merged components. A detector can find local contrast near existing boundaries while topology remains wrong.

The probe supports feasibility of obtaining source evidence without pre-existing endpoints, but not the sufficiency of this detector for reconstructing complete artwork. Ridge maps show potential thin support; width, continuity, paired boundaries and junction decisions are still absent. No geometry candidate was generated from them, and no result-driven tuning was performed.

Comparative assessment (reports/SOURCE_DISCOVERY_ASSESSMENT.md):

1. **Preferred next hypothesis:** multiscale source color-boundary evidence plus ridge/paired-boundary width support, followed by localized region birth/splitting or explicit strokes and validated topology. Geometry from the raster can add a missing structure; face restructuring cannot.
2. Mature Canny/Devernay chained subpixel points are a useful controlled localization baseline, but do not decide regions/physical structure. IPOL source is AGPL-3.0-or-later; no wholesale product copy is proposed. Current probe uses installed scikit-image pixel Canny, not Devernay.
3. Marker/region-driven segmentation plus shared graphs can provide ownership, but automatic marker birth and shading oversegmentation require controls; changing global segmentation now would confound this isolation.
4. A mature planar arrangement/DCEL is valuable for maintaining incidence, not discovering missing boundaries. New C++/license/integration costs are not justified for this tiny probe.
5. Reject micro-path SVG as main discovery source: it largely restates sampled raster transitions without an independent signal. Retain it as fidelity reference.
6. Defer differentiable/joint photometric geometry optimization: it does not remove missing-topology/model ambiguity and can reward microgeometry. No neural or hosted dependency is justified here.

Primary sources: [scikit-image Canny](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.canny), [ridge filters](https://scikit-image.org/docs/stable/api/skimage.filters.html), [IPOL Canny/Devernay](https://www.ipol.im/pub/art/2017/216/), [CGAL topology/geometry separation](https://doc.cgal.org/latest/Arrangement_on_surface_2/index.html). Published capability is not observed reconstruction performance on our images.

## 9. Resources, testing and independent QA

Eight monitored construction/probe workers completed in 27.978 summed wall seconds, sampled tree peak 185.543MiB. Longest principal worker 4.369s; longest source probe 3.852s. Evaluation/rendering took 78.706s, sampled peak 182.672MiB. All exit codes0; no resource limit fired. Conservative all-12-logical-processor upper bound on these monitored steps is 1280.2CPU-seconds, below7200. Packaging/setup/QA are separately bounded engineering work. Sampling every requested50msplus enumeration overhead can miss short peaks; these are samples, not certified memory maxima.

Nine implementation tests passed, including directed occurrence/winding preservation, no silent open-walk closure, zero-area retention, split budget failure, source determinism/immutability and no spurious constant-image evidence. Five face tests were independently rerun by QA. Independent QA verifies exact source/reference/ownership invariants, raw SVG equality, actual curve SVG/PNG identity, failed fitted exports, guard skips, K01control and no embedded raster/script. Numerical curve predicates and SVG parsing are not full continuous topology certification or owner visual acceptance.

See reports/QA_FINAL_REVIEW.md and preserved passive audit scripts/evidence. QA identified the concrete exporter mechanism; no defect was hidden to make the control pass. The source probe uses no evaluator truth. The complete source, configs, candidates, SVG/PNG evidence and manifests are retained. Unknown-rights external fine fixture and derivatives stay local-only with hashes and original retrieval paths; no public redistribution grant is inferred.

## 10. Next geometry decision

**GO recommended for a new bounded source-driven region/stroke discovery test**, after a small exporter-contract correctness prerequisite. Freeze a corrected compound-path export baseline with per-label raw/fitted parity, intentional point-contact fixtures and independent renderer/command checks. That prerequisite should not become another indefinite geometry-count research cycle.

Then test whether paired source contours/ridges with width and junction constraints can propose a previously missing thin component or crown-band/material boundary without evaluator templates. Include fine/Arabic/Shield/K01 and explicit false-join/false-detail controls, retain complete interior vetoes, and compare curves plus region ownership. A subpixel boundary baseline and a stroke representation should be considered where closed thin regions are unstable. Do not equate an edge detector's dense output with valid complete geometry.

Raw-face decomposition is **VERIFIED as representation normalization in this bounded set**, not a new image reconstruction capability. Safe-fitting benefit on the three affected cases is **NOT ESTABLISHED** because the primary matched test stopped. Complete visible geometry remains **NOT_ACCEPTED**. No final appearance loop, broad engine or production integration has been authorized or implemented. Stop here for the owner's next GO/NO-GO.
