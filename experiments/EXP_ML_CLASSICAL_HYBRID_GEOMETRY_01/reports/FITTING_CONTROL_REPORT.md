<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T08:21:42Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T08:21:42Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T08:21:42Z"}
END_DOC_PROVENANCE -->
# Frozen-trace fitter stability control

## Scope and scientific interpretation

**VERIFIED:** the two previously rejected Fine Features traces can be fitted inside the unchanged 0.6 px numerical deviation gate using chord-scaled unit tangents and bounded source-supported subdivision. No discovery, segmentation, alpha, width estimation or evaluator reference is changed. This is a downstream fitting correction, not evidence that source discovery reconstructs the four intended components or that ML is better.

**NOT ESTABLISHED:** correct artistic geometry, shared-region topology, widths, component completeness, complete thin-feature recovery and final visual fidelity. The raw source traces themselves are lattice-derived; fitting them closely can preserve their sampling artifacts. There is no pixel-cell/box fallback, but these curves are not certified professional reconstruction.

## Exact frozen inputs

Input: `work/exporter_discovery/external_results/fine_features/discovery/proposals.json`, SHA256 `66734234c37b3c07575d659026664c77f7087d7f1b70b244b596b892f20d6450`.

Only saved `curve_deviation` rejects, chains 0 and 2, are used. No discovery rerun. Historical `discovery_strokes.py` SHA256 `1d49331d6750a6dfddb650e6e4ad72130317df1768ee79b33ac1344869060dd6` is imported unchanged and Python tracing captures the exact cubics its unchanged `_fit` rejects.

Chain 0 float64 point-array SHA256: `3082d320bae7d4aa14d8e714098f099a6c101f6475a85af2f3369197f748fe5a`.

Chain 2 float64 point-array SHA256: `aab61ebcc45e34418a53c7339a6e1adbdd5423e20440e3c3a3c1ec1bebf63764`.

The Arena-derived traces, SVGs and PNGs remain local external research evidence pending rights clarification. Generic first-party fitter/test/control source can be reviewed for isolated research reuse. Do not publish these trace-derived outputs without clearance.

## Minimal intervention

The inherited centered tangent `(next-prev)/2` produces overly long short-chord handles when adjacent RDP vertices have unequal spacing. The correction uses the sum of adjacent unit chord directions, normalized, with each segment's handle independently scaled to its own chord length / 3. The inherited 60 degree sharp-corner rule and RDP epsilon 0.35 px remain fixed.

If the whole trace exceeds the numerical 0.6 px envelope, the worst interval is divided by inserting its middle original source support sample. All prior knots are retained. Limits: eight subdivision rounds, 64 cubics, 30 seconds per trace. An unresolved case is rejected. No raw-grid export fallback occurs.

The envelope uses two directed point-to-line-segment distances, adaptive control-hull flattening <=0.002 px and segmentwise sampling <=0.01 px. It adds 0.007 px for sampling/flattening uncertainty. These are numerical measurements and a conservative practical envelope, **not exact continuous arithmetic certification**. They eliminate the former nearest-sampled-vertex artifact. The fitter's acceptance gate does not replace shared-graph/topology evaluation.

## Measured results

| Trace | Cubics old → new | Curve→raw max old → new | Raw→curve max old → new | New numerical envelope | Subdivisions |
|---|---:|---:|---:|---:|---:|
| 0 | 31 → 36 | 0.677619 → 0.480715 px | 0.439482 → 0.490153 px | 0.497153 px | 5 |
| 2 | 36 → 37 | 0.842000 → 0.566528 px | 0.457190 → 0.566503 px | 0.573528 px | 1 |

**Negative/limited evidence:** raw→curve error increases for both traces; improvement is the reduction of worst overshoot and symmetric maximum, not uniform pointwise improvement. Added cubics are 16.1% and 2.8%. Both old and new flattened individual lines are simple numerically. Pairwise/shared topology is not certified. No width accuracy is claimed.

First execution fitting times were 2.0075 s and 0.5907 s; reproducibility execution approximately 1.8792 s and 0.5900 s. Machine loading affects timing. Replication results include 20 ms sampled Python-process RSS peak 80.609 MiB; renderer subprocess memory is not measured. Model inference is outside this control.

## Tests and real outputs

Five unit tests pass: unequal-chord handle bound, intentional right-angle corner preservation, reject cubic budget without fallback, reject nonfinite inputs, actual segment-distance measurement on a long straight trace.

Each execution produces four actual SVGs (old rejected, new control, raw diagnostic, overlay) and 12 successful resvg renders at 1x, 4x and 16x. Native SVG dimensions 128×96; 16x renders are 2048×1536. Native-scale render times about 0.013–0.020 s; 16x about 0.074–0.097 s. Raw SVG is explicitly diagnostic only. The overlay is blue new, red old rejected, grey raw. The 4x overlay was visually inspected; curves follow both long traces while visible small oscillations remain.

Results: `results/RESULTS.json`; repeatability execution: `replication/RESULTS.json`. The geometric measurements and cubic coordinates repeat exactly; timing and memory naturally differ.

## Reproduction

From the shared Codex workspace, with existing `work/agd-native/Scripts/python.exe`, `work/geometry-deps` and `work/resvg/resvg.exe`:

```powershell
& .\work\agd-native\Scripts\python.exe .\work\ml_geometry\fitting_control\test_stable_fit.py
& .\work\agd-native\Scripts\python.exe .\work\ml_geometry\fitting_control\run_control.py .\work\ml_geometry\fitting_control\another_new_output_directory
```

Output directory must not exist; historical outputs are never overwritten. Runtime versions recorded in replication: Python 3.14.2, NumPy 2.4.4, SciPy 1.18.1, OpenCV headless 4.14.0.94, Shapely 2.2.0, psutil 7.2.2. No installation or new dependency download occurred.

Recommendation: use this as a common **controlled downstream fitter**, preserving old-fitter results separately, only if the main arm's resource budget permits. Its relatively expensive dense numerical validation should not be mistaken for a production-optimized fitter. Independent QA remains the parent task's responsibility. Geometry NOT_ACCEPTED; architecture NOT_APPROVED.
