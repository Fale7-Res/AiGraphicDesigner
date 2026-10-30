<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:13:29Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:13:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:13:29Z"}
END_DOC_PROVENANCE -->
# SVG exporter correctness, matched safe fitting, and source-driven stroke discovery

Geometry **NOT_ACCEPTED**. Production architecture **NOT_APPROVED**. No appearance engine or ML model implementation.

## 1. Verified baseline and publication

Starting localHEAD/tracking/remote main were independently verified as `52187f898be2524591f147840234bb57e64e476e`, clean. The complete original owner vision and previous isolation, thin and raw-face reports/QA were read and preserved. Image generation, Arabic typography, semantics, Magic Layers and professional editability remain authoritative future requirements. The historical140searches/24conditionmatrix were not rerun.

All changes are isolated in EXP_EXPORTER_DISCOVERY_01. Historical source/SVG/PNG/metrics and negative outcomes remain byte-preserved. Frozen source/candidate/reference pins were verified before execution; independent QA verified61pins. New protocol covers three ordered phases and one discovery configuration, with no result-driven threshold changes.

Git staging failed once this cycle: `git add -- experiments/EXP_EXPORTER_DISCOVERY_01` → `fatal: Unable to create 'C:/Users/Mohamed/Desktop/AiGraphicDesigner/.git/index.lock': Permission denied`. No new commit or push is claimed; no repeated Git write or ACL bypass was attempted. Research continued. The exact owner-run scoped PowerShell publication script, file inventory and final receipt accompany the dashboard. Do not duplicate a commit if the owner has already published it.

## 2. Phase A — exact defect and correction

The affected historical helper is `EXP_COMPLETE_GEOMETRY_ISOLATION_01/geometry_eval.py:svg_graph`. It emits `Z` for logical closed chains, then removes later `M` commands when constructing one compound face walk. `Z` closes to the actual SVG subpath origin and changes the current point, not to an imagined chain origin. This produces wrong closure edges and changes subsequent drawing state.

The new isolated `svg_exporter.py` expands each logical closure as an explicit oriented line **before reversing or concatenating**. Reversed cubics swap controls and reverse the complete walk, including its implied closing edge. Each real face contour gets oneM and finalZ. Open stroke chains remain open; separate closed chains retain their own subpaths. Region order and evenodd holes/nesting are preserved. Unsupported/nonfinite/disconnected/open face data are rejected; no snapping, topology repair, raster flattening, or hidden image is used.

Default17significantdigits roundtrip floats; an explicit corrected8digit control isolates the closure fix from historical rounding. The primitive geometry, not a sampled raster, drives serialization. Strict endpoint consistency tolerance is1e-8. These checks do not repair already-invalid curves or certify all SVG features.

### Scope and affected measurements

Read-only caller audit finds the one historical definition and14call mentions in analyze_matrix, audit_raw_labels, final_diagnostics, validate_geometry, historical overlays/tests, thin evaluate_study and raw-face run_case. Exposure requires fitted compound-region assembly with embedded closed chains. Raw region export and independent curve-only paths do not have this wrong-origin defect.

Potentially affected outputs include fitted foreground masks/IoU, Arabic proxy component/hole counts, visible region-ID microgeometry, region render visuals and raw-face fitted-equivalence gates. Numerical array areas, chain controls, shared incidence, raw label ownership and source boundary/guide distances are unaffected. Render coverage/compositing findings based on these exports must be reconsidered individually. Earlier VTracer fidelity/appearance pipelines using other serializers are not declared invalid.

Static inspection of other named version01/02/03 exporters found independentM-beforeZpatterns rather than this exact compoundM-stripping pattern. This is scoped inspection, not exhaustive production certification. No native VTracer exporter defect is established. See reports/EXPORTER_CORRECTNESS_AUDIT.md and exporter_callsite_audit.json.

### Tests actually run

Nine exporter tests cover open/closed paths, independent subpaths, compound contours, holes/islands, shared boundaries, repeated junctions, embedded closed chains, mixed open/closed strokes, reversed cubics, corners, input immutability and fail-closed invalid input. Eight actual resvg generated/canonical fixture pairs match fullRGBA bytes; hole/interior pixels also have independent assertions. Independent QA ran the nine tests and400checks with the separate fontTools parser over100random closed walks (both directions, raw/fitted). Root combined suite passes17tests including eight discovery tests. These are bounded correctness controls, not a complete arbitrary-SVG proof.

## 3. Phase A/B — frozen re-export impact and matched controls

