<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T05:38:04Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T05:38:04Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T05:38:04Z"}
END_DOC_PROVENANCE -->
# Reproduce coverage-aware fixed-geometry fitting

Research only. Architecture **NOT_APPROVED**. Read REPORT.md, reports/BASELINE_AUDIT.md and frozen inputs/manifest.json. Historical code, geometry, inputs and prior negative results remain untouched. Sources/licenses remain in the saved experiments; the two new analytic fixtures are authored CC0 and are not a real-image benchmark replacement.

Use the existing Windows isolated Python and resvg; pinned package versions are in requirements.txt/reports/environment.json. No new dependencies were installed for this cycle.

```powershell
$py = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\agd-native\Scripts\python.exe'
$env:AGD_RENDERER = 'resvg'
$env:AGD_RENDERER_EXE = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\resvg\resvg.exe'
$env:AGD_INHERITED_FITTER = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_GEOMETRY_APPEARANCE_ABLATION_01\fit_appearance.py'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
Set-Location 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_COVERAGE_AWARE_FITTING_20261028'
& $py -m unittest discover -s . -p 'test_*.py' -v
& $py research.py
& $py audit_results.py
```

Completed results are verified and reused, not rerun. Missing/corrupt partial evidence is refused. For independent execution copy Python source, requirements and frozen inputs (including manifest) to a NEW sibling experiment folder, retaining historical imports in the same experiments parent. Historical absolute baseline paths intentionally remain unchanged. The two fixture local paths are frozen absolute paths too: keep the original frozen input directory as the source of truth. Do not regenerate/tune fixtures after fitting. Run research.py there; it derives output ROOT from its own file location. On a different computer relocate all manifest paths transparently and document the old/new hashes before execution. Do not call --prepare to silently replace a frozen manifest.

The bounded driver runs all nine cases, new controls first, with 900s/4GiB sampled worker limits and 300s fitting limits. Probe calls have15s bounds; maps are capped200MiB uncompressed. Limits are sampled, not OS reservations. Existing seven interior baselines are copied unchanged; two new-control baselines require a disclosed adapter that strips mask/opacity only for old RGB fitting and restores them on the exported SVGs. Source truth colors are not supplied to the fitter. RGB probe maps include the original masks, opacity and paint order.

In a fresh output directory only, run `& $py presentation.py --build` to produce owner sheets and actual SVG zoom renders. It refuses to overwrite prior presentation evidence. Reuse shipped index.html for completed review; do not delete evidence to force it. Actual native SVGs: results/<case>/{Aflat,Agrad,B,C,pixel,truth}/output.svg where applicable. Quantitative results: reports/metrics.csv, reports/integrity.json, per-case fitting.json and coverage/maps.json. Known-flat paint bias is in reports/paint_recovery.json; local feature errors in reports/critical_feature_errors.json.

No paid API, external AI service, new tracing, geometry movement, extra detail paths, topology changes, stroke or alpha reconstruction is used. Existing real RGBA source-grid alpha masks remain. The periodic test split is untouched by this fitting update, not independent of historical source-derived geometry/paint initialization.
