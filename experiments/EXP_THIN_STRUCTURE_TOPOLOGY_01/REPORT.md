<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T11:43:19Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T11:43:19Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T11:43:19Z"}
END_DOC_PROVENANCE -->
# Thin-structure discovery and topology-safe initialization — bounded research report

Production architecture: **NOT_APPROVED**. Geometry milestone: **NOT_ACCEPTED**.

## Decision and evidence status

**VERIFIED:** Executed eight new candidates (A and B on four fixed cases), with four byte-preserved baseline graph copies. No previous 24-condition study or 140-candidate search was rerun. Neither proposed combined case passed its frozen prerequisites; no combined candidate was constructed. No parameters or acceptance thresholds were tuned after the results.

**VERIFIED:** Track A failed to recover the fragmented fine-feature control and made no changes to Arabic or K01. Three Shield connector proposals changed four gap pixels and merged three label pairs, but did not change the measured crown coverage. Track B repaired three collapsed rings on K01 and two on Arabic, without adding graph chains or cubic commands. It made no accepted changes on fine_features or Shield.

**SUPPORTED BUT LIMITED:** Local fitting damage can be corrected with a constrained smooth primitive when the surrounding raw faces are valid. This is a small numerical/topological repair, not proof of useful missing-detail discovery, complete artwork, high visual fidelity, or generalization.

**NOT ESTABLISHED:** Complete crown accuracy, independent Arabic outline fidelity, analytically certified global topology, final raster-to-vector appearance fidelity, or suitability as a production default.

## Baseline, scope and frozen policy

Local and remote main initially matched `1a401a1b2c9e95233625143f790ade6816b8427c`; all four owner-published checkpoints were present and the working tree was clean. The original owner vision was read completely and preserved. Image generation, Arabic typography, professional editing, semantic groups, Magic Layers and QA remain product requirements, outside this experiment's implementation.

The frozen protocol checkpoint is `f395ec568fcd79b08e30a54455e527404db69e43`, frozen before candidate creation. See protocol.json, PROTOCOL_FREEZE.json, BASELINE_PINS.json and references/INHERITED_REFERENCE_PINS.json. Sources, saved Arena labels and common-face graphs, and evaluator references were hash-pinned. This cycle deliberately tests the previously failing Arena partition; it does not recompare every VTracer partition or retrain a segmenter.

Known controls retain IoU>=0.97, area recall>=0.95, correct component/hole counts, boundary mean<=0.45px and p95<=1.25px, with critical-component vetoes. No criterion was relaxed. Shield annotations have 1.2–2px approximate AI-trace uncertainty and no qualified human ground truth: strict 1px acceptance is NOT_ESTABLISHED. Arabic measurements use a source-threshold proxy, not independent font outlines. Evaluator-only references and ROIs are never passed to constructors.

## Track A — implementation and hypothesis

Hypothesis: source-supported local connections can restore missing thin support without increasing global segmentation granularity. `track_a.py` extracts 8-neighbor skeleton endpoints from each original label, estimates width and outward tangent, and considers different nonadjacent regions within 12px. Lab color compatibility, facing directions, width ratio, a common gap label, and local foreground/background mixture evidence gate a bounded 4-neighbor Dijkstra connector. Its path must stay in a 1.5px corridor, take at most 12 steps and add at most 12 gap pixels. Maximum 512 pairs and 32 accepted connectors; no parameter search.

Only connector gap pixels change ownership; the joined endpoint label identities merge. This can falsely combine similar-colored objects. The convex Lab mixture is a heuristic, not physical source-over compositing or semantic evidence. It cannot recover a wholly absent region or discover arbitrary internal boundaries. Single-pixel fragments without a supported skeleton tangent are not eligible. Unchanged inherited initialization follows discovery.

Selected over global threshold reduction, global super-resolution segmentation, or tracing every edge because this gives a small independently measurable intervention without thousands of new regions. Ridge/paired-boundary discovery would cover broader failures but was not silently substituted when this endpoint hypothesis failed.

## Track B — implementation and hypothesis

Hypothesis: valid short L-shaped raw support need not disappear when its initial cubic collapses to a chord. `track_b.py` tests exactly three raw vertices A,B,C spanning two orthogonal unit steps whose existing fit is chord-collinear and incident to a raw-valid nonzero ring with zero fitted signed area. It proposes one cubic [A,B,B,C], preserving endpoints, chain IDs, incidence, region identities and all face references.

