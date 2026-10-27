<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T14:46:14Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T14:48:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T14:46:14Z"}
END_DOC_PROVENANCE -->
# Generalization and alpha-aware reranking: final bounded report

Evidence closure: 2026-10-27T14:46:12+00:00. Architecture remains **NOT_APPROVED**. The owner approved packaging saved evidence without repeating the completed search.

## Findings

The eight completed cases contain 140 successful search candidates and zero recorded candidate failures. They cover seven independent originals: G05 is a correlated native-resolution center crop of G02. The alpha-aware minimum-background reranker selected the same winning trial for all three RGBA cases; opaque cases deliberately retained their inherited winners. All eight `new.svg` files and selected PNGs are byte-identical to their `inherited` aliases. **No reconstruction improvement was demonstrated.** This is an informative negative result, not an optimizer success claim.

The saved winners match raster samples extremely closely at the tested dimensions. All eight winners have zero cubic/quadratic path commands; tiny-cell geometry is evident across the saved set. Camera matches exactly at its tested 320x320 resolution; that does not establish exact reconstruction of its 512x512 original or coherent geometric artwork. High SSIM and SVG validity do not establish clean geometry, scale-independent detail reconstruction, meaningful regions, semantic editability, or typography reconstruction.

The selected Arabic lettering, Tux and translucent dice outputs preserve 8-bit alpha exactly at tested dimensions in saved resvg renders; recomputed alpha MAE and maximum error are zero. This uses source-derived equal-alpha horizontal run paths in a vector mask. It has explicit pixel-grid dependence and is not a solution to coherent alpha-boundary reconstruction. Some nonwinning candidates have incomplete RGB paint coverage and therefore nonzero effective alpha errors despite the attached mask. Exact alpha is claimed only for the selected tested outputs, not all candidates.

## Measured results

RGB metrics below use each case's worst-SSIM background (white for opaque cases). Background PSNR can differ; full white/black/bluegray metrics are in `reports/verification.json` and saved `case_result.json`. `exact` means zero tested MSE, represented as null PSNR in inherited JSON, not an invented finite dB value. Path counts include mask paths for RGBA images; masks contain many subpaths, so path-tag counts alone understate complexity.

| Case | Tested dimensions | Candidates | SSIM | PSNR dB | Paths | SVG bytes | Recorded total s | Sampled worker MiB |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| G01_coffee | 320x213 | 19 | 0.997893949 | 54.972 | 55898 | 3,266,303 | 182.8 | 146.9 |
| G02_chelsea | 320x213 | 19 | 0.999222749 | 58.014 | 60502 | 3,406,968 | 199.6 | 151.7 |
| G03_rocket | 320x214 | 19 | 0.996047145 | 52.693 | 30892 | 1,760,005 | 171.2 | 125.9 |
| G04_camera | 320x320 | 13 | 1.000000000 | exact | 62550 | 3,518,916 | 135.3 | 162.7 |
| G05_chelsea_nativecrop | 256x256 | 19 | 0.999823372 | 62.844 | 60920 | 3,251,022 | 223.7 | 157.9 |
| G06_arabic | 210x320 | 19 | 0.999935564 | 73.203 | 2452 | 317,916 | 115.7 | 95.2 |
| G07_tux | 265x314 | 13 | 1.000000000 | exact | 8747 | 553,917 | 89.2 | 102.4 |
| G08_dice_alpha | 320x240 | 19 | 0.999543891 | 58.525 | 18454 | 1,430,162 | 195.0 | 112.2 |

Total recorded case wall time is 1312.3 seconds. These are prior execution measurements, not newly repeated timings. Memory is the maximum sampled worker/process-tree RSS in inherited telemetry; 10ms polling can miss brief peaks and it is not a whole-session exact memory ceiling. RGBA total times include alpha evaluation; opaque and RGBA totals therefore measure different workloads. Performance at larger original dimensions is unvalidated.

## Dataset and provenance

