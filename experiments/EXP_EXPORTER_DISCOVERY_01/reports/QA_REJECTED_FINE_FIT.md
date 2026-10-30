<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:13:29Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:13:29Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:13:29Z"}
END_DOC_PROVENANCE -->
# Read-only diagnostic: rejected Fine Features strokes

**VERIFIED:** both long Fine Features source chains were rejected for actual cubic displacement beyond the frozen0.6px gate. Coarse nearest-sample distances contribute error in one direction but do not explain away the rejection.

No configuration, constructor, saved candidate, acceptance decision, or evaluation threshold was changed. This diagnostic called the unchanged private `_fit` only on the two saved rejected source polylines, captured its local arrays using Python tracing, and independently compared those same cubics against raw line segments. It did not rerun source discovery or the benchmark matrix. Input proposal JSON SHA256 remained `66734234c37b3c07575d659026664c77f7087d7f1b70b244b596b892f20d6450`.

| Saved chain | Frozen sampled point-NN deviation | Dense cubic→raw segment maximum | RDP-only polyline Hausdorff | Outcome |
|---|---:|---:|---:|---|
|0|0.673353px|approximately0.67736px|0.342997px|Still rejected |
|2|0.836103px|approximately0.83985px|0.316228px|Still rejected |

The independent comparison uses inherited convex-hull cubic flattening at0.01px and source/curve polyline sampling at0.01px, followed by Shapely point-to-line-segment distances. Segmentwise sampling gives maxima slightly different from whole-curve arclength sampling because sampling locations differ. This is strong numerical evidence of overshoot, not exact continuous predicate certification. Already-saved curve samples also exceed0.6px when measured against source segments directly (0.665222px and0.829315px), so the conclusion does not depend on nearest-neighbor sampling density or a newly relaxed test.

**VERIFIED mechanism:** Douglas–Peucker produces unevenly spaced vertices. The centered Hermite tangent uses half the next-minus-previous vertex vector without scaling to each adjacent segment's chord length. A long neighboring chord can therefore generate a very long handle on a short segment. In chain0, one1px chord receives a first control handle about5.54px long. In chain2, a1.414px chord receives a first handle about3.50px long. These create genuine local excursions away from the raw source chain. No sharp corner was detected on either chain under the frozen60degree rule; invoking corner preservation did not constrain these smooth-but-unequally-spaced knots.

**VERIFIED measurement limitation:** chain0's largest raw-sample→curve-sample nearest-neighbor distance is0.62156px, while that same raw point is only0.00649px from the flattened curve's line segments. Fixed32sample counts can therefore overestimate one directed distance on a long segment. That artifact is real but does not rescue either rejected chain because independent curve→raw distances still exceed0.6px.

**SUPPORTED BUT LIMITED:** on these two chains, the fitting stage damaged an otherwise available long source-derived centerline. This is stronger evidence than a blanket claim that the source discovery found nothing. It does not prove the centerlines match independent truth, have correct widths, recover four intended components, or safely integrate with the shared face graph. Their raw skeletons remain raster-derived and a small Hausdorff distance to them does not establish professional vector geometry.

**HYPOTHESIS for a later approved test:** chord-aware/centripetal tangent parameterization or a bounded-error cubic fitter could preserve long discovered chains while avoiding overshoot. Merely increasing the0.6px gate would not correct the demonstrated geometric error. No alternative fitter was implemented or accepted in this diagnostic.

Local-only derived external evidence (do not publish without rights clearance): `work/exporter_discovery/external_results/fine_features/rejected_fit_diagnostic_details/rejection_analysis.json`, `REJECTED_CURVES_DIAGNOSTIC_ONLY.svg`, and `REJECTED_16x.png`. The SVG overlays raw source-skeleton polyline in blue and the unchanged rejected cubic in red. It is prominently labeled rejected diagnostic evidence and is not an accepted reconstruction or a fallback export. Generic reproduction script: `diagnose_rejected_fit.py INPUT_PROPOSALS_JSON NEW_OUTPUT_DIRECTORY`.