Incident groups are accepted together or rolled back. Guards check raw validity, repaired area sign and minimum ratio, closure, frame containment, hole/disjointness relationships, and no new bad curve-pair identities using 0.01px flattened predicates. Near pairs below 0.02px remain unresolved and reject. Two passes and 256 eligible chains bound the search. This is conservative numerical validation, not an exact continuous-intersection certificate.

The cubic rounds the raw L corner (approximately 0.177px deviation for the unit construction); it does not preserve an intentional sharp corner exactly. It also does not prove a tiny raw face is meaningful artwork. No raw-L fallback, box fallback, new face, source-grid outline, global stroke or underlay was introduced. General spline replacement and unrestricted curve optimization were rejected for this cycle because they would confound this specific failure mechanism.

## Independent results

| Case | Condition | Collapsed rings | Invalid fitted rings | Chains / cubics | Known silhouette IoU |
|---|---|---:|---:|---:|---:|
| fine_features | baseline | 3 | 4 | 22 / 36 | 0.820243 |
| fine_features | A | 3 | 4 | 22 / 36 | 0.820243 |
| fine_features | B | 3 | 4 | 22 / 36 | 0.820243 |
| G06_arabic | baseline | 69 | 78 | 539 / 514 | no independent GT |
| G06_arabic | A | 69 | 78 | 539 / 514 | no independent GT |
| G06_arabic | B | 67 | 76 | 539 / 514 | no independent GT |
| A01_shield | baseline | 131 | 153 | 809 / 737 | no independent GT |
| A01_shield | A | 130 | 152 | 804 / 734 | no independent GT |
| A01_shield | B | 131 | 153 | 809 / 737 | no independent GT |
| K01_linear_corner_hole | baseline | 3 | 3 | 93 / 88 | 0.950662 |
| K01_linear_corner_hole | A | 3 | 3 | 93 / 88 | 0.950662 |
| K01_linear_corner_hole | B | 0 | 0 | 93 / 88 | 0.950662 |

### Fine-feature fragmentation: negative result

**VERIFIED:** Raw foreground remains 13 components against four in the independent known-vector control. The fitted mask has 12 components, IoU 0.820243, area recall 0.870523, width MAE 0.412px and three false-split excesses under the fixed overlap diagnostic. A tested 13 pairs and accepted none: unsupported tangents/endpoints and same-label pairs prevented useful proposals. B's six eligible chains were rejected because their incident raw face contains an invalid raw ring. All A/B geometry and renders remain unchanged.

The 1.25px curve recall is only 0.747103 and the large dot recall 0.735474. Therefore neither visual smoothness nor high boundary proximity establishes feature completeness. This is evidence against the chosen discovery mechanism on this control, not proof that all source-driven methods fail.

### Arabic: very limited repair, topology unresolved

**VERIFIED:** A accepted no bridge from 512 tested pairs; 302 additional pairs were truncated by the frozen budget. B changed four controls, reducing collapsed rings 69→67 and invalid rings 78→76. The source-proxy IoU changes only 0.920244959→0.920290289. Proxy fit topology stays 24 components/25 holes, raw proxy 6/1, source proxy 40/9; the proxy includes antialiasing and threshold artifacts and is not typography ground truth. No correct Arabic stroke, counter or hole reconstruction is claimed. Many proposed B repairs touch a raw-invalid enclosing face and are rolled back.

### Shield and complete crown: no demonstrated recovery

**VERIFIED:** A accepts three bridges (four connector pixels) near x=101 and x=272–275, outside the dedicated crown review ROI. Regions 392→389, chains 809→804, cubics 737→734, collapsed rings 131→130 and invalid rings 153→152. This is an altered segmentation/refit result, not evidence that a crown component was recovered. Pair budget tested 512/1468; 956 pairs were truncated, so failure does not exhaust all possible source connections.

**VERIFIED:** B accepts zero of 174 eligible chains; inherited raw-invalid faces and an affected ring that remains invalid/zero veto groups. It preserves the original Shield candidate. No claim is made that every rejected local cubic is individually bad: coupled face safety can block an otherwise useful local correction.

All frozen named crown diagnostics are retained below. Values are guide-recall within each annotation uncertainty band, not certified contour accuracy or component correspondence. Extra nearby boundaries can satisfy proximity. None is a pass criterion by itself. Central fold illumination remains ambiguous and is not forced into physical topology.

