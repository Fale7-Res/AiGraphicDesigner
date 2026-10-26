<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-25T15:03:37Z"}
END_DOC_PROVENANCE -->
# VTracer fidelity-first bounded research

Production architecture **NOT_APPROVED**. Owner priority is now native-resolution visual fidelity first; complexity, semantic layers and advanced editability remain subsequent requirements. No historical version is changed. No commits or pushes are made.

Python package is pinned to `vtracer==1.0.0a4` (native engine `1.0.0-alpha.4`). Read `reports/PARAMETERS.md`: the Gradient Step UI control maps to `layer_difference`; it does not create SVG gradients. Official tagged source/license snapshots are in `reference/`.

## Reproduction

Python3.12, Linux, Inkscape1.2.2. Install Inkscape with your OS package manager, then:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s src -p 'test*.py'
python reproduce.py --destination ../EXP_VTRACER_REPRODUCTION_LOCAL --run
```

Single image:

```bash
python src/search.py --input inputs/A03_burger_layers.png --output my_burger_search
```

Use fresh output directories. All tested configs, successful SVGs/renders/metrics and failed trial logs are retained. `best.svg` means highest fixed multi-metric score among the bounded candidates, not a proven global optimum or a guarantee of perceptual superiority. Visual review is recorded separately.

## Design

13 diverse pilots plus four local probes, maximum17 trials/image. Includes owner settings, coordinate precision, spline simplification, stacked/cutout, polygon/pixel, color precision, gradient step, watershed and monochrome controls. Local probes can be ineffective for pixel mode; identical outcomes are preserved, not claimed as new gains.

One common config is selected using only shared pilots on A01/A03/A05/A10. It is frozen before eight other cases are evaluated. Only after all eight common-preset evaluations do we tune those cases independently. The eight images are held out from this preset selection, not novel images never seen in any project research. The 12-case suite cannot prove a universal preset.

`results/` holds primary per-image search. `holdout_common/` contains the eight frozen-preset tests. `results_baselines/` contains fresh renders of exact historical SVGs, not new tracing-engine runs. `refinement/` contains the fixed-geometry color/antialiasing diagnostic. Additional isolated configuration controls, when present, are separately identified as post-hoc research; they do not rewrite the primary trial ranking.

All12 originals are untagged RGB, assumed sRGB. The input adapter converts declared profiles to sRGB and explicitly composites alpha onto white; arbitrary transparency preservation is not claimed. Synthetic raw-alpha failures are retained under `reports/color_contract/`. The sRGB profile identity smoke test does not certify all ICC transforms.

The high-fidelity Pixel outputs are genuine vector paths without embedded images, but are closely tied to the original pixel grid. Large counts are measured and accepted for this milestone, not disguised as professional clean vectors. Enlarged source-resolution PNGs diagnose pixel errors; native high-resolution SVG renders assess scaling behavior without inventing high-resolution ground truth.

Timing and memory are recorded per worker. Trace timing excludes interpreter startup and renderer; isolated process wall time includes both. Separate parent/child memory high-water is not a simultaneous whole-tree peak. Historical generation timing cannot be inferred from rerender times.
