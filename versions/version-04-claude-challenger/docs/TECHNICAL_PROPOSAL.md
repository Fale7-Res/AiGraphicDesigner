<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T00:24:16Z", "last_action": "CREATED", "last_change_id": "CHALLENGER-V04-IMPORT", "last_edited_at_utc": "2026-10-18T00:24:16Z", "last_editor": "owner-claude-import", "tracking_started_at_utc": "2026-10-18T00:24:16Z"}
END_DOC_PROVENANCE -->
# Version 04 Challenger — Pre-implementation Technical Proposal

**Status:** Proposal recorded before implementation; this version is an independent experiment, not an approval or promotion of any project architecture.

## Owner's objective

The authoritative owner vision asks for editable, semantically organized Clean SVG that preserves shapes, overlap, gradients, shadows, highlights, and visual identity. It explicitly rejects splitting every shading speck into an independent art object when a coherent object-plus-appearance group is a better design. A raster-faithful but semantically fragmented SVG is therefore a useful fidelity experiment, not the final product goal.

## What the inspected Version 01 code actually does

`versions/version-01/src/pipeline.py` applies a bilateral filter, CIELAB K-means (default 16 colors), `findContours(RETR_CCOMP)`, `approxPolyDP`, and a custom Schneider-style cubic-curve fit. It orders color clusters by global pixel count, draws a 0.75 px stroke by default, and only tries a simple linear gradient when an optional flag is enabled. The source imports neither SAM 2 nor LaMa; those stages appear in the architecture hypothesis but are not implemented in the inspected pipeline. The gradient estimator fits one linear trend from pixels inside a contour and is not a decomposition of material, highlight, shadow, and transparency. The contour hierarchy is two levels (CCOMP), while global cluster-area ordering cannot by itself establish the correct object occlusion order.

Observed 12-image V01 renders visibly posterize photographic textures and smooth illumination into flat islands; narrow strokes can bloat silhouettes or cross nearby colors. The committed `all_12_rerun_metrics.json` reports mean PSNR 18.19 dB and mean SSIM 0.6218 for its cited run. These are repository-recorded measurements, not assumed to be reproducible under a different renderer. A separate A01 diagnostic (including a corrected planar experiment) is not the same 12-image baseline, and will not be mixed into the baseline column.

## Competing strategies considered

### Strategy A — topology-aware planar regions + adaptive contours + Bézier fitting

Quantize or segment the image in a perceptual color space, construct mutually exclusive regions, trace shared pixel-cell boundaries so neighbors share exactly the same edge, then simplify contours under a boundary-distance budget and fit piecewise cubic Béziers. Fit gradients only where the region's color field is well explained by them; preserve holes/containment with explicit topology.

**Strengths:** natural fit for flat illustrations and logos; recognizable closed shapes; fewer editable objects; explicit shared boundaries, holes, and topology; can retain crisp silhouettes. **Risks:** textured food, translucency, broad soft shadows, and metallic highlights demand many regions or richer appearance models; palette quantization still discards detail; fitting independent contour colors does not recover object semantics. This approach is related to—but will not reuse—the V01 contour/Bezier implementation and its already-recorded planar experiment.

### Strategy B — adaptive vector surface tessellation with local appearance fitting (selected)

Partition the source into a spatial quadtree of non-overlapping rectangular cells. Split cells according to their measured color reconstruction error and edge/high-frequency energy rather than a fixed global palette. Represent each accepted leaf with its mean color, or an SVG linear gradient only when a local linear color model measurably reduces residual error. Allocate a fixed primitive budget by the greatest reducible error first, so high-contrast edges and detailed areas receive more cells while smooth regions remain coarse. Cell boundaries are shared by construction; no independent contour masks, global cluster painter's order, or Bézier fit is required.

**Strengths:** directly targets rendered pixel fidelity across flat regions, gradients, shadows, texture, and transparency already composited in the source; deterministic CPU-friendly processing; exact non-overlapping partition avoids contour gaps/overdraw caused by independently fitted regions; every primitive remains SVG-native and there is no embedded image. It offers an explicit complexity/fidelity control. **Risks:** cell boundaries are axis-aligned, so silhouettes can staircase at insufficient resolution; region tessellation is not object-aware or semantically editable; piecewise local gradients can show discontinuities; very textured images may need thousands of cells. This is a vector tessellation approximation, not a claim of clean semantic object layers.

## Selection and rejection rationale

Strategy B is selected as the challenger because Version 01's dominant observed failures are loss of color detail and gradients, and the requirement says not to trade fidelity away just to reduce path count. It is maximally different from Version 01's quantize-then-contour-then-Bézier pipeline, uses only local CPU-friendly numerical operations, and has a direct tunable error/primitive-budget trade-off. Strategy A remains a strong future candidate for a semantic/illustration mode but is not the best first independent test of fidelity on this mixed set of logos, calligraphy, foods, and illuminated advertising.

## Controlled protocol

1. Generate an SVG for a deterministic known synthetic composite before tuning on the supplied shield.
2. Run A01 with a small budget sweep; visually inspect and record the selected settings before processing the remaining 11 images.
3. Preserve the 12 source images and existing V01 outputs unchanged; use their source dimensions and render all candidate SVGs using the same local Inkscape CLI renderer at native dimensions.
4. Measure MSE, PSNR, SSIM, edge-map precision/recall/F1, binary foreground-mask IoU (only as a proxy; no authoritative object masks are supplied), paths/primitives, path anchor/control count, bytes, generation time, and peak process RSS. Report both the original recorded V01 metrics and fresh renderer-consistent metrics where possible.
5. Treat any axis-aligned contour artifacts, loss of tiny detail, gradient discontinuities, and primitive-budget failures as regressions. No embedded `<image>` element is permitted in generated SVGs.

## Research references checked before implementation

- Sun et al., *Image Vectorization using Optimized Gradient Meshes* (ACM 2007): an optimization-based, editable gradient-mesh alternative for multicolored/photorealistic images. https://www.microsoft.com/en-us/research/publication/image-vectorization-using-optimized-gradient-meshes/ . Research reference only; no code copied.
- Achanta et al., *SLIC Superpixels Compared to State-of-the-Art Superpixel Methods*, IEEE TPAMI 34(11), 2012, DOI 10.1109/TPAMI.2012.120: boundary-aware superpixels as a candidate segmentation primitive. https://pubmed.ncbi.nlm.nih.gov/22641706/ . Research reference only; no code copied.
- Li et al., *Differentiable Vector Graphics Rasterization for Editing and Learning*, ACM TOG 39(6), 2020: vector/raster loss optimization is promising in principle. Public implementation `BachiLi/diffvg` is Apache-2.0, but its installation stack includes a native/C++ build and PyTorch-oriented dependencies, so it is deferred rather than introduced into this CPU-first experiment. https://github.com/BachiLi/diffvg . No code copied.
- Potrace source repository (GPL-2.0): useful for understanding boundary tracing for binary silhouettes but not adopted for this full-color image reconstruction; no code copied. https://github.com/lgcc/potrace .

## License / provenance notes

The challenger algorithm is newly implemented for this repository and does not vendor, port, or copy source from the cited repositories. References above are research/context pointers; respective papers, source repositories, and licenses remain owned by their authors. The benchmark images and V01 artifacts remain the project owner's existing assets and are preserved unmodified.
