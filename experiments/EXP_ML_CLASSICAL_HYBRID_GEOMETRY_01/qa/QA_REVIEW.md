<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T08:21:42Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T08:24:43Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T08:21:42Z"}
END_DOC_PROVENANCE -->
<!-- DOC_PROVENANCE {"created_at_utc":"2026-10-30T08:05:08Z","last_edited_at_utc":"2026-10-30T08:12:09Z","tracking_started_at_utc":"2026-10-30T08:05:08Z","last_action":"EDITED","last_change_id":"AGD-ML-INDEPENDENT-QA","last_editor":"ml_geometry_qa"} -->
# Independent QA — pretrained/Classical/Hybrid geometry

Reviewer: /root/ml_geometry_qa. **AUDIT_RESULT: PASSED for bounded artifact integrity and metric checks, with the limitations below; full report/dashboard review remains pending.** This reviewer did not run inference, retrace candidates, change features, or select parameters. Geometry remains NOT_ACCEPTED; production architecture NOT_APPROVED.

## Verified independently

- Read complete AGENTS, owner vision and prior exporter final QA. The original complete product scope is preserved; appearance, typography implementation and Magic Layers are absent from reviewed constructors.
- All 34 protocol source/baseline/evaluator/exporter pins match actual SHA256. The ONNX cache hash independently matches a50d01dc8481549c7dedb9eb3e0123b810a016520df75e4669a504609982cdd0. The immutable OpenCV revision and model-directory MIT notice are recorded; this is explicit publisher licensing evidence, not an inference from the framework license.
- Inspected inference and construction source completely. Inference reads only RGB source and ONNX. Constructor uses source RGB, frozen classical edge evidence, learned probabilities and shared old/stable fitters; no evaluator contours, truth masks, benchmark-specific geometric construction or model training are passed into candidate generation. Case names choose paths, not shape templates.
- Independently checked all four raw ONNX outputs: finite 1x1x256x256. Native probabilities equal sigmoid of the saved raw output resized with bilinear interpolation, exactly in this environment. BGR means and scale match the published OpenCV wrapper; the actual 256-square input differs from upstream default 512 and distorts aspect ratio before native remapping.
- Five stable-fitter unit tests pass independently. These verify per-chord handles, corner support, fixed complexity rejection, finite input and segment distance semantics. They do not establish complete reconstruction.
- Parsed all twelve saved stable candidate SVGs, checked path counts/cubic commands against saved accepted geometry and exact numerical control-point roundtrip. Each path has exactly one move; all cubic junctions are equal. No image/script/foreignObject/rect appears. Independently rendered all twelve with actual resvg. Closure semantics use the corrected exporter. These outputs are open-boundary proposals, not complete shared faces.
- All accepted curves currently report sampled-simple numerical paths. This does not prove mutual intersection freedom or certify exact continuous topology.

## Scientific limitations and required disclosure

