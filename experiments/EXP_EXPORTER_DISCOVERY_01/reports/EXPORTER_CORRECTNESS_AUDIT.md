<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:00:15Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:00:15Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:00:15Z"}
END_DOC_PROVENANCE -->
# Research exporter correction

Created 2026-10-29; historical source is preserved unchanged.

## Verified defect

`EXP_COMPLETE_GEOMETRY_ISOLATION_01/geometry_eval.py:72-106` has the affected exporter. Its local `data()` appends `Z` to every fitted closed chain. Face assembly removes the initial `M` from later chains but leaves their `Z`. That close therefore returns to the containing SVG subpath's origin rather than the closed chain's own origin. It also resets the current point, affecting following commands. The [SVG 2 path specification](https://www.w3.org/TR/SVG2/paths.html#PathDataClosePathCommand) defines these current-point/subpath semantics.

The raw branch does not append chain-level `Z`, so this particular defect affects fitted compound face exports, not raw branch exports. Independent stroke paths retain their own `M` and do not have this wrong-origin defect. A closed chain used in isolation is likewise not evidence of failure. Graph numerical measurements performed directly on arrays are not changed by this serialization defect.

Prior passive audit reports 1/7/24/0 affected embedded closes for Fine Features/Arabic/Shield/K01. Those counts and benchmark consequences are inherited findings, not a new benchmark rerun by this implementation task.

## Minimal corrected strategy

`svg_exporter.py` provides compatible `svg_graph(graph, raw=False, regions=False, foreground=None)` with optional keyword-only `precision=17` or `precision=8`.

- Convert each logical closed chain's implicit straight closure into an explicit `L` to its own start.
- Reverse the complete directed walk, including that closure, when a face uses a reverse reference. Reverse cubic order and swap its control points.
- Concatenate only endpoint-connected walks; reject disconnected chains and open face loops. No endpoint snapping or geometric repair occurs.
- Emit one `M ... Z` for each actual closed face contour. Preserve region order and inherited `fill-rule="evenodd"` for holes and nested contours.
- Export independent stroke chains separately. Open chains have no `Z`; closed chains retain closing-join behavior through `Z` after their explicit closure.
- Default 17 significant digits roundtrip Python floats. Precision 8 provides closure-correct legacy-rounding control for fitted impact attribution. Raw legacy formatting was 6 significant digits; raw grid coordinates in these controls are integers, but general raw precision should not be conflated with the closure correction.
- No new faces, chains, curves, rectangles, masks, rasters, or fitting parameters are introduced.

The strict consistency tolerance is 1e-8 coordinate units. This is an explicit rejection bound, not a proof of mathematically exact curve incidence. Existing graph validity failures remain visible and are not repaired by serialization.

## Caller audit and impact scope

`exporter_callsite_audit.json` records exact file/line mentions from read-only repository scanning before the new experiment source was integrated. There is one historical definition and 14 call mentions:

- `EXP_COMPLETE_GEOMETRY_ISOLATION_01/analyze_matrix.py`: raw labels and raw/fitted region or chain exports.
- `audit_raw_labels.py`: raw-only region exports.
- `final_diagnostics.py`: fitted visible-region IDs (potentially affected); independent chain failure examples (not wrong-origin affected).
- `make_overlays.py`, `package_evidence.py`: independent chain drawing (not wrong-origin affected).
- `validate_geometry.py`: fitted foreground region render and therefore render-derived topology/IoU can be affected.
- `test_isolation.py`: historical synthetic region serializer control, not broad correctness coverage.
- `EXP_THIN_STRUCTURE_TOPOLOGY_01/evaluate_study.py`: fitted foreground and per-condition region outputs can be affected; direct array metrics remain unchanged.
- Its `additional_diagnostics.py` and `dashboard.py` draw independent chain paths, not assembled face fills.
- `EXP_RAW_FACE_JUNCTION_01/run_case.py`: fitted region equivalence gate is directly affected; raw gate is not affected by embedded fitted Z.

These are call-site categories, not claims every output from them is wrong. Exposure requires an actual embedded closed chain and the relevant compound walk configuration. Impact on exact historical artifacts must be measured against frozen graphs with closure-only and precision controls. Historical SVG/PNG files are not replaced.

Read-only inspection of other named exporters in version-01 planar tracer, version-01 pipeline, version-02 pipeline and version-03 Bézier helpers shows independent `M` initialization before closing each subpath, or standalone cubic commands consumed by such initialization. No analogous removal of `M` while retaining an embedded `Z` was found there. This is scoped static inspection, not an exhaustive production correctness certification. VTracer's native exporter is not implicated by the research helper bug; no VTracer-native defect is established.

## Independent controls actually executed

Nine unit test methods passed with Python 3.14.2. They include an independent M/L/C/Z command-state interpreter (does not reuse serializer segment generation), exact known expected reversed-cubic control points and closure segments, immutability, fail-closed unsupported/disconnected/open/nonfinite controls, and explicit precision testing.

The actual resvg 0.49.0 executable rendered eight generated/canonical SVG fixture pairs: open path, closed sharp corner, nested hole/island contours, embedded closed-chain/repeated junction, reversed cubic, independent closed subpaths, mixed open/closed strokes, and opposite-direction shared boundary faces. Each generated/canonical pair had identical full RGBA pixel bytes. Nested holes additionally have independent occupied/empty/island pixel assertions. This validates these bounded fixtures, not arbitrary renderer/graph correctness.

Run `python -B test_svg_exporter.py`. Set `AGD_RESVG` for another resvg location and `AGD_EXPORTER_FIXTURE_OUTPUT` to preserve actual SVG/PNG fixtures. The test fails rather than silently skipping if resvg is unavailable. No historical benchmark fitting or candidate matrix was executed by this task.

## Remaining limits

No serializer can restore missing segmentation or crown boundaries. Evenodd face decomposition can alter antialias/compositing when paint grouping changes; corrected O/R renderer equivalence must therefore be tested, not assumed from path algebra alone. Closed invalid graphs can remain self-intersecting. The independent parser intentionally supports only the explicit absolute command vocabulary emitted by this serializer and is not a universal SVG parser. No final geometry acceptance or appearance similarity claim is made.
