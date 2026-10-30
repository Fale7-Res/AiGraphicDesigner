<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:13:29Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:13:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:13:29Z"}
END_DOC_PROVENANCE -->
# Independent QA — frozen protocol and exporter implementation

Reviewer: /root/export_discovery_qa. This is a pre-benchmark review and abstract verification, not final geometry acceptance.

## VERIFIED

- Independently verified 61 frozen policy, source/candidate, dependency and reference hashes. Evidence: verify_frozen.py and frozen_integrity.json. No candidate/reference mutation was performed.
- Inspected the historical svg_graph implementation and affected call sites. The embedded-chain `Z` defect is real and scoped to compound fitted-region assembly. Chain-only geometry, analytic area and native VTracer exports are not shown defective by this audit.
- Inspected staged svg_exporter.py. Explicit logical chain closure precedes concatenation; complete directed traversal is reversed including its implicit closure; reversed cubic controls are swapped correctly. Actual face contours alone receive final `Z`. Open standalone chains remain open. Disconnected/nonfinite/unsupported/open-face inputs reject instead of repairing.
- Independently executed all nine staged regression tests, including actual resvg canonical fixtures; all passed. Controls include open/closed paths, sharp corners, nested evenodd holes, shared boundaries, independent subpaths, embedded closures, reversed cubics and mixed open/closed output.
- Independently implemented a third-party fontTools path parser audit, separate from the implementation's parser. Four hundred semantic checks passed: 100 deterministic random closed L/C walks, raw/fitted, both orientations. Evidence: independent_semantics.py/json. No benchmark segmentation or fitting was rerun.

## Phase B constraints

Frozen O/R render equivalence remains prerequisite; a failure blocks that case. No parameter or safety-guard changes are permitted. Decomposition changes ring counts and target grouping, so accepted chain identities and full control-point deltas must accompany raw/collapsed-ring counters. Component/hole correctness and crown geometry cannot be inferred from area repairs alone. Old render-derived foreground/proxy metrics, topology counts and visible microgeometry may be affected; old chain/area evidence remains independently useful.

## Phase C source-only assessment

discovery_strokes.discover accepts native uint8 RGB only and uniform fixed parameters. No evaluator mask, case name, guide, source SVG or ROI enters construction. Paired flank Lab support, skeleton tracing, constant-width profiles and bounded cubic proposals can produce strokes independent of existing segmentation endpoints. This meets the intended stronger discovery hypothesis at proposal level.

Important limitations are frozen rather than tuned away: centerline evidence starts on pixel centers, not subpixel localization; width is one median per stroke; skeleton junctions split chains without graph integration; flank contrast can respond to lighting ridges; source_confidence is not calibrated structural confidence. Curve-error testing is sampled, not continuous certification, and may overreject long straight spans because fixed 32-interval samples sparsely cover them. Existing full geometry and critical components must remain unaccepted if unsupported. Constructor CONFIG resource fields are descriptive; the outer worker monitor must actually enforce 60s/512MiB.

The owner-directed classical/pretrained/hybrid comparison belongs to final recommendation only. No model download, training, hosted inference, new neural dependency or architecture adoption is authorized inside this experiment.

Final saved-output and scientific-claim QA remains pending. Tests establish bounded serialization behavior, not professional geometry or final visual fidelity.
