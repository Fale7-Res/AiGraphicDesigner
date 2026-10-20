<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:15Z", "last_action": "CREATED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:55:15Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:15Z"}
END_DOC_PROVENANCE -->
# Image-Guided V04 Repair Proposal — Before Implementation

## What the reference image requires

1. **Clean geometry:** replace pixel-aligned rectangles and jagged approximations with closed, smoothed vector contours; preserve strong corners where the source has real corners.
2. **Real gradients, not a grid of color tiles:** use local, multi-stop SVG gradients only when color change inside a region is spatially coherent; use flat fills for regions that do not support a gradient model.
3. **No source-edge pixel stencil:** remove the previous Canny-run overlay. It improves numerical edge metrics by copying locations/colors from the source, but creates thousands of micro-subpaths and does not infer clean shape geometry.
4. **Preserve detail without flattening every detail into a separate tiny shape:** use perceptual, boundary-aware superpixels and contour simplification with a controlled error budget; do not add strokes around every visible color variation unless needed to close a rendering seam.
5. **Separate appearance components only where evidence supports it:** the engine can approximate a base color surface and smooth shading through gradients. It cannot reliably infer semantic base/shadow/highlight layers from an already-composited RGB image without object masks, depth/material priors, or user guidance. This limitation must remain explicit.
6. **Complexity as a constraint, not a substitute for fidelity:** report number of regions/paths, curve segments, SVG size, PSNR/SSIM and edge metrics side by side. Do not optimize solely for aggregate pixel scores.

## Alternatives considered

- **A. Topology-constrained region graph + boundary fitting:** segment into labels, represent each shared boundary once, simplify it under a geometric tolerance, and fit cubic Bézier curves while preserving holes and adjacency. This is the strongest long-term shape/editability direction, but a correct planar graph implementation is a larger task.
- **B. Boundary-aware superpixels + smooth cubic contours + local multi-stop gradients (selected for this repair):** use SLIC regions to avoid a global fixed palette; derive each region from a smooth vector contour; fit gradients locally only when measured color variation is coherent; remove the old pixel-edge residual entirely. This changes the old tiled/sampled representation into a compact curve-and-gradient representation. It does not claim semantic object separation.

Selection: B is the most defensible local CPU experiment for this repair iteration. Its risks—region fragments, local gradient seams, imperfect semantic grouping, and fine texture simplification—will be measured instead of hidden.

## Acceptance protocol

- Start with known smooth geometry and A01 shield; then test the same 12 images.
- Render both the untouched Version 01 baseline and V04 with the same Inkscape CLI at the source dimensions.
- Record MSE, PSNR, SSIM, 1-pixel tolerance edge precision/recall/F1, contour/path and cubic segment counts, SVG bytes, generation time, and sampled process memory.
- Inspect the contact sheet specifically for stepped borders, mosaic-like shading, lost Arabic strokes, blurred details, halo seams, and over-fragmented object layers.
- No embedded `<image>` or pixel-run residual. All output must be actual SVG vector shapes/gradients.
- A metric win does not imply Clean SVG success; semantic object/shadow/highlight separation and professional editability are reported as not solved unless the output actually supports them.
