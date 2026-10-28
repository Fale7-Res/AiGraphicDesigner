<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T03:30:09Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T03:34:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T03:30:09Z"}
END_DOC_PROVENANCE -->
# Vector reconstruction bottlenecks — bounded diagnostic and corrective research

Production architecture: **NOT_APPROVED**. This cycle preserves image generation, Magic Layers, semantic grouping, professional SVG geometry/editing, Arabic typography and the complete immutable owner vision. It introduces no paid API, hosted model, new product architecture or replacement tracing engine.

## What was run

Local and GitHub main both verified at `ec4849376f2bcc74339175e4bd991de83e7dfe0a`; initial working tree clean. This isolated experiment is `EXP_VECTOR_BOTTLENECKS_20261027`. Seven existing cases: shield, coffee, native cat crop, Arabic lettering, dice alpha, and two analytic known-vector controls. Previous 140 searches and the completed nine-case ablation were not rerun.

Saved detail128 B/C/D vectors, renders, metrics and fitter diagnostics are reused. Detail192 and256 use exactly the same watershed/cutout/spline pilot configuration except `watershed_detail`. Fourteen new geometry traces total, unchanged appearance fitter (at most four equally spaced stops, same sample split and regional budget). B is inherited solid paint; C optimized flat paint; D adaptive flat/linear/radial paint. Their path geometry and masks remain identical within each level. Transparent cases retain the same source-derived alpha-run mask; RGB/alpha limitations are evaluated separately.

Additional independent controls: exact known SVG geometry refitted using current C/D, exact shared-edge square partitions vs known union, deliberate one-pixel gap and curved exterior silhouette. One deliberately narrow corrective intervention: matching-fill SVG stroke width0.25, painted before fill, with round joins. It changes coverage/overlap and can expand an exterior by nominal0.125 source pixels; it is not a topology repair. Tests pair this change with the exact same D192 baseline on all seven cases. Coverage controls independently test the same intervention against saved D128 on five real cases; these are distinct comparisons.

## Headline native results

All values below are white-background SSIM, except the last column is MSE on the same D192 pair. Full native RGB, three-background, alpha, PSNR, DeltaE76, edge F1, highpass and worst32px-tile metrics remain in result.json files and reports/granularity_metrics.csv. Corrections were not selected independently per image. The uniform192 correction setting was chosen after observing nonmonotonicity and a moderate geometry budget; it is an explicitly exploratory choice, not a held-out model-selection study or an accepted default.

| Case | A pixel reference | D128 saved | D192 | D256 | D192+stroke0.25 | D192 / corrected MSE |
|---|---:|---:|---:|---:|---:|---:|
| A01_shield | 0.995660 | 0.815371 | 0.832419 | 0.807782 | 0.850059 | 211.101 / 190.301 |
| G01_coffee | 0.997894 | 0.535965 | 0.597912 | 0.592644 | 0.634843 | 297.086 / 248.142 |
| G05_chelsea_nativecrop | 0.999823 | 0.395686 | 0.502264 | 0.534701 | 0.548078 | 278.663 / 222.296 |
| G06_arabic | 0.999999 | 0.999457 | 0.999664 | 0.998830 | 0.999696 | 0.368 / 0.818 |
| G08_dice_alpha | 0.999622 | 0.843116 | 0.920880 | 0.927664 | 0.932225 | 71.247 / 58.173 |
| K01_linear_corner_hole | 0.999464 | 0.978980 | 0.977760 | 0.995629 | 0.981433 | 23.422 / 20.250 |
| K02_radial_shared_curves | 0.998299 | 0.913501 | 0.811491 | 0.764463 | 0.866477 | 99.474 / 48.851 |

The apparent Arabic SSIM gain from the192stroke is a negative result under MSE and local error. K02 is another essential negative: more regions progressively damage smooth radial appearance. All input cases and all levels remain visible in the dashboard, rather than only the strongest results.

## 1. Geometry oracle: region representation matters, but appearance is not solved

