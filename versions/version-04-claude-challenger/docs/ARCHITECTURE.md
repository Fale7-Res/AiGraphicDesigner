<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T00:24:16Z", "last_action": "CREATED", "last_change_id": "CHALLENGER-V04-IMPORT", "last_edited_at_utc": "2026-10-18T00:24:16Z", "last_editor": "owner-claude-import", "tracking_started_at_utc": "2026-10-18T00:24:16Z"}
END_DOC_PROVENANCE -->
# Version 04 — Algorithm and Output Architecture

## End-to-end flow

```text
RGB raster (native pixel grid)
        |
        +--> RGB integrals + Sobel edge energy
        |        |
        |        +--> adaptive quadtree splits ranked by reducible local SSE
        |                  |
        |                  +--> per-leaf flat fill or locally fitted SVG linearGradient
        |                                  |
        |                                  +--> base vector surface SVG
        |
        +--> grayscale Canny(80, 160) --> one 3x3 dilation --> edge-band mask
                                                |
                                      source RGB quantized to 5 bits/channel
                                                |
                                  same-color horizontal run-length encoding
                                                |
                                      SVG paths grouped by quantized color
                                                |
                       base surface + source-derived edge paths (hybrid vector-only SVG)
```

## Surface reconstruction

`src/challenger.py::IntegralStats` precomputes integral images for each RGB channel, squared channel values, spatially weighted channel values, and a Sobel-derived edge-energy field. Rectangle sum and local linear-fit statistics are therefore evaluated from a constant number of integral-image reads per candidate, rather than walking every pixel again for each leaf.

For a cell, a flat-color model has residual sum of squares (SSE)

\[
E_{flat} = \sum_{p\in R} \|I(p)-\bar I_R\|_2^2.
\]

A spatial linear RGB fit is estimated from the first moments. The spatial/color slope matrix is factorized with SVD; a rank-1 direction supplies a candidate SVG linear gradient. Its residual is accepted only when the relative and per-pixel SSE gains exceed the configured thresholds and the cell is large enough. A local gradient is an appearance approximation, not a physically meaningful shader or decomposed material layer.

The algorithm starts with the full image rectangle. Each candidate split divides a rectangle along integer midpoints into two or four non-overlapping cells. A priority queue splits the leaf whose children are predicted to remove the largest amount of current representation SSE per additional leaf, with a modest edge-energy multiplier. Splitting stops when the requested leaf budget or pixel-sized cell limit is reached. This is independent of Version 01's global palette/contour/Bézier pipeline.

Each final leaf becomes one SVG `<rect>`, either a solid RGB fill or a reference to a generated `linearGradient`. Cells exactly cover the image domain without overlapping fill geometries by construction. Edges are shared as rectangle borders, but the rectangular grid does not conform to arbitrary object boundaries, so it can show stair-stepped silhouettes.

## Edge-band residual (later iteration)

After the first image-set visual review, the surface-only SVG did not adequately preserve thin boundaries. The final version adds `add_edge_residual_layer`:

1. Convert input RGB to grayscale, run Canny thresholds 80/160.
2. Dilate the edge mask with a 3×3 kernel once.
3. Quantize selected original RGB pixels uniformly per channel to 5 bits/channel.
4. Form maximal horizontal runs of adjacent selected pixels with identical quantized RGB values.
5. Store each run as a pixel-aligned closed SVG subpath and group paths by fill color.
6. Paint this residual group after the base tessellation with `shape-rendering="crispEdges"`.

This is **hybrid vector-only** because raster-derived values are encoded as thousands of editable SVG shapes—not because object semantics were inferred. It does not include `<image>`, base64 data, external raster links, or other raster payload. The SVG `<desc>` labels the hybrid representation explicitly. Standard SVG supports an `<image>` element for bitmap content; this implementation forbids it so renderer fidelity must come from actual vector primitives rather than an image wrapper. See the W3C SVG 2 embedded-content specification in the research references.

## Why 5 bits/channel

A four- versus five- versus six- versus eight-bit residual-color sweep was run on A02, A09, A10, and A12. In these four cases, 5-bit/channel color was a measured compromise: it was much closer to 6/8-bit quality than 4-bit on the two logo-like cases and significantly smaller than exact RGB paths on the detail-heavy cases. It is not claimed to be globally optimal; other images may favor another setting.

## Current SVG characteristics

- Base rectangles: 9,000 per benchmark image at the default budget.
- Base gradients: selected by local rank-1 regression improvement.
- Edge corrections: source Canny mask, dilated and run-length encoded; number varies by image.
- Semantic labels/groups: none beyond technical IDs/metadata and the edge residual group.
- Text: paths/pixels are not recognized as text; Arabic glyph semantics and font identity are not inferred.
- Shadows/highlights: preserved as rendered appearance where sampled by cells/edge residuals, not separated into editable layers.
- Occlusion: source order is not inferred. The surface layer is non-overlapping; the edge residual is painted above it.

## Main tunables

| Setting | Default | Meaning |
|---|---:|---|
| `max_cells` | 9,000 | hard leaf cell budget |
| `min_gradient_side` | 8 px | smallest cell side eligible for local gradient |
| `min_gradient_gain` | 0.16 | minimum relative SSE improvement for gradient |
| `min_gradient_sse_gain_per_pixel` | 3.0 | minimum SSE gain per pixel for gradient |
| `edge_priority_weight` | 1.5 | mild importance multiplier for high-gradient cells |
| `dilation` | 1 | edge-band expansion by 3×3 neighborhood |
| `color_bits` | 5 | per-channel quantization in edge-band residual |

## Performance / implementation scope

The tested images are around 370×250 pixels and the final run uses local CPU NumPy/OpenCV code and an Inkscape CLI renderer. It does not invoke paid services, a cloud GPU, or custom model training. The result is deterministic on the measured inputs and toolchain; the verifier regenerates every final SVG and checks byte equality. The Python-process peak RSS sample and fresh render-time figures are documented in `experiments/metrics/RESULTS_REPORT.md` and `summary.json`.
