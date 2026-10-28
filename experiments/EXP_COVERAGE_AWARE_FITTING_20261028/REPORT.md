<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T05:38:04Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T05:38:04Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T05:38:04Z"}
END_DOC_PROVENANCE -->
# Coverage-aware appearance fitting — bounded technical conclusion

Production architecture **NOT_APPROVED**. This is an isolated research implementation, not a production default or completion of visual fidelity, Clean SVG or Magic Layers. The complete owner vision—including image generation, Arabic and general typography, semantic layers and professional editing—remains authoritative and unchanged.

## Decision

**Partial support for the primary hypothesis.** Boundary-aware inverse compositing repairs a real appearance-estimation defect on known narrow colored regions and improves the saved five-category real-case reconstruction under the tested geometry and renderer. It does not bring complex images close to the pixel-equivalent reference. Coverage holes, missing geometry, texture and appearance-capacity restrictions remain. Another minor fitter optimization should not be the main next research investment.

## Scope and controls

Local HEAD, tracking main and GitHub API main verified `ed6072b15d3f9fca4774856ffcf31909d1785fd7`; initial working tree clean. No historical files or owner vision were edited. Frozen inputs/manifest.json records source/baseline SHA256, protocol and budgets before fitting. Five real cases reuse unstroked detail192 RGB spline geometry and fixed masks; two old controls reuse exact source geometry; two new CC0 compact known-vector controls test subpixel ribbon, shared curves, strong contrasts, junction, hole, boundary highlight, source-over overlaps and soft vector alpha. No140searches, geometry sweeps or traces were rerun.

Four fitted conditions: Aflat and Agrad are inherited interior-only flat/adaptive paint; B is coverage-aware flat; C is coverage-aware adaptive flat/linear/radial, at most four equally spaced stops. All preserve the same ordered visible path data, transforms, fill rules, group/path opacity, mask geometry and alpha-gradient dependencies. There are no new shapes, strokes, geometry movement, stop-opacity changes or topology edits. Pixel-reference SVGs and known truth render separately. The two old controls' pixel references are saved fixed-pixel traces, not a new adaptive search. New controls have true source SVG but no pixel trace.

Seven existing baselines are copied byte-for-byte, not refitted. They are rendered once for a common evaluation and alpha check. For the two new controls only, a disclosed adapter gives the old fitter temporary opaque/unmasked geometry, then transplants only fitted RGB paint into the exact original masked/opacity scene. This is the old fitter's limitation, not an opaque-versus-transparent comparison. Initial visible colors are uniform gray; unused original RGB truth gradients are stripped before fitting. Truth paint parameters are used only after fitting for diagnostic evaluation.

## Why the old fitter misses information

See reports/BASELINE_AUDIT.md for precise original source line references and hashes. `_ownership` requires exact ID color, alpha255 and four-neighbor agreement, rejects viewport edges, then removes source-alpha-zero samples. This deliberately avoids assigning mixed colors to one region, but excludes most partial-coverage information. No interior samples retain inherited flat paint; insufficient split counts prohibit gradient validation. At detail192,335/900 regions across five cases have no interior samples. Arabic contributes175 nearly invisible regions, so this count is not335 useful lost features. Paint order is retained but inverse source-over is absent; independent fitting of a translucent composite and later restoring opacity can mix it twice.

## New measured model and optimizer

For each visible path, render the full fixed SVG with every RGB path black and that path white. Preserve all opacity, masks and ordering. Difference from the all-black premultiplied render estimates its effective contribution Wi after occlusion/compositing. It is not an isolated geometric area coverage map. All-white and random-color render controls check closure and linear prediction. NPZ arrays are optimizer/diagnostic evidence and are never embedded in SVGs.

The fitted premultiplied prediction is Pblack + sum(Wi*paint_i). For equal MSE over white, black and bluegray backgrounds, use target `Ps + (Ar-As)*mean(background)`; leave the target unclipped, constrain paint RGB to0–255. Wi already contains alpha, so there is no second source-alpha weighting. This minimizes a three-background objective up to a fixed alpha-dependent constant; it cannot solve alpha error. Raw source-over mixtures are never treated as an opaque region's observed paint.

