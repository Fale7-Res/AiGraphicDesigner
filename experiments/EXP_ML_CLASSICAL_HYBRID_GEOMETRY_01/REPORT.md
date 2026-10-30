<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T08:21:42Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T08:24:43Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T08:21:42Z"}
END_DOC_PROVENANCE -->
# Pretrained ML vs Classical CV vs Hybrid Geometry

**Geometry: NOT_ACCEPTED. Production architecture: NOT_APPROVED.**

## Technical decision

The learned-edge model runs locally, but this study does **not** establish a reliable cross-category geometry improvement. DexiNed loses important Shield and Arabic evidence that classical CV detects. The hybrid rule helps some examples but is not consistently better. None reconstructs complete shared regions, crown artwork, Arabic counters, or all thin features.

There is also a distinct construction bottleneck: useful detected contours disappear through whole-trace complexity and deviation rejection. K01 detects its boundary loops in every arm but exports no accepted curves. A narrowly scoped fitter correction repairs two previously rejected Fine Features traces, without proving correct object connectivity.

**Recommendation:** request a bounded contour-retention and closed-loop construction study next. Use these frozen maps and traces, compare source-corner/arc-length partitioning and periodic closed-loop fitting against whole-chain rejection, and account for every lost contour. Require endpoint, closure, hole, junction, topology and complexity checks. This is a construction contract experiment, not another detector threshold search. Region discovery remains unresolved; a separately budgeted pretrained region-proposal test may follow if memory feasibility is established. Do not adopt DexiNed, the hybrid, or a new production architecture from this evidence.

## 1. Repository and preservation

Starting local HEAD, tracking main and independently queried remote main all matched `fe6d925c51a500031577fc13dea21d3fa943c9b7`; the working tree was clean. The original owner vision was read completely. Prior generalization, isolation, thin-structure, raw-face and corrected-exporter research and QA were inspected. Historical outputs remain unchanged. Neither the 140 adaptive searches nor the 24-condition matrix was repeated.

All repository additions are isolated here. Image generation, professional editable SVG, Magic Layers, semantics and Arabic typography remain part of the full vision. No final colors, gradients, lighting, shadows, training, fine-tuning, paid API, private image upload or production integration occurred.

## 2. Model selection and rights

Selected: **OpenCV DexiNed ONNX**, `edge_detection_dexined_2024sep.onnx`, revision `01a752eb4006688376e576dc24941c54608f6dd0`. Exact size: 47,235,563 bytes. SHA256: `a50d01dc8481549c7dedb9eb3e0123b810a016520df75e4669a504609982cdd0`. Downloaded bytes were verified before inference. The publisher explicitly licenses all files in this model directory under MIT; its notice is retained. This is checkpoint-directory evidence, rather than an assumption based on the framework license. Weights remain outside Git.

