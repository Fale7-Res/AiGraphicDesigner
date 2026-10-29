<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T11:43:19Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T11:43:19Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T11:43:19Z"}
END_DOC_PROVENANCE -->
# Reproducibility

Windows run used Python3.14.2, NumPy2.4.4, SciPy1.18.1, scikit-image0.26, OpenCV4.13.0.92, Pillow12.1.1, psutil7.2.2, Shapely2.2.0 and resvg0.49.0. No hosted AI or neural model. Inherited Arena source is an external dependency from the owner-provided ZIP, with hashes pinned by the preceding isolation package; rights are unresolved, so not copied into product code.

From the actual repo, set AGD_ISOLATION_WORK to the task work directory containing geometry-deps and resvg. Use the same pinned previous experiment and external ZIP extraction as described in EXP_COMPLETE_GEOMETRY_ISOLATION_01/REPRODUCIBILITY.md. The working Python environment is outside Git.

```powershell
$Repo = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner'
$Work = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'
$env:AGD_ISOLATION_WORK = $Work
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
$Python = Join-Path $Work 'agd-native\Scripts\python.exe'
Set-Location -LiteralPath (Join-Path $Repo 'experiments\EXP_THIN_STRUCTURE_TOPOLOGY_01')
& $Python -m unittest discover -p 'test_*.py' -v
```

Saved outputs are sufficient for visual review; no candidates need rerunning. For independent reproduction in a separate local copy of the experiment with no existing result files, run `run_study.py <case> baseline`, then A and B for each of the four protocol cases, under the previous safe_monitor.py (600s/4096MiB). The runner refuses overwrite. `evaluate_batch.py` measures saved graphs; `dashboard.py` creates actual SVG detail exports. Do not run AB: the frozen gate was not met. Do not rerun the historical 24-condition or140-candidate searches.

PRE_EXECUTION_SOURCE_PINS.json records construction and initial presentation source bytes. Constructor/evaluator bytes were not tuned after outputs; dashboard presentation was later improved to show source-coordinate bridge overlays and before/after mechanisms. Additional analysis source and output hashes appear in the final artifact manifest. Reference hashes and frozen protocol hashes remain unchanged.

No fine-feature fixture/derived image is published until reuse rights are clarified. The local evidence manifest supplies exact hashes and original local retrieval paths. Other actual source inputs are the pinned saved working images; there is no hardcoded benchmark geometry in either constructor.