1. **Resource amendment:** the frozen initial protocol says512, but reports/RESOURCE_DECISION_BEFORE_RETRY.json records one256 fallback after a512 resource stop and before new completed predictions. This is a documented feasibility amendment, not model superiority evidence. Final report must expose both configurations and failure. Native classical detection vs downsampled learned inference compares the feasible systems on this laptop, not pure matched-resolution detector capacity.
2. **SAM:** skipped from a conservative risk screen. No measured SAM CPU failure or proof of incompatibility exists. Its absent region-proposal arm limits conclusions to learned edge evidence.
3. **Initial construction memory monitor:** launcher-only sampled RSS3.9MiB does not measure child Python/OpenCV memory. Actual construction peak RAM is unavailable for those runs; cannot claim that768MiB was enforced. Inference monitor correctly sums process tree. Preserve this defect and use improved monitor only for future independent runs; no unnecessary retracing to manufacture measurements.
4. **Display width deviation:** protocol says0.7px diagnostic strokes; inherited corrected exporter actually emits0.35px. All arms share it, but rendered proximity/coverage metrics are width-sensitive. Do not silently claim protocol-exact width, or change original candidates after results.
5. **Fitting safety:** stable_fit accepts on numerical deviation, not on the simple-path field. It is an overshoot/deviation control, not a topology-safe reconstruction method. Mutual crossings, missing regions, holes and connectivity must remain separate negative metrics.
6. **Budgets:** length-ranked128-trace selection and old+stable fitting share120s arm time. Post-fit recall is potentially confounded by selection/compute limits; report discovery first and explicit rejection reasons. Absence from accepted curves does not prove absence in ML evidence.
7. **Hybrid subset:** gating can delete learned evidence but cannot birth boundaries absent from learned evidence. Improved apparent precision through deletion does not establish completeness. Joint recall/precision and critical guides are necessary.
8. **References:** Shield guides remain1.2–2px uncertain and incomplete human truth. Arabic threshold topology is a proxy. Source-Canny-distance false-positive metric cannot distinguish all genuine new boundaries from metallic lighting. Do not label those metrics semantic correctness.
9. **Rights:** the Arena Fine Features source and derived outputs must remain local-only pending reuse rights. Published hashes and reproduction instructions are acceptable; publication cannot claim a fully redistributable dataset.

## Snapshot result integrity

|Case|Classical paths/cubics|ML paths/cubics|Hybrid paths/cubics|
|---|---:|---:|---:|
|Shield|127/1068|30/317|32/387|
|Arabic|1/33|23/441|20/363|
|K01|0/0|0/0|0/0|
|Fine Features|15/51|1/39|1/39|

Numbers are verified artifact counts, not acceptance scores. Empty K01 candidates are a real failure requiring pre-fit/fitter attribution. Sparse Shield results cannot establish full crown/frame reconstruction. No final-image SSIM, completed holes, variable-width thin objects, graph integration or complete geometric acceptance is established by these open strokes.

## Independent quantitative follow-up

Brute-force distance calculations independently reproduce all48 Shield raw guide recalls (16guides across3arms), including uncertain/appearance guides. An independently implemented four-neighbor interior test reproduces all six known-control boundary recalls. These checks validate reported numerical proximity, not completeness of the references or semantic correctness. The two exact-source controls use8x mask sample centers mapped back by division8, consistent with source-pixel-center traces.

Verified13 available detail SVG viewBoxes and corresponding1x/16x dimensions. They are genuine rerenders of SVG ROIs, not enlarged raster crops. Other outputs generated after this snapshot are outside this count.

Arabic ML discovery recall0.921281 → selected0.917162 → fitted0.522654; Fine ML0.988281 →0.976863 →0.461238. The large latter reductions occur downstream of discovery/selection through whole-chain rejection and fitting capacity. They cannot be attributed to detector failure alone. K01 has3long raw loops in every arm, but2cubic-budget and1deviation-budget rejection leaves all candidates empty. This is preserved failure, not an accepted logo geometry result.

Independently evaluated the two saved frozen fitting-control traces using1025 Bernstein samples/cubic and actual segment distance. Old→new worst curve-to-raw deviations are0.677974→0.481063px and0.843879→0.566938px, agreeing with the reported numerical method within0.003px. Both new curves fit under the unchanged0.6px gate; saved control coordinates replicate exactly. Raw-to-curve error increases, so this is bounded overshoot improvement, not uniform pointwise improvement or solved thin geometry.

Visually inspected actual native ML SVG on white for Shield and Arabic and Shield evidence overlay. Crown silhouette/band portions are recognizable; long shield-frame contours and complete internal ornament support remain absent or unverified. Arabic boundary strokes remain partial, with no constructed filled counters or glyph topology. Those visible failures must remain prominent.

Evidence: audit_saved.py/AUDIT_SAVED.json, audit_metrics.py/METRICS_AUDIT.json, audit_fit_control.py/FIT_CONTROL_AUDIT.json and twelve independent native resvg PNGs in this QA directory. Final report, later holdout evidence and dashboard need separate review when available. No Git publication verified by this reviewer.