Inputs were frozen before benchmark execution and selected across domains rather than on achieved scores. `inputs/manifest.json` records authors, source/license URLs, original and normalized SHA256 hashes, dimensions, transforms and alpha statistics. `dataset/sources/` retains license/source snapshots; `dataset/originals/` retains all seven originals. Coffee is a food/beverage photograph, not broad evidence across food types. Rocket includes smoke/soft transitions; Chelsea challenges fur/fine detail; Camera is grayscale photography; Arabic is raster lettering; Tux is a shaded raster mascot; dice is a **published 3D-rendered raster illustration, not a photograph**.

Most tests are max-edge 320 Lanczos normalizations. G05 is a 256x256 center crop without resampling; Tux uses original 265x314 dimensions. Arabic's original alpha is almost binary (two partial-alpha pixels); the normalized image contains many partial-alpha samples introduced by resampling. Tux original alpha is binary. Dice has genuinely complex native translucency but was evaluated downsampled. Seven sources and three alpha cases are a bounded cross-domain check, not a universal-generalization estimate. Normalized rasters and vector derivatives retain each source's applicable license; Tux attribution and CC-BY-SA dice obligations are retained in the manifest.

## Optimizer observations and unresolved audit

The saved optimizer explored recorded `bw`, `color-cluster`, and `watershed` families using the inherited pilot/detail/stagnation strategy, with a configured cap of 24 candidates and 240 seconds of search dispatch per case. Actual counts are 13 or 19 because stopping rules returned early. This cycle did not modify the candidate domain or perform the previously planned independent parameter-domain audit. The runtime cap does not bound a whole RGBA case, since later alpha-candidate rendering is additional work. A selected candidate is strongest only within the evaluated candidates under the inherited score, not a globally optimal vector reconstruction.

The reranker maximizes the minimum inherited fidelity score across white/black/bluegray, then mean score and inherited RGB score. Its unchanged winners provide no evidence of improvement, nor proof that it is useless for unseen inputs. Scoring and early stopping may favor exact pixel-mode detail; this work did not establish reliable selection of coherent geometry. Search robust-selection and representation quality remain distinct questions.

## Verification and visual evidence

`package_evidence.py` runs no tracing, optimizer, or SVG renderer. It checks frozen input/original hashes, all case statuses and 140 candidate artifact pairs, byte identity of inherited/selected aliases, exact tested alpha for selected RGBA results, and independent metric recomputation from saved selected PNGs. Six metric fields per evaluated background reproduce within 1e-12 relative/absolute tolerance. It parses 213 saved SVGs and rejects embedded raster tags, scripts, foreign objects and external hrefs; it fully decodes 553 saved PNGs plus original JPEG imagery. The saved-artifact inventory hashes every file in inputs/dataset/results before and after packaging and confirms no byte changes. XML parsing and safe element checks are structural validation, not exhaustive W3C SVG conformance or topology validation.

`reports/dashboard.html` displays source rasters and actual saved SVGs with browser 1x/4x/16x scaling and white/black/bluegray backgrounds. Cases are sorted with the worst SSIM first. Lossless comparison sheets include original, inherited, selected and x32 RGB error; 16x nearest-neighbor worst-error tile sheets are explicitly sampled-raster diagnostics rather than new SVG renders or high-resolution ground truth. Browser SVG appearance is owner review evidence, not a separately measured second-renderer certification. Full-size means full tested dimensions here; original source files remain available for inspection.

## Remaining limitations and recommendation

This evidence closes the interrupted saved-output packaging scope without rerunning its 140 candidates. Dedicated QA covers frozen provenance, candidate counts, unchanged selection, sampled alpha, all saved vector/PNG integrity, preservation hashes, and generated visual assets. Independent parent QA remains a separate gate. There is no broad original-resolution benchmark, repeated runtime distribution, independent renderer certification, owner visual acceptance, Arabic text/font recovery, semantic grouping, or professional geometry certification.

Preserve these results as the strongest saved pixel-equivalent reference. The approved fixed-geometry appearance ablation should test whether richer fills improve coherent spline reconstruction without adding cells. Compare its results against these references, not merely against its optimized-flat condition. No production architecture, Clean SVG, Magic Layers, image-generation or typography scope is replaced or approved by this experiment.
