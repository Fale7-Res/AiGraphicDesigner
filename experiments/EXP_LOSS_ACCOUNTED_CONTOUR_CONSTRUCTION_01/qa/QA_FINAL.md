<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T15:23:52Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T15:23:52Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T15:23:52Z"}
END_DOC_PROVENANCE -->
<!-- DOC_PROVENANCE {"created_at_utc":"2026-10-30T15:20:31Z","last_edited_at_utc":"2026-10-30T15:20:31Z","tracking_started_at_utc":"2026-10-30T15:20:31Z","last_action":"CREATED","last_change_id":"AGD-CONTOUR-QA-FINAL","last_editor":"contour_qa"} -->
# Independent final QA — loss-accounted contour construction

**AUDIT_RESULT: PASSED for bounded experimental evidence, with limitations below. Geometry NOT_ACCEPTED; production architecture NOT_APPROVED.**

Reviewer: `/root/contour_qa`. This reviewer did not implement construction features, rerun detection/inference, alter thresholds/references, or rerun the candidate matrix. QA writes only independent audit code, records and verification renders. Reviewed complete owner vision, AGENTS, previous ML report/QA and actual old/new construction, stable fitter, corrected exporter, monitor, evaluation, frozen protocol, final REPORT and saved artifacts. The full project vision is preserved; no final appearance, training or production integration is accepted by this audit.

## Frozen inputs and experimental isolation

Independently verified all 74 protocol pins using the explicit final source amendment, plus all four final pre-execution source pins. The initial partition implementation hash was superseded in `PRE_EXECUTION_SOURCE_FREEZE.json` before candidates; this is disclosed rather than silently editing the original protocol. Constructors receive original source points, fixed thresholds/budgets and source-derived partition geometry. Evaluator guides/masks are separate; no benchmark-specific answer geometry or image ROI enters construction. Case names route files only.

All 18 saved O SVGs are byte-identical to prior stable outputs. All 18 recomputed O metric boundary/guide records exactly match corresponding prior frozen records. Packaged and executed ASTs match for run_case.py, monitor.py and partition_fit.py; provenance comments do not change behavior. No model download or inference is necessary or present in these construction comparisons.

## Exhaustive source-edge and loss ledger audit

The independent original-input audit verifies **13,094 traces** across six cases × three arms. Trace IDs are complete and unique; all stored raw lengths independently match source coordinates. No duplicate undirected raw edge occurrence was found.

For all **36 P/Q conditions**, independent inspection verifies:

- Every consecutive edge of every original trace belongs to exactly one accepted/rejected/skipped interval. Shared split anchors are allowed; edges are never duplicated or omitted.
- Independently recomputed interval arc lengths agree with records; accepted plus rejected length equals total raw length and saved summaries.
- Accepted interval IDs correspond exactly to exported chains, without silently discarded accepted partitions or duplicated output spans.
- Controls are finite. Consecutive cubic endpoints match exactly; original source anchors and closed endpoints are unchanged.
- Cubic/path totals match metadata, with at most4096 cubics per condition.
- Closed flags are emitted only for fully retained closed source traces. Q retains33 closed contours across the18 case/arm sets; this count is not a filled-region or hole count.

The stage-0 skeleton audit independently confirms six omitted vertices: Shield Classical1 and Astronaut Classical5. They are isolated pixels, with no traced incident contour length. All other sets have zero omitted skeleton vertices. Those omissions belong upstream of fitting and are not hidden in retention claims.

## Independent curve and SVG verification

All36 new SVGs are parsed independently. Their M/C/Z commands and17-digit coordinates round-trip exactly to saved control points; closure commands occur only for genuinely closed chains. SVG trees contain only svg/path elements, diagnostic strokes have fill=none, and no embedded raster, foreignObject, scripts, rectangles or underlay appears. Independently rendered all18 Q SVGs through actual resvg. Empty O/CAP control SVGs remain visibly empty rather than being repaired by fallback content.

Independent Bernstein evaluation, without importing the production fitter/flattening code, samples129 points per cubic. Every accepted curve remains within0.6px of its corresponding raw interval in that direction. Reverse numerical checks sample source segments at<=0.05px spacing against Bernstein polyline approximations, allowing0.003px numerical comparison allowance. All36 conditions pass. This is independent numerical corroboration, **not an exact continuous deviation certificate**.

Independent sampled shape predicates find zero newly self-intersecting chains where the original source was simple, and zero new mutual proper crossing/overlap pairs compared with corresponding raw source traces. The test does not certify exact arithmetic topology, all near contacts, gapless fills, or correct omitted junction incidence. Inherited source intersections or missing features remain possible.

All three K01 arms retain three valid closed contours in both P and Q. Independent pairwise source/fitted polygon containment relationships agree. This verifies closed contour nesting, **not filled-region ownership or true hole semantics**: the oval boundary and quadrilateral decoration cannot both simply be relabeled holes. The exporter produces boundary strokes, not completed faces.

## Separately frozen cap-only diagnostic

