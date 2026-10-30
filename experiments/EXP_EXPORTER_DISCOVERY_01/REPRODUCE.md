<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:13:29Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:13:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:13:29Z"}
END_DOC_PROVENANCE -->
# Reproduction and evidence

Saved outputs are sufficient for visual review. Do not rerun140searches or24conditions. Python3.14.2, NumPy2.4.4,SciPy1.18.1,scikit-image0.26,OpenCV4.13.0.92,Pillow12.1.1,psutil7.2.2,Shapely2.2.0,resvg0.49.0 reused; no environment/binary/MLweight committed. Independent QA uses existingfontTools parser.

```powershell
$Repo = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner'
$Work = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'
$Experiment = Join-Path $Repo 'experiments\EXP_EXPORTER_DISCOVERY_01'
$Python = Join-Path $Work 'agd-native\Scripts\python.exe'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
$env:AGD_ISOLATION_WORK = $Work
$env:AGD_EXPORTER_FIXTURE_OUTPUT = Join-Path $Experiment 'phase_a\fixtures'
$env:PYTHONPATH = "$Experiment;$Work\geometry-deps;$Repo\experiments\EXP_COMPLETE_GEOMETRY_ISOLATION_01;$Repo\experiments\EXP_THIN_STRUCTURE_TOPOLOGY_01"
Set-Location -LiteralPath $Experiment
& $Python -m unittest discover -p 'test_*.py' -v
```

For independent candidate reproduction use a separate local copy with fresh empty results, never overwrite these saved outputs. `phase_b.py CASE` verifies source/reference policy hashes, copies savedO/R/B/A and labels, reexports using corrected17 andclosureonly8controls, checksrawnative/8x+fitted8xexactRGBAequivalence, thenrunsunchangedTrackBonlyonthethreepreviouslyblockedcases. K01RBiscopiedfrompreviouscontrol. Monitoreachworker600s/4096MiB. `discovery_strokes.py FROZEN_WORKING_PNG NEW_OUTPUT_DIR` usesRGBonly,fixedconfig,60s/512MiB externallyenforced; refusestargetoverwrite. No thresholdsearchorML.

`measure.py` binds the isolated serializer into evaluator module objects in-memory only, recomputes affected foreground/proxy/visibleID metrics, measures proposals and actual SVG hypotheticalunion, and preserves original affected values. `review.py` generates actual SVG/PNG1x4x16xviews. Sourcecontrast and diagnosticpaint are not finalappearance. `qa/` retains independent passive audit scripts; original task workspacepaths may need adjustment in another machine. Fine fixture/truth/derivative inputs require the owner ZIP and prior frozen extraction; see EXP_COMPLETE_GEOMETRY_ISOLATION_01/REPRODUCE.md. Rightsunresolved→local-onlydata manifest, no public copy.

Original graph geometry/params and source/reference hashes are frozen in BASELINE_PINS/FREEZE. Constructor source hashes precede execution. Later evaluator/comment-only changes are disclosed in SOURCE_CLOSURE. Frozen accepted/rejected Coutputs unchanged after separate read-only Fine fit diagnostics. Historical source/exporters/results are preserved; corrected outputs live only here.

Publication blocked by protected Git metadata. Use delivered Publish-Research.ps1 from owner's own authenticated terminal; it stages only this experiment, creates commitonlyifneeded,pusheswithoutforce,andverifiesremoteSHA. No publication success is claimed by file generation.
