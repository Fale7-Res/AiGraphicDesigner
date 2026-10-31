# START CHANGE AGD-UNIVERSAL-REPORT | 2026-10-31T11:07:29Z | EDITED | Author: root
from pathlib import Path
import json,hashlib,shutil,datetime,collections
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');W=Path.cwd()/'work';E=R/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01';O=Path.cwd()/'outputs/universal_geometry_review';O.mkdir(exist_ok=True)
rows=json.loads((E/'reports/METRICS.json').read_text());protocol=json.loads((E/'protocol.json').read_text());lookup={(r['case'],r['condition']):r for r in rows};resources=json.loads((E/'reports/RESOURCES.json').read_text());combined=json.loads((E/'reports/COMBINED_RESOURCES.json').read_text());graph=json.loads((E/'reports/ENDPOINT_GRAPH_DIAGNOSTIC.json').read_text())
text='''# Universal geometry reconstruction: bounded decision report

Geometry: **NOT_ACCEPTED**. Production architecture: **NOT_APPROVED**.

## Decision

**VERIFIED:** this nine-case, six-condition study produced actual SVG geometry, native/full4x renders and true vector-rendered 1x/4x/16x detail views. No model inference, training, new detector thresholds, final appearance or production changes were used. O/P were reused byte-for-byte for six existing cases. Only Burger, Logo and Camera required unchanged classical extraction plus historical O/P construction once.

**SUPPORTED BUT LIMITED:** C removes redundant cubic spans under the same 0.6px numerical source-envelope gate without improving missing component completeness. R constructs bounded atomic faces where source curves already close; it does not solve incomplete region discovery. **S is rejected as a universal selection improvement.** Crown guide proximity improves, but several other categories lose substantial contour evidence. S+R passes the frozen control prerequisites but does not repair that regression.

**NOT ESTABLISHED:** professional complete geometry, semantic region ownership, full crown fidelity, true Arabic glyph topology, physical-vs-lighting precision, or final image fidelity. No SSIM/PSNR success is claimed for diagnostic line drawings.

## Starting state, publication and owner vision

Starting local main and remote main were both `8fbe261710e8ec668f13a1986b53ef2871a896fb`, clean before this experiment. Owner original vision was read completely. Image generation, future appearance, Arabic typography, semantic groups, Magic Layers, editability, version history and QA remain authoritative and untouched.

The first scoped `git add -- experiments/EXP_UNIVERSAL_REGION_COHERENCE_01` failed: `.git/index.lock: Permission denied`. This is Git metadata filesystem permission, not an established authentication failure. No retry/bypass/ACL changes. All checkpoints remain **uncommitted and unpublished** unless the owner subsequently runs the scoped publisher and verifies remote HEAD. See `Publish-Research.ps1`; no claim of upload is made.

## Frozen design and isolation

`protocol.json` froze source/baseline/constructor/reference hashes, budgets and rules before candidate runs. Camera bytes were pinned before inference/construction; Camera ran last after code lock. Publicly familiar Camera is a project-new holdout in this series, not evidence of arbitrary unseen-world generalization. Six cached cases use saved Classical predictions/traces, preserving coordinate systems and the corrected exporter. This cycle isolates construction/selection/integration on Classical evidence; it does not rerun the previous Classical/ML/Hybrid matrix or establish cross-detector generalization.

Development: Shield/Arabic/K01; validation: Fine Features/Horse/Astronaut/Burger/Logo; holdout: Camera. Parameters were selected from generic synthetic fixtures and frozen without tuning on benchmark results. Independent references were evaluator-only. Burger/Logo are inherited AI-generated initial12 low-resolution crops without vector truth. Fine Features source and every derivative remain owner-local pending Arena reuse rights; numeric results and hashes are preserved publicly.

O: stable historical whole-trace fitter. P: principal saved partitioned control. S: same >=6px eligibility and128-trace cap; fixed 0.35 persistence +0.25 normalized contrast +0.15 closure +0.15 junction +0.10 coherence score, tie trace ID. No length term. The >=6 restriction is deliberately unchanged to isolate ranking from P's internal eligibility gate; this experiment does not claim to recover <6px features. New-source O uses the historical stable fitter/cap/deviation but is newly reconstructed, not historical saved evidence.

R: exact endpoint cubic halfedge rotation, no snapping or inferred closure; retain valid positive-area bounded cycles and immediate containment as atomic faces. Export original cubic references through corrected serializer. Every unsafe/open chain remains an explicit unintegrated stroke. Atomic nested partitions are not automatically glyph holes, physical objects or occlusion ordering. Source border-Lab hints never remove geometry. Numerical flattening0.005px screens validity, not exact continuous certification.

C: exact P input, first32 longest chains, endpoint/tangent-constrained chord-length least squares with balanced subdivision. Preserve P source interval anchors and corners, same0.6px bidirectional numerical envelope, closure/winding/containment/incidence checks and rollback. Require fewer cubics; this is only a necessary capacity improvement, not sufficient professional smoothness. Nothing is replaced by raw-grid paths.

S+R: frozen prerequisites were met on independent controls: K01 and Fine S recall did not drop >0.01, R produced safe faces and no new measured crossing. Then unchanged S curves entered unchanged R. This is a justified ablation, not promotion of S.

Budgets: one CPU thread,768MiB sampled worker-tree cap,700MiB available-RAM reserve,300s/case worker,120s S fitting,30s R and C cooperative checks,4096cubics/case,5400s total construction,200MiB public evidence target,50MiB/file. Cooperative module timing can finish an in-progress predicate; outer worker monitor is the enforced hard limit. No system installation/GPU use.

## Per-image results

Source recall below is proximity to frozen classical evidence at1.25px, **not precision against meaningful artwork**. Preserving lighting/texture also scores. R/SR counts are atomic geometric partitions, not accepted design objects.

|Case|P source recall|S source recall|P→C cubics|R / SR faces|P→C tiny cubic length fraction|
|---|---:|---:|---:|---:|---:|
'''
for case in protocol['cases']:
 p,s,c,r,sr=[lookup[(case,k)] for k in ['P','S','C','R','SR']]
 text+=f'|{case}|{p["source_edge_agreement_proxy"]["recall"]:.4f}|{s["source_edge_agreement_proxy"]["recall"]:.4f}|{p["cubics"]}→{c["cubics"]}|{r["filled_atomic_faces"]} / {sr["filled_atomic_faces"]}|{p["micro"]["tiny_cubic_length_weighted_fraction"]:.4f}→{c["micro"]["tiny_cubic_length_weighted_fraction"]:.4f}|\n'
