<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T00:24:17Z", "last_action": "CREATED", "last_change_id": "CHALLENGER-V04-IMPORT", "last_edited_at_utc": "2026-10-18T00:24:17Z", "last_editor": "owner-claude-import", "tracking_started_at_utc": "2026-10-18T00:24:17Z"}
END_DOC_PROVENANCE -->
# Version 04 Challenger — Benchmark Results

**Representation:** hybrid **vector-only** adaptive surface tessellation plus 5-bit/channel source-derived edge-band residual paths. No `<image>` elements / embedded source raster.
**Status:** completed local experimental evaluation; no global approval state modified. The independent verifier regenerated all 12 final SVGs byte-identically: **True**; all were XML-well-formed, rendered at input dimensions, and contained zero embedded raster image elements. The independent verifier regenerated all 12 final SVGs byte-identically: **True**; all were XML-well-formed, rendered at input dimensions, and contained zero embedded raster image elements. The independent verifier regenerated all 12 final SVGs byte-identically: **True**; all were XML-well-formed, rendered at input dimensions, and contained zero embedded raster image elements.

## Protocol

The same 12 supplied PNGs were used at their native dimensions. The consistent Version 01 baseline is `versions/version-01/experiments/preliminary_visual_tests/outputs/A01_v01_vector.svg` through `A12_v01_vector.svg`. Every Version 01 and Version 04 file was rendered with the same local Inkscape CLI to the same width and height. Freshly rendered metrics are the primary comparison; old Version 01 experiment metrics are retained separately for provenance.

Version 04 has two stacked vector-only parts: (1) an adaptive rectangular surface tessellation, with selected local linear gradients, and (2) a source-derived correction only along a 1-iteration 3×3-dilated Canny edge band, quantized to 5 bits per RGB channel and merged into horizontal runs within same-color SVG paths. This second component was selected after the pure surface output showed visible staircase/edge losses. It is **not** semantic object reconstruction and should not be described as a clean, professionally layered SVG.

The edge residual intentionally refers to source edge pixels, so high edge recall partly reflects a source-driven correction. Its complexity cost is real and must be considered beside metrics.

## Per-image results

| Image | V01 PSNR | V04 PSNR | Δ PSNR | V01 SSIM | V04 SSIM | Δ SSIM | Edge F1 V01 → V04 | V04 cells | V04 residual paths | V01 SVG KB | V04 SVG KB |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 19.92 | 30.87 | +10.94 | 0.7444 | 0.9151 | +0.1707 | 0.740 → 0.915 | 9000 | 1951 | 176 | 890 |
| A02 | 19.31 | 27.66 | +8.36 | 0.5897 | 0.8720 | +0.2823 | 0.760 → 0.912 | 9000 | 3638 | 865 | 1462 |
| A03 | 17.26 | 28.46 | +11.20 | 0.5487 | 0.8906 | +0.3419 | 0.840 → 0.928 | 9000 | 5268 | 779 | 1518 |
| A04 | 17.74 | 27.60 | +9.86 | 0.5074 | 0.8565 | +0.3492 | 0.593 → 0.849 | 9000 | 2190 | 566 | 1098 |
| A05 | 20.79 | 27.71 | +6.92 | 0.6561 | 0.8811 | +0.2250 | 0.713 → 0.912 | 9000 | 2502 | 386 | 1104 |
| A06 | 17.94 | 30.27 | +12.34 | 0.4730 | 0.8616 | +0.3886 | 0.773 → 0.954 | 9000 | 4098 | 641 | 1365 |
| A07 | 18.31 | 27.96 | +9.66 | 0.5967 | 0.8847 | +0.2880 | 0.838 → 0.935 | 9000 | 4114 | 908 | 1579 |
| A08 | 17.39 | 28.02 | +10.63 | 0.5364 | 0.8731 | +0.3367 | 0.602 → 0.852 | 9000 | 1290 | 493 | 1062 |
| A09 | 18.12 | 26.04 | +7.92 | 0.7410 | 0.8826 | +0.1417 | 0.789 → 0.806 | 9000 | 1111 | 274 | 836 |
| A10 | 15.62 | 24.61 | +8.99 | 0.7648 | 0.8920 | +0.1272 | 0.849 → 0.864 | 9000 | 1336 | 363 | 938 |
| A11 | 16.73 | 27.99 | +11.25 | 0.5219 | 0.8849 | +0.3631 | 0.806 → 0.928 | 9000 | 4351 | 892 | 1547 |
| A12 | 17.15 | 29.35 | +12.20 | 0.5052 | 0.9030 | +0.3978 | 0.764 → 0.955 | 9000 | 2214 | 739 | 1287 |

## Controlled experiments before the 12-image run

