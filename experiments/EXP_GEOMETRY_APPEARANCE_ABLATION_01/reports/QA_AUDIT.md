<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T14:58:15Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T15:07:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T14:58:15Z"}
END_DOC_PROVENANCE -->
# Independent QA audit

AUDIT_RESULT: PASSED — bounded execution and saved-evidence contracts only. Production architecture remains **NOT_APPROVED**. This verdict does not approve visual fidelity, coherent geometry, Clean SVG, Magic Layers, or owner acceptance.

Auditor: `/root/ablation_qa`, independent from the runner, fitter and prior-evidence packaging authors. Audit performed on 2026-10-27 against local baseline commit `c9bd9d95c680e1404165025915ed1739050ede74` and isolated uncommitted research additions.

## Scope and independently executed checks

- Read complete owner vision, repository QA/provenance instructions, `run_experiment.py`, `fit_appearance.py`, both ablation test modules, and previous experiment packaging source/report/tests. Historical owner vision and implementations were not edited by this auditor.
- Independently executed the five fitter tests: all passed, including actual resvg linear/radial renders, transformed paths, gradient capacity, alpha-squared fitting and fixed geometry.
- Independently executed six saved-generalization tests: all passed. They verify eight cases/seven originals, 140 successful candidates, identical inherited/selected winners, selected tested alpha, 213 SVG / 553 PNG integrity, metrics, visual assets and preservation inventory. No historical searches or SVG renders were repeated by this audit.
- Independently executed the five ablation saved-artifact tests: all passed. The complete nine-case suite, hashes, strict ordered B/C/D geometry and alpha-mask identity, SVG/PNG safety, metrics, zoom sheets and known-control geometry artifacts passed.
- An additional independent read-only script checked frozen source/reference/geometry/ground-truth hashes, ordered C/D path attributes, exact B/C/D mask subtrees, sorted two-to-four gradient stops, absence of image/filter/script/foreign-object elements, winning SVG hashes, and independently recomputed white-background MSE and SSIM for all 36 principal SVGs. Recomputed values match saved values exactly.
- Eight adversarial checks passed: the strict geometry contract detects style, fill-rule, transform and path-order drift; fitting rejects inherited style, opacity, mask and filter inputs.
- After integration, independently verified all eight scoped Python source hashes against generated mirrors, all 62 verbatim code blocks against actual source, and all 62 documented declaration ranges against AST function/class lines. Both scoped registries record zero exact-name duplicates. File relationship descriptions are generic; their precision is a documentation limitation, not proof of richer architectural analysis.

## Findings raised and resolved

| Severity | Finding | Resolution |
|---|---|---|
| HIGH | Rocket source was initially evaluated as raw RGB while inherited A/B were ICC-normalized sRGB. This produced a false A-reference SSIM of 0.929119. | Parent retained the confounded run under negative results and reran only the corrected bounded appearance case using saved normalized sRGB. Correct A SSIM is 0.996047144718033. Other seven prior dataset raw/prepared RGBA arrays were independently checked and are identical. No historical search rerun was needed. |
| MEDIUM | Initial runner did not enforce frozen input hashes or completed-output hashes on reuse. | Pre-run frozen source/reference/geometry/ground-truth checks and completed output-hash checks added. |
| MEDIUM | Identical geometry and masks do not guarantee byte-identical output alpha in resvg. | Independent checks found one-level C/D alpha quantization differences in seven cases, zero difference in Arabic and K01. Parent was notified to measure/disclose them. Geometry/mask identity is the experimental invariant; exact rendered-alpha identity is not claimed. |
| MEDIUM | Generic spline statistics were insufficient as known-vector geometry evidence. | Known controls now include 4x foreground-union IoU, bidirectional boundary distances and foreground-hole counts, with explicit classification assumptions and limited scope. |

No unresolved blocking feature or evidence-contract defect was found in the final checked principal artifacts. Final report/governance packaging must retain the qualifications below.

