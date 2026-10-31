<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:16:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:16:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:16:24Z"}
END_DOC_PROVENANCE -->
# Restricted local geometry engine

`geometry_engine.py` exposes `GeometryToolEngine(rgb, traces, initial_items,
output_dir, repo, work, renderer=None)` and `geometry_tool_schemas()`.
The parent supplies trusted paths and immutable source data. Model-controlled
arguments have no file paths, code, shell commands, model names, credentials,
raw coordinates, or network URLs. The only coordinates are normalized source
inspection ROIs; they do not construct geometry.

Call `dispatch(tool_name, arguments)` for all controller operations. Returned
values are JSON-safe. `export_state()` returns a deep copy of accepted curves
and hashes; it is a trusted application API, not a model tool.

Tools:

- `inspect_region`: `{roi:[x0,y0,x1,y1]}` in normalized source coordinates.
- `get_candidates`: same ROI and `limit:1..16`. Existing trace IDs are excluded.
  Ranking first exposes traces meeting unchanged >=6px fitter eligibility,
  then fixed source-gradient support/closed contour/local support and trace ID.
  Ineligible traces fill unused shortlist slots only; no short connector is
  recovered by changing this presentation policy. Each
  proposal explicitly records >=6px eligibility and uncertainty about lighting.
- `stage_candidates`: `{trace_ids:[...]}` with 1..4 unique frozen source IDs.
  Uses the historical P partitioned fitter without modifying its .6px gate,
  source coordinates or corner/closed-loop policy. Staging does not change the
  accepted geometry. Every requested trace receives a ledger entry.
- `commit_change`: `{}` validates and atomically appends safe staged curves.
- `rollback_change`: `{}` first discards pending geometry, otherwise restores
  the previous committed snapshot exactly. Rollbacks do not replenish budgets.
- `validate_geometry`: `{}` returns fixed complexity/closure diagnostics.
- `render_geometry`: `{scale:1|4|16}` invokes the trusted resvg executable on
  corrected serializer output. Model cannot choose filenames or executable.

Budgets are shared by every controller:12 total calls,2 committed edits,
144 paths,4096 cubics,<=4 source traces per staging call,20 seconds cooperative
fit deadline,30-second renderer timeout,16 million preview pixels. The caller
must additionally enforce process-tree runtime/RAM limits. These are CPU
geometry operations and need no provider access.

The path cap allows16 extra paths beyond the principal128-path P control;
all controllers receive the same cap. Multiple output chains from one trace
consume multiple paths. Rejected partitions remain in the per-trace ledger.
No arbitrary interpolation, endpoint snapping, region birth, detector reruns,
pixel-grid fallback, segmentation edits or semantic region ownership occurs.

Safety guards reject newly introduced sampled self-intersections, proper
crossings/overlaps not present in corresponding raw polylines, displaced
crossing evidence, duplicate curves, disconnected chains and false closure.
Existing intentional raw crossings are retained as uncertainty, not interpreted
as valid planar faces. Inherited baseline validity is not retrospectively
claimed. Numerical flattening and .6px fitting checks are not certified exact
continuous predicates. No complete geometry acceptance follows from tool tests.

Each call creates an exclusive `event_NNN.json` with previous-record hash,
before/after geometry hashes, validated arguments and response. Invalid arguments
are not echoed into logs. This is application-level append-only evidence, not
tamper-proof storage against an OS user with filesystem access. Geometry replay
is deterministic; renderer/fitter durations in audit evidence are observational
and excluded from geometry identity. Use a new empty output directory per replay.

Run12 synthetic controls:

```powershell
& '.\work\agd-native\Scripts\python.exe' -m unittest discover -s work\agentic_geometry\engine -p test_geometry_engine.py -v
```

Controls cover actual resvg1/4/16 rendering; strict finite schemas; prohibited
path/code inputs; staging isolation; exact rollback; duplicate IDs and duplicate
geometry; closed corners/shared endpoints; nested boundaries without invented
hole semantics; deterministic geometry replay; normalized ROI bounds.

No model or paid API was executed by this module or its tests.

Source gradient uses the mean RGB intensity derivative, so equal-luminance
color boundaries can receive low support, texture and lighting can score well,
and blank regions have little discriminating evidence. It is a candidate-order
heuristic, not calibrated structural confidence or geometric ground truth.
The policy is identical for deterministic, recorded mock and optional model
controllers; source and evaluator data remain isolated.
