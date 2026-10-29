<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:51:26Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Complete Geometry Isolation — technical decision report

**Production architecture: NOT_APPROVED. No candidate passes the complete reconstruction gate.**

**Recommendation:** treat segmentation/discovery and fitting safety as separate problems. Do not adopt Arena wholesale or globally replace its initializer with VTracer. The study supports both causes; it does not certify complete crown reconstruction or high final appearance fidelity.

## 1. Repository, recovery and publication

**VERIFIED:** the starting local/tracking/remote baseline was `ed6072b15d3f9fca4774856ffcf31909d1785fd7`. The completed coverage-aware package contained1,359 files /125,638,409 bytes. Its inventory and hashes were verified, ten tests passed again, and it was committed as `bd61aaebf72e0a2a83106139ec69d304713221a8`. The frozen protocol and independently reviewed references were committed as `649bc4a`. See `PUBLICATION.md` for later checkpoints and exact publication status.

The140-candidate search and unrelated appearance experiments were not repeated. The full original owner vision was read and preserved. No production, appearance, semantic, typography or Magic Layers implementation changed.

Git metadata writes now succeed. Push failed because this execution identity could not use Windows `wincredman`, followed by disabled terminal prompts. This is an authentication/credential-store blocker, not an index-lock failure in this run. Command-local OpenSSL with certificate verification successfully reads remote HEAD. No ACL, TLS validation or repository protection was changed. **Local commits are not claimed pushed.** Owner-run publication instructions accompany each checkpoint; no repeated blocked push was attempted.

## 2. Executed matrix and scientific controls

**VERIFIED:** all six cases × two segmentations × two initializers completed:24 conditions.

- **S_A:** saved Arena labels for Shield and fine_features; the original external Felzenszwalb algorithm for Tux, Arabic, Cat and K01, frozen at scale400, sigma0.8, minimum-area12 and low-contrast merge threshold9.
- **S_V:** pinned VTracer1.0.0-alpha.4 raw watershed at detail192/minimum-area0. Compositor color-similarity merging is disabled for both initializer inputs. This differs from historical finalD192 geometry, which is context rather than a matched control.
- **F_A:** original external Arena initialization, tolerance0.8, smoothing1, three fitting iterations; no refinement, optimizer or fallback.
- **F_V:** unmodified native VTracer shared-boundary spline defaults; no CurvePass or additional simplification pass.

All use the same native-size, white-composited opaque sRGB working image, positive inside labels and0 for the canvas exterior. No transparency reconstruction is claimed. External Arena source remains outside the repository; its hashes are recorded. The new Rust bridge uses public VTracer interfaces and retains its MIT license. Python3.14/current Windows numerical libraries are documented; Linux equivalence is not assumed.

### Exact-label and face-assembly integrity

**VERIFIED:** all12 same-label pairs have identical raw unit edges and adjacent-label pairs. Injective24-bit region-ID SVG renders recover every input label at native pixel centers with zero wrong RGB values and zero nonopaque pixels. Input label SHA256 values agree across initializers.

Face traversal differs even when pixel ownership is identical: Arena's Shield raw assembly has18 invalid/weakly self-touching rings under the numerical checker; the native assembly has none. Comparing these native ring counts directly would confound fitting with face assembly. The primary evaluation therefore maps each native curve onto the same Arena raw chain IDs and face references using exact edge signatures and reversal only. **No control point moves.** Original native graphs and exports remain available. The common assembly is not assumed valid merely because it is shared.

Independent QA caught two measurement errors. The preliminary color palette repeated every200 labels; the final audit uses an injective palette. Native closed rings require SVG closepath; final measurements include that closure without pinning open chains. Preliminary diagnostics are preserved and labeled superseded. No candidate was refitted or selected using evaluator truth.

## 3. References and acceptance limits

The protocol, criteria and source-only annotations were frozen before benchmark generation, in commit `649bc4a`. An independent AI reviewer checked hashes, complete declared crown coverage, junction/gap review scope and annotation roles. Neither annotator nor constructor used new candidate results as templates.

