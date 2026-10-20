<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:16Z", "last_action": "CREATED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:55:16Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:16Z"}
END_DOC_PROVENANCE -->
# V04 Image-Guided Repair — Root-Cause Analysis

## Reference requirements

The supplied review sheet is treated as the acceptance reference for this iteration. It calls for (1) logically grouped base/shadow/highlight appearance, (2) genuine SVG gradients rather than small color tiles, (3) blur represented separately where possible, (4) accurate smooth outside edges, and (5) high fidelity without a pixelated appearance.

The owner's original vision remains the authoritative long-term specification: professionally editable, semantically organized Clean SVG, not only a visually similar but fragmented SVG.

## Defects in the previous V04 approach

The previous challenger emitted an adaptive rectangular tessellation and then overlaid color-quantized source pixels along a dilated Canny edge band. This could improve PSNR, SSIM and edge recall, but it reproduced raster pixel locations rather than finding clean geometry. Consequences were:

- axis-aligned stepping / visible squares around diagonal shapes and calligraphy;
- thousands of tiny path runs following source pixels;
- SVGs whose high-level layer names did not correspond to meaningful objects;
- no separate representation for object base color, cast shadow, specular highlight, or optical blur;
- the false impression that better raster metrics alone meant better editability.

Version 01 has a different core bottleneck: global CIELAB color quantization (default 16 colors) occurs before contour extraction and Bézier fitting. Lost color variation and details cannot be restored by smoothing the remaining contours. Its contour/painter-order strategy also does not build a full object occlusion graph.

## Repair implemented

The source-edge stencil has been removed. Version 04 now:

1. creates perceptual SLIC superpixels from a lightly bilateral-filtered image;
2. merges adjacent superpixels using a cost balancing a 2D quadratic RGB surface-fit error with measured Lab boundary contrast;
3. traces closed region boundaries on integer pixel-cell edges, so adjacent regions share precisely the same internal coordinates and do not create independently smoothed cracks;
4. models each region with a flat fill or a locally measured multi-stop linear/radial SVG gradient;
5. estimates only a coarse foreground/background composite mask with CPU GrabCut, then simplifies and fits a cubic-curve representation to the *outside silhouette*; complementary clip paths confine the same region surface to foreground and background;
6. adaptively allocates approximately 220–560 regions based on edge density and how broadly those edges are distributed through the image, instead of one fixed count for every image;
7. emits SVG path and gradient elements only—no embedded image, data URI, external raster, or source-edge micro-path stencil.

This specifically fixes the old rectangular-tile appearance, preserves actual gradient primitives, ensures exact shared internal borders, and improves the smooth composite outer contour.

## What's not solved

- GrabCut labels one coarse composite foreground/background split; it does **not** identify every object, its depth order, or object-specific shadows.
- The SVG does not yet recover a guaranteed, independently editable `base`, `shadow`, `highlight`, and `blur` stack for each semantic object. It preserves the already-composited appearance using local gradients and region fills. A single flattened RGB source is under-constrained for unique recovery of those layers.
- Internal region borders are exact/shared but are not all smooth Béziers; smoothing them independently would recreate the cracks observed in the previous implementation. A topology-constrained shared-curve graph is the right next step.
- Fine texture is approximated by a bounded number of regions. PSNR/SSIM improves across all 12 benchmark images, but edge recall regresses on 11/12 and edge F1 on 7/12. Some thin texture details therefore remain missing. This is explicitly reported.

## Evidence from controlled tuning

A higher-detail configuration (1,300 starting SLIC segments, up to ~800 target regions) improved some images further. Example: A02 edge F1 rose from 0.661 at 461 target regions to 0.767 at 692 regions. A09 improved from 0.877 at 220 regions to 0.900 at 396 regions in one 1,600-start-segment tuning run. However, high-region/high-start configurations caused the full benchmark run to exceed the local tool's execution window on the hardest image; they were therefore not adopted as the default and are not mixed into the final 12-image table. Partial tuning outputs are preserved separately as exploratory data where complete parameter rows were recorded.

## Summary

This iteration addresses the visible pixel-tile and outside-edge issues without an embedded raster. It is a meaningful step toward the image's requirements, not a claim that semantic layer decomposition, blur recovery, or professional object-level editability is solved. See `experiments/metrics/RESULTS_REPORT.md` for complete per-image numbers and named regressions.
