# Version 04 — Image-Guided Vectorization Repair (Portable Bundle)

This bundle contains the isolated challenger implementation and the actual 12-image test artifacts. Keep the archive directory structure intact after extracting.

Included:
- `versions/version-04-claude-challenger/`: code, dependencies, tests, version-scoped catalog, architecture/root-cause/experiment docs, 12 final SVGs, 12 V04 PNG renders, 12 baseline PNG renders, side-by-side comparisons, metrics, verification and reproducibility logs.
- `AI_Graphic_Designer_Test_Images_Initial_12/`: exact benchmark source images.
- `versions/version-01/experiments/preliminary_visual_tests/outputs/`: 12 committed Version 01 baseline SVGs (read-only baseline).
- `versions/version-01/experiments/fidelity_diagnostics/all_12_rerun_metrics.json`: existing V01 reported metrics for provenance.
- `versions/version-01/src/pipeline.py` and `src/geometry/bezier.py`: source files reviewed for the root-cause analysis, if present.
- `docs/product/OWNER_ORIGINAL_VISION.md`: original owner vision, unmodified.
- `reference/visual_review_sheet.jpg`: user-supplied image that defined the repair criteria.

## Run on Windows

Install Python 3.10+ and the free Inkscape desktop application, then from the extracted archive root:

```powershell
py -m venv .venv-v04
.\.venv-v04\Scripts\Activate.ps1
py -m pip install -r versions/version-04-claude-challenger/dependencies/requirements.txt
py versions/version-04-claude-challenger/src/run_synthetic.py
py versions/version-04-claude-challenger/src/run_benchmark.py --segments auto --reuse-existing-renders
py versions/version-04-claude-challenger/src/verify_outputs.py
py -m unittest discover -s versions/version-04-claude-challenger/tests -v
```

`--reuse-existing-renders` still regenerates each V04 SVG and only reuses a native-size cached PNG when the SVG matches byte-for-byte. Omit this flag for a fresh Inkscape render of every baseline and candidate SVG (slower but independent of cached renders). Pass `--inkscape \"C:\Program Files\Inkscape\bin\inkscape.exe\"` if Inkscape is not on PATH.

## Important limits

This repair replaces the previous square-tile and pixel-run stencil with region-based SVG paths, real linear/radial gradients, common internal region borders, and a smoother composite outer silhouette. It is not yet semantic Clean SVG: it does not recover a separate base/shadow/highlight/blur layer stack for each named object. The report documents that edge recall regresses on 11/12 images and edge F1 on 7/12, despite PSNR/SSIM improvement on all 12. Do not treat a higher aggregate image metric as proof of professional editability.
