<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:16:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:16:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:16:24Z"}
END_DOC_PROVENANCE -->
# Independent QA preflight

Scope: isolated tool-controlled geometry proof of concept. No live provider call, key reading, feature implementation, historical experiment rerun or candidate tuning is performed by this reviewer.

Required falsification checks:

- Every model-visible tool has a finite typed contract, rejects extra properties, nonfinite numbers, bool-as-int, out-of-range coordinates and unknown IDs. No executable code, paths, URLs, Git actions or credentials are accepted as tool arguments.
- A malformed or unsafe edit leaves accepted geometry unchanged. Rollback restores a prior accepted state, records an auditable event and cannot remove the immutable history.
- Deterministic replay from frozen inputs reproduces geometry hashes, SVGs and action decisions. Audit hash-chain integrity is checked by an independent implementation.
- Candidate construction and planner context exclude evaluator-only masks/guides/answer curves. Evaluation may use them only after construction.
- The deterministic and mock controllers have identical action and crop/iteration budgets. A mock plan is a contract test, never evidence of learned planning performance.
- Corrected serializer preserves continuous cubic coordinates and closed-subpath behavior. Actual renderer output is required. No embedded image, source-grid rectangles or raster underlay is permitted in exported geometry.
- Live Groq remains blocked unless account free-tier/available quota/zero-charge status and permitted transmitted images are independently established. An API key, successful request, model listing or rate-limit headers alone cannot establish billing status.
- Existing staircases, uncertain crown guides, Arabic raster proxies, photographic edge ambiguity and incomplete semantic regions remain explicitly limited claims.

Prior evidence reviewed: complete owner vision; AGENTS and provenance policy; Universal Region/Coherence report and independent final QA. Parent reports baseline local/remote main `46870cbf`; this review does not independently certify publication yet.

Awaiting implemented tool/controller API for adversarial and replay tests. Geometry NOT_ACCEPTED. Architecture NOT_APPROVED. Real AI performance NOT_TESTED until authorized live inference exists.