Known original SVG geometry and known original paint render pixel-identically to the saved native control images (fresh actual SVG renders, MSE0). Holding that exact geometry, current flat and gradient fitters produce actual SVGs; d, transforms, fill rules and order are unchanged. All oracle output regions were fitted from samples, with no inherited-solid fallback. Source solids were retained only in initialization; original gradient definitions were removed before fitting.

For K01, exact-geometry gradient D reaches SSIM0.997822, PSNR46.47dB, MSE1.4646; saved reconstructed D128 is0.978980,33.48dB,MSE29.2124. For K02, oracle D reaches0.987726,38.54dB,MSE9.0952; reconstructed D128 is0.913501,31.46dB,MSE46.4684. Exact source geometry therefore materially improves the attainable result under this fitter, but does not recover the known appearance perfectly.

This comparison changes region partition and number of independently fitted appearances, not merely boundary coordinates. Its MSE difference is not a causal percentage attributable solely to contour error. Appearance restrictions remain demonstrable: K01's original middle stop0.45 is absent from the current equally spaced stop family at the same endpoints; fitted endpoints are restricted to sample extent. K02's original radius101 is independent, whereas the fitter derives radius from visible sample extent and restricts focal point to center. Limited optimization can also contribute. No new optimizer was introduced to disguise that residual.

Known-control geometry metrics additionally compare foreground unions at4×: IoU stays approximately0.988–0.993 across levels, holes remain1 for K01 and0 for K02. K02's good outer silhouette alongside severe appearance degradation at higher granularity demonstrates that a correct outer contour is insufficient. These metrics do not certify internal region correspondence, absence of intersections or physical-object topology.

## 2. Exact coverage diagnosis: seams can exist without geometry gaps

The diagonal and reversed-shared-cubic fixtures exactly partition a112×112 square. Rendering two separately painted paths in resvg yields112 and119 native opaque-interior samples with alpha loss, respectively; none is fully uncovered. Their summed deficits are26.353 and20.082 source-pixel equivalents. The single known-union square and the compound representation of these exact controls have zero interior deficit.

This directly supports source-over antialiasing/compositing as a coverage-loss mechanism on exact shared geometry in the tested renderer. Two partially covered adjacent paints can accumulate alpha as a+b(1−a), rather than geometric coverage summing to one. It does not establish a renderer implementation bug, nor show that every real-image hole has the same cause. A deliberate1px geometric gap remains after the stroke; the correction is not a substitute for missing geometry.

Real D128 white-region diagnostics produce3435/3023/2312/0/1889 native interior alpha-deficit samples versus the conditional compound comparison on shield/coffee/cat/Arabic/dice. The real compound is explicitly **not** a Boolean union: winding, holes and overlaps may change its interpretation. Per-region4× alpha occupancy was measured on all five real cases, with zero/multiple counts retained; alpha128 threshold ties are not analytic intersection proofs. Alpha heatmaps distinguish coverage deficits from excess. Seam-location samples, width-radius diagnostics, 1×/4×/16× controls and costs are saved. Only resvg is independently working and verified here; cross-renderer agreement remains unvalidated.

## 3. Corrective intervention: partial coverage gain, measurable harm and residuals

The0.25 matching-fill stroke retains every underlying path d, order, fill, gradient and mask. It adds no new painted shapes or background underlay, but intentionally overlaps neighboring regions. Source and result SVGs are independently checked for exactly those permitted changes. The stroke is reversible by removing its five added attributes; it is not a final geometry engine.

On exact diagonal control it reduces the native coverage deficit26.353→15.918 source-pixel equivalents, while also adding60.549 pixel equivalents of exterior coverage around the square. A single curved exterior control expands coverage by27.290 native pixel equivalents and gains21 thresholded support samples. Exterior damage is a documented failure, not concealed behind improved seam numbers. At4×/16× the SVG stroke width grows in display pixels because it is fixed in source units.