- **S00 known geometry, surface-only baseline:** 320×240, 9000 cells, PSNR 22.15 dB, SSIM 0.8547, SVG 542 KiB. The synthetic source includes nested shapes, highlights, a ring/hole, and a pre-composited soft shadow.
- **S00 hybrid edge-band iteration:** PSNR 25.61 dB, SSIM 0.8947, edge F1 0.682, SVG 651 KiB. This output is explicitly a source-derived hybrid vector representation.

| A01 surface-only leaf budget | PSNR | SSIM | Edge F1 | SVG KiB | Generation ms | Render ms |
|---:|---:|---:|---:|---:|---:|---:|
| 1000 | 21.69 | 0.7491 | 0.564 | 114 | 268.2 | 234.8 |
| 2500 | 23.04 | 0.7940 | 0.689 | 199 | 462.9 | 272.0 |
| 5000 | 24.11 | 0.8307 | 0.767 | 344 | 701.4 | 358.0 |
| 9000 | 24.46 | 0.8536 | 0.789 | 586 | 1077.2 | 539.8 |
These A01 figures are for the **surface-only** iteration before edge residual paths were added; they are a budget diagnostic, not final hybrid performance.

## Aggregate comparisons

- **mse:** V01 mean 1074.58133; V04 mean 109.51544; V04 better on 12/12 images; worse/tied on 0/12.
- **psnr_db:** V01 mean 18.02251; V04 mean 28.04430; V04 better on 12/12 images; worse/tied on 0/12.
- **ssim:** V01 mean 0.59877; V04 mean 0.88312; V04 better on 12/12 images; worse/tied on 0/12.
- **edge_precision_1px:** V01 mean 0.70719; V04 mean 0.83296; V04 better on 10/12 images; worse/tied on 2/12.
  Images where V04 was worse/tied: A09, A10.
- **edge_recall_1px:** V01 mean 0.83918; V04 mean 0.98526; V04 better on 12/12 images; worse/tied on 0/12.
- **edge_f1_1px:** V01 mean 0.75562; V04 mean 0.90089; V04 better on 12/12 images; worse/tied on 0/12.
- **small_edge_component_recall_proxy:** V01 mean 0.78264; V04 mean 0.97407; V04 better on 11/12 images; worse/tied on 1/12.
  Images where V04 was worse/tied: A04.
- **foreground_iou_proxy:** V01 mean 0.92109; V04 mean 0.96288; V04 better on 12/12 images; worse/tied on 0/12.

## Complexity and performance

- Mean V01 SVG size: 590.1 KiB; mean V04 SVG size: 1223.9 KiB.
- Mean V01 path count: 633; mean V04 total paths: 2839; mean V04 residual color paths: 2839.
- Mean V01 estimated path anchors/control points: 34485; V04 path-command point estimate: 120359, plus 9000 rectangles (36000 implicit corners). The V04 estimate excludes implicit SVG rectangle geometry from the path-command point total; rectangles are shown separately.
- Mean V04 surface-generation plus edge-overlay time: 1446.7 ms; median 1517.9 ms.
- Fresh Inkscape render timing (when available): V01 mean 258.0 ms; V04 mean 595.0 ms, based on 12 images.
- Sampled Python-process peak RSS across the full run: 123.9 MiB (10 ms sampler; a sampled process value, not guaranteed to capture the instantaneous system peak).

## Interpretation / failures

PSNR and SSIM compare pixels; Canny edge precision/recall/F1 is threshold- and renderer-dependent. The small-edge-component recall and foreground IoU use heuristic image-derived masks, not annotated semantic ground truth. None of these metrics proves that a human finds the result more editable or professionally composed.

Explicit regressions in this run: edge precision fell on A09 and A10 despite their edge-F1 increases (A09 0.811 → 0.675, A10 0.796 → 0.762); the small-edge-component recall proxy fell on A04. The representation also regresses strongly on object count / ease of editing: every image has 9,000 rectangular cells plus 1,111–5,268 residual color paths; average SVG size grows from about 590 KiB to 1,224 KiB. A semantic/editability score was not measured and semantic reconstruction is not implemented.

The edge-band residual can substantially improve silhouette and thin-stroke metrics, but does so by representing many source pixels as grouped, quantized SVG path runs. This increases file size and object/path counts, and means the improvement is a deliberate detail-preserving hybrid vector representation rather than recovered vector primitives. The axis-aligned base tessellation can still staircase diagonal silhouettes and cannot infer names, ownership, object overlap, meaningful groups, text semantics, transparent material layers, or separable shadows/highlights. Gradient estimates are local rank-1 RGB fits, not physically based illumination or a true optimized gradient mesh. Results should not be generalized beyond these 12 inputs.

## Reproducibility

From repository root: `python versions/version-04-claude-challenger/src/run_benchmark.py --budget 9000 --a01-sweep`. For just final 12-image generation / evaluation, run `python versions/version-04-claude-challenger/src/finalize_metrics.py --budget 9000`. Requires the dependencies in this folder and a local Inkscape CLI. All source inputs and Version 01 artifacts remain unchanged.