| Component | Uncertainty px | Raw baseline | Fitted baseline | Fitted A | Fitted B |
|---|---:|---:|---:|---:|---:|
| shield_outer_silhouette | 1.8 | 0.9358 | 0.8886 | 0.8886 | 0.8886 |
| metallic_outer_bevel_ridge | 1.8 | 0.2076 | 0.1588 | 0.1588 | 0.1588 |
| metallic_inner_bevel_ridge | 1.5 | 0.8226 | 0.7603 | 0.7603 | 0.7603 |
| red_gold_material_interface | 1.2 | 0.7155 | 0.6343 | 0.6343 | 0.6343 |
| crown_complete_visible_outline | 1.7 | 0.7215 | 0.6970 | 0.6970 | 0.6970 |
| crown_left_tip_and_flank | 1.5 | 0.6995 | 0.6919 | 0.6919 | 0.6919 |
| crown_left_inner_tip | 1.5 | 0.6737 | 0.6632 | 0.6632 | 0.6632 |
| crown_center_tip_and_lobes | 1.7 | 0.9348 | 0.9078 | 0.9078 | 0.9078 |
| crown_right_inner_tip | 1.5 | 0.7266 | 0.6629 | 0.6629 | 0.6629 |
| crown_right_tip_and_flank | 1.7 | 0.6638 | 0.5971 | 0.5971 | 0.5971 |
| central_ornament_internal_fold | 2.0 | 0.8288 | 0.7740 | 0.7740 | 0.7740 |
| lower_band_upper_edge | 1.2 | 0.3515 | 0.3324 | 0.3324 | 0.3324 |
| lower_band_lower_edge | 1.5 | 0.2975 | 0.2890 | 0.2890 | 0.2890 |

The crown outline, tips, central ornament and band remain recognizable but distorted/incomplete in the fitted drawing; the dedicated true-SVG crown crops expose that failure. **NOT ESTABLISHED:** exact completeness, strict 1px performance, physical boundary versus shading classification, correct region identity at every junction. No human-reviewed tighter annotation was available; the existing reference was preserved rather than upgraded by assertion.

### K01: safety repair is real; final geometry still fails

**VERIFIED:** B accepts six chains, restores three collapsed rings and removes all three invalid fitted rings. The flattened domain diagnostic reports zero uncovered area, exterior area and overlap multiplicity. Shared references, endpoints and component/hole counts remain unchanged (one foreground component, one hole). However known silhouette IoU stays exactly 0.950661647273557, below 0.97, boundary mean 1.268px and p95 2.035px exceed policy. The repair concerns tiny tonal faces, not the main foreground silhouette. Correct holes plus closed curves are insufficient for acceptance.

## Combined condition and stopping

Neither predefined target qualifies: fine has neither A discovery nor B repair; Shield has no accepted B repair. `reports/COMBINED_DECISION.json` records the skip. Arabic repair does not authorize a combined Shield trial. The branch stopped without relaxing guards or trying further color/tangent thresholds to manufacture a win.

## Coverage, intersections, corners and anti-mosaic evidence

All candidates have zero shared-reference failures and zero measured endpoint gap. Shield retains seven measured crossing/overlap pairs in baseline, A and B; other cases report zero such pairs. Near-pair and raw/fit ring defects remain in most cases. Accepted B repairs introduce no new bad-pair identities under the numerical guard, which does not certify the unchanged global arrangement. Coverage is NOT_ESTABLISHED where fitted rings are invalid; no hidden make_valid polygon repair was used. K01 B's zero numerical domain gaps do not certify antialiasing/compositing coverage. No new appearance correction was tested.

Track B adds zero paths, chains, faces, labels or cubic commands. A merges label identities; it does not add pixel-cell export paths. All actual geometry SVGs were checked for embedded raster elements. Inherited tiny cells remain visible: restoring their area is not a clean-vector success. Visible 2px microgeometry lower/upper bounds remain approximately 0.008%/1.98% fine, 0.021%/2.20% Arabic, 0.079%/2.22% Shield and 0.003%/1.24% K01. No 10%-area alarm is triggered, but that is not proof of professional geometry. Many narrow elongated strips escape a two-dimensional tiny-box metric.