On saved D128 it modestly improves white SSIM/MSE on four real cases and worsens Arabic. On D192 it improves white SSIM on all seven cases and MSE on six; Arabic MSE increases by0.449797 and worst-tile RMSE by0.488962 despite slightly better SSIM. Shield192 alpha MAE falls2.671→1.663, coffee4.098→2.575, cat4.678→2.905 and dice1.579→0.994 (0–255 units). These remain nonzero. Masks do not gain support where source alpha is zero in this sample, but partial alpha and internal appearance still change. Full-background metrics and local errors remain decisive; no global-stroke default is approved.

## 4. Granularity frontier: useful range exists locally, not universally

Real-case RGB path counts grow from22–35 at128 to167–188 at192 and828–1052 at256. Useful detail can return: cat and dice gain SSIM. Yet shield/coffee SSIM decreases192→256, and Arabic's native MSE grows substantially. Cat256 SSIM rises while its MSE worsens relative to192. Higher region count cannot be scored by one metric alone.

The effects interact. More boundaries can recover a feature but also create more AA seams; smaller or thinner regions have fewer usable interior samples and may lose gradient fitting. Coffee's alpha MAE rises1.96→4.10→7.80, and cat1.61→4.68→9.51, across128/192/256. This trend is measured, but cannot be interpreted as an independent additive segmentation-versus-rendering percentage.

At256, shield704/1034 and dice753/1039 regions lack retained interior fitting samples. Their alpha-weighted visible areas are about6.50% and13.24%, respectively; all fallback reasons cover7.92% and18.55%. Known K01 has812/818 no-interior regions covering47.67% of visible sampled area; K02's fallback footprint is27.40%. Some are narrow shading ribbons/rings rather than1×1cells. The fitter's four-neighbor interior erosion and sample minimums thus become an independently observed bottleneck as partitions fragment. The exact error contribution is not isolated by those counts alone.

Visible-area-weighted ≤2×2 RGB paths stay below0.72% on real cases, with ≥99.995% of source-visible alpha weight assigned in the native crispEdges ID diagnostic. This rules out widespread tiny-cell area under **that sampled definition**, not all pixel-equivalent representations. Long thin shading strips, jagged lattice-derived boundaries and source alpha-run masks remain. Low tiny-cell area and many cubic commands are insufficient evidence of professional geometry. The two analytic controls demonstrate that extra luminance-following contours can be artificial even when outer silhouette is accurate.

## Complexity and phase costs