The Shield references cover silhouette, frame interfaces, material separation, all five crown tips and valleys, central ornament/lobes, flanks, both band edges and important joins. The uncertain central fold remains a mandatory visual-review item marked UNKNOWN, not a forced physical or closed boundary.

**NOT ESTABLISHED:** strict1px crown accuracy. All approximate Shield traces have1.2–2px uncertainty and no human/exact ground truth. We retain the original1px gate; we do not relax it to manufacture a pass. Tux, Arabic and Cat have review ROIs rather than invented complete contour truth. Analytic controls use independent source-vector renders, with explicitly sampled mask uncertainty.

## 4. Primary common-face results

|Case|Segmentation|Initializer|Raw nonzeroâ†’zero rings|Invalid fitted rings|Cubics|
|---|---|---|---:|---:|---:|
|A01_shield|S_A|F_A|131|153|737|
|A01_shield|S_A|F_V|207|209|963|
|A01_shield|S_V|F_A|0|6|862|
|A01_shield|S_V|F_V|0|0|1468|
|G07_tux|S_A|F_A|59|63|590|
|G07_tux|S_A|F_V|66|67|955|
|G07_tux|S_V|F_A|3|9|590|
|G07_tux|S_V|F_V|4|5|993|
|G06_arabic|S_A|F_A|69|78|514|
|G06_arabic|S_A|F_V|85|86|959|
|G06_arabic|S_V|F_A|65|67|360|
|G06_arabic|S_V|F_V|81|81|338|
|G05_chelsea_nativecrop|S_A|F_A|43|99|818|
|G05_chelsea_nativecrop|S_A|F_V|201|220|1216|
|G05_chelsea_nativecrop|S_V|F_A|0|17|1442|
|G05_chelsea_nativecrop|S_V|F_V|1|2|2314|
|fine_features|S_A|F_A|3|4|36|
|fine_features|S_A|F_V|4|5|71|
|fine_features|S_V|F_A|21|34|186|
|fine_features|S_V|F_V|33|33|30|
|K01_linear_corner_hole|S_A|F_A|3|3|88|
|K01_linear_corner_hole|S_A|F_V|3|3|309|
|K01_linear_corner_hole|S_V|F_A|6|6|168|
|K01_linear_corner_hole|S_V|F_V|9|9|212|

Counts refer to rings, not distinct lost pixels or additive percentages of final image error. Polynomial integration independently confirms all24 reported collapse counts. The concrete raw/fit face10 SVGs demonstrate an actual collapse. “Invalid raw ring” may reflect face assembly/weak simplicity, not necessarily absent source segmentation.

**VERIFIED:** on saved Arena Shield labels, F_A collapses131 rings and F_V207. The proposed mature-fitter substitution is therefore not a general repair. On the frozen VTracer Shield labels, both collapse0; F_A still has6 invalid fitted rings and F_V0 under these checks. The latter does not pass completeness, coverage or exact topology gates.

The interaction matters: the VTracer partition contains fewer tiny rings and different useful boundaries. Removing a problematic ring from the input is not proof that the fitter preserved its detail. Cat, Arabic and Tux retain substantial failures, so no cross-category winner is selected.

## 5. Shield and crown

**VERIFIED visually:** the crown is present in all four conditions. Candidate tips, central spike/lobes, flanks and band curves are visible. “The whole crown is missing” would be incorrect. Deformation, extra internal lines and incomplete boundary support remain.

The table reports diagnostic reference-to-boundary recall within1px for the two native pairings. All four condition tables are in the case JSONs. These numbers are not correspondence-certified precision or complete geometry acceptance: nearby texture boundaries can inflate coverage and the references themselves are uncertain.

|Shield component|Arena raw|Arena fitted|VTracer raw|VTracer fitted|
|---|---:|---:|---:|---:|
|shield_outer_silhouette|0.689|0.639|0.942|0.879|
|metallic_outer_bevel_ridge|0.090|0.058|0.107|0.054|
|metallic_inner_bevel_ridge|0.627|0.609|0.572|0.517|
|red_gold_material_interface|0.641|0.560|0.641|0.495|
|crown_complete_visible_outline|0.581|0.522|0.629|0.525|
|crown_left_tip_and_flank|0.576|0.470|0.525|0.384|
|crown_left_inner_tip|0.621|0.540|0.618|0.537|
|crown_center_tip_and_lobes|0.734|0.679|0.690|0.555|
|crown_right_inner_tip|0.648|0.558|0.629|0.453|
|crown_right_tip_and_flank|0.481|0.449|0.400|0.299|
|central_ornament_internal_fold|0.692|0.671|0.630|0.568|
|lower_band_upper_edge|0.319|0.281|0.970|0.965|
|lower_band_lower_edge|0.269|0.252|0.680|0.618|

