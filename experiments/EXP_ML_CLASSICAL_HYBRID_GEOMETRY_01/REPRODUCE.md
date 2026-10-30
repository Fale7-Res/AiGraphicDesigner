<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T08:21:42Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T08:23:42Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T08:21:42Z"}
END_DOC_PROVENANCE -->
# Reproduction and review

For review, open `review.html` and `REPORT.md`. The owner-local dashboard at `outputs/ml_geometry_review/review.html` additionally links the restricted Fine Features evidence and old/new frozen-trace fitting control. Existing outputs require no rerun.

## Runtime

Use a separate virtual environment with Python 3.14.2 and `requirements.txt`. The measured run reused the existing isolated `work/agd-native` environment read-only, plus Shapely from `work/geometry-deps`. No system changes or CUDA are required. resvg 0.49.0 is an external executable kept outside Git.

## Safe independent reproduction

Use a scratch copy with **empty results**, preserving original input hashes and previous experiment modules. Do not overwrite saved candidates. Set `AGD_REPO` to that scratch repository and `AGD_WORK` to its scratch work folder. Retain `EXP_EXPORTER_DISCOVERY_01` and `EXP_RAW_FACE_JUNCTION_01` for the unchanged tracer, classical extractor and corrected serializer. Put the packaged source scripts into `work/ml_geometry` if using the supplied worker launchers; put `stable_fit.py` in `work/ml_geometry/fitting_control` or on PYTHONPATH.

Download the exact pinned ONNX URL in `reports/MODEL_PROVENANCE.json` and verify its SHA256 before loading. Store it outside Git. `acquire_model.py` records the retrieval logic; its local paths may need adjustment. No checkpoint Python code is loaded.

`infer_dexined.py SOURCE_PNG WEIGHTS_ONNX NEW_OUTPUT_DIR` performs the final **256 px** CPU configuration, preserving logits and sigmoid. Supervise at 180 seconds / 1536 MiB process-tree RSS, preserving at least 700 MiB available RAM. The upstream 512 px resource failure and pre-retry amendment remain evidence; do not overwrite them or repeatedly search resolutions.

`construct_geometry.py CASE` consumes `results/CASE/ML/predictions.npz` and refuses existing construction outputs. Keep the same 6 px chain minimum, 128 proposal budget, 64 cubic budget and 0.6 px deviation threshold. Supervise each arm at 120 seconds and each case at 384 seconds / 768 MiB. The first four historical construction RAM records measured only the launcher; their true peak is unavailable.

Run `evaluate_results.py` only after all candidates finish. It reads evaluator-only masks/guides, never feeds them to construction. Frozen legacy absolute paths must be adjusted on a different machine **while preserving content hashes**. `build_review.py` creates actual SVG render comparisons through the existing resvg executable in `work/resvg`.

Run `python -m unittest test_stable_fit test_metrics -v` from this experiment with its path, the corrected-exporter path and isolated Shapely path on PYTHONPATH. The nine exporter regression tests remain in `EXP_EXPORTER_DISCOVERY_01/test_svg_exporter.py`. Recorded root outcome: 18 passing tests. Tests are engineering controls, not complete geometry acceptance.

Fine Features source, truth and derived outputs require the owner's original Arena ZIP and prior frozen local extraction. Rights are unresolved; `reports/LOCAL_ONLY_FINE_MANIFEST.json` records paths and hashes. Do not publish these assets. Generic fitter source, numerical summaries and retrieval information are preserved. No 140-search or 24-condition rerun is necessary.

## Publication

Git metadata writes remain blocked in the sandbox. The owner-run `outputs/ml_geometry_review/Publish-Research.ps1` checks actual branch, origin, ancestry and index scope; stages only this experiment; commits only if needed; safely pushes; and verifies the remote SHA. It never uses indiscriminate staging or force push. Exclude weights, environments, caches and unknown-rights assets. No new publication is claimed until GitHub confirms the SHA.