## Scientific conclusion checked against actual outputs

Gradient fitting provides real appearance-capacity evidence at fixed geometry. It does **not** meet the owner fidelity goal. White-background SSIM for shield changes C 0.748810 to D 0.815371 while A is 0.995660; coffee changes 0.485733 to 0.535965 while A is 0.997894; fine-detail fur changes 0.325667 to 0.395686 while A is 0.999823. Arabic selects no gradients and C/D are unchanged. Other cases also retain substantial gaps. These are distinct claims from geometric validity and generalization.

Visual inspection of actual native sheets and shield 16x vector render confirms restored broad shading but inaccurate outline/band/crown placement and lost texture. Fur remains severely simplified, including eyes and whiskers. Dice retains incorrect segment boundaries/reflection detail. The radial known control recovers its highlight but preserves spurious watershed shading bands. Improved SSIM/MSE alone does not justify acceptance.

Known-control foreground IoUs are approximately 0.99108 and 0.99308; expected foreground hole counts are retained. These foreground-union checks do not prove internal region correspondence, junction correctness, nonintersection, complete topology, semantic coherence or professional editability. One uniform watershed detail128 geometry is tested; this does not falsify all VTracer spline configurations or the shared-boundary core.

## Material limitations

- Fitting uses disjoint deterministic periodic training, selection and test pixels. This validates interpolation on the same image, not held-out spatial blocks or domain generalization. Tiny regions without independent samples retain flat models and disclose that limitation.
- Only interior pixels are fitted; antialiasing mixtures, seams, missing boundaries and texture are not optimized. At most four equally spaced gradient stops, radial focal point equal to center, restricted center search and clipped least squares are capacity/optimization constraints, not globally optimal appearance fitting.
- Source alpha is held in identical inherited run masks for B/C/D. This is explicitly grid dependent. Alpha-squared weighting improves the visibility objective but does not reconstruct coherent alpha geometry. Actual output alpha and three background appearances must remain visible in the report.
- Safety checks parse SVG/XML and reject prohibited raster/external/script content. They are not exhaustive SVG conformance, Illustrator/Figma/Photoshop interoperability, or a second-renderer certification.
- Process memory is sampled simultaneous tree RSS, with a soft 4GiB guard and ten-minute process limit, not a guaranteed OS-enforced peak ceiling. Runtime measurements are single bounded executions, not statistical performance distributions.
- Prior generalization evidence has seven independent originals across eight cases, mostly max-edge320 rasters. It is not an original-resolution or universal-generalization benchmark. The alpha-aware reranker changed no winning candidate; no improvement may be attributed to it.

## Preservation and governance qualification

Initial tracked tree was clean. At final artifact audit, the sole tracked modification was the prior generalization experiment's scoped session WAL; new files were scoped research packaging and the new experiment. Untracked historical `__pycache__` files were reported to the parent for verified generated-cache cleanup. No owner vision, production approval state, historical algorithm, saved search, SVG or PNG evidence was intentionally modified. Saved-evidence tests confirm preserved input/dataset/result bytes.

Scoped code-mirror hash/snippet/line checks are independently complete. The parent must finish document provenance and final inventory after integrating this report. Repository-wide governance has historical blockers and must not be reported as globally passing based on this bounded QA. No Git commit or push is certified by this audit; publication requires actual Git confirmation or the scoped owner-run procedure.

Recommendation: retain these results as a positive but insufficient fixed-geometry appearance ablation. A follow-up should separate segmentation/geometry error from appearance capacity, including known geometry controls, before committing to a replacement engine or broad curve-motion architecture. Any substantially different experiment requires a new owner decision.


## Independent packaging follow-up

Agent ablation_qa independently verified ZIP CRC, all261 derivative byte hashes and manifest correspondence; all36 nativeSVG hashes remain unchanged; all216individualzoomPNGs and54comparison sheets remain available; all99dashboardlinksresolve. ScopedgovernancePASS. Noenginechangesornewexperiments were performed.
