<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:17Z", "last_action": "CREATED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:55:17Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:17Z"}
END_DOC_PROVENANCE -->
# External Research and License / Provenance Notes

The current repair was implemented locally and does not vendor, copy, or invoke a third-party vectorizer. These references informed candidate directions; they are not evidence that V04 reproduces those systems.

| Reference | Relevance | Decision and license/provenance boundary |
|---|---|---|
| Achanta et al., “SLIC Superpixels Compared to State-of-the-Art Superpixel Methods,” IEEE TPAMI 34(11), 2012. https://pubmed.ncbi.nlm.nih.gov/22641706/ ; DOI https://doi.org/10.1109/TPAMI.2012.120 | SLIC provides a practical CPU superpixel partition with boundary adherence and speed/memory evaluation. | V04 calls `skimage.segmentation.slic`; it does not copy the paper's implementation. The code uses the scikit-image dependency's own license, listed with that package. Research record confirms the method and publication. [PubMed source](https://pubmed.ncbi.nlm.nih.gov/22641706/) |
| Sun et al., “Image Vectorization using Optimized Gradient Meshes,” ACM TOG, 2007. https://www.microsoft.com/en-us/research/publication/image-vectorization-using-optimized-gradient-meshes/ | Optimized meshes are a more expressive way to capture smooth, editable highlights and illumination than many flat-color patches. The paper uses an energy-minimization formulation and allows user guidance. | V04 currently fits regional SVG linear/radial gradients; it does **not** implement this optimized gradient-mesh algorithm. The paper's source/code is not copied. [Microsoft Research source](https://www.microsoft.com/en-us/research/publication/image-vectorization-using-optimized-gradient-meshes/) |
| Li et al., “Differentiable Vector Graphics Rasterization for Editing and Learning” / DiffVG. https://github.com/BachiLi/diffvg | Differentiable rasterization can optimize a vector scene against a rendered-image loss, potentially refining paths and gradients after initialization. | Deferred: native/C++ and PyTorch-oriented build/dependencies complicate the current low-resource CPU path. The upstream repository declares Apache-2.0; no DiffVG code was copied or included. [DiffVG repository](https://github.com/BachiLi/diffvg) |
| Potrace. https://github.com/lgcc/potrace | Smooth tracing of binary masks is a useful alternative for monochrome silhouette/logo tasks. | Not used for this full-color multi-material benchmark. The linked upstream repository lists GPL-2.0; its source was not copied, run, or bundled. [Potrace repository](https://github.com/lgcc/potrace) |
| W3C SVG 2. https://www.w3.org/TR/SVG2/ | SVG provides paths, gradient definitions, clip paths and image elements. | V04 output uses paths, linear/radial gradients and clip paths; the validator rejects embedded/external raster references. The standard is used to guide SVG-compatible output; no W3C source code is incorporated. |

## Genuinely different approaches considered

1. **Topology-preserving planar region graph with shared-boundary Bézier fitting.** This is a strong long-term direction for editing clean object outlines, holes, and overlaps, but requires an explicit adjacency/ownership graph and joint curve optimization so neighbors share exactly the same fitted boundary.
2. **Adaptive surface tessellation with source-edge residuals.** This was the previous V04 experiment. It improved pixel scores but produced tile-like edges and thousands of pixel-following micro-paths, so it was rejected as the final current representation.
3. **Selected approach: boundary-aware SLIC region merging + exact shared internal cell edges + smoothed composite outer silhouette + local gradients.** This removes the stencil and many square patches while remaining CPU-friendly. It is still region-based rather than semantically object-based.

## Licensing statement

Only the references and upstream license statements are recorded here. No complete third-party vectorizer source was copied into `src/`. Existing source images, the owner vision, and Version 01 baselines remain project assets; this repair does not change their ownership or terms.
