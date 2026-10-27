<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T14:46:14Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T14:46:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T14:46:14Z"}
END_DOC_PROVENANCE -->
# Saved generalization experiment

Research only; global architecture **NOT_APPROVED**. Read [REPORT.md](REPORT.md), [visual dashboard](reports/dashboard.html), [verification](reports/verification.json) and [metrics CSV](reports/metrics.csv).

This directory retains the completed 140-candidate run across eight cases / seven independent originals. No reranking improvement was observed: all selected SVG and PNG aliases are byte-identical. Do not rerun the optimizer to rebuild this evidence package.

## Reproduce packaging without search

Use Python with NumPy, Pillow, SciPy, scikit-image and the sibling Windows experiment's metric dependencies. The locally used environment is Python 3.14.2, NumPy 2.4.4, Pillow 12.1.1, SciPy 1.18.1, scikit-image 0.26.0. `package_evidence.py` imports only metric helpers from the sibling Windows extension. It does not invoke VTracer or resvg.

From this directory, substituting the appropriate Python executable:

```text
python -B package_evidence.py
python -B -m unittest test_saved_evidence -v
```

The packaging command regenerates only its reports/comparison files. It inventories `inputs/`, `dataset/`, and `results/` before and after; it fails if evidence bytes change. `--verify-only` performs read-only saved checks. `reports/saved_artifact_inventory.json` can independently detect subsequent drift. Tests require the packaging artifacts to exist. Existing `runner.py` and `acquire_dataset.py` are historical executable protocol sources; do not invoke them merely to inspect results. Original result files are not edited by closure packaging.

## Visual review

Open `reports/dashboard.html` locally. Choose actual SVG 1x, 4x or 16x display and white, black or bluegray backgrounds. Expand comparison sheets and amplified error maps. SVG browser zoom is real vector display; nearest-neighbor PNG crop sheets are labeled raster diagnostics. Whole-case native metrics are based on saved resvg output, not browser screenshots. `inputs/manifest.json` and source snapshots provide licensing and attribution; retain them when sharing derivatives.

## Provenance / isolation

This closure adds packaging code, dedicated QA, reports, visual sheets and scoped memory/governance metadata only. Historical inputs/results/runner and the authoritative owner vision remain intact. There is no embedded raster shortcut, no new architecture approval, and no claim that pixel-grid paths are coherent geometry. Alpha masks use source-grid run shapes and remain grid dependent.