O/R/B/A are copied frozen graphs; no source segmentation or original fitting rerun. O is original, R decomposed walks with identical chains, B previous guard, A failed endpoint discovery. RB is the unchanged historical guard on R. K01RB was reused from the previous saved control rather than refitted again.

Corrected O/R raw native/8x and fitted8x RGBA images match exactly on all four cases: the previously blocked gate now passes without relaxation. Directed occurrences, labels, incidence and original control points are unchanged. The precision-controlled8x comparison for O is:

| Case | Legacy→closure-correct8 changed pixels | Correct8→roundtrip17 changed pixels |
|---|---:|---:|
| fine_features | 8735 | 0 |
| G06_arabic | 19070 | 3 |
| A01_shield | 78232 | 3 |
| K01_linear_corner_hole | 0 | 0 |

Thus the closure-only control reproduces the prior8,735/19,070/78,232/0pixel discrepancy. The small precision effect is separately disclosed. This is now an experimentally isolated serialization effect, not changed source geometry. Historical outputs remain in their original directories marked affected/superseded by this report, not silently replaced.

Arabic original source-proxy IoU was0.920244959; corrected O/R is0.931811351. This is serialization correction, not new glyph geometry. Fine and K01 foregroundIoUs remain0.820243346/0.950661647. Shield has no exact raster-independent foreground/crown truth; its guide distances are unchanged by serialization. Corrected priorB Arabicproxy becomes0.931857170. Every per-condition summary preserves historical affected values alongside corrected values. Only this four-case relevant set was re-exported, not every historical matrix.

## 4. Phase B — does face decomposition unblock the guard?

**VERIFIED: yes, bounded local corrections are now accepted on all three previously blocked cases.** Guard code, parameters and conservative rejection rules are unchanged; no meaningful guard was bypassed. The R-face partition changes the ring denominator and coupling groups, which is the experimental intervention.

| Case | Condition | Rings | Invalid fitted | Collapsed raw-nonzero rings | Cross/overlap pairs |
|---|---|---:|---:|---:|---:|
| fine_features | R | 27 | 6 | 6 | 0 |
| fine_features | RB | 27 | 0 | 0 | 0 |
| G06_arabic | R | 235 | 71 | 69 | 0 |
| G06_arabic | RB | 235 | 7 | 5 | 0 |
| A01_shield | R | 500 | 139 | 133 | 7 |
| A01_shield | RB | 500 | 112 | 106 | 7 |
| K01_linear_corner_hole | R | 45 | 3 | 3 | 0 |
| K01_linear_corner_hole | RB | 45 | 0 | 0 | 0 |

Accepted changed chain counts are6Fine,128Arabic,50Shield; K01is the reused six-chain control. Every changed segment is exactly the frozenA,B,B,Ccubic with original endpoints. Labels, all non-segment chain metadata, face references and incidence remain unchanged within R→RB. Corrected exporter changes serialization only; decomposition changes representation only; RB changes the local curves. These effects are not conflated.

Fine's6collapsed cycles become0, but foregroundIoU only0.820243→0.825394 and fitted components **12→15 versus truth4**. Restoring tiny disconnected faces can worsen a completeness metric; this is not successful thin reconstruction. Arabic69→5collapsed cycles and proxyIoU0.931811→0.933549 remain structurally unresolved. Shield133→106collapsed and139→112invalid fitted rings retain seven measured crossing/overlap pairs and inaccurate internal geometry. K01still0.950662IoU, one component/one hole, below0.97acceptance. Numeric validity is not visual acceptance.

Ring denominators cannot be compared as if every old ring represented one physical component: O/R differ18→27Fine,226→235Arabic,464→500Shield. R→RBholds each denominator fixed. Numerical0.01pxcurve flattening/predicates remain conservative and non-certified; an alternate independently sampled crossing audit exposed floating/nearly-coincident sensitivity, so absolute alternate counts are not promoted as exact topology. No new bad pair is accepted under the frozen guard.

## 5. Phase C — selected method and scientific isolation

The selected hypothesis is **paired-flank source ridge-to-stroke discovery**, not another endpoint-connection threshold change. It reads nativeRGBonly and can propose a thin object missing from the label partition. GaussianLabσ0.6, eight normals and radii1.5/2.5/4px require two contrasts>=15Lab, flank disagreement<=12Lab and vector cosine>=0.9. Normal NMS and source skeleton graph tracing produce maximal chains independently of segmentation endpoints. Redundant diagonal graph chords are suppressed; loops are traced once.