| Case | Detail | RGB paths | Closed subpaths | Cubic segments | Visible≤2px area | Integer-lattice coordinate fraction | D SVG bytes | Fit seconds | Native D render seconds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A01_shield | 128 | 35 | 36 | 1586 | 0.0000% | 0.285 | 56,930 | 3.952 | 0.153 |
| A01_shield | 192 | 188 | 189 | 2890 | 0.0054% | 0.396 | 114,713 | 7.729 | 0.125 |
| A01_shield | 256 | 1034 | 1034 | 4474 | 0.1720% | 0.562 | 238,486 | 10.468 | 0.209 |
| G01_coffee | 128 | 26 | 27 | 1622 | 0.0000% | 0.386 | 54,187 | 3.545 | 0.123 |
| G01_coffee | 192 | 167 | 171 | 3458 | 0.0000% | 0.418 | 144,477 | 9.763 | 0.208 |
| G01_coffee | 256 | 1043 | 1054 | 6504 | 0.1350% | 0.535 | 304,183 | 12.524 | 0.229 |
| G05_chelsea_nativecrop | 128 | 22 | 22 | 1404 | 0.0000% | 0.409 | 44,955 | 3.915 | 0.158 |
| G05_chelsea_nativecrop | 192 | 184 | 184 | 4533 | 0.0000% | 0.440 | 183,793 | 13.359 | 0.193 |
| G05_chelsea_nativecrop | 256 | 1052 | 1055 | 8654 | 0.0290% | 0.504 | 367,625 | 15.956 | 0.214 |
| G06_arabic | 128 | 28 | 55 | 6 | 0.0012% | 0.986 | 182,630 | 0.707 | 0.192 |
| G06_arabic | 192 | 176 | 343 | 30 | 0.0440% | 0.974 | 197,632 | 0.475 | 0.107 |
| G06_arabic | 256 | 828 | 1283 | 176 | 0.7110% | 0.946 | 250,543 | 0.617 | 0.107 |
| G08_dice_alpha | 128 | 29 | 35 | 850 | 0.0000% | 0.342 | 442,407 | 3.875 | 0.239 |
| G08_dice_alpha | 192 | 185 | 219 | 1882 | 0.0003% | 0.446 | 498,155 | 6.672 | 0.250 |
| G08_dice_alpha | 256 | 1039 | 1089 | 2802 | 0.3001% | 0.628 | 583,088 | 3.866 | 0.205 |
| K01_linear_corner_hole | 128 | 25 | 26 | 346 | 0.0000% | 0.315 | 15,971 | 1.912 | 0.109 |
| K01_linear_corner_hole | 192 | 125 | 126 | 328 | 0.0163% | 0.577 | 30,730 | 3.519 | 0.157 |
| K01_linear_corner_hole | 256 | 818 | 819 | 4 | 1.7806% | 0.999 | 68,199 | 0.497 | 0.107 |
| K02_radial_shared_curves | 128 | 18 | 19 | 428 | 0.0000% | 0.272 | 17,889 | 1.304 | 0.142 |
| K02_radial_shared_curves | 192 | 142 | 144 | 1310 | 0.0293% | 0.384 | 55,081 | 1.130 | 0.127 |
| K02_radial_shared_curves | 256 | 773 | 775 | 2088 | 0.9733% | 0.575 | 116,429 | 0.555 | 0.089 |

128phase timings are inherited saved measurements, not new executions. Timing fields and measured resources are retained at each trace/render/fit. Reliable freshly monitored analytic-control sweeps took28.65s and20.47s, sampled process-tree peaks173.75/175.34MiB. Paired192 correction workers took approximately2.9–5.6s, sampled peaks85.2–97.1MiB. Sampling can miss brief peaks and is not an OS memory reservation.

Two post-level historical-spline context attempts stalled after all uniform levels finished; the old outer supervisor encountered Windows AccessDenied during timeout cleanup. Coffee's outer walltime and missing dice outer measurement are **invalid as algorithm-performance evidence**. Their completed numerical outputs were recovered from saved evaluation JSONs and SVG hashes, without refitting. Partial context artifacts and logs remain. A new isolated monitor checks PID+creation-time identity before cleanup and reports uncertain descendants after a bounded wait; short root/child timeout diagnostics passed. No historical supervisor source was edited. A small control-adapter source-path failure is also preserved under negative_results; it happened before any new control trace and was corrected.

Strong saved historical spline outputs are reused as contextual comparisons where complete. They use different clustering/hierarchy and inherited appearance, so they do not isolate granularity. Some can be more faithful than this watershed family at much higher geometric complexity. The stalled optional context comparisons are not relabeled successful, and further context rerendering is disabled by default in reproduction.

## 5. Fine detail and localized appearance

Cat gains some contrast/feature layout with more regions but still loses fur, eyes and thin detail. Coffee loses wood grain and spoon reflections; shield metallic/local highlights remain misplaced; dice's localized reflections remain wrong. Highpass RMSE, edge F1 and worst32px tile metrics quantify residual differences but do not prove which missing contour or illumination feature caused them. No sesame-seed-specific case was added; conclusions about that feature remain untested.

The source appearance often needs additional meaningful localized degrees of freedom. Flat/linear/centered-radial gradients cannot necessarily represent complex illumination or high-frequency texture compactly. Arbitrary photographic pixels cannot be guaranteed exactly with a small fixed set of smooth primitives. This experiment added no detail overlays or micro-paths to inflate scores, and it does not promise a sparse universal solution.