**SUPPORTED BUT LIMITED:** some localized problems exist before curve fitting. The upper-band guide has raw recall0.319 on Arena versus0.970 on VTracer. That supports a local partition difference, not the absence of the entire Arena band. Both partitions weakly support the outer bevel guide; whether that guide is a physical/material boundary or illumination edge remains uncertain. Exact crown-detail correctness is **NOT ESTABLISHED**.

The dashboard shows the entire crown, labels, raw cracks, all four fitted outputs and true SVG viewport renders at1×/4×/16×. A recognizable outer silhouette never overrides a failed internal component.

## 6. Known-vector and thin-feature controls

|Known case|Condition|Raw IoU|Fitted IoU|Rawâ†’fit components (truth)|Thin foreground recall|
|---|---|---:|---:|---|---:|
|fine_features|S_A_F_A|0.785920|0.820243|13â†’12 (4)|0.870523|
|fine_features|S_A_F_V|0.785920|0.765214|13â†’11 (4)|0.807528|
|fine_features|S_V_F_A|0.778707|0.834356|4â†’4 (4)|0.906026|
|fine_features|S_V_F_V|0.778707|0.819778|4â†’4 (4)|0.887363|
|K01_linear_corner_hole|S_A_F_A|0.950788|0.950662|1â†’1 (1)|0.998698|
|K01_linear_corner_hole|S_A_F_V|0.950788|0.950150|1â†’1 (1)|0.998946|
|K01_linear_corner_hole|S_V_F_A|0.989252|0.991182|1â†’1 (1)|0.996115|
|K01_linear_corner_hole|S_V_F_V|0.989252|0.989883|1â†’1 (1)|0.995486|

The masks come from actual independent truth-SVG renders at8×. A fixed source-only corner-color-distance>8 majority rule maps each region to foreground. It is evaluator correspondence, not a construction template, pruning instruction or winner selector. Distances retain sampling/antialiasing uncertainty of roughly1/8 source pixel; this is not exact analytic certification. Four-connected8× component counts are not interchangeable with Arena's older native-resolution counts.

**VERIFIED under this diagnostic definition:** Arena's fine-feature partition already has13 foreground components versus4 in truth, before any fitting. F_A yields12 and F_V11; both fail continuity and area recall. VTracer's raw partition has4 components but IoU0.778707. Correct component count alone hides width/area error; fitted IoUs0.834356/0.819778 remain below0.97.

K01 on the VTracer partition recovers one foreground component and one hole with about0.99 IoU. Yet several tonal rings still collapse. A partial foreground-mask pass cannot pass full region geometry or internal completeness.

## 7. Root-cause findings

| Claim | Classification | Evidence / limit |
|---|---|---|
| Fitting destroys some valid raw geometry | **VERIFIED** | Face10 has two three-vertex L chains enclosing1px²; both fitters produce coincident diagonal/zero-area geometry. |
| Arena's short-chain fitting rules cause its collapse | **VERIFIED** | Corner detection,0.8 tolerance and short-piece recursion admit the diagonal approximation. |
| VTracer is immune to short-chain collapse | **REJECTED** | Native simplification also collapses short chains; fixed-label results worsen on several partitions. |
| Upstream thin-region connectivity is inadequate | **VERIFIED, bounded** | Fine-control raw13-versus4 component mismatch before fitting under the fixed mask definition. |
| The precise Arena clustering-versus-fragment-merge cause is known | **NOT ESTABLISHED** | Saved pre-merge labels are absent. |
| Real Shield discovery/misalignment contributes | **SUPPORTED BUT LIMITED** | Raw support differs around band/crown/frame guides; uncertain references prevent exact semantic omission claims. |
| Both segmentation and initialization contribute | **SUPPORTED BUT LIMITED** | Independent upstream and downstream failures; interactions prevent additive causal percentages. |
| Fewer invalid rings proves complete high fidelity | **REJECTED** | Critical details, coverage and later appearance remain separate gates. |

