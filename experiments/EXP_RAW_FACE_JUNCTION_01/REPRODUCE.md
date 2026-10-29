<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T12:39:52Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T12:39:52Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T12:39:52Z"}
END_DOC_PROVENANCE -->
# Reproduce or inspect the bounded study

Use saved outputs for owner review; no need to rerun prior24conditions,140searches or earlier repairs. New experiment protocol, baseline source pins and evaluator-reference pins are hash-frozen in FREEZE.json. Source constructor pins precede benchmark execution. Native Windows runtime reused Python3.14.2, NumPy2.4.4, SciPy1.18.1, scikit-image0.26, Pillow12.1.1, psutil7.2.2, Shapely2.2.0 and resvg0.49.0; environments/binaries/caches are outside Git. No new dependencies or hostedAI.

```powershell
$Repo = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner'
$Work = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'
$Python = Join-Path $Work 'agd-native\Scripts\python.exe'
$Experiment = Join-Path $Repo 'experiments\EXP_RAW_FACE_JUNCTION_01'
$env:AGD_ISOLATION_WORK = $Work
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
$env:PYTHONPATH = "$Experiment;$Work\geometry-deps;$Repo\experiments\EXP_COMPLETE_GEOMETRY_ISOLATION_01"
Set-Location -LiteralPath $Experiment
& $Python -m unittest discover -p 'test_*.py' -v
```

In a separate copy with fresh empty result directories only, run run_case.py with each of the four protocol case IDs under the existing safe_monitor.py (600s/4096MiB). It refuses output overwrite and verifies all frozen baseline files; it copies saved O/B and labels rather than refitting/resegmenting. R walks are exact endpoint cycles. Three RB branches must skip under the preserved fitted-render gate; do not alter it to force runs. Then run source_evidence_probe.py <frozen-working.png> <new-output-directory> under90s/1024MiB. Its constructor reads only RGB. It is evidence, not candidate geometry.

measure_results.py reuses inherited numerical evaluators and actual resvg; it reports fixed controls and separate source-map distance diagnostics. review.py creates owner-facing SVG/PNG zooms and overlays. Inputs are pinned existing artifacts; external fine source/truth/derived data require the owner's original geometry_only_v2_deliverable.zip and earlier local extraction. See preceding EXP_COMPLETE_GEOMETRY_ISOLATION_01/REPRODUCE.md. Fine assets/derivatives and Arena source remain external pending rights clarification, with local inventory hashes; they are not copied into the public research scope.

No fitting code or historical exporter changed. Added scripts are isolated experimental traversal, evaluation, source-evidence and presentation modules. Any future exporter repair must be its own disclosed matched control; current failed equivalence outputs are preserved.