Bilateral0.25pxprofiles through4.5pxestimate half-contrast widths; median width<=6px. Chains must be>=6px. Douglas–Peucker0.35px and corner-aware cubicHermite fitting (turn>=60°) provide continuous proposals, max64cubics/chain and128proposals. A sampled symmetric deviation<=0.6pxis required; rejection has no pixel-polyline fallback. Ranking is source support×length, with no evaluator tuning. Constantwidth, pixel-center lattice initialization, localNMSfragmentation, thin lighting false positives and sampled-distance limitations are explicit.

This addresses TrackA's inability to birth absent strokes. Unfiltered Canny would trace abundant lighting/texture; global oversegmentation changes ownership and risks cell proliferation; a universal graph engine or neural dependency exceeds this frozen test. Paired flanks still cannot distinguish every metallic highlight from structural artwork. Uniform blue strokes are geometry diagnostics, not appearance reconstruction.

### Actual new candidates and negative results

| Case | Accepted source strokes | Cubics | Rejected chains | Crossings with inherited boundaries |
|---|---:|---:|---:|---:|
| fine_features | 0 | 0 | 3 | 0 |
| G06_arabic | 17 | 126 | 97 | 32 |
| A01_shield | 24 | 105 | 160 | 8 |
| K01_linear_corner_hole | 0 | 0 | 9 | 0 |

No proposed stroke self-intersections or mutual proper crossing/overlap were measured under the specified samples. That does not certify compatibility with inherited boundaries, junctions or region ownership. The32Arabic/8Shieldboundarycrossings may be intentional overlays or conflicts; no automatic graph integration is claimed. Original labels/faces/holes remain untouched. Actual cubicSVGs, renders, accepted/rejected audits and source overlays are supplied.

**Fine Features — negative final proposal result:** source tracing found two long connected traces, unlike the inherited13foreground fragments, but both whole curves were rejected for deviation (about0.673/0.836px); one short trace was also rejected. No accepted Cstroke or new shared connection exists. Read-only follow-up on the same frozen traces confirms genuine cubic overshoot from uneven knot spacing and large unscaled centered tangents; dense curve-to-rawsegment errors remain approximately0.677/0.840px. Sparse nearest-sample distance also contributes to one direction but is not the main rejection cause. No threshold, fitting algorithm or output was changed. MLwouldnotfix this downstreamfittingdefect byitself. Rejected diagnostics are shown as rejected, not grid fallback artwork.

**Arabic — sparse proposals and regression:**17strokes/126cubics are genuine separate SVG geometry, but they do not reconstruct complete glyph outlines/counters. Proposal-only source-proxyIoU is0.063633. The actual hypothetical painted union with correctedO **decreases** proxyIoU0.931811→0.918758 and changes6components/1hole to1component/7holes (source-thresholdproxy40/9). This is a false-connection/coverage warning, not proof of glyph-level truth. The union remains an unintegrated diagnostic; it is not a reconstruction improvement.

**Shield — no complete crown recovery:**24strokes/105cubics include short crown-tip/light-ridge, rim and band snippets. They do not form the full crown silhouette, central ornament, both band edges or complete red/gold/frame interfaces. Pairedcontrast also accepts highlights; neither source confidence nor guide proximity establishes a structural boundary. Dedicated crown1x/4x/16xviews show these limitations. Strict1pxaccuracy remainsNOT_ESTABLISHEDwith unchanged1.2–2pxAIguide uncertainty.

**K01 — no proposal regression:**zeroacceptedCstrokes, nine short-chain rejections. Existing region/hole control remains unchanged. This is a useful negative control, not proof of universal false-positive suppression.

## 6. Internal artwork, coverage, width and anti-mosaic evidence

All13namedShieldguidecomponents are retained in the per-candidate metrics, covering silhouette, outer/innermetal, material separation, all crown tips/flanks/lobes, ornament and upper/lowerbands. Major lower-band guide support remains poor; restoring tiny rings does not recover the band. Ccenterline guide support is separately labeled stroke proximity, not region-boundary recall. Central fold illumination stays ambiguous and is not forced into a physical contour. No external silhouette metric overrides missing interior geometry.

Known-control measurements use the frozen independent8xsource-vector masks, with sampled uncertainty. Arabic remains a rasterthresholdproxy, not fontGT; photographs were not newly tested. Width estimates are sourceprofilemedians, not proof of correct variable-widthlettering. Per-case metrics contain known widthMAE, falsejoin/splitdiagnostics, coverage and actual error maps.

Corrected serialization introduces no new geometry. RBadds no chains/faces/labels/cubics, but retains existing tiny faces whose meaning is unverified. Ccreates only bounded cubicstrokes, no rectangles, embedded image, underlay or sourcegridfallback; all acceptedCpath spans exceed2px. Existing lattice distributions and4xvisible microgeometry remain measured with antialiasing uncertainty; low pathcount or cubic commands do not certify professional geometry. Source centers are rasterderived; this is not claimed subpixel boundary reconstruction.

