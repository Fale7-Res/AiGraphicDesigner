<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:50:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Reference audit — evaluator only, pending independent QA

Prepared 2026-10-28T14:18:57+00:00. No candidate generation, engine reconstruction, tracing/search or appearance fitting was run. Global architecture NOT_APPROVED.

## Shield

Original repository source is369x249, SHA256 `900b7ee76d9428ab30b654e584a6dd72ea924c55cc116420edfa387527a134f1`. Independently authored approximate polylines are in `references/shield_complete_boundary_reference.json` and `.svg`; `shield_reference_overlay_4x.png` and crown crop support visual QA. They cover the complete DECLARED major contour set: outside silhouette; both metallic bevel boundaries; red/gold interface; full five-tip crown outline/flanks/four valleys; both central ornament lobes and internal fold; both lower-band edges; major junctions and negative-space checks. Subcomponents intentionally repeat outline portions for separate missing-component veto checks; global contour aggregates must deduplicate them.

This is **AI-authored approximate raster annotation, not independent human or exact vector ground truth**. Uncertainty bands are usually1.2–1.8px, central fold2px, highlights broader. It cannot certify subpixel accuracy or unconditional95% precision at1px. Strict fixed metrics and uncertainty-aware evidence must be reported separately; do not lower the frozen acceptance thresholds to accommodate annotation errors. Complete means all predeclared visually significant contours, not every texture, reflection, shadow or hidden/amodal object boundary. The bottom silhouette meets the source frame and is uncertain. Appearance-only highlight/shading traces are separate and excluded from mandatory structural coverage.

## Known controls and rights

`known_control_reference_manifest.json` registers existing fine_features and K01 truth/source SHA256s without copying their originals. Actual resvg8x truth renders and diagnostic foreground masks are stored locally under `C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\reference_prep\external_reference_renders`; paths/hashes/method recorded. Fine-feature assets have unresolved external Arena rights, so neither originals nor derived renders/masks are vendored into this public repository. K01 remains in its original repository location. Corner-background-distance>8 masks are clearly diagnostic and need independent evaluator agreement with analytic expected topology; they are not silently promoted to exact mask truth. Source SVG curves remain the primary known reference.

## Other real inputs

`real_case_review_rois.json` freezes visible feature/continuity ROIs for Tux, Arabic lettering and native cat crop, with source hashes. These are **not** invented contour ground truth and cannot yield valid numerical boundary precision/recall. Tux needs both eye boundaries, beak, belly, feet, wing/hand and exterior components; Arabic needs all loop/stem/sweep/terminal and thin crossing continuity; Cat needs both lids/iris/pupil,nose and whiskers, while fur/illumination stays uncertain. ROI review does not recover semantics or editable typography.

## Pending gate

Independent QA must inspect shield full/crown overlays and all named component presence before the parent freezes these references and before any candidate is generated. Annotation corrections must be append-recorded before that freeze, never tuned after observing candidate failures. Uncertain/missing evidence must remain UNKNOWN, not fabricated precision or automatic success. References are evaluator-only and must never be supplied to segmentation, curve initialization, construction templates or candidate selection.

## Pre-freeze independent QA clarification

Independent reviewer ablation_qa inspected full/crown overlays and found the declared crown coverage complete at an approximate level. The central internal fold remains a mandatory visible-feature REVIEW item with UNKNOWN interpretation; it is not a required physical closed boundary or topology veto. It is now amber/dashed in the overlay. All traces remain unsuitable for strict1px certification (NOT_ESTABLISHED). Fine-detail ROI rectangles are review windows only: exemptions require positively identified genuine foreground detail, never arbitrary pixel-grid faces/background islands inside a box. No candidate was observed before this clarification. Freeze remains pending final reviewer acknowledgement.

## Reference freeze

After independent QA verified the requested role clarifications, the descriptive evaluator set was frozen at 2026-10-28T14:24:39+00:00, before candidate generation. Set SHA256 `e70a475ab8fcaea275084f77f807428c2183485b3687d32e4b66fd295ac6d0cc`; per-file hashes in `references/FREEZE.json`. This accepts declared feature coverage for descriptive evaluation only. Strict shield1px numerical acceptance remains NOT_ESTABLISHED. No production/geometry milestone is approved.
