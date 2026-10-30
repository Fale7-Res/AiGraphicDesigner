<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:13:29Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:13:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:13:29Z"}
END_DOC_PROVENANCE -->
# Independent final QA — exporter correctness and source discovery

Reviewer: /root/export_discovery_qa. **Bounded engineering/research evidence supported; geometry NOT_ACCEPTED and architecture NOT_APPROVED.** No benchmark segmentation/fitting was independently rerun, no parameter search or candidate edits were performed. QA independently parsed saved outputs, numerically integrated curves, decoded renders, and ran abstract serializer controls.

## VERIFIED — frozen controls and serializer correctness

Independently verified 61 frozen policy, source/candidate, dependency and reference hashes. O/R graphs retain identical chain geometry and per-label directed occurrence multisets; all copied O/R/B graphs and labels match their frozen hashes. Historical Track B source is pinned unchanged. No constructor receives evaluator contours, truth masks or case-specific construction ROIs.

Nine serializer regression tests independently passed, including actual resvg canonical controls. A separate third-party fontTools parser audit passed 400 random raw/fitted, forward/reverse closed L/C semantic checks. Passive parsing of 36 corrected benchmark region/raw-region SVGs, 5,961 region paths and 212,645 segments exactly matches independently assembled directed graph commands, including implicit chain closure and reversed cubic controls. Evenodd semantics are retained. These checks establish serialization correctness in the tested domain, not certified global geometric topology.

Independently decoded all 12 corrected O/R raw-native, raw8x and fitted8x comparisons: zero differing RGBA pixels. The previously blocked equivalence prerequisite now passes for every case. Scope remains the verified compound research exporter: no defect in VTracer's native exporter or production application is inferred. Historical defective exports remain preserved. Eight-digit closure-only and separate seventeen-digit precision controls appropriately isolate mechanisms.

## VERIFIED — decomposition unblocks unchanged guarded fitting

RB changed exactly the chain IDs recorded as accepted: Fine 6, Arabic 128, Shield 50; K01 reuses the prior six-chain control. Every changed chain is exactly one A,B,B,C cubic with original endpoints. Faces, labels, incidence, raw support, chain identities and all non-segment metadata remain unchanged. No new paths, labels, source-grid rectangles or implicit topology edits are inserted.

Independent eight-node Gaussian signed-area integration yields:

| Case | R rings / collapsed | RB rings / collapsed |
|---|---:|---:|
| Fine | 27 / 6 | 27 / 0 |
| Arabic | 235 / 69 | 235 / 5 |
| Shield | 500 / 133 | 500 / 106 |
| K01 | 45 / 3 | 45 / 0 |

These are matched R/RB denominators. Original O denominators differ after walk decomposition and cannot be used to imply additional missing-artwork recovery.

An alternate 128-interval-per-cubic sampled cross/overlap audit found no new R→RB pair identities in any case. Absolute counts are numerically sensitive for nearly coincident collapsed chords and differ from the frozen control-hull flattening counts; neither diagnostic certifies continuous topology. The frozen seven Shield crossing/overlap pairs and unresolved invalid geometry remain acceptance blockers. Do not present restored area as a proof of correct source detail or globally valid artwork.

## VERIFIED — rendered structural limits remain

Independently decoded saved foreground PNGs and recounted IoU/components/holes:

- Fine O/R IoU 0.820243, 12 components; RB 0.825394, **15 components against four**. Better area overlap accompanies worse connectivity. Thin geometry remains failed.
- Arabic corrected O/R proxy IoU 0.931811; RB 0.933549. Both have six components/one hole against a threshold proxy's 40/nine. This is not independent glyph-outline truth or correct typography.
- K01 stays 0.950662 with one component/one hole. Topological area correction does not improve the main silhouette or pass 0.97.

No source-driven discovery of a missing crown component can be attributed to fixed-label serialization or area repair. The 1.2–2px Shield reference uncertainty still prevents strict one-pixel completeness claims.

## VERIFIED — new source geometry proposals, negative discovery outcome

The source-only paired-flank constructor has no labels, guides, truth curves or case name as inputs. Saved source-file and RGB-array hashes match actual input. Proposal SVG path counts match 0 Fine, 17 Arabic, 24 Shield, 0 K01; all explicitly remain unintegrated into the shared graph. Fine's two long source chains failed the fixed curve-deviation check; no threshold was relaxed. Isolated ridge extraction is not recovery of complete thin shapes.

QA independently rendered actual Shield/Arabic proposal SVGs with resvg and visually compared native sources. Shield contains sparse short crown-tip/lighting, rim and band snippets; complete crown outline, ornament and band are not recovered. Arabic proposals are isolated fragments, not complete contours/counters. Source paired contrast remains ambiguous between geometry and narrow lighting/texture.

Arabic's actual hypothetical paint-union diagnostic **worsens** proxy IoU to 0.918758 and changes topology to one component/seven holes, versus corrected baseline six/one. The source proxy remains 40/nine. This is direct evidence against naively integrating these proposals. Fine/K01 propose nothing, so their hypothetical unions remain baseline. No complete structural recovery or safely integrated topology is demonstrated.

The proposals use continuous bounded cubic strokes rather than source-grid rectangle fallback. However centerline evidence begins at pixel centers, uniform median widths lose variation, sampled curve deviation is not a continuous bound and junction integration is absent. Small curves are not automatically meaningful details. A zero proposal-proposal crossing count cannot certify safe placement relative to existing boundaries; root measurements report additional baseline crossings and must remain explicit.

## Artifacts, resources and remaining uncertainty

At audit time 282 saved SVGs parsed and 381 PNGs decoded/verified, with no image/script/foreignObject elements or decoding errors. Legacy defective exports are intentionally included as evidence. This is artifact integrity, not final delivery-link/human visual acceptance. Root may add dashboard derivatives after this snapshot.

Reviewed monitored execution logs: all eight construction workers return zero; sampled memory and wall times remain below frozen per-phase limits. Measurement rerun completed after a missing Path import was fixed in the evaluator; the initial failure log is preserved and constructors were not rerun. Sampling can miss brief peaks; no certified maximum-memory claim is made. QA does not certify Git publication.

## Recommendation

Retain the corrected research exporter and decomposition as validated prerequisites. Safe fitting is now demonstrably unblocked but remains a topology-safety improvement, not complete drawing reconstruction. The stronger source-proposal hypothesis produces real curves but **does not demonstrate useful cross-category missing-structure recovery** and naively harms Arabic. Do not continue by loosening thresholds or integrating fragments unguarded. The next major research decision should focus on reliable structural evidence/region or variable-width stroke discovery with explicit internal-component references and topology integration, comparing classical and local pretrained evidence as a controlled future hypothesis. No pretrained model, weights, training or architecture adoption occurred here.

Evidence scripts/results are staged under work/exporter_discovery/qa_stage. No full geometry, final appearance or production readiness is approved by this review.
