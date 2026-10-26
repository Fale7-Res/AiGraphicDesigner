<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-25T15:03:37Z"}
END_DOC_PROVENANCE -->
# Fidelity-first research conclusion

Architecture remains **NOT_APPROVED**. VTracer is the strongest measured native-resolution fidelity baseline in this cycle. Retain it for continued fidelity research; do not replace the production architecture or call the milestone complete. Shield background/shadow and cup tonal transitions remain visibly defective.

## Executed evidence

The owner's preset remains trial_00. Exact version: Python VTracer1.0.0a4, native1.0.0-alpha.4; tagged source/license snapshots and parameter semantics are in reference/ and PARAMETERS.md. Gradient Step maps to layer_difference and does not generate SVG gradients. At0 it also changes diagonal clustering. Simplify is an additional tolerance; path precision rounds coordinates. Their minimum settings are not assumed optimal.

All twelve benchmark originals were traced and rendered by Inkscape at native dimensions:204 primary trials (13 diverse pilots plus4 local probes each),8 frozen-common trials, and20 separately declared follow-up trials. Four fixed-geometry refits each produced3 conditions. Thirty-seven historical SVGs were freshly rerendered; historical generation engines were not rerun. All successful candidates, parameters, metrics and failed/interrupted evidence are retained.

| Condition | Mean SSIM | Mean PSNR dB | Mean edge F1 | Mean DeltaE76 |
|---|---:|---:|---:|---:|
| Owner spline preset | 0.9088 | 26.490 | 0.9403 | 3.575 |
| Original V04 | 0.8831 | 28.044 | 0.8680 | 3.130 |
| Repaired V04 | 0.7348 | 21.763 | 0.7747 | 6.863 |
| Primary per-image selection | 0.9836 | 42.605 | 0.9881 | 0.690 |
| Final selection including follow-ups | 0.9869 | 45.002 | 0.9908 | 0.580 |

Final rows are **post-hoc per-image selection**, not generalization. Primary frozen-preset heldout8 mean SSIM is0.98936; the separately frozen follow-up heldout8 mean is0.99241. These are historical benchmark images held out from configuration selection, not novel-domain data. No universal optimal preset is demonstrated. RESULTS.md, metrics.csv, summary.json and finalists.json contain full per-image measurements, local errors, candidate provenance and complexity.

## Implemented methods and controls

The automatic search prepares images with explicit color/alpha handling, isolates each candidate in a fresh process, renders native SVG, rejects embedded raster/external content, measures a fixed multimetric score and retains rankings. It compares color/binary/watershed clustering, stacked/cutout, spline/polygon/pixel, coordinate precision and simplification. The score combines SSIM, capped PSNR, edgeF1, color difference and highpass error without a complexity penalty. Highest score need not mean highest SSIM or perceptual perfection.

The common configuration was selected on A01/A03/A05/A10 using only shared pilots, frozen, then applied to eight holdouts before their per-image search. Local probes often become no-ops after pixel mode wins; these retained failures do not establish exhaustive optimization.

Visible-support color fitting keeps geometry fixed, verifies ownership using two bijective RGB-ID renders, then fits each visible path's mean color. Crisp-edge rasterization produced no change. Color refit gave negligible gains and a negative logo SSIM change, so expansion stopped after four cases. The tiny shield gain is retained as a numerical finalist, not presented as a breakthrough.

A subsequent bounded control compared pixel cutout/stacked and layer_difference0/1. Cutout0 provided no composite advantage over stacked0. The frozen stacked1 condition improved eleven final selections but did not fix the shield. The0→1 effect also changes diagonal clustering, so it cannot be attributed to a single smooth-gradient threshold. No new pixel patches or learned model were added.

## Failure interpretation and acceptance

The high-fidelity winner uses dense pixel-derived paths: primary selections have about35,547–80,443 paths; final selections about35,815–82,216. Genuine SVG with no embedded bitmap is not compact professional artwork. All path commands, control coordinates, rectangles, bytes, CPU/wall and separate parent/child peak memory are recorded; zero cubics is not zero geometry. Complexity is accepted for this milestone, not disguised.

Before results, research gates proposed all-image SSIM≥0.95, mean≥0.97, PSNR≥30dB, edgeF1≥0.90, meanDeltaE76≤3, no raster and no critical visual loss. These are proposals, not owner approval. Shield PSNR remains approximately24.41dB and its broad shadow is flattened. **The milestone fails**, despite improved fine details and high mean metrics.

The failed fixed-geometry refit suggests smooth-region loss is substantially a clustering/flat-paint representation problem, not merely color optimization. That is an inference, not proof of one universal cause. Spline smoothing also loses real detail. Semantic understanding was not required to expose these numerical failures; adding segmentation AI alone would not restore tonal variation inside constant-fill shapes. No AI training, paid API or local model is warranted by this bounded experiment.

## Visual, color and reproducibility limits

Native review supports improved seeds, materials and lettering, with background banding still visible. VISUAL_REVIEW.md records case-specific observations. comparisons_final/ holds source/owner/final/V04/Repair sheets and enlarged crops. Enlarged PNGs are nearest-neighbor native renders, not higher-resolution truth; renderer_check/ separately contains actual4x SVG renders on two cases.

CairoSVG and Inkscape primary Burger/calligraphy renders were identical; this does not validate all candidates/renderers. All twelve originals are untagged RGB assumed sRGB. Declared profiles are converted to sRGB and alpha explicitly flattened on white. Synthetic raw-alpha failures are retained; a transparent image causes a native failure in one mode. White-composited fixtures and sRGB-profile identity passed, but arbitrary ICC transforms and transparent SVG reconstruction are unvalidated.

Local detail metrics use fixed4x4 tiles, highpass residuals and20historically confirmed seed centers. They are not comprehensive seed detection precision/recall, semantic segmentation accuracy, or Arabic OCR. Exact Arabic lettering resemblance does not provide editable fonts or shaping.

QA distinguishes one independently rerun byte-identical Burger candidate, recomputation from saved renders, and fresh historical rerenders. Recovery records document corrupted PNGs regenerated from unchanged SVGs. The reproduction launcher prepares a fresh destination and refuses existing directories; its preparation was tested, but the full already-completed benchmark is not needlessly replayed at packaging time. Linux/WSL Python3.12 and Inkscape1.2.2 are the measured environment; native Windows is not certified.

## Next priorities and full owner vision

Next, isolate smooth low-contrast cluster loss by comparing variance-constrained clustering against a limited smooth-paint representation on identical residual regions, with held-out evaluation and a finite budget. This recommendation is unimplemented. Do not compensate blindly with thousands of patches or indefinite iterations.

After fidelity acceptance: complexity reduction under a fidelity-loss budget; semantic object ownership/occlusion and Magic Layers; surgical layer edits; planned generation with approved-preview/layer recomposition consistency; Arabic/Latin typography, shaping and unseen-glyph/font-identity tests. OWNER_SCOPE.md maps these to the complete owner vision. No end-to-end implementation of these later requirements is claimed.