Flat B uses bounded coordinate least-squares with a tiny1e-4 train-only ridge toward the original flat seed and selection checkpointing. C starts from the better selection score of Agrad/B and makes two deterministic regional residual-fitting passes using the inherited appearance model/search. It preserves the same family and four-stop capacity, but changes the coupled objective, boundary samples, warm start and iteration schedule together. Thus C's gains establish this fitting strategy, not a causal percentage attributable solely to erosion or an equal-compute optimizer ablation. Known thin-region flat-paint recovery is the cleaner direct mechanism test.

Train/selection/test pixels follow `(x+3y)%5`:012/3/4. Selection chooses models/checkpoints; partition4 does not affect decisions. This is interpolation within the same source, and historical geometry/seeds already used the image. It is not unseen-image statistical generalization. Region diagnostic scores are contribution-weighted final mixed-pixel residuals, not uniquely identifiable independent paint errors.

## Native results

SSIM below is actual white-background SVG rendering. Balanced MSE is float composited byte-RGB error averaged across three backgrounds; other native quantized metrics, PSNR, alpha, premultiplied RGB, boundary/interior and worst tiles remain in reports/metrics.csv and case JSONs. Strict adaptive improvements occur on7/9 cases; the two old exact controls are unchanged. All five real cases improve actual and held-out balanced MSE. Analytic and real results are not pooled into a universal-performance claim.

| Case | Pixel SSIM | Interior Agrad SSIM | Coverage C SSIM | Agrad → C balanced MSE | Held-out Agrad → C MSE |
|---|---:|---:|---:|---:|---:|
| A01_shield | 0.995660 | 0.832419 | 0.834470 | 213.4992 → 165.4371 | 209.7854 → 165.5270 |
| G01_coffee | 0.997894 | 0.597912 | 0.609277 | 275.1024 → 240.3580 | 271.5926 → 242.0580 |
| G05_chelsea_nativecrop | 0.999823 | 0.502264 | 0.511164 | 240.9741 → 217.4468 | 242.5280 → 222.0448 |
| G06_arabic | 0.999999 | 0.999664 | 0.999730 | 0.2788 → 0.2666 | 0.3487 → 0.3218 |
| G08_dice_alpha | 0.999622 | 0.920880 | 0.924511 | 66.8550 → 53.3471 | 68.7683 → 56.9531 |
| K01_linear_corner_hole | 0.999464 | 0.997822 | 0.997822 | 1.4646 → 1.4646 | 1.4657 → 1.4657 |
| K02_radial_shared_curves | 0.998299 | 0.987726 | 0.987726 | 9.0952 → 9.0952 | 9.0835 → 9.0835 |
| F01_thin_shared_junction_hole | none; truth1.0 | 0.958858 | 0.985081 | 44.2302 → 9.6126 | 43.1584 → 9.5474 |
| F02_soft_alpha_overlap_highlight | none; truth1.0 | 0.965461 | 0.996575 | 48.0064 → 1.2579 | 47.9756 → 1.2506 |

The remaining pixel-reference gap is large. Shield, Coffee, Cat and Dice remain visibly incomplete despite better fitted paint. There is no evidence here that existing spline segmentation is sufficient for extremely high fidelity. For exact K01/K02, coverage fitting leaves the old residual unchanged: endpoint/radius/stop restrictions and optimization capacity remain relevant. A correct outer/source contour and broad gradient-family membership do not guarantee that the restricted parameterization can reproduce known source shading.

## Negative and limited results

Flat B lowers balanced MSE on all9 cases but lowers white SSIM on Shield, Cat, Dice and K01. It is not a safe perceptual default. Arabic C also worsens black-background quantized MSE by0.014658 and SSIM by0.000324 despite its balanced objective gain. Individual background errors and local worst tiles are reported even when aggregate error decreases. No optimization was continued simply to eliminate those negatives.

