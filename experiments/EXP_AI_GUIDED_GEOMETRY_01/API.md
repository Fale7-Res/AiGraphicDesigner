<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:16:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:16:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:16:24Z"}
END_DOC_PROVENANCE -->
# Data flow and authority

Owner-approved experiment configuration supplies native RGB, frozen source traces and saved P geometry to GeometryToolEngine. Planner supplies only strict function arguments (ROI or source IDs). The engine stages curves using the pinned P fitter and guards, retains immutable event ledgers, serializes through the corrected exporter and calls fixed local resvg. Provider has no geometry/filesystem/Git execution authority.

run_sessions.py compares deterministicB and recordedmockM; evaluate_sessions.py alone reads truth/guide files. groq_pilot.py calls the interchangeable adapter, validates structured tool arguments, executes locally, returns diagnostics and actual preview images. Provider requests are bounded and defaultdryrun. Journal/geometry/replayidentity separate observedtimings.

Existing network diagnostics/atomic region integrator are evaluator-only here. No semantic region assembly, detector birth, acceptedcurve refinement or full appearance implementation is claimed. These require new controlled tools/decisions.
