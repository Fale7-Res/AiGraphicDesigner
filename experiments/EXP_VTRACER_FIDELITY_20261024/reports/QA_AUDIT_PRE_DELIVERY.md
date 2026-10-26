<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-25T23:21:01Z", "last_action": "CREATED", "last_change_id": "VTRACER-AUDIT-ARCHIVE", "last_edited_at_utc": "2026-10-25T23:21:01Z", "last_editor": "parent", "tracking_started_at_utc": "2026-10-25T23:21:01Z"}
END_DOC_PROVENANCE -->
# Independent VTracer fidelity research audit

AUDIT_RESULT: PENDING_COMPLETE_BENCHMARK

Scope: isolated `EXP_VTRACER_FIDELITY_20261024`, not production approval or semantic reconstruction certification.

## Code and protocol review

Read complete `src/search.py`, `src/evaluate.py`, `src/test_search.py`, `src/baselines.py`, `run_benchmark.py` and `protocol.json`. Search normalizes input explicitly, renders native dimensions, excludes embedded raster/external references/scripts, records all trials, and uses an explicit multimetric score without a complexity penalty. The shared evaluator's source-resolution metrics are not proof of scalable professional artwork.

Development selection uses only the thirteen shared pilots across A01/A03/A05/A10; adaptive local probes are excluded from common-preset selection. The runner freezes the selected preset, evaluates all eight held-out images, records completion, then separately performs per-image optimization. The protocol is sound as written; final artifacts and chronology remain to be checked. The benchmark suite is finite and already familiar to the project, so no universal optimality claim is justified.

## Verified evidence so far

- Independent rerun of the A03 selected candidate produced a byte-identical SVG and PNG, with exact metric and score equality; recorded in `qa_reproduction.json`.
- Native A03 source/best visual review: substantial preservation of seed/material details; dark-background tonal quantization remains visible. Pixel-mode source fidelity is not smooth scalable reconstruction.
- A03's four local probes have identical metrics to the pixel-mode pilot winner. This is a retained no-op result, not proof that all parameter directions are optimized.

## Findings

| Severity | Finding | State |
|---|---|---|
| MEDIUM | Historical baseline highpass error used sigma2 while search used sigma1; DeltaE duplicated | Requested shared `extra_metrics` and recomputation from existing PNGs |
| LOW | Composite score can favor different tradeoffs from human judgment | All metrics retained; native visual review and separate acceptance gate required |
| LOW | Worker timeout does not explicitly terminate a process group | Native renderer itself has a120s timeout; no timeout failure observed yet |

## Closing checks pending

Complete twelve-image search and eight frozen-preset evaluations; all output PNG integrity; per-trial metrics/score/structure reproduction; ranking/best-file identity; frozen configuration provenance; final baselines consistency; exact source mirrors and catalog; historical hashes.

No AI training, semantic layers, Arabic recognition or general alpha-preserving SVG reconstruction is certified by this audit.