| Case | Aflat → B white SSIM | Aflat → B balanced MSE |
|---|---:|---:|
| A01_shield | 0.785448 → 0.784195 | 546.5602 → 521.4510 |
| G01_coffee | 0.546755 → 0.547799 | 356.7881 → 345.5556 |
| G05_chelsea_nativecrop | 0.412251 → 0.410178 | 346.8511 → 338.3127 |
| G06_arabic | 0.999664 → 0.999730 | 0.2788 → 0.2666 |
| G08_dice_alpha | 0.904186 → 0.903193 | 91.6449 → 84.2431 |
| K01_linear_corner_hole | 0.854810 → 0.854623 | 1150.0181 → 1149.6078 |
| K02_radial_shared_curves | 0.859566 → 0.861693 | 705.5785 → 704.4289 |
| F01_thin_shared_junction_hole | 0.675351 → 0.696585 | 1929.7725 → 1892.6228 |
| F02_soft_alpha_overlap_highlight | 0.853876 → 0.868684 | 318.2219 → 265.2940 |

Known flat thin-region paint RMSE improves104.119→6.260 bytes for the0.849px F01 ribbon and103.521→8.643 for the0.671px translucent F02 ribbon under B. These are actual known paint-color comparisons, distinct from final image fidelity. Some originally exact solid paints acquire small biases, demonstrating coupled model compensation rather than perfect paint recovery. reports/paint_recovery.json evaluates all fitted conditions on known-flat regions; reports/critical_feature_errors.json covers the hole, junction, highlight, overlap, soft-alpha and thin-feature boxes. These residuals can detect deterioration but cannot uniquely attribute every boundary error to color bleeding.

Coverage is not repaired. Alpha masks/opacity are fixed exactly in XML; native alpha can change by one byte for gradient paints due to renderer quantization, which is measured, not hidden. Flat B alpha is unchanged. No large underlay, duplicated shapes or stroke correction is used. Source-grid alpha-run dependence remains on real transparent inputs, especially Arabic/dice. Approximate coverage probes can explain RGB changes, not manufacture missing support or correct a silhouette.

## Identifiability, resources and geometry quality

Unobservable/weak regions retain seed information or regularization; adding their nominal path count to 'successfully fitted thin regions' would be false. Gram positive-rank ratios exclude thresholded null modes and are not full condition numbers. Highly correlated mixtures or weak opacity make inversion poorly conditioned. The random-color and final-forward checks in fitting.json quantify byte-quantized surrogate mismatch; all acceptance claims use actual exported SVGs.

| Case | Old zero-interior regions | New unobservable regions | Effective Gram positive rank / regions | Condition ratio |
|---|---:|---:|---:|---:|
| A01_shield | 86 | 0 | 188 / 188 | 8.78e+04 |
| G01_coffee | 19 | 0 | 167 / 167 | 1.09e+03 |
| G05_chelsea_nativecrop | 5 | 1 | 183 / 184 | 207 |
| G06_arabic | 175 | 18 | 158 / 176 | 9.44e+08 |
| G08_dice_alpha | 50 | 20 | 165 / 185 | 1.91e+08 |
| K01_linear_corner_hole | 1 | 0 | 3 / 3 | 5.97 |
| K02_radial_shared_curves | 1 | 0 | 3 / 3 | 4.99 |
| F01_thin_shared_junction_hole | 1 | 0 | 7 / 7 | 112 |
| F02_soft_alpha_overlap_highlight | 1 | 0 | 5 / 5 | 438 |

| Case | RGB paths | Cubic segments | ≤2px bbox paths | Integer lattice fraction | Map / fit / worker seconds | Sampled peak MiB |
|---|---:|---:|---:|---:|---:|---:|
| A01_shield | 188 | 2890 | 2 | 0.396 | 21.35 / 34.70 / 92.30 | 306.48 |
| G01_coffee | 167 | 3458 | 0 | 0.418 | 17.47 / 37.39 / 107.47 | 229.07 |
| G05_chelsea_nativecrop | 184 | 4533 | 1 | 0.440 | 21.21 / 48.51 / 116.05 | 239.77 |
| G06_arabic | 176 | 30 | 172 | 0.974 | 25.92 / 2.44 / 46.05 | 242.12 |
| G08_dice_alpha | 185 | 1882 | 23 | 0.446 | 37.09 / 29.84 / 101.10 | 271.13 |
| K01_linear_corner_hole | 3 | 3 | 0 | 1.000 | 0.38 / 1.14 / 10.86 | 93.73 |
| K02_radial_shared_curves | 3 | 6 | 0 | 1.000 | 0.36 / 1.70 / 14.76 | 97.80 |
| F01_thin_shared_junction_hole | 7 | 11 | 0 | 0.915 | 0.40 / 2.26 / 11.09 | 93.66 |
| F02_soft_alpha_overlap_highlight | 5 | 16 | 0 | 0.914 | 0.44 / 2.63 / 11.80 | 94.24 |