Coverage remainsNOT_ESTABLISHEDwhere fitted arrangements are invalid. FineRBnumericalvalidity and K01zero flattened coverage defects do not prove complete ownership or source fidelity. Source-over antialiasing seams are separate from path closure semantics. Hypothetical proposal unions were actually rendered but never promoted as safe sharedregiongraphs. No finalSSIM/photorealistic/appearance milestone is claimed.

## 7. Runtime, resources, tests and independent QA

Eight monitored B/Cworkers used 62.305s summed wall time, peak sampled tree RSS 255.215MiB. PhaseCpeak 106.727MiB, longestCworker 3.753s. Evaluation/rendering took 99.954s, sampled peak 245.348MiB. All final workers returned0; no600s/4GiBor60s/512MiB limit fired. Conservative all-12-logical-processor upper bound 1947.1CPU-seconds is below7200. Requested50mssampling can miss short peaks. Setup/packaging/QA are separate engineering work.

Root17implementationtests pass. Independent QA separately ran9exportertests,400fontToolssemanticchecks and tens of thousands of benchmark path-command comparisons. It confirmed frozen hashes, corrected exactequivalence, unchanged guard/config, candidate/reference separation, signed-area collapse counts, maskmetrics and actual renderability. Numerical intersection sensitivity is documented rather than concealed.

An evaluator integration error (missingPathimport, discovered before measurementscompleted) is preserved in MEASUREMENT_INITIAL_FAILURE.log; source constructors, scientific parameters and frozen candidates were unchanged. Historical files are not edited by in-memory evaluator serializer bindings. Completed measurements use the corrected explicit serializer consistently for foreground, Arabicproxy, visibleIDs and actualSVGs.

## 8. Next milestone: ClassicalCV / pretrainedML / hybrid

See reports/NEXT_MILESTONE_ML.md for a short primary-source comparison. **Engineering recommendation:** a bounded hybrid feasibility comparison is justified, but ML superiority isNOT_ESTABLISHED. Learned context may help distinguish missing structural regions from shading; it cannot repair serialization or uneven-knot cubicovershoot. Separate pre-fitdiscovery quality from post-fitgeometry in any model trial.

Suitable candidates for an owner-approved next test are CPU-first pretrainedDexiNed/OpenCVONNXedge evidence and SAM2.1Hieratiny prompted regions, compared with the classical controls and a fixed hybridpostprocessor. SAM3/3.1conceptsegmentation is a higher-cost alternative, not a default. Read-only hardwareinventory foundGeForceMX130with2048MiB; noGPUinference was attempted. Exact model feasibility/latency/VRAMonthislaptop isunverified. Record exactweight/code licenses and revisions before any futuredownload; use isolated runtimes, no traininginitially. NoMLweights/training/integrationoccurrednow.

Next controlled decision should include internal-component vetoes, source-onlyautomaticprompts separatefromevalannotations, falsepositive lighting controls, unseenimages, and the same correctedserializer/topologytests. A model that finds only the outerShield or loses crownornament/Arabiccountershasnotmetthegoal. The known curvefittingstability limitation needs a distinct control, not attribution toML. Do not begin this new direction without ownerGO.

## 9. Deliverables and final decision

ActualSVGs andnativePNG/1x4x16xviews are in results and the ownerHTMLdashboard. Fineexternalfixture/derivatives remainlocal-only withhashmanifest; no publicredistributionrights areassumed. Reproductioninstructions, original/correctedimpactvalues, guardaudits, discoveryrejections, QA, source/configpins and fullinventory areincluded. Exactownerpublicationcommands accompanytheoutputs becauseGitmetadatawritesremainblocked.

**VERIFIED:** serializerdefectcorrected andmatchedgate restored; rawfacedecompositionunblocks narrowguardrepairs; newsource-onlycubicstrokeproposalsgeneratedonArabic/Shield.

**SUPPORTED BUT LIMITED:** topology-safetyimprovement, sparsecandidate discovery and scopedrendercorrectness.

**NOT ESTABLISHED:** completecrown/Arabic/thingeometry, safeintegrationofCproposals, universalhighfidelity,MLbenefit orproductionreadiness. Fine andArabicnegativeoutcomesremainprominent.

Stopafterthisapprovedcycle. GeometryNOT_ACCEPTED; architectureNOT_APPROVED. AwaitownerGO/NO-GOforthenextmajorresearchmilestone.
