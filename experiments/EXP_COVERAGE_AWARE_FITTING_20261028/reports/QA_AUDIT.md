<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T12:31:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T12:31:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T12:31:24Z"}
END_DOC_PROVENANCE -->
# Independent QA — coverage-aware appearance fitting

## Verdict

**PASS for the bounded research evidence, with partial hypothesis support.** This is not approval of a production fitter, coherent-geometry reconstruction, universal fidelity, or the global architecture. Production architecture remains **NOT_APPROVED**. No additional geometry engine or image experiments were implemented by QA.

Scope: `EXP_COVERAGE_AWARE_FITTING_20261028`, initially based on clean local main `ed6072b15d3f9fca4774856ffcf31909d1785fd7`. Read complete owner vision, preserved inherited fitter, new fitter/driver/fixtures/tests/audit/presentation, README and final REPORT. This report distinguishes independent checks from parent-run checks.

## Independent checks performed

- Reviewed the frozen manifest, all nine completed result/fitting JSONs and saved artifacts. A passive independent checker verified frozen source/baseline hashes, output SVG hashes, map NPZ hashes, ordered visible-path geometry/transforms/fill rules, fixed opacity/masks, and F02 alpha-gradient definition bytes. It rejected raster/script/filter/foreignObject content, unresolved/external references, and gradients exceeding four stops.
- Independently recomputed three-background quantized SSIM/MSE and float composited full/held-out MSE from saved native renders for **all nine cases**, including map closure and final surrogate-versus-actual consistency. All passed. These checks neither refitted nor retraced any image.
- Independently executed two actual-resvg fitter tests (2.021 seconds), six fixture tests (0.128 seconds), and three additional XML adversarial assertions. Mask-gradient mutation is detected, allowed RGB mutation retains geometry signature, and shared RGB/mask gradient dependencies are rejected. Parent separately records the complete final ten-test run with no skips; QA did not repeat that fitting run.
- Visually inspected native Agrad/C/truth renders for both new analytic controls. The narrow bright ribbon and translucent overlap improvements are visible, while scene geometry remains fixed. This is mechanism evidence on known geometry, not independent natural-image generalization.
- Read final REPORT and calibrated its claims against saved metrics. Parent's final artifact integrity reports 285 SVG and 690 PNG files valid; that exhaustive count is parent-run, whereas the independent nine-case core checks above were run by QA.

## Findings and negative results

Actual balanced three-background MSE improves strictly in **seven of nine** adaptive comparisons. The two inherited exact-geometry controls are unchanged; they must not be counted as wins. All five real cases improve full and held-out balanced MSE:

| Case | Agrad MSE | Coverage C MSE |
|---|---:|---:|
| Shield | 213.499165 | 165.437103 |
| Coffee | 275.102417 | 240.358024 |
| Cat | 240.974149 | 217.446841 |
| Arabic | 0.278837 | 0.266571 |
| Dice RGBA | 66.854974 | 53.347058 |
| K01 exact linear geometry | 1.464627 | 1.464627 |
| K02 exact radial geometry | 9.095215 | 9.095215 |
| F01 narrow ribbon/junction | 44.230192 | 9.612598 |
| F02 soft alpha/overlaps | 48.006402 | 1.257869 |

The strongest saved pixel-equivalent references remain substantially better on complex real images. Cat C white SSIM is about 0.5112 versus 0.99982 for its saved pixel reference; Coffee is about 0.6093 versus 0.99789. Better fitted paint does not establish adequate geometry or the extremely-high-fidelity milestone.

Flat B improves balanced MSE in all nine cases but **reduces white SSIM on Shield, Cat, Dice and K01**. Arabic adaptive C worsens black-background quantized MSE by 0.014658 and SSIM by 0.000324 despite improving the primary balanced objective. These negatives are retained explicitly in the report. An aggregate objective is not a guarantee for each background or local feature. The native flat-pair presentation addition is appropriate for exposing this tradeoff.

## Scientific and implementation assessment

The three-background target `Ps + (Ar-As)*mean(background)` is algebraically correct for fixed output alpha in byte-RGB units. Leaving this effective target unclipped while bounding paint coefficients is necessary. Full-scene Wi already includes coverage and opacity; there is no second source-alpha weighting. Residual pseudo-target weighting by Wi squared is equivalent to the intended weighted linear design.

Initial source review found mask-style rejection and accidental removal of alpha-gradient definitions. Both were corrected before the validated outputs. Mutable RGB-gradient definitions are now distinguished from the fixed alpha dependency closure. The completed-result reuse guard now validates frozen inputs before returning and verifies core source/cache/SVG/render artifacts, rather than trusting completion JSON alone.

Ordered RGB geometry, topology, masks and opacity remain fixed across conditions; no new detail paths, strokes or changed contours compensate for failure. Actual rendered alpha nevertheless differs by up to **one byte** for some real adaptive outputs because renderer quantization is paint-dependent; exact XML mask preservation must not be described as byte-identical rendered alpha. Flat B alpha is unchanged in the measured cases. Real transparent inputs retain inherited alpha-grid dependence.

The effective-map model is approximate: eight-bit rendering, unassociation and gradient integration create nonzero closure/random-forward error. Recorded random-color RMSE ranges roughly 0.052–0.414 RGB bytes; final actual renders, not the surrogate alone, support the outcome. Unsupported general SVG paint/compositing constructs remain outside this parser's validated contract.

Periodic train/selection/test pixels are separate for this fitting update, but historical geometry and seeds already used these source images. This is conditional within-image interpolation, not a new statistically independent generalization set. Adaptive C changes objective, coupled support, warm start and schedule together; attribution solely to one erosion mechanism or additive causal percentages would be unjustified. Known thin-region paint recovery is the cleaner direct mechanism check.

Two unchanged exact-geometry controls retain meaningful residuals. Limited inherited gradient endpoint/radius/stop parameterization and proposal optimization can still constrain the result even when geometry is known. Weak or highly correlated contribution maps also make paint recovery nonunique; regularization and seed retention matter. Broad boundary masks include translucent interiors and are not physical contour truth.

## Recommendation and remaining closure

Accept this as evidence that coverage-aware inverse paint fitting fixes a real bounded defect, while preserving the substantial remaining fidelity gap and background/perceptual regressions. Retain it as a research tool. A separately approved bounded geometry/region-refinement comparison is justified; this experiment itself does not authorize that implementation. Preserve all historical work and the complete owner vision.

Final independent closure: all eight Python source mirrors contain their current SHA256 and verbatim declaration snippets; all 53 AST function/class declaration ranges match exactly, with none omitted. All 464 local dashboard href/src targets exist. Viewed the final worst-performing Cat native comparison and actual 16× worst-error viewport: both honestly expose severe lost texture/detail and remaining visible boundary seams, rather than suggesting the small metric improvement solves reconstruction. Source nearest-neighbor and pixel-reference panels are visibly distinguished from spline renders.

Git publication is not certified by QA and no commit/push is claimed. No remaining blocker was found for delivery of this bounded evidence package.
