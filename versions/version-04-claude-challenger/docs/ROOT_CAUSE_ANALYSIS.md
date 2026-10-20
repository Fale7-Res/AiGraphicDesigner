<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T00:24:16Z", "last_action": "CREATED", "last_change_id": "CHALLENGER-V04-IMPORT", "last_edited_at_utc": "2026-10-18T00:24:16Z", "last_editor": "owner-claude-import", "tracking_started_at_utc": "2026-10-18T00:24:16Z"}
END_DOC_PROVENANCE -->
# Independent Root-Cause Analysis — Version 01 Fidelity Limits

## Scope and baseline selection

The owner's Arabic source of truth is `docs/product/OWNER_ORIGINAL_VISION.md`. It asks for semantically organized, professionally editable Clean SVG that retains shapes, coherent overlapping objects, colors, gradients, shadows, highlights, and the source design's visual identity. Its intent is not met merely by a valid SVG or by converting every local shade into an independent path.

For the controlled 12-image comparison, the baseline is the committed Version 01 files `versions/version-01/experiments/preliminary_visual_tests/outputs/A01_v01_vector.svg` through `A12_v01_vector.svg`. Other Version 01 experiments include A01-specific diagnostic/revised outputs and different renderer settings; these were not mixed into the 12-image baseline. The repository's prior `all_12_rerun_metrics.json` is preserved as provenance, but the primary results here use **fresh Version 01 and Version 04 renders from the same Inkscape CLI** at the input's native pixel dimensions.

## Findings grounded in source and observed outputs

### 1. A small global palette is a structural bottleneck for photographs

`versions/version-01/src/pipeline.py::SequentialPipeline.process_image` applies a bilateral filter and color quantization in CIELAB, defaulting to `n_colors=16`. It then traces contours in the quantized label map. This works as a posterization/illustration strategy but creates a hard limit: detail and smooth color variation discarded by quantization cannot later be restored by fitting a more elaborate boundary. Food textures, fine highlights, and broad illumination become a small number of solid-color islands.

### 2. Contour tracing does not guarantee truly shared boundaries

The implementation discovers contours for each label/cluster and uses OpenCV's `RETR_CCOMP` hierarchy plus `approxPolyDP`, then fits Bézier segments. CCOMP describes a two-level component/hole hierarchy, not a complete semantic overlap scene graph. Independently extracted contour boundaries can approximate the same boundary differently on opposite sides; later filling/stroking may create edge swell, seams, or tiny gaps. The output's 0.75 px default stroke is especially consequential on thin details. A curve fitter can smooth the trace it receives, but cannot restore geometry that palette quantization removed.

### 3. Global area ordering is not object occlusion reasoning

The current pipeline orders color clusters by global pixel count. Large-region-first ordering is a heuristic, not a per-object depth/occlusion graph. It does not establish that a tomato is in front of a plate, a logo ornament sits above lettering, or a shadow belongs to a particular object. This can misrepresent overlaps even if each contour is individually smooth.

### 4. The optional gradient fit is local and limited

`estimate_linear_gradient` performs a simple spatial linear regression on the pixels inside a contour, applies variance / fit-quality thresholds, and emits a linear gradient only when its single-direction regression passes. This is not an optimized gradient mesh, multi-material surface, or a decomposition into base color, specular highlight, cast shadow, ambient occlusion, and transparency. One linear direction cannot model two-dimensional lighting patterns, sharp highlight boundaries, or layered translucent materials reliably. The source imagery also arrives already composited, so material/illumination layers cannot be uniquely inferred from RGB alone.

### 5. The architecture description overstates the implemented pipeline

The source inspected for Version 01 imports OpenCV and NumPy and implements filtering, clustering, contours, and a custom Schneider-style Bézier fit. The inspected `pipeline.py` does not implement SAM 2 object masks or LaMa inpainting. Those are hypotheses described elsewhere, not stages in this executable implementation. No benchmark credit is given for those unimplemented steps.

### 6. Existing metrics needed a renderer-consistent rerun

The repository's documented Version 01 all-12 measurements average about 18.19 dB PSNR / 0.6218 SSIM for its recorded run. This is historical project data, not assumed to equal a new Inkscape render. On the current same-renderer protocol, the selected baseline averages 18.02 dB PSNR and 0.5988 SSIM; small differences from the recorded run are plausible because metrics depend on render/export settings. Both sources of measurements are retained separately.

## Why the challenger changed after visual inspection

The first Version 04 iteration used only adaptive rectangular cells and local gradients. It improved pixel metrics, but the contact sheet showed visible stair-stepping around Arabic calligraphy and logo silhouettes; most edge recall values remained below the source. That was a real geometric regression which PSNR/SSIM alone understated.

The second iteration added a **quantized source-edge residual**, not an invented object detector: detect Canny edges in the original, dilate one 3×3 neighborhood, quantize RGB colors in that narrow band, run-length encode same-color horizontal spans into SVG subpaths, and paint those spans above the surface approximation. This restored source-aligned edge detail without embedding a raster. It also increased path counts and SVG size, so the improvement is a compromise rather than a free win.

## Root-cause conclusions by objective

| Objective | Version 01 failure mode | Version 04 response | Remaining problem |
|---|---|---|---|
| Geometry / silhouette | contour smoothing, stroke swell, no explicit shared-edge graph | non-overlapping base cells + source-derived edge residual | residual follows raster pixels instead of recovering vector curves; edge precision regresses on A09/A10 |
| Color / illumination | 16-cluster palette; optional one-direction local gradient | local per-cell color fits, adaptive detail allocation | gradient discontinuities; no physical/material layer decomposition |
| Complexity / editability | hundreds of smooth paths on average | 9,000 base rectangles plus many edge-color paths | substantial path / file-size increase; not practical as clean editable art |
| Semantics | no robust object grouping/depth inference | deliberately deferred | no object identity, named layer tree, live text, separable shadows/highlights |

## Decision

Version 04 is a useful independent **pixel-fidelity experiment**, not an architecture replacement recommendation. It demonstrates that color/edge residuals can improve a raster similarity objective on this benchmark; it does not demonstrate that raster-to-SVG semantic decomposition is solved. A future production candidate should combine a shared-boundary planar graph / topology constraints, boundary-aware region segmentation, curve simplification with a visual-error budget, and explicit appearance layers. It should compare a low-complexity mode and a fidelity-first hybrid mode, and must be judged by designer edit tasks as well as raster metrics.
