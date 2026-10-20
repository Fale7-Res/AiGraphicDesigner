<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:19Z", "last_action": "EDITED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:59:13Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:19Z"}
END_DOC_PROVENANCE -->
# V04 Image-Guided Repair — 12 Image Results

**Representation:** merged, boundary-aware SVG regions with exact shared pixel-cell edges internally, a smoothed composite silhouette clip, and local multi-stop linear/radial gradients. No source-edge pixel-run stencil; no embedded raster. This is still region-based and not semantic Clean SVG.

## Per-image metrics

| ID | PSNR V01 | PSNR V04 | Δ | SSIM V01 | SSIM V04 | Edge F1 V01→V04 | Paths V01→V04 | SVG KiB V01→V04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 19.92 | 22.89 | +2.97 | 0.7444 | 0.8290 | 0.740→0.813 | 148→442 | 176→289 |
| A02 | 19.31 | 21.79 | +2.48 | 0.5897 | 0.6870 | 0.760→0.661 | 989→924 | 865→624 |
| A03 | 17.26 | 20.79 | +3.53 | 0.5487 | 0.6998 | 0.840→0.750 | 915→946 | 779→599 |
| A04 | 17.74 | 23.46 | +5.73 | 0.5074 | 0.7474 | 0.593→0.699 | 582→588 | 566→487 |
| A05 | 20.79 | 24.09 | +3.30 | 0.6561 | 0.7810 | 0.713→0.629 | 350→564 | 386→365 |
| A06 | 17.94 | 21.64 | +3.71 | 0.4730 | 0.6437 | 0.773→0.675 | 671→782 | 641→545 |
| A07 | 18.31 | 22.07 | +3.77 | 0.5967 | 0.7172 | 0.838→0.779 | 1052→1104 | 908→710 |
| A08 | 17.39 | 23.18 | +5.79 | 0.5364 | 0.7704 | 0.602→0.715 | 552→594 | 493→443 |
| A09 | 18.12 | 21.00 | +2.89 | 0.7410 | 0.8023 | 0.789→0.877 | 219→442 | 274→288 |
| A10 | 15.62 | 18.46 | +2.84 | 0.7648 | 0.7933 | 0.849→0.858 | 290→522 | 363→323 |
| A11 | 16.73 | 21.08 | +4.35 | 0.5219 | 0.7002 | 0.806→0.761 | 993→1078 | 892→688 |
| A12 | 17.15 | 20.69 | +3.54 | 0.5052 | 0.6464 | 0.764→0.710 | 830→948 | 739→573 |

## Aggregates

- **mse:** V01 1074.5813; V04 459.9150; V04 better on 12/12. Regressions/ties: none.
- **psnr_db:** V01 18.0225; V04 21.7634; V04 better on 12/12. Regressions/ties: none.
- **ssim:** V01 0.5988; V04 0.7348; V04 better on 12/12. Regressions/ties: none.
- **edge_precision_1px:** V01 0.7072; V04 0.8181; V04 better on 12/12. Regressions/ties: none.
- **edge_recall_1px:** V01 0.8392; V04 0.6937; V04 better on 1/12. Regressions/ties: A01, A02, A03, A04, A05, A06, A07, A08, A10, A11, A12.
- **edge_f1_1px:** V01 0.7556; V04 0.7439; V04 better on 5/12. Regressions/ties: A02, A03, A05, A06, A07, A11, A12.
- **foreground_iou_proxy:** V01 0.9211; V04 0.9373; V04 better on 8/12. Regressions/ties: A04, A05, A09, A12.

## Controlled synthetic fixture

- Known-geometry input: 320×240; PSNR 25.00 dB; SSIM 0.9349; edge F1 0.872; 220 regions; 182 gradient definitions; SVG 228.1 KiB.
- Fixture includes nested shield layers, highlight patch, ring/hole detail, small marks and a pre-composited soft shadow. It does not validate semantic shadow recovery because the shadow is already baked into the source raster.

## Geometry and runtime

- Mean SVG size: V01 590.1 KiB; V04 494.4 KiB.
- Mean vector regions/paths: V01 633; V04 744. Mean exact region-boundary segments/image: 34749; smoothed silhouette cubic segments: 50.
- Mean V04 generation: 1754.4 ms; V04 render: 294.6 ms; V01 render: 269.8 ms.
- Peak sampled Python-process RSS: 181.4 MiB (10 ms sampling; not a guaranteed instantaneous peak).
- Renderer timings were reused from the prior paired run for 12 V04 and 12 V01 images where regenerated SVG bytes matched and cached PNG dimensions matched.

## Interpretation / limitations

The image-guided repair removes the rectangular tile surface and source-edge micro-path stencil. Local multi-stop linear/radial gradients address the request for real SVG gradients, exact shared internal borders reduce cracks, and a smoothed GrabCut composite silhouette improves outer contour continuity. However, per-object base/shadow/highlight/blur layers are **not** independently recovered yet: the mask is only a foreground/background approximation, and the input is a flattened RGB image. Region boundaries can merge adjacent semantic objects; fine texture is approximated by a bounded number of regions. PSNR/SSIM improved for every input, but edge recall is lower on 11/12 images and edge F1 is lower on 7/12. These remain meaningful detail-preservation regressions. Metrics are pixel/edge proxies, not a professional designer edit test; the visual-reference goals are only partially met.