No worker hit900s/4GiB or300s fit limits. Resource measurements include50ms requested process-tree RSS sampling and can miss short peaks. Maps are capped200MiB uncompressed. Native/zoom renderer measurements and fitting times are saved separately. The measured scene has no CSS/filter/blend/use/strokes and uses explicit opaque RGB paint with separate opacity/masks; arbitrary SVGs, implicit RGBA color literals and other renderers remain unsupported/unvalidated.

RGB geometry is exactly fixed across Aflat/Agrad/B/C, so path counts, subpaths, Bezier counts, bounding-box scale distribution and lattice alignment cannot improve or worsen in this experiment. This rules out *new* pixel-mosaic geometry, not inherited grid dependence or professional vector quality. Prior visible-area microgeometry findings remain applicable to the identical baselines. Arabic is strongly lattice-aligned and alpha masks may use pixel runs. Valid XML, many curves and low tiny-cell counts are not proof of coherent semantic geometry or valid topology.

## Validation and owner evidence

Ten automated tests pass with actual resvg enabled: fractional source-over coefficients, subpixel support, soft alpha preservation, cache-corruption refusal, fixture truth/geometry licensing/hashes, split/protocol contract and the three-background objective identity. Initial test discovery skipped the two renderer tests when one environment variable was omitted; the final recorded run supplies it and passes all10 with no skips. Independent QA checks exported geometry/mask dependencies, map hashes, actual metrics and sample policy; see reports/QA_AUDIT.md. Final reports/integrity.json independently recomputes MSE/held-out metrics, parses every SVG, rejects embedded raster/script/foreignObject, verifies all PNGs and checks worker success. It does not prove arbitrary nonintersection or global topology.

index.html shows every case, worst first, with source, strongest saved pixel reference, Agrad/B/C, errors, alpha/coverage maps, full SVGs and native PNGs. Real SVG viewport crops render at1×/4×/16×. Source NN crops are pixel displays, not high-resolution geometry ground truth. Large photo defects and unchanged old controls are retained prominently. Historical negative results are unchanged. Root-wide provenance verification is recorded read-only and has preexisting global failures; scoped source mirrors/provenance are validated separately rather than modifying history.

## Exact next recommendation

Keep this fitter as a research tool, not a global default. It establishes that appearance estimation near boundaries is correctable, but the magnitude and visual residuals do not justify spending the next cycle solely on another small fitter tweak. Recommend an owner-approved bounded **appearance-aware local region/geometry refinement** study: freeze this fitting method, use saved residual maps to nominate a small fixed budget of contour/region changes across Shield, Coffee, Cat and an alpha/control case, and compare against identical fixed-geometry paint-only optimization. Separately control movement of existing boundaries versus addition of one compact local region, so missing contours/detail can be distinguished from insufficient appearance capacity. For smooth known controls, an independently bounded free-endpoint/radius appearance control would test the remaining parameterization ceiling, not replace the geometry study.

Reject blanket global strokes (coverage/silhouette tradeoff), indiscriminate segmentation increases (previous nonmonotonicity/seams/fallbacks), pure path-count reduction, and another pixel-cell fidelity shortcut. No new reconstruction architecture or refinement engine has been implemented here. A larger change requires owner approval. Visual-fidelity and overall architecture remain unapproved pending owner review.

## Git and preservation

All changes are under this new experiment only; tracked historical files remain unchanged. A fresh normal `git ls-remote origin refs/heads/main` failed in this execution context with `schannel: AcquireCredentialsHandle failed: SEC_E_NO_CREDENTIALS (0x8009030e)`. GitHub connector independently confirms the main SHA above. Protected Git metadata was not repeatedly retried; no commit or push is claimed. The delivered scoped owner-run publisher verifies main/origin, inventory hashes and remote equality, stages only this experiment, commits with `[AGD-CODEX-RESEARCH]`, pushes normally and verifies the remote SHA. It never force-pushes, merges or rewrites history.