Verified `CAP512_DIAGNOSTIC_FREEZE.json` and the exact executed source hash. The code changes only the old stable fitter's maximum_segments64→512 on the identical three K01 source traces per arm;0.6px deviation,0.35px RDP and eight refinement rounds remain fixed. All nine traces still fail deviation_budget; all three SVGs are empty and independently renderable.

This supports the narrow conclusion that raising capacity alone under the old bounded fitting procedure does not reproduce the observed K01 repair. It does not independently identify which partition/corner/refinement ingredient caused every gain, nor establish that periodic smoothing was necessary. Main O/P/Q outputs remain unchanged by this separately frozen diagnostic.

## Tests, resources and artifact checks

Independently ran the nine construction tests: all pass. Tests cover long-contour accounting, periodic loops, sharp corners, opposite winding, source endpoints/shared junction coordinates, open P/Q equivalence, and explicit deadline/complexity/invalid-input losses. Unit tests establish bounded contracts, not complete artwork reconstruction.

Reviewed controlled process-tree monitoring evidence: a touched64MiB child is included, measuring96.27MiB tree RSS versus3.91MiB launcher RSS; the separate48MiB limit stops the owned tree. All18 main workers completed, each with descendant PIDs and nonzero samples. Maximum sampled tree RSS is159.875MiB; summed main worker wall time661.176s. Sampled RSS can miss peaks and double-count shared pages. These are not exact unique-memory or instantaneous maxima. Cap-only diagnostic telemetry is separate.

At this audit snapshot296 repository PNGs decode/verify. Dashboard local href/src checks resolve **604 repository references and723 owner-dashboard references**, with zero broken links. The owner dashboard includes restricted Fine Features evidence; its derivative images/geometry must remain local-only. QA/native_renders also includes Fine Features and must not be copied wholesale into public history. Numeric audit records and code are publishable subject to the experiment's provenance policy.

## Visual findings and anti-mosaic limits

Inspected actual K01 and Shield Classical native comparison sheets, and independent resvg outputs. K01's old empty result becomes a recognizable exterior, oval and internal quadrilateral in P/Q. The drawing still contains obvious staircase/jitter, especially at high zoom. Shield Classical remains fragmented and lighting-heavy; the crown does **not** become a complete recognizable internal reconstruction.

Long-path bounding boxes conceal tiny cubics. Independent audit records include cubic control-box scales and short-chord fractions; the main evaluator additionally reports flattened-curve span and length-weighted short-cubic fractions. The reported approximately23.8% K01 Classical P and37.4% Arabic Classical P short-cubic length are negative vector-quality evidence. No explicit pixel fallback was found, but retaining lattice-derived traces as cubics is not proof of professional continuous geometry. No anti-grid acceptance is granted.

## Scientific claims and remaining uncertainty

**VERIFIED:** meaningful old construction loss, exhaustive edge accounting, recovery of K01 closed contours, sampled fit/endpoint consistency, failure of the cap-only control, preserved negative outcomes and periodic Arabic regression.

**SUPPORTED BUT LIMITED:** improved retained boundary support for Arabic/Fine Features and useful partitioning as a research construction control. Increased per-trace capacity and partition/refinement are coupled; this matrix does not identify all independent causal contributions.

**NOT ESTABLISHED:** complete Shield crown/ornament, correct glyph outlines/counters, complete foreground-object topology, shared filled regions, professional smoothing, photographic boundary truth, final-image fidelity or production readiness. Shield guides remain uncertain1.2–2px proximity evidence; Arabic references remain source-threshold proxies. Restoring more reflection/texture curves is not necessarily restoring structural geometry.

The final report accurately distinguishes selection loss from fitting loss, and source evidence from reference truth. In particular, Shield Classical raw-all crown support near0.85 becomes only~0.302 selected; P retains the selected length but crown support remains~0.304. Further local fitter tuning cannot be credited with recovering evidence excluded by that selection policy. Other boundaries remain genuinely absent or ambiguous in frozen evidence.

## QA recommendation

Retain P as a bounded construction control; do not adopt Q globally. A next separately approved experiment may test source-supported junction/region integration and component-aware selection, with explicit critical-component and microgeometry/coherence vetoes. Do not begin another detector search just to compensate for already-detected but excluded traces. Geometry remains NOT_ACCEPTED; architecture NOT_APPROVED. No new architecture or research milestone is implemented or approved by this QA.

Publication itself is outside this audit's certification. Root must verify actual Git remote SHA or provide scoped owner-run commands; local artifact integrity cannot be represented as successful GitHub publication.

Evidence: PREFLIGHT_QA.md, ORIGINAL_TRACE_AUDIT.json, CANDIDATE_AUDIT.json, GEOMETRY_AUDIT.json, DELIVERY_AUDIT.json, FINAL_LINKS_CAP_AUDIT.json and their independent audit scripts. Counts describe this saved snapshot; subsequent provenance/packaging-only additions require appropriate final inventory updates.