Arabic remains particularly confounded by the inherited pixel-run alpha mask carrying the visible glyph silhouette. No Arabic text recognition, font matching, editable typography or coherent glyph-outline reconstruction is claimed. Transparent dice likewise retains grid-dependent alpha. RGB gains do not solve alpha reconstruction.

## Answers to the separate success questions

1. **Supported mechanisms:** exact shared geometry can suffer AA/source-over coverage loss; region/appearance partition matters in the oracle; granularity is nonmonotonic; fine partitions lose fitting support; localized detail remains absent. Real traced gaps versus compositing loss are not fully separated analytically.
2. **Targeted fix:** matching-paint strokes partially reduce coverage deficits, but do not fully remove them and can damage silhouettes/appearance.
3. **Actual fidelity:** measured paired native improvements occur on several categories, with explicit Arabic and radial-control counterexamples. Scores alone do not establish acceptance.
4. **Generalization:** bounded cross-category evidence, not arbitrary-image guarantees or full native-original-size tests.
5. **Pixel-grid avoidance:** widespread tiny-cell area is low in this moderate range, but thin artificial shading strips and alpha runs prevent a clean-vector claim.
6. **Coherent validity:** SVGs are genuine vectors; fixed-fit geometry/mask invariants pass. Full geometric intersection/topology correctness and professional editability remain unverified.
7. **Near the reference:** no. Even improved192+stroke outputs remain far below the high-fidelity pixel reference on the complex real cases; the architecture and fidelity milestone remain unapproved.

## Next technical recommendation

Retain the current moderate-detail baselines, oracle and coverage fixtures. Do not replace VTracer or apply strokes globally based on this study. The next most informative bounded correction is **coverage-aware appearance fitting on fixed geometry**: explicitly model antialiased mixtures and test fitting support for thin regions instead of discarding their boundary pixels, while preserving the same geometry, source alpha and evaluation split. Use exact oracle controls and192 geometry, compare against the unchanged current fitter, include deliberate contrasting-region boundaries to expose color bleeding, and inspect local/global renders. This targets directly observed support and compositing limitations without adding a new geometry engine.

After that, test appearance-aware region discovery or selective detail reconstruction if errors still demand new boundaries. Constrained geometry/appearance alternation remains plausible, but moving curves alone cannot solve absent fur/reflections or restrictive appearance models. Free stop positions and independent radial radius deserve a separate oracle-only optimization ablation; they were not silently added here. Local overlays and learned models were not implemented. A major new engine requires a new owner decision.

## Reproduction, QA and preservation

Source code, frozen protocol, SVGs, native PNGs, true vector4×/16× crops, error maps, coverage heatmaps, masks, geometry metrics, resource records and negative outputs are retained. Fifteen automated tests pass (3oracle,6coverage,6granularity/correction/visibility/monitor/inventory), with independent QA. Area metrics include occlusion/alpha weighting and explicitly report unassigned samples; they are sampled pixel-center diagnostics, not exact continuous geometry measures. Spatial boundary-band/interior errors are disjoint measurement partitions, not causal error percentages.

No full Clean SVG/Magic Layers work, AI API, force-push, history rewriting or production architecture change was performed. New research is scoped to this experiment. Historical source, owner vision, previous artifacts and negative results are preserved. Git publication remains a separate verified operation; no commit/push is claimed unless confirmed explicitly in the publishing handoff.


## Final governance/publication status

Scope-local code mirrors and provenance pass. Root-wide governance checks remain failing due to existing registry drift and non-UTF8 legacy documentation; their actual logs/exit codes are retained in reports/root_governance.json and root_*.log. Root governance and historical encodings were not silently repaired. Final independent QA and artifact inventory accompany the review package.

Git metadata still has explicit write-deny ACLs for the sandbox. No add/commit/push was retried or claimed; scoped owner-run publication commands and the complete SHA256 change inventory are provided. Baseline local/remote main at start:ec4849376f2bcc74339175e4bd991de83e7dfe0a. Global architecture remains NOT_APPROVED.