text+='''
S improves no known-control boundary recall: Arabic, K01 and Fine are unchanged; their eligible trace sets fit within the same budget. Shield source recall drops0.5458→0.3460; Burger0.1840→0.0905; Astronaut0.1950→0.0674; Logo0.7875→0.6692; holdout Camera0.2636→0.1073. This is direct evidence that the frozen score prioritizes confident short details at the expense of coverage under a count budget. It does not prove the discarded contours were all true physical boundaries. No weights were retuned.

P and S accepted every selected source interval in8/9cases; Horse remains0.712 because the inherited512cubic per-trace budget rejects part of its long trace. All rejected intervals stay in ledgers, accepted+lost length conserves every raw edge. R/SR never delete proposals; the default boundary/topology metrics describe all preserved strokes. `integrated_only` separately measures actual face-boundary support; the dashboard explicitly distinguishes these scopes. A region SVG is not credited with unintegrated stroke recall.

### Shield: crown and internal structure

**VERIFIED mixed guide support, NOT accepted crown.** Approximate crown outline recall P0.3036→S0.4158; central tip/lobes0.343→0.490; right inner tip0.299→0.539; central ornament fold stays0.770. Upper/lower band guide proximity improves0.214→0.285 /0.613→0.725. Left tip/flank worsens0.068→0.055. Outer metallic ridge falls0.308→0.058; red/gold interface remains low0.131→0.196. These uncertain1.2–2px guides are proximity signals, not matched contour correspondence or independent strict1px truth. Crown tips, band continuity and full ornament drawing remain incomplete in actual SVG views.

R creates zero Shield faces; all128 P chains remain open/dangling/unbounded strokes. S+R forms only two atomic faces, not a complete crown or shield region assembly. C changes no material completeness: P crown coverage is essentially unchanged. A more recognizable fragment is insufficient for acceptance.

### Burger, logo and photographs

Actual Burger views show S emphasizing seeds/top details while losing important filling/cheese/lettuce contour support. R's18 faces primarily describe small isolated details such as seed-like components; no complete bun/filling region ownership follows. Logo R has12 bounded atomic faces but114 P chains remain unintegrated. Astronaut R has1 face, Camera4. No independent semantic/structural truth exists for these photographs or logo source crops. Lighting and texture falsepositives remain unresolved, not converted into asserted physical boundaries. Camera reproduces the selection failure after algorithm freeze; universal improvement is therefore not supported.

### Arabic, Fine Features and K01

Arabic fitted boundary proxy recall remains0.9730 across P/S/C, seven closed contours plus one open proposal; R yields7 atomic faces. Counters receive distinct diagnostic partition IDs, which does not validate true glyph hole ownership or typography. Source threshold is not independent font geometry.

Fine remains0.8495 independent known-vector boundary recall; R yields3 faces while15 strokes stay unintegrated. This does not recover the four intended complete foreground structures or demonstrate healed thin connectivity. No endpoint invention or template geometry was used.

K01 retains3 closed curves and3 atomic partitions, boundary recall0.9994 unchanged. Its oval background void and colored inner decoration are retained as different nested atomic partitions; containment alone is not labeled semantic hole truth. The existing independent foreground mask excludes an intended colored interior decoration, so its boundary precision is not full-artwork structural precision.

## Attribution: why region integration is blocked

**VERIFIED diagnostic:** exact trace-endpoint multigraph cycle rank E−V+components changes as follows:

|Case|All raw cycle potential|After >=6px filter|P selected|S selected|
|---|---:|---:|---:|---:|
'''
for row in graph:
 st=row['stages'];text+=f'|{row["case"]}|{st["all_raw"]["cycle_rank"]}|{st["eligible6"]["cycle_rank"]}|{st["P_selected"]["cycle_rank"]}|{st["S_selected"]["cycle_rank"]}|\n'
