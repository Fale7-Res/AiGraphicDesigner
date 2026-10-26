<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "VTRACER-DELIVERY-QA", "last_edited_at_utc": "2026-10-25T23:20:31Z", "last_editor": "final_audit", "tracking_started_at_utc": "2026-10-25T15:03:37Z"}
END_DOC_PROVENANCE -->
# Independent final delivery audit

AUDIT_RESULT: PASS_RESEARCH_ARTIFACTS_WITH_DOCUMENTED_LIMITATIONS

The all-artifact check and targeted recovery verification are complete. This is a research-artifact audit, not production approval or independent retracing of every candidate. The prior pending report is preserved as QA_AUDIT_PRE_DELIVERY.md.

## Independently executed this session

- Read complete search/evaluation, benchmark runner, historical rerender, extension and visible-color-refit source and relevant tests.
- Ten research tests passed; see tests_delivery.log. ResourceWarnings about PIL handles remain a minor implementation issue, not a failed fidelity assertion.
- Recomputed native-render metrics, composite scores and serialized geometry for248 successful result records:232 current primary/common/extension trials plus16 retained interrupted-run records.
- Recomputed37 historical conditions and checked4 fixed-geometry refit cases, including invariant geometry and non-increasing least-squares SSE.
- Checked20 rankings and349 SVG files for parsing, raster exclusion and external/script references.
- Full PNG scan decoded502 files and found one truncated400% Burger render. Its recovery was independently verified afterward;503 total PNGs pass across full scan plus targeted closure. The original failure remains in qa_checks.json; qa_recovery_closure.json resolves it. Two earlier trial PNG repairs also decode and exactly reproduce their saved metrics.
- Recomputed four-development common-preset argmax and hash, checked all eight primary frozen configurations, all eight separately frozen extension configurations and all twelve final SVG/PNG source-copy identities. See qa_delivery_protocol.json.
- Exercised extension development-resume guard: existing freeze hash unchanged and no new trial executed (qa_extension_resume.json).

The existing qa_reproduction.json records an earlier independent A03 retrace with byte-identical SVG/PNG and exact metric equality. It was read but not rerun in this delivery closure. Historical engines were not regenerated here: saved historical SVGs were rendered earlier, and their metrics were recomputed now. Do not describe all248 checks as independent tracing reproductions.

## Visual inspection

Independently viewed final A01 and A03 native comparison sheets. Shield crown, foreground contours and material detail are much closer than the owner preset, but the background and soft shadow remain badly flattened/stepped. Burger seeds and filling boundaries are substantially preserved, with dark background tonal quantization remaining. Other cases retain separately attributed visual review records. No blinded perceptual study, complete sesame detection precision/recall, Arabic OCR or unseen-domain generalization is established.

Final mean SSIM0.986856 and PSNR45.0016 are per-image post-hoc selection statistics, not held-out-preset quality. The shield failure prevents declaring the fidelity milestone passed.

## Remaining limitations

- Pixel-mode outputs contain dense source-grid-derived geometry. Raster-free SVG does not establish clean scalable artwork, semantic layers or professional editability.
- The fixed multi-metric score can choose tradeoffs different from SSIM or human judgment; all metrics and visual review are retained.
- Four adaptive probes after pixel-mode selection are often no-ops, not evidence of a global optimum.
- Runner completion markers do not themselves strictly enforce all expected input identities/success statuses; this audit verifies the actual delivered cases independently. Tighten preflight for reuse on arbitrary datasets.
- Worker timeout does not terminate a process group explicitly; renderer has its own timeout. No benchmark timeout failure observed.
- Explicit white alpha compositing is the tested contract. Arbitrary transparency, ICC profiles and cross-editor compatibility are not certified.
- Historical high-pass sigma mismatch was corrected to the same extra_metrics implementation; initial superseded summary remains available.

Reviewed reproduce.py and the delivery installer: reproduction uses a new directory, ordinary differing file collisions are diverted, identical files skipped and exclusive creation prevents overwrite. An intermediate-directory collision or symlink fails safely rather than being replaced. The full new reproduction launcher was not rerun end-to-end to avoid repeating completed benchmarks; parent tested preparation/refusal and installation fixtures.

Mirrors, catalog/provenance, historical-file hashes, archive integrity, manifest completeness and installation on the owner's unseen local project are parent delivery checks, outside this artifact auditor's certification. No GitHub write operations or production approval are authorized by this audit. Architecture remains NOT_APPROVED.
