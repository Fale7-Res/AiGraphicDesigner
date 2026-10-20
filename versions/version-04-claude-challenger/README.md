<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T00:24:10Z", "last_action": "CREATED", "last_change_id": "CHALLENGER-V04-IMPORT", "last_edited_at_utc": "2026-10-18T00:24:10Z", "last_editor": "owner-claude-import", "tracking_started_at_utc": "2026-10-18T00:24:10Z"}
END_DOC_PROVENANCE -->
# Version 04 — Claude Challenger (Independent SVG Reconstruction Experiment)

**Status:** isolated experiment only. This folder does not approve, replace, or alter Versions 01–03 or the project-wide architecture approval state.

Version 04 tests an independent, CPU-compatible alternative to the Version 01 quantize → contour → Bézier pipeline. The final benchmark representation is **hybrid vector-only**: adaptive rectangular surface tessellation and optional local SVG linear gradients, plus quantized source-derived path runs in a dilated edge band. It contains no embedded `<image>` elements. Do not confuse this high-fidelity experimental representation with semantically organized Clean SVG: it deliberately trades object count and ease of editing for appearance fidelity.

## Main artifacts

- `docs/TECHNICAL_PROPOSAL.md` — the strategy comparison recorded before implementation.
- `docs/ROOT_CAUSE_ANALYSIS.md` — independent analysis of observed Version 01 limitations and baseline caveats.
- `docs/ARCHITECTURE.md` — the algorithm, SVG schema, and trade-offs.
- `docs/EXTERNAL_RESEARCH_AND_LICENSES.md` — independent research references and license/provenance notes.
- `src/challenger.py` — vector surface model, local gradient fitting, edge-band residual conversion, and Inkscape render helper.
- `src/run_synthetic.py` — generates a known-geometry test before the photographic/logotype benchmark.
- `src/run_benchmark.py` — A01 budget sweep plus orchestration of the final 12-image run.
- `src/finalize_metrics.py` — generates final SVGs and metrics, makes visual comparisons, and writes the results report.
- `src/measure_renders.py` — fresh paired Version 01 / Version 04 Inkscape render-time measurements.
- `src/verify_outputs.py` — independent byte-identical regeneration, XML, raster embedding, and render-dimension checks.
- `tests/` — small CPU tests of budget, XML, gradients, and residual layer invariants.
- `experiments/outputs/` — all 12 native-size final SVGs (`A01`–`A12`).
- `experiments/rendered/` — actual rendered PNGs, including paired fresh timing renders.
- `experiments/comparisons/` — per-image Original vs Version 01 / Antigravity vs Version 04 / Claude comparisons, plus a 12-image contact sheet.
- `experiments/metrics/RESULTS_REPORT.md` — per-image and aggregate measurements, regressions, complexity, and limitations.

## Run on Windows or Linux

Python 3.10+ is recommended. In a clean environment, run from the **repository root** (not from inside `src`):

```powershell
py -m venv .venv-v04
.\.venv-v04\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r versions/version-04-claude-challenger/dependencies/requirements.txt
```

Install the free desktop build of Inkscape and make `inkscape.exe` available on `PATH`. If it is not, pass its full path to `--inkscape`.

Run the synthetic-known-geometry test first, then the A01 surface-only cell-budget diagnostic and the full benchmark:

```powershell
py versions/version-04-claude-challenger/src/run_synthetic.py
py versions/version-04-claude-challenger/src/run_benchmark.py --budget 9000 --a01-sweep
py versions/version-04-claude-challenger/src/verify_outputs.py
py -m unittest discover -s versions/version-04-claude-challenger/tests -v
```

`--a01-sweep` evaluates 1,000 / 2,500 / 5,000 / 9,000 **surface-only** cells before the final hybrid benchmark. The final run overwrites only Version 04's `experiments/outputs`, `experiments/rendered`, `experiments/comparisons`, and `experiments/metrics` outputs. Existing Version 01/02/03 code and experiment outputs are inputs/read-only baselines.

To measure fresh paired Inkscape rendering times separately (the script preserves the evaluation PNGs), use e.g.:

```powershell
py versions/version-04-claude-challenger/src/measure_renders.py --ids A01,A02,A03,A04,A05,A06
py versions/version-04-claude-challenger/src/measure_renders.py --ids A07,A08,A09,A10,A11,A12
```

To reuse existing V01 render PNGs during a complete run, pass `--skip-v01-render` to `src/finalize_metrics.py`. The fresh-renders performance CSV is a separate timing sample.

## Reproducibility and interpretation

The benchmark scripts keep the original source dimensions and use the same Inkscape CLI for V01 and V04. `benchmark_results.csv/json` records per-image PSNR, SSIM, MSE, edge precision/recall/F1, heuristic small-edge recall, foreground IoU proxy, SVG structure/size, timings, and residual complexity. `verification.json` records whether a separate regeneration is byte-identical, XML is well-formed, outputs are raster-free, and renderer dimensions match.

These metrics do not establish professional editability. Version 04's edge band is explicitly derived from the input and represented as quantized SVG paths; its improvement is therefore not a fair claim of recovering unknown scene semantics. For this experiment, source-derived geometry is permissible, but an embedded original raster is not.

## Dependencies and resource scope

The pipeline uses NumPy, OpenCV, Pillow, scikit-image, and psutil; rendering is external Inkscape. The tested flow is local CPU processing, does not use paid APIs or cloud GPUs, and does not train a model. The resource figures in the results report are from the current execution environment and should not be treated as a guarantee for other Windows laptops.
