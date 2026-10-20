<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:17Z", "last_action": "CREATED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:55:17Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:17Z"}
END_DOC_PROVENANCE -->
# V04 Image-Guided Repair — Architecture

## Pipeline

```text
Input RGB raster
  ├─ edge-preserving bilateral preprocessing
  ├─ SLIC perceptual superpixels
  ├─ adjacency graph + shared-border Lab contrast
  ├─ region merging by color-surface fit error + boundary penalty
  ├─ shared integer pixel-cell boundary paths for internal regions
  ├─ per-region appearance fit: solid fill OR multi-stop linear/radial SVG gradient
  └─ coarse GrabCut foreground mask
       └─ simplified cubic outside silhouette + complementary clip paths
             └─ vector-only SVG + Inkscape render + pixel/edge/complexity metrics
```

## Region merge objective

Each region is modeled as a low-order 2D quadratic RGB surface for the purpose of estimating whether adjacent regions can merge without destroying spatial color structure. The merge cost includes the increase in model residual, normalized by region area/channel dynamic range, plus a penalty derived from observed Lab contrast along the shared boundary. This allows smooth illumination to merge while preferring not to merge across strong color changes. It does not establish that a boundary is a semantic object boundary.

## Contour strategy and why it is hybrid

Internal region contours are traced on pixel-cell edges (integer coordinates); shared boundaries use identical vertices on both sides. They are simplified only by removal of collinear vertices. The code intentionally does not fit each shared internal edge as an independent cubic curve because slightly different curve fits can leave cracks/overlaps when regions meet.

Instead, only the *external composite silhouette* is fitted to cubic segments and used for clipping. This makes outside edges smoother without changing the shared internal topology. The clip mask is a coarse foreground/background approximation from GrabCut, not object-instance segmentation.

## Appearance

A per-region regression compares a flat fill against multi-stop gradients. The linear candidate uses the dominant RGB spatial direction, then bins source colors along that direction to obtain stop colors. The radial candidate tests data-derived center locations (center of region, luminance-weighted bright/dark centers, and extrema) and is selected only when it reduces residual enough. These are real SVG `linearGradient` and `radialGradient` elements; they are not a grid of tiny color rectangles.

This recovers some smooth color transitions, but it does not produce a full optical/material model. The source may already combine surface albedo, cast shadow, specular light, ambient occlusion, blur, and transparency into one RGB value. Without interaction, depth, alpha, and semantic priors, those components are not uniquely separable. The current `foreground-region-reconstruction` and `background-region-reconstruction` clip groups are technical compositing groups—not individual named objects with guaranteed base/shadow/highlight sublayers.

## Resource and output constraints

- Python, NumPy, OpenCV, scikit-image, Pillow, psutil; Inkscape CLI for rendering.
- CPU only; no paid API, cloud GPU, or model training.
- Default adaptive target region range: 220–560, set using measured edge density and spatial edge coverage.
- Vector paths and gradient definitions only. Embedded SVG `<image>` elements, base64 raster payloads, external raster links, and source-derived pixel-run overlays are prohibited.
- Results are validated with same renderer and native dimensions for Version 01 and Version 04; a separate script regenerates SVGs byte-for-byte to check determinism.

## Reproducibility

From the repository root:

```powershell
py -m pip install -r versions/version-04-claude-challenger/dependencies/requirements.txt
py versions/version-04-claude-challenger/src/run_synthetic.py
py versions/version-04-claude-challenger/src/run_benchmark.py --segments auto
py versions/version-04-claude-challenger/src/verify_outputs.py
py -m unittest discover -s versions/version-04-claude-challenger/tests -v
```

A local Inkscape CLI must be on PATH. Use `--inkscape` in the benchmark script if it is installed elsewhere.
