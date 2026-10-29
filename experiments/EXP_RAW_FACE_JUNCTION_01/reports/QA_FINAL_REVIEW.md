<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T12:39:52Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T12:39:52Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T12:39:52Z"}
END_DOC_PROVENANCE -->
# Independent final results QA — raw-face/junction study

Reviewer /root/raw_face_qa. Passive audits of saved four-case O/R/B plus K01 RB; no candidate construction, refitting, parameter search or rerendering by QA. Abstract tests were independently run before candidates. Complete geometry is **NOT_ACCEPTED**; architecture **NOT_APPROVED**.

## VERIFIED — preservation and matched raw representation

Independently compared full graph fields and segmentation arrays. O and R have exactly equal chains, all raw vertices and fitted control points, incidence/adjacency, dimensions and non-face metadata. Per-label Counters of directed chain occurrences match exactly. Independently summed signed raw areas per original walk and per label; differences are <=1e-9. O/R curve-only SVG and PNG hashes are identical on all four cases.

Independently decoded actual saved native/8x raw region-ID renders: every RGBA pixel agrees on all four cases. This establishes the promised raw-coverage control for these renders; top-visible region IDs alone do not certify hidden overlap, but occurrence/chain invariants independently preserve parity.

| Case | O raw-invalid / rings | R raw-invalid / rings | Splits |
|---|---:|---:|---:|
| Fine | 1 / 18 | 0 / 27 | 9 |
| Arabic | 7 / 226 | 0 / 235 | 9 |
| Shield | 18 / 464 | 0 / 500 | 36 |
| K01 | 0 / 45 | 0 / 45 | 0 |

These are simple-walk decomposition results, not newly discovered regions or recovered components. Changed denominators must accompany all ring counters. Point contacts remain point contacts. K01 correctly stays unchanged.

## VERIFIED — frozen fitted-render gate fails in three cases

Independently recounted O/R fitted-region8x differing RGBA pixels: fine **8,735**, Arabic **19,070**, Shield **78,232**, K01 **0**. Saved RB is absent in the three failed cases and the explicit skipped ledgers are correct. K01 RB exists and its entire graph equals the previously saved B control exactly.

Therefore **safe-fitting unblocking is NOT_ESTABLISHED on the three cases where raw-invalid walks were corrected**. No guard may be bypassed, frozen criterion weakened, or skipped branch presented as an executed negative. K01 only reconfirms a previous local correction, not a new raw-face benefit.

## VERIFIED exporter mechanism; attribution is limited

The inherited `EXP_COMPLETE_GEOMETRY_ISOLATION_01/geometry_eval.py:87` appends `Z` to each closed chain's fitted command string. Line97 removes every later chain's initial `M` while concatenating them into a containing face subpath. SVG `Z` then closes to the containing subpath's original move point, not the embedded chain's own start. Line99 adds another final close.

Passive command-state tracing identifies wrong embedded close destinations in O: fine **1**, Arabic **7**, Shield **24**, K01 **0**; R has **0** in every case. Each produces an unintended command-position jump into a following chain. By independent curve/ring reconstruction, actual O/R fitted-ring endpoint gaps are **zero on all cases**. Thus the observed discrepancy has a concrete exporter-command explanation and is not evidence that R moved control points or lost raw support.

This proves the defect exists and affects the failing conditions. A future isolated corrected-export test would be needed to quantitatively attribute every changed pixel or establish corrected O/R renderer equivalence. No such replacement/rerender was performed by this QA. Historical exporter stays unchanged. Frozen primary RB skips remain binding despite the diagnosed mechanism.

## Structural outcome and denominator caveats

Saved metrics show fine fitted IoU remains0.820243 and raw13 components versus known4; discovery/continuity did not improve. Arabic source-proxy IoU changes0.920245→0.931811 while chain-only drawing is byte-identical: this is export/grouping behavior, not new letter outlines. The proxy still has6 fitted components/1hole versus raster-threshold40/9, and is not independent glyph truth.

Shield crossing/overlap count remains7 with the exact same chain geometry; no new crown component can be credited to this face repartition. Its raw-invalid18→0 and fitted-invalid153→139 must not obscure changed464→500 ring denominator or collapsed131→133 tally. Fine collapsed3→6 likewise exposes separate cycles, not newly destroyed control points. All important internal artwork remains unaccepted under unchanged uncertain1.2–2px guides.

K01 RB corrects3 collapsed rings exactly as oldB, yet IoU0.950661647273557 is unchanged and below.97. This is topology safety only, not improved silhouette.

## Source-driven feasibility probe

Reviewed `source_evidence_probe.py:39` and wrapper97: constructor inputs are uint8 native source RGB only, fixed uniform constants; no labels, case geometry, references or evaluator ROIs. Lab multiscale Canny and both-polarity luminance Sato produce maps, not chains/regions. Source inspection found no evaluator leakage or image-specific hardcoding. Evaluator distance-to-raw-cracks is a later measurement, not a constructor input.

Shield's3,428 of12,634 persistent source edges farther than2px from raw cracks represent unmodeled image contrast, potentially shading, texture or aliasing. They are not verified missing structural boundary pixels or crown recovery. Fine's zero beyond2px does not exclude sub2px connectivity gaps. Pixel-indexed Canny is not subpixel vector reconstruction. Probe maps do not establish width, junction topology, semantic structure or a deployable engine.

## Artifact checks and limits

At audit time parsed **117 SVGs** and decoded/verified **152 PNGs** across public result and local-only fine directories. No SVG image/script/foreignObject tag found. This is XML/decoding and saved-output checking, not independent renderer execution, human crown annotation, final dashboard visual acceptance or a proof that inherited tiny geometry is professionally coherent. Final packaging may add derivatives.

Audit scripts and exact evidence: baseline_face_audit.json, output_integrity.json, exporter_audit.json, artifact_audit.json in work/raw_face_qa. Frozen protocol SHA checks passed before execution. A draft extra passive flattening audit was interrupted for redundant computation; corrected cached-point version completed6.7s, without candidate mutations.

**Recommendation:** deliver this honest representation/exporter diagnosis. Correct and independently validate compound-path export in a separate scoped control before inferring fitting gains. Do not spend another indefinite cycle on face counts. Missing structures still require source-driven discovery, with explicit topology and internal-component evaluation and a new owner decision before broader engine construction.
