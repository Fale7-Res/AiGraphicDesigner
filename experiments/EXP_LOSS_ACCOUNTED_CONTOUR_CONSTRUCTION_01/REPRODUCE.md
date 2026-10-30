<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T15:21:31Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T15:21:31Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T15:21:31Z"}
END_DOC_PROVENANCE -->
# Reproduction and review

Open `review.html` and `REPORT.md` to inspect saved results without rerunning construction. The owner-local dashboard under `outputs/contour_construction_review` also includes the restricted Fine Features evidence.

Use the existing isolated `work/agd-native` Python runtime plus `work/geometry-deps` and `work/resvg/resvg.exe`. Versions are inherited from EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01/requirements.txt. No detector, model download or inference is required. The previous predictions and all source polylines are immutable inputs.

For an independent reproduction, use a scratch repository/output tree with the same historical modules and byte-verified frozen sources. Set AGD_REPO and AGD_WORK appropriately. Put the packaged run_case/monitor/run_study scripts into `work/contour_construction` and partition_fit into `work/contour_construction/implementation`, or adjust the explicit implementation import path. Keep the historical stable_fit module and corrected svg_exporter on PYTHONPATH. The prior manifest contains absolute legacy reference paths; adjust paths only while preserving hashes. Do not overwrite this experiment's saved directories.

1. Verify all protocol pins, applying only the explicit PRE_EXECUTION_SOURCE_FREEZE amendment to the partition implementation.
2. Run `test_partition_fit.py` in the pinned numerical environment. Nine tests should pass.
3. Validate the process-tree monitor with the controlled child-allocation test before reporting memory. It must include child PIDs and demonstrate the configured stop.
4. Run `run_case.py CASE ARM` into a fresh empty results directory. It consumes frozen construction.json only, copying O and generating P/Q. Preserve the 120-second condition / 300-second worker, 768 MiB tree RSS and 700 MiB available RAM limits. Record all failures instead of raising budgets after viewing results.
5. Run `evaluate.py` after candidates complete, then `review.py`. These evaluator-only stages read references and render actual SVGs; they do not change constructor geometry. The main matrix has 18 saved O baselines and 36 new P/Q candidates.
6. The separately frozen K01 cap-only diagnostic calls the old stable fitter with maximum_segments=512 while keeping its .6 gate and eight rounds. All nine saved attempts fail; it is not a fourth selected production condition.

Fine Features requires the owner's original Arena ZIP and previous frozen extraction; rights remain unresolved. Preserve local derivatives and hashes without redistributing them in Git. No source grid fallback, arbitrary closure, final appearance or reference-based construction is permitted.

Git publication is denied in this sandbox. Run the delivered scoped Publish-Research.ps1 from the owner's authenticated PowerShell. It stages only this experiment, preserves unrelated work, checks ancestry, avoids duplicate commits and verifies the remote SHA. Never use indiscriminate staging, reset or force push.