text+='''
This post-run diagnostic does not alter candidates, thresholds or acceptance. Independent QA recomputed with BFS. The large cycle loss occurs before fitting, especially at the per-trace minimum-length filter. It explains why smoothing accepted long chains cannot reconstruct all closed relationships. **SUPPORTED BUT LIMITED:** local trace eligibility/selection destroys network closure potential. **NOT ESTABLISHED:** every lost cycle is meaningful; many are source-grid noise, shading or tiny junction artifacts. Blindly retaining all short links would recreate the prohibited failure mode.

R preserves all P controls and finds valid atomic faces where exact shared relationships already exist. No new inferred joins/crossings are inserted. It therefore succeeds as conservative graph bookkeeping but cannot solve missing region assembly. This is a more precise negative result than claiming the curve fitter or renderer failed.

## Coherence and anti-mosaic

'''
before=sum(lookup[(k,'P')]['cubics'] for k in protocol['cases']);after=sum(lookup[(k,'C')]['cubics'] for k in protocol['cases']);changed=sum(lookup[(k,'C')]['coherence']['accepted_changes'] for k in protocol['cases'])
text+=f'C changes{changed} chains, reducing{before}→{after} cubics ({(before-after)/before*100:.2f}%). All nine length-weighted <=2px cubic-span fractions decrease modestly, as the table shows; source boundary/proxy recall is essentially unchanged. Curvature/tangent/lattice measurements are stored per chain in `quality`/C audit. Independent QA sampled accepted C curves against their exact source intervals: max0.581431px; no new sampled crossing/overlap/incidence conflicts. This numerical evidence is not a certified continuous guarantee.\n\n'
text+='''Actual4x/16x SVG renders still show staircases and many tiny spans. No raster, rectangle mosaic or pixel-grid fallback is introduced, but that does not make these curves professional. Atomic face area-weighted microgeometry and shared-interface counts are in `R_diagnostics.json`; stroke length×constant-width proxies are explicitly not true visible-area ownership. A reduction in cubic count is not a completed clean-vector milestone.

## Tests, QA, resources and reproducibility

21 synthetic packaged tests pass: deterministic source selection, closed loops, corners, shared junctions, open/dangling structures, nested partition/hole handling, improper intersections, reversing-collinear control-hull flattening and real resvg1/4/16renders. Prior partition/exporter sources are hash-pinned; no historical matrix rerun. Independent QA separately checked source/reference isolation, all ledgers, baseline byte identities, exact selection scores, R preservation and face validity, C displacement/topology, SVG commands and45 native resvg renders. See `qa/FINAL_QA.md` and audit JSONs. Unit success is not geometric acceptance.

'''
text+=f'Nine construction workers all completed in{sum(x["wall_seconds"] for x in resources):.3f}s summed monitored wall, sampled process-tree peak{max(x["sampled_tree_RSS_peak_mib"] for x in resources):.3f}MiB. Combined integration/render worker{combined["wall_seconds"]:.3f}s, sampled peak{combined["sampled_tree_RSS_peak_mib"]:.3f}MiB. Monitor validated descendant inclusion with64MiB touched allocation and48MiB controlled kill before benchmark claims. Summed RSS can double-count shared pages and sampling misses instantaneous peaks; this is not exact maximum. Primary evaluator/render pass has individual render timings but was not enclosed by a resource monitor; these memory peaks are construction/combined-worker measurements, not entire end-to-end dashboard generation.\n\n'
text+='''Reproduction uses installed isolated `work/agd-native`, `work/geometry-deps`, pinned historical modules and `work/resvg/resvg.exe`. No global packages change. `REPRODUCE.md` explains an isolated replica procedure; do not overwrite existing evidence with reruns. Protocol original source pins stay immutable. Post-execution evaluator/scope/graph diagnostics and combined wrapper hashes/timings are separately recorded, not falsely described as original frozen implementation. An initial renderer-test path needed a portable cwd/work/resvg correction before benchmark execution; no algorithm or criterion changed to obtain a pass. Provenance comments initially used approximate future author times; final comment-only timestamp correction is logged with pre/post hashes and is not a candidate algorithm change.

## Alternatives rejected and next decision

Length-only ranking was retained as control, not preferred universally. Confidence-only short detail preference failed its multi-category test. Selecting every edge or globally increasing segmentation was rejected as a microgeometry/lighting trap. Snapping endpoints, planarizing arbitrary crossings, interpreting every nested contour as a hole and inventing closure were rejected because no source-supported ownership/connection proof exists. Aggressive smoothing or relaxing0.6px was rejected; C deliberately gives modest changes rather than detail loss. New model inference would not fix the demonstrated trace-filter closure loss and was not repeated.

**Recommended next bounded experiment — network-aware contour assembly before eligibility filtering**, with P predictions frozen. Test whether short source-supported junction connectors can be treated as graph relationships and assembled into meaningful continuous contour groups before applying a group-level evidence/complexity budget. Compare identical evidence with per-trace>=6 filtering versus junction-aware grouping; independently measure cycles, false joins, critical detail, tiny faces and true vector spans. Use known-vector junction/noise controls plus Arabic/Burger/Shield/holdout. Do not accept all short pixel edges or build thousands of tiny faces. Freeze source confidence/continuity rules and microgeometry vetoes before running. Keep C as an optional unchanged conservative control. A closure potential gain alone cannot pass; independent internal-component and false-join controls must improve.

**GO recommendation:** only that next bounded network-aware assembly study, subject to owner approval. **NO-GO:** promote S as universal, treat R atomic IDs as finished artwork, claim C complete clean SVG, start appearance, or integrate a production engine. Stop here for owner review.
'''
(E/'REPORT.md').write_text(text,encoding='utf-8');shutil.copy2(E/'REPORT.md',O/'REPORT.md')
rep='''# Reproduction and evidence policy

Use a separate experiment replica directory or checkout. Do not delete or overwrite frozen results. Python3.14.2 and existing isolated dependencies: NumPy2.4.4, SciPy1.18.1, skimage0.26, OpenCV4.14.0.94, Pillow12.1.1, psutil7.2.2, Shapely2.2 (work/geometry-deps); resvg0.49 in work/resvg. The code imports historical repository modules at pinned hashes and uses the original Codex workspace cwd. No model weights, global install or paid service.

`universal_run.py CASE` is the one-case source-only worker; `launch.py` validates process-tree monitor and runs the frozen nine cases, Camera last. It intentionally refuses existing output folders. For exact reproduction, copy the new research directory and update ONLY its E destination in the replica plus historical import paths; source/algorithm pins remain. Cached O/P six controls must stay byte-identical. New Burger/Logo/Camera historical O/P are recomputed from unchanged classical evidence. Exact wall-time budgets are machine-dependent; resource-stop outcomes must be retained rather than overwritten.

`evaluate_universal.py` evaluates base O/P/S/R/C; `combined_control.py` checks the frozen gate then performs unchanged S→R; `region_scope_metrics.py` adds integrated-only scope; `graph_diagnostic.py` performs post-run endpoint graph attribution; `build_review.py` creates public/local HTML. Run each with the isolated Python from the original cwd. Do not rerun evaluate_all after combined unless preserving SR rows; it deliberately builds only the five primary metrics. Tests: `python -m unittest discover -s experiments/EXP_UNIVERSAL_REGION_COHERENCE_01 -p test_*.py -v` with PYTHONPATH pointing to work/geometry-deps and cwd the Codex workspace.

Source truth masks/guide annotations enter evaluation only. Fine Features source, all traces/SVG/PNG/QA visual derivatives stay work/universal_geometry/local_only/fine_features; public metrics/hashes keep that result reproducible for an owner with the supplied fixture. No rights are inferred for Arena assets. Model weights/venvs/build caches never enter Git. All public evidence is inventoried and hashed; no required source, output or negative result silently omitted. Camera is installed skimage data, CC0 per installed dataset doc. Frozen initial12 AI-generated crops inherit repository provenance and lack independent geometric truth.

Publication is owner-run because `.git/index.lock` was filesystem-denied once. Run scoped Publish-Research.ps1; it validates branch/remote/staging and ancestry, commits only intended experiment, pushes normally and compares local vs remote SHA. It creates no duplicate commit if nothing is staged. Never force push or reset unrelated work.
'''
(E/'REPRODUCE.md').write_text(rep,encoding='utf-8')
publisher=(Path.cwd()/'outputs/contour_construction_review/Publish-Research.ps1').read_text().replace('EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01','EXP_UNIVERSAL_REGION_COHERENCE_01').replace('Evaluate loss-accounted contour construction and closed loops','Evaluate universal contour selection region integration and coherence')
publisher=publisher.replace('$Lines = @(& git @GitArgs)','$Lines = @(& git -c "safe.directory=$Repo" @GitArgs)')
(E/'Publish-Research.ps1').write_text(publisher);(O/'Publish-Research.ps1').write_text(publisher)
print('Report saved',before,after,changed)
# END CHANGE AGD-UNIVERSAL-REPORT | 2026-10-31T11:07:29Z | EDITED | Author: root
