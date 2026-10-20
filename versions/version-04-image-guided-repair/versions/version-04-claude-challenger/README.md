<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:14Z", "last_action": "EDITED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:59:12Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:14Z"}
END_DOC_PROVENANCE -->
# Version 04 — Image-Guided Vectorization Repair

This repair directly targets the defects shown in the supplied V01/V04 visual-review sheet: blocky gradient areas, broken/jagged outlines, loss of detail, and excessive independent fragments.

## What changed

- Removed the previous rectangle-tessellation and Canny pixel-run correction representation.
- Initial SLIC regions are merged by a cost that balances 2D quadratic color-surface fit error against observed Lab color difference on the shared boundary. Smooth shading can merge while strong discontinuities are penalized.
- Each internal region boundary is traced along shared pixel-cell edges. Adjacent shapes use exactly matching internal geometry instead of separately smoothed paths, which previously created visible cracks.
- A CPU GrabCut pass estimates a coarse composite foreground mask. Its external silhouette alone is simplified and fitted with cubic segments; complementary clip paths keep the internal region fill and background from leaking across the silhouette.
- Region interiors use a solid fill, local multi-stop linear gradient, or local radial gradient depending on the measured RGB fit. These are SVG gradients, not square color tiles.
- The number of regions is selected adaptively from edge density and spatial coverage of texture, with more regions for distributed photographic detail and fewer for flat logo/calligraphy regions.
- The output contains SVG paths and gradients only: no embedded image, no base64 raster, and no edge-pixel micro-path stencil.

## Honest limitations

This is not yet the owner's full goal of semantically organized Clean SVG. GrabCut produces only a coarse foreground/background composite mask, not separate named objects. The tool does not reliably reconstruct object identity, z-order between semantic objects, editable text, or independent base/shadow/highlight material layers. Smooth gradients and the silhouette clip improve appearance, but some high-frequency photographic details are simplified. In the latest same-renderer run PSNR and SSIM improved on all 12 images, while edge recall was lower on 11 images and edge F1 lower on 7 images. The regressions are recorded rather than hidden.

## Run on Windows

Install a local Inkscape CLI and Python dependencies:

```powershell
py -m venv .venv-v04
.\.venv-v04\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r versions/version-04-claude-challenger/dependencies/requirements.txt
py versions/version-04-claude-challenger/src/run_synthetic.py
py versions/version-04-claude-challenger/src/run_benchmark.py --segments auto --reuse-existing-renders
py versions/version-04-claude-challenger/src/verify_outputs.py
py -m unittest discover -s versions/version-04-claude-challenger/tests -v
```

Pass a fixed region budget for controlled sweeps (e.g. `--segments 320`) or leave it `auto`. Both Version 01 and Version 04 SVGs are evaluated at source PNG dimensions with the same Inkscape CLI. `--reuse-existing-renders` is an optional resume mode: it first regenerates the V04 SVG and reuses a cached PNG only when the new SVG is byte-identical and the PNG has the expected dimensions. Fresh rendering remains the default when this check fails. The benchmark writes results under `experiments/` only.

## Reports

- `docs/IMAGE_GUIDED_REPAIR_PLAN.md` — criteria from the visual-review image and strategy choice.
- `docs/ROOT_CAUSE_ANALYSIS.md` — why the previous representation produced tiles/cracks and which regressions remain.
- `docs/ARCHITECTURE.md` — region merging, shared internal boundaries, smooth outside silhouette, and local gradient fitting.
- `docs/EXTERNAL_RESEARCH_AND_LICENSES.md` — research references and source/license boundaries.
- `docs/EXPERIMENT_NOTES.md` — separately recorded higher-detail and compactness probes, including why they are not the selected default.
- `experiments/metrics/RESULTS_REPORT.md` — per-image PSNR/SSIM/edge and complexity comparisons, including regressions.
- `experiments/metrics/summary.json` and `benchmark_results.csv` — raw numbers.
- `experiments/metrics/verification.json` — deterministic regeneration, XML, raster-free and render-dimension verification.
- `experiments/comparisons/all_12_contact_sheet.png` — all 12 Original vs Antigravity V01 vs Repaired V04 results.

All work is isolated to this directory. Versions 01–03, the owner vision document, and global architecture approval were not edited.