No new paint engine, stroke underlay, detail path insertion, geometry optimization, topology edit or hidden source-image shortcut was used.

## 8. Topology, coverage and anti-mosaic checks

Adaptive control-hull flattening uses a0.01px bound before double-precision predicates. Diagnostics include ring validity, degeneracy, endpoint gaps, shared reversal, self-intersections, crossings/overlap and unresolved near-pairs. These are numerical checks, not a certified continuous Bézier arrangement proof. Invalid rings leave coverage NOT_ESTABLISHED; no make_valid or hidden geometric repair is applied.

Shield S_V_F_V has zero invalid common rings and zero crossing warnings, but its flattened union still shows2.1953px² uncovered inside the canvas and23.4516px² outside it. It is therefore not accepted as a correct gapless reconstruction. Shared curve IDs alone do not guarantee coverage or containment.

Visible microgeometry is measured from actual4× region-ID SVGs. Fully opaque exact-color samples and unclassified antialias/alpha samples provide an empirical lower/upper interval. It is not a guaranteed analytic bound: rare blended colors can coincide with region-ID colors. Results repeat at1/2/4px scales and include lattice fractions, region/chain/cubic counts and source-owned areas. No blanket ROI exemptions are applied.

All Shield2px-grid-area upper bounds remain below about2.3%, so its frozen10% alarm does not fire. This is **SUPPORTED BUT LIMITED**, not professional-vector certification: collapse can erase tiny faces and genuine Arabic/fine details may be small. Low path count and cubic commands alone do not establish coherent geometry. No micro-paths were added to improve a score.

Actual resvg0.49.0 SVG exports and renders are supplied. Pixel-equivalent references are saved context, not new appearance results. This geometry-only study makes no new SSIM/PSNR or photographic reconstruction success claim.

## 9. Reproduction, resources and independent QA

See REPRODUCE.md, frozen protocol/reference hashes, candidate hashes, execution logs and local-only external evidence manifest. Unknown-rights fine-feature assets and derivatives are preserved locally and excluded from Git; the original owner ZIP and exact hashes are required for reproduction. No evidence is silently omitted.

The matrix used19 monitored workers: summed worker wall time95.201s; sampled peak process-tree RSS161.19MiB; Arena process CPU19.25s. The conservative all-logical-processors upper bound is1142.4s, below7200s. No600s/4GiB worker limit fired. The whole Arena batch shares one600s cap, a stricter aggregate bound. Sampling can miss short peaks; native per-process CPU was not directly measured. Setup/build and evidence packaging are separate from the fitting budget.

Six Rust interface tests and seven Python measurement/export tests passed, including an actual rendered shared-boundary/hole fixture. Independent QA findings and their dispositions are in reports/QA_FINAL_REVIEW.md. Neither these tests nor QA approve complete geometry.

## 10. Next decision

**NO-GO:** adopt Arena unchanged, globally switch to the native VTracer initializer, raise granularity indiscriminately, claim complete crown geometry from silhouette metrics, resume another appearance-fitting cycle, or approve production architecture.

**Recommended next experiment, requiring owner GO:** separate a topology-safe short-chain initialization guard from a source-driven thin-boundary/region-discovery control. The guard must preserve meaningful corners/areas on these frozen labels without adding pixel cells; the discovery control must recover missing thin support rather than merely optimize existing curves. Evaluate both independently on the fine control, Arabic and crown, with strict negative preservation. If only one track is approved, prioritize thin-structure discovery against a safe initialization control, because the raw thin partition already fails.

This is a proposed bounded research direction, not implementation authorization or a final architecture. Human review/refinement of Shield references is needed before strict complete-crown acceptance. The full owner vision—image generation, complete artwork, professional editable SVG, semantic groups, Arabic/typography, Magic Layers and visual QA—remains intact. Stop after this study and await the owner's next decision.
