<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T11:43:19Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T11:43:19Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T11:43:19Z"}
END_DOC_PROVENANCE -->
# Track A — localized source-supported reconnection

Research only; production architecture NOT_APPROVED. Baseline is frozen S_A labels plus unchanged F_A initialization on fine_features, Arabic, Shield and K01. This track changes labels only; Track B is separately isolated. No benchmark was run during design.

## Hypothesis and intervention

Some missing thin support is a short disconnection between existing, similarly colored label regions despite a source-visible connector. A narrow, source-supported connector may recover continuity without globally increasing segmentation detail. This cannot discover a wholly absent crown band, new object or missing material region. If no proposal meets the gates, return original labels unchanged and record the negative.

`discover(rgb, labels, config=None) -> (new_labels, audit, evidence_arrays)` receives only common native-size white-composited sRGB pixels and positive frozen labels. There is no case name, reference, evaluator ROI or truth input. No Arena code is copied. The parent uses unchanged inherited F_A on the resulting labels.

## Frozen method

1. Skeletonize each existing label component locally using 8-neighbor connectivity; explicitly pad bounding boxes with background. Skeleton points of degree1 are endpoint candidates. Trace up to3 available skeleton steps inward and negate that vector for the outward tangent. Endpoint distance-transform radius must be <=2px.
2. Enumerate different-label endpoint pairs within12px. Existing four-neighbor-adjacent label pairs are forbidden: this is not a global same-color consolidation. Region mean Lab separation must be <=12, outward tangents must each face the other endpoint with cosine>=0.75, and local radius ratio must be <=2.5 with radius floor0.5px.
3. A common gap label must occur among the four-neighbors of both endpoints. The foreground prototype is the mean of the two region mean Lab vectors. The background prototype is the median common-gap source Lab in a1.5–3.5px flank band around the endpoint-to-endpoint segment, requiring at least3 samples. The bounded prototype ROI has4px margin. Insufficient contrast/support rejects the proposal; no global background fallback.
4. Require foreground/background Lab contrast>=15. Project each source pixel onto the background→foreground Lab segment, **clip mixture fraction to[0,1]**, and compute residual against that convex projection. A path pixel must have fraction>=0.15 and residual<=8Lab. Mean connector fraction must be >=0.35. This is a heuristic source-evidence gate, not physically exact antialias/color inference.
5. Run deterministic **four-neighbor Dijkstra**, confined to a1.5px corridor and the two endpoint regions/common gap label. Each step has unit geometric length and cost `1 + 2*(1-t) + residual/8`; costs are nonnegative. Route length is <=12 steps (=12px arclength), and <=12 new gap-label connector pixels. Skeleton8-connectivity is never a route fallback.
6. Rank proposals by path cost, connector-pixel count, minimum/maximum source label IDs and endpoint y/x coordinates. Greedily accept at most32 bridges, rechecking conflicts and newly existing adjacency. Merge the two endpoint-region identities into the lower ID, assign only connector pixels from the common gap region, and preserve all other spatial region memberships. Canonical ID renumbering after edits is bookkeeping, not extra geometry. A no-edit result preserves input labels exactly.

Before geodesic evaluation, endpoint pairs are sorted by distance then labels/coordinates and capped at512 per case. Audit records total/considered pairs and truncation. This is a computational cap, not evidence that an untested proposal is invalid.

## Exact parameters

```json
{
  "version": "endpoint_color_geodesic_v1",
  "skeleton_connectivity": 8,
  "endpoint_degree": 1,
  "endpoint_tangent_steps": 3,
  "max_endpoint_radius_px": 2.0,
  "max_pair_distance_px": 12.0,
  "max_path_steps": 12,
  "max_new_connector_pixels": 12,
  "max_bridges": 32,
  "max_endpoint_pairs": 512,
  "max_label_lab_distance": 12.0,
  "min_facing_cosine": 0.75,
  "max_endpoint_width_ratio": 2.5,
  "radius_floor_px": 0.5,
  "corridor_radius_px": 1.5,
  "background_flank_min_px": 1.5,
  "background_flank_max_px": 3.5,
  "background_min_samples": 3,
  "min_fg_bg_lab_contrast": 15.0,
  "min_mixture_fraction": 0.15,
  "max_mixture_residual_lab": 8.0,
  "min_mean_mixture_fraction": 0.35,
  "common_gap_label_required": true,
  "original_adjacent_pair_forbidden": true
}
```

## Controls, evidence and failure interpretation

Abstract tests cover a source-visible connector missing from labels, an intentional source-blank gap, parallel offset features, an already adjacent tonal partition, determinism/input immutability, pair-budget truncation and convex mixture bounds. They verify implementation behavior, not generalization. Same-color structures can still be falsely joined when the source evidence is ambiguous; these gates are not a semantic guarantee.

Each accepted edit logs endpoints, source labels/common gap, route coordinates, changed connector pixels, cost, prototypes, mixture support and residual. Evidence arrays include connector mask and endpoint coordinates. These are diagnostic source hypotheses, never hidden raster content in exported SVG. No new region is inserted, no pixel-rectangle fallback is exported, and no independent stroke representation or global detail increase is introduced.

The intervention merges region identities and can remove an originally meaningful separation. One-pixel connector ownership can distort thin width/area. A region-level mean can poorly describe gradients, and fixed foreground/background gates may reject real features. A fragmented singleton has no useful skeleton tangent and may remain unrepairable. Shield's missing internal bands may have no endpoint pair and therefore remain unchanged. Unmodified F_A may still collapse a repaired thin face. Report raw connectivity/area, final geometry safety and appearance-independent component review separately; do not call lower component counts alone a success.

Source annotations, crown templates and known truth must never be read by this constructor. All four benchmark cases use the same defaults without retuning. Negative results are preserved; no-proposal is an explicit result rather than permission to broaden the method.