`reports/GRID_COMPLEXITY_DIAGNOSTICS.json` adds inherited raw unit-axis right-turn length, cubic versus noncollinear-cubic commands and complexity. Raw crack staircase is source-grid evidence and is explicitly not a final-curve smoothness certificate. Integer lattice statistics and area-weighted distributions are retained in per-candidate metrics. True SVG exports are independently rendered at 1x, 4x and 16x; enlarged source pixels are not treated as high-resolution contour truth. Exact intentional corner preservation is not established by the rounded repair.

## Root causes and uncertainty

1. **VERIFIED upstream failure:** fine-feature fragmentation exists in labels before fitting (13 vs four components). A's bounded endpoint proposal failed to fix it. Small disconnected fragments often lack a usable tangent; color/adjacency gates can reject the structures we wanted to reconnect.
2. **VERIFIED fitting damage:** some raw-valid tiny rings become zero-area chords. B corrects five rings across K01/Arabic under its safety checks.
3. **VERIFIED representation/assembly blocker:** affected raw-invalid rings/faces prevent conservative acceptance on fine and Shield. These checks do not determine whether the underlying label topology, raw face walk, repeated junction traversal or common-face graph interpretation is responsible in every case.
4. **SUPPORTED BUT LIMITED:** a raw face/junction representation that can express point contacts and holes consistently is a prerequisite for broader safe local fitting. Accepting repairs through invalid surrounding faces would evade, rather than solve, that problem.
5. **NOT ESTABLISHED:** exact additive causal shares of missing geometry, fitting, coverage or eventual appearance errors. No final SSIM/PSNR or appearance victory is claimed in this geometry-only experiment.

## Runtime, resources and QA

Primary workers completed in 53.815 summed wall seconds; maximum sampled process-tree memory 139.918 MiB. Slowest worker 14.359s. Evaluation and native/zoom rendering took 49.729s with sampled peak 175.301MiB. Requested 50ms sampling can miss short peaks; these are observed samples, not hard peak bounds. All worker return codes zero and no time/memory limits triggered. Per-case CPU times and timing logs are preserved.

The unit suite passed 13 tests, including boundary mixture controls, false join/split measurements, deterministic discovery, shared endpoints/reversed references, hole preservation and rejection/rollback. The initial NumPy shaped-inverse integration failure is preserved; it was corrected by flattening the inverse array before any candidate run, without changing the scientific method. Independent QA rechecked frozen hashes, constructor isolation, graph invariants, candidate/render hashes and negative results. See reports/QA_FINAL_REVIEW.md for scope and limitations. QA does not supply human crown ground truth or certify global vector quality.

## Reproducibility, evidence rights and publication

See REPRODUCIBILITY.md, index.html, per-case results, source pins and artifact manifest. Actual SVGs, PNGs, graphs, labels, audits and metrics are included for repository-licensed/owner benchmark cases. The external Arena fine fixture and its derived evidence remain local-only pending clarified redistribution rights; external/LOCAL_EVIDENCE_MANIFEST.json records paths and hashes, and the owner dashboard includes that local evidence. Arena source remains an external comparison dependency; no wholesale engine merge or product reuse is approved.

Git metadata writes work. Push failed once because Windows Credential Manager could not persist credentials and the noninteractive prompt could not read Username. No ACL/security change, repeated retry or false publication claim was made. Validated checkpoints are committed locally on main. The owner-run Publish-CommittedCheckpoints.ps1 verifies repo, branch, remote, fetch/ancestry, safe push and exact remote SHA; it stages nothing and will not duplicate commits. See the delivered publication receipt for final local SHAs and remote verification.

## Recommended next decision

**Recommend a bounded raw-face/junction validity isolation next, before broader spline or appearance optimization.** On the same small controls, determine whether invalid raw rings arise from label point contacts, repeated-vertex face walks, holes or graph assembly, and compare a topology-consistent face representation while holding labels fixed. Independently prototype continuous source ridge/paired-boundary proposals that include singleton fragments, against the failed endpoint mechanism; do not merely loosen all A thresholds. Freeze false-connection, width, thin-continuity and interior-component gates before testing.

This is a proposed next scope requiring owner GO. Do not promote this repair globally, adopt the full Arena engine, begin appearance reconstruction, or replace the architecture. Keep the five-ring repair as research evidence and the failed discovery mechanism as a negative result. Complete crown and thin-feature recovery remain mandatory; final extremely high visual fidelity has not been lowered or achieved.