[Pinned checkpoint](https://huggingface.co/opencv/edge_detection_dexined/blob/01a752eb4006688376e576dc24941c54608f6dd0/edge_detection_dexined_2024sep.onnx) · [license](https://huggingface.co/opencv/edge_detection_dexined/blob/01a752eb4006688376e576dc24941c54608f6dd0/LICENSE).

**SAM 2.1 Hiera Tiny: SKIPPED_RESOURCE.** Official code/checkpoints have Apache 2.0 terms; Tiny has 38.9M parameters and approximately 156 MB weights. The official runtime requires PyTorch >=2.5.1 and torchvision >=0.20.1 and uses a 1024 px image encoder. Only about 3 GiB RAM was available before inference. Installing/loading another runtime under this cycle's 1.5 GiB worker limit was not justified. This is a conservative risk screen, **not an observed SAM inference failure or proof of incompatibility**. No SAM weights or dependencies were downloaded. Consequently, a region-proposal ML arm was not evaluated. [Official SAM 2 requirements and checkpoints](https://github.com/facebookresearch/sam2).

TEED was reviewed as a lightweight learned-edge fallback, but not run: DexiNed's bounded fallback completed, and another edge model would not supply the missing region-proposal contrast. Exact candidate alternatives, licenses and unresolved issues are in `reports/MODEL_SELECTION_EVIDENCE.md`.

## 3. Actual runtime and bounded feasibility

The existing isolated `agd-native` environment was reused read-only: Python 3.14.2, OpenCV headless 4.14.0.94, NumPy 2.4.4, SciPy 1.18.1, scikit-image 0.26.0, Pillow 12.1.1 and psutil 7.2.2. Existing isolated Shapely 2.2.0 and resvg 0.49.0 support evaluation/rendering. No global Python, CUDA, driver or package upgrade was made. Tested OpenCV 4.14 compatibility is observed; the current demo's broad OpenCV >=5 requirement is not treated as an automatic incompatibility.

MX130 with 2048 MiB VRAM was independently observed. Inference explicitly uses CPU, two OpenCV threads and one OpenBLAS thread. No GPU inference was attempted; process VRAM was not independently sampled.

The upstream **512 px** attempt exceeded the frozen 1536 MiB worker limit at approximately **1594.6 MiB sampled tree RSS** and was stopped before producing a complete prediction. A single **256 px fallback** was documented and frozen before inspecting completed predictions or evaluation results. It uses the same checkpoint and preprocessing for every case; memory limits were not raised. See `RESOURCE_DECISION_BEFORE_RETRY.json` and the preserved failed run.

All six 256 px workers completed. Sampled process-tree peaks were about 1286–1289 MiB, with whole-worker times of 3.9–6.3 seconds. Model load and actual forward times are recorded separately in each inference JSON. Sampling can miss short allocation peaks and the supervisor can overshoot a limit between polls. This is feasible-system evidence, not certified maximum memory.

## 4. Frozen experiment and fairness

`protocol.json` freezes hypotheses, sources, 34 dependency/reference hashes, scoring, budgets and the intended comparison before inference. The resource amendment is explicit. Native classical CV versus learned 256 px inference compares feasible systems on this laptop, **not equal-resolution detector architectures**. Downsampling may erase small details. Square resizing also distorts aspect ratio before coordinates map back to native dimensions.

Inference uses BGR float32, scale 1, means (103.5,116.2,123.6), the fused output, sigmoid and bilinear native-size remapping. Raw logits and sigmoid fields are saved. Confidence is never normalized independently by each image's minimum/maximum. No tuning uses evaluator masks, crown guides, answer curves or manual prompts.

Two additional project-unseen checks were frozen before their outputs: **H01 horse**, CC0 by Andreas Preuss/Openclipart, and **H02 astronaut**, NASA public domain. Both come from [documented scikit-image data](https://scikit-image.org/docs/stable/api/skimage.data.html). The model may have encountered these popular public images during training; training-unseen status is not established. No additional independently referenced Arabic holdout was obtained.

## 5. Arms and the two evaluation stages

**Classical:** unchanged saved multi-scale Lab Canny evidence from the prior source probe; the unchanged extractor is used for new images. The previous paired-flank stroke results (0/17/24/0) remain a separate inherited reference. Paired centerlines with width are not mislabeled equivalent to boundary edges.

**ML:** fused sigmoid hysteresis with weak threshold 0.3 and strong threshold 0.5.

**Hybrid:** retain learned weak evidence within 1.5 px of classical evidence, or learned confidence >=0.7 anywhere; use the same 0.3/0.5 hysteresis. This rule cannot discover evidence absent from ML. It can remove or reconnect predictions and therefore requires both recall and precision assessment.

All arms use the same skeleton tracing, minimum length 6 px, at most 128 length-ranked traces, at most 64 cubics per trace, and a 0.6 px deviation limit. Old and repaired fitters remain separate controls. No evaluator reference or artwork-specific construction ROI is used.

**Stage 1** saves raw maps, every candidate polyline, skeleton components, junctions, endpoints and eligible trace selection. **Stage 2** saves accepted/rejected curves and reasons, old/stable SVGs, deviation and intersection measurements, and actual renderer outputs. Compare full raw evidence, selected evidence and fitted geometry separately.

The inherited corrected serializer actually emits **0.35 px diagnostic strokes**, versus the protocol's stated 0.7 px. This deviation is shared by all arms and disclosed; candidates were not changed after evaluation. Centerline support metrics are separate from rendered width. Open-boundary proposals do not establish face ownership, valid regions, holes or glyph connectivity.

## 6. Quantitative comparison

Boundary recall below uses a 1.25 px tolerance. Fine Features and K01 use independent 8× sampled source-vector masks. Arabic and horse use raster-threshold proxies, **not independent glyph/vector truth**. Shield and the photograph lack exact contour ground truth. All precision, selected-stage and per-guide measurements are in `reports/METRICS.json`.

| Case | CV rawâ†’fit recall | ML rawâ†’fit recall | Hybrid rawâ†’fit recall | CV / ML / Hybrid paths |
|---|---:|---:|---:|---:|
| A01_shield | No independent contour truth | No independent contour truth | No independent contour truth | 127 / 30 / 32 |
| G06_arabic | 0.973 â†’ 0.042 | 0.921 â†’ 0.523 | 0.929 â†’ 0.447 | 1 / 23 / 20 |
| K01_linear_corner_hole | 0.997 â†’ 0.000 | 0.989 â†’ 0.000 | 0.989 â†’ 0.000 | 0 / 0 / 0 |
| fine_features | 0.977 â†’ 0.288 | 0.988 â†’ 0.461 | 0.988 â†’ 0.461 | 15 / 1 / 1 |
| H01_horse | 0.993 â†’ 0.008 | 0.774 â†’ 0.095 | 0.909 â†’ 0.141 | 1 / 8 / 10 |
| H02_astronaut | No independent contour truth | No independent contour truth | No independent contour truth | 127 / 124 / 125 |

## 7. Shield crown and structural completeness

Approximate full-crown guide recall before fitting is **0.850 classical / 0.528 ML / 0.539 hybrid**. After fitting it becomes **0.302 / 0.489 / 0.473**. The better fitted ML value therefore does not prove better discovery: classical starts with more evidence and loses more downstream.

ML raw outer-silhouette support is approximately 0.984, but fitted support is zero because its long contour is rejected. Raw central-ornament/fold guide support is 0.966 classical versus 0.135 ML/hybrid; this guide includes ambiguous illumination. Upper-band support is 0.786/0.577/0.577; lower-band support is 0.913/0.308/0.308. Outer metallic-ridge support is 0.412/0/0. Crown tips, valleys, ornament, both bands, metallic frames and red/gold boundaries remain individually visible in the dashboard.

ML suppresses some appearance-only evidence: the upper-right specular guide falls from classical 1.0 to learned 0.517, and a horizontal crown highlight from 0.866 to 0.037. It simultaneously loses important structural evidence. These observations do **not** establish reliable lighting-versus-material classification. Existing guides have roughly 1.2–2 px uncertainty and lack qualified independent human ground truth. Strict 1 px crown acceptance and complete interior reconstruction remain unverified.

## 8. Arabic, Fine Features, K01 and holdouts

Arabic classical raw proxy recall is 0.973 versus 0.921 ML and 0.929 hybrid. ML loses support **0.917 selected → 0.523 fitted**; hybrid loses **0.918 → 0.447**. Classical loses **0.973 → 0.042**. Boundary-network component counts do not represent correct letters, counters or filled glyph objects. No complete Arabic reconstruction is established.

Fine Features raw known-boundary recall is 0.977 classical versus 0.988 learned/hybrid. ML selected support falls **0.977 → 0.461 fitted**. This is limited discovery evidence plus a substantial independent construction loss; it is not recovery of all four foreground objects. Arena fixture rights remain unresolved, so its images, tensors, curves and renders are owner-local only, with hashes and retrieval information published.

K01 detects three closed boundary traces in every arm, with approximately 0.989–0.997 raw recall, then produces **zero accepted curves**. Two traces exceed the cubic budget; one exceeds the bounded deviation/refinement limit. Empty SVGs are preserved and prominently labeled as failures. No threshold was relaxed and no pixel fallback was inserted.

Horse raw proxy recall is 0.993 classical, 0.774 ML and 0.909 hybrid. Hybrid improves on the learned prediction, but not on classical evidence. All fitted results remain poor. Astronaut has fewer learned skeleton fragments and fewer texture traces, but no independent physical-boundary truth; both classical and learned evidence are dense. Trace budgets discard many details. No photographic completeness or universal generalization is claimed.

## 9. Controlled fitting-stability correction

The two previously rejected **identical frozen Fine Features traces** were fitted using normalized chord directions, per-segment chord-length/3 handles, the same 60° corner and 0.35 px RDP settings, at most eight supported subdivisions and 64 cubics. No reference geometry or relaxed threshold was used.

Trace 0 curve-to-source maximum decreases **0.677619 → 0.480715 px**, with a new numerical symmetric envelope of **0.497153 px** and 31→36 cubics. Trace 2 decreases **0.842000 → 0.566528 px**, envelope **0.573528 px**, and 36→37 cubics. Both satisfy the unchanged 0.6 px gate. Two executions reproduce identical coordinates; independent QA confirms the overshoot decrease.

Negative tradeoff: source-to-curve directed error increases on both traces. This is a worst-deviation improvement, not a uniform improvement at every point. The envelope adds sampling/flattening uncertainty; it is not exact continuous certification. Five tests and actual 1×/4×/16× old/new SVG renders passed. No new source feature or correct shared-region connectivity is created by this fitter.

## 10. Topology, anti-mosaic and remaining construction limits

Accepted candidates use continuous cubic boundary strokes and the corrected serializer. No embedded raster, hidden underlay, pixel rectangle or raw-grid fallback is exported. Tiny bounding-box counts, half-grid alignment, axis-aligned length and length×width microgeometry proxies are recorded. The latter is **not true visible-area ownership**. Lattice-derived evidence and oscillations remain; cubic commands and low path count do not prove professional geometry.

No measured proper mutual crossings were found among these accepted proposal centerlines. That does not validate missing curves, shared junctions, region closure, holes or gapless coverage. The fitter accepts on deviation, not on a complete topology certificate. Whole-contour budget rejection, nonperiodic endpoint treatment and lack of graph integration remain major limitations. No final-image SSIM or appearance-fidelity claim is made.

## 11. Resource and execution limitations

Four primary construction cases total approximately 133.5 seconds; horse takes 9.1 seconds and astronaut 144.7 seconds. Each arm finishes within its 120-second bound. **The initial four construction RAM records measured only the Python launcher (~3.9 MiB); actual process-tree peaks and enforcement of their 768 MiB cap are NOT_ESTABLISHED.** QA found this bug. The corrected monitor measures whole trees for the later holdouts: approximately 127.8 and 165.3 MiB. Primary runs were not repeated to manufacture missing telemetry.

Initial construction failed on an isolated Shapely import before generating candidates; logs are retained and the path was corrected. Evaluation later encountered an empty-array dtype error and an attempt to read an unfinished astronaut result. These were evaluator/integration errors; no model or geometry search was rerun. Constructor hashes, initial failures, final source snapshots and disclosed comment-only packaging changes are retained.

## 12. Independent QA and deliverables

Independent QA checked 34 frozen pins, the exact ONNX hash, four primary inference tensors with exact sigmoid/resize reconstruction, twelve candidate SVG command/control-point roundtrips and independent resvg renders, five fitter tests, 48 Shield guide recalls, six known-control recalls, real 16× SVG viewBox rendering and the two-trace overshoot control. Final QA addresses the later holdouts/dashboard separately; do not extend a four-case audit count without evidence.

Open `review.html` for repository-safe comparisons. The owner-local dashboard also includes restricted Fine Features and frozen-trace control SVGs/renders. Source code, configurations, raw tensors, all accepted/rejected traces, metrics, native/4×/16× renders, resource records, negative results and reproduction instructions are retained. Weights, environments, caches and unknown-rights external assets are excluded from Git.

## 13. Publication

Scoped staging was attempted once and failed: `Unable to create .../.git/index.lock: Permission denied`. No ACL change, force-push, history rewrite or repeated Git write was attempted. No new commit/push is claimed. The owner-run `Publish-Research.ps1` checks branch, remote, ancestry and staged scope, commits only when needed, pushes safely and verifies the remote SHA. Ending state and inventory are recorded at closure.

## Claim classification and next decision

- **VERIFIED:** local pretrained inference, actual SVG proposals, distinct detector-versus-fitting losses, the two-trace overshoot correction and the empty K01 failure.
- **SUPPORTED BUT LIMITED:** small Fine Features pre-fit recall gain; hybrid improvement over ML on horse; suppression of some highlight evidence; bounded fitter benefit.
- **HYPOTHESIS:** loss-accounted chain partitioning and periodic loop fitting can retain useful detected contours without a pixel mosaic; region-level learned context may improve structural discovery.
- **NOT ESTABLISHED:** consistent ML/hybrid superiority, complete crown/Arabic/thin geometry, correct shared regions/holes, SAM CPU failure, photographic geometric truth, final-image fidelity or production readiness.

Stop here for owner GO / NO-GO. Geometry remains NOT_ACCEPTED; architecture remains NOT_APPROVED.

## Final independent closure

The independent final QA now includes both holdouts: all six saved inference fields reconstruct exactly from raw logits, 18 candidate SVGs match saved controls and independently render, 15 true SVG ROI checks pass, and 171 PNGs decode. Dashboard link checks resolve 243 repository references and 300 local references. Seven packaged source ASTs plus the fitter match execution sources. Root tests pass 18/18 (nine fitter/metric tests plus nine corrected-exporter tests). See `qa/QA_FINAL.md`. This is bounded evidence acceptance, not geometric acceptance or publication certification.

## Governance verification limitation

Scoped experiment mirrors and document provenance pass. The repository-wide `change_tracking.py verify` command returns failure, with 256 reported issues; 25 mention this experiment. Full output and scope counts are retained in `reports/ROOT_PROVENANCE_VERIFY.json` and `GOVERNANCE_SCOPE_LIMITATION.json`. Historical governance files were not rewritten to obtain a pass. Root-wide governance is not certified by this research package.
