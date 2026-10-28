<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T03:30:09Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T03:34:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T03:30:09Z"}
END_DOC_PROVENANCE -->
# Reproduce Vector Bottleneck Diagnostics

Architecture NOT_APPROVED. Read REPORT.md and protocol.json. Requires the pinned existing Windows environment and resvg0.49.0; no new dependencies or paid APIs. Environment versions are in reports/environment.json. Source fixtures/licensing/provenance remain in the previous experiments; all are existing benchmark assets. Analytic controls are known-source geometry diagnostics, not an inference engine.

PowerShell setup (set `$py` to the existing isolated interpreter):

```powershell
$py = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\agd-native\Scripts\python.exe'
$env:AGD_RENDERER = 'resvg'
$env:AGD_RENDERER_EXE = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\resvg\resvg.exe'
$env:PYTHONDONTWRITEBYTECODE = '1'
Set-Location 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_VECTOR_BOTTLENECKS_20261027'
& $py test_oracle.py
& $py test_coverage.py
& $py test_bottlenecks.py
& $py bottlenecks.py
```

Completed granularity cases are hash-verified and reused. Do not delete results to force a rerun. To regenerate independently, copy Python source, requirements, protocol and frozen inputs/manifest.json to a NEW sibling directory while retaining the historical dependencies in the repository. Manifest source paths deliberately continue referencing the verified existing historical sources. The seven source hashes and savedresult hashes are checked. `bottlenecks.py` uses its own script directory as ROOT. The new directory must be empty of results; partial cases are refused. Run `run_cycle.py --phase granularity`, `run_cycle.py --phase oracle`, `run_cycle.py --phase coverage`, `run_cycle.py --phase corrections`, then `run_cycle.py --phase dashboard`. This driver supplies the fresh paths and phase resource bounds. Partial/nonempty incomplete oracle/coverage destinations are refused; hash-verified complete phases are reused. No inherited140candidate searches are dispatched.

Historical-spline context is disabled by default after two optional post-level context stalls; enable AGD_INCLUDE_HISTORICAL_CONTEXT=1 only for a separately justified diagnostic. It is not part of the controlled granularity experiment. The current128artifacts are reused, not re-estimated. All new workers have sampled4GiB/900s bounds; fitting is180s per granular level. Native renderer calls still use the historical adapter and have their own reported limits.

`bottlenecks.py --dashboard` rebuilds the comparison images from actual vectors and existing native outputs, without fitting or tracing. Oracle/coverage dashboards are shipped separately. Extra historical context changes region family and is not a controlled variable. The new recovery metadata documents exactly which completed evaluations were reused after the interruption. Preserve negative_results and failed historical_spline contexts.

Main dashboard: index.html. Full native SVGs: results/granularity/<case>/<detail>/{B,C,D}/output.svg and results/corrections/<case>/output.svg. Native source/A reference and JSON metrics are alongside. All zooms render the actual SVG by changing its viewport; nearest-neighbor source crops are only raster references, not high-resolution contour truth.


`run_cycle.py --phase granularity|oracle|coverage|corrections|dashboard|tests` provides bounded orchestration and completed-output reuse. Use the phases individually in that order (tests last); do not paste the pipe-separated list as a shell command. Existing oracle/coverage evidence is reused and should be checked with its dedicated tests/inventory, not overwritten. Granularity workers use900s/4GiB sampled bounds, oracle300s, coverage300s controls/600s real, corrections180s. Native calls remain subject to historical renderer limitations. Run the dashboard phase after all evidence phases; it does not refit or retrace.
