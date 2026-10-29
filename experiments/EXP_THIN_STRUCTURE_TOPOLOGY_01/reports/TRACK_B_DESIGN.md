<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T11:43:19Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T11:43:19Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T11:43:19Z"}
END_DOC_PROVENANCE -->
# Track B — frozen short-chain initialization guard

Research scope only. Global architecture `NOT_APPROVED`; no complete topology, clean-vector, fidelity or semantic-editability claim.

## Hypothesis and intervention

The inherited matrix demonstrated a concrete failure: two raw unit-L chains enclosing a valid nonzero region can both become the same diagonal. Track B tests only whether this particular destruction can be prevented without changing labels, canonical chains, shared references or endpoints. It does not repair missing segmentation, invalid raw face walks, arbitrary narrow contours or all sharp corners.

`initialize_safe(graph, config=None) -> (graph, audit)` receives normalized geometry only. It receives no source image, annotation, foreground truth, appearance or per-image setting. Historical saved S_A_F_A common-face graphs are the inputs; they are not refitted externally.

Eligibility is frozen: exactly three raw vertices comprising two orthogonal unit crack edges; open chain; inherited fitted paint-independent geometry collapsed onto its endpoint chord within1e-8px; original endpoints already pinned; participation in a raw-valid ring with absolute raw area>1e-6 and absolute fitted area<=1e-6. Existing invalid raw rings are explicitly unresolved; they are not made valid.

The sole proposal is a single cubic `[A,B,B,C]`, where A/B/C are the existing raw start/bend/end. It stays within the raw control triangle and retains A/C exactly. It rounds a canonical unit-L bend by approximately0.177px corner distance: this is not exact preservation of an intentionally sharp corner. No straight raw-L replacement, pixel-grid polyline, box, new cell, new region, chain insertion or alternate fitting family is attempted.

## Exact uniform configuration

```
model = single_cubic_A_B_B_C
area_epsilon = 0.000001
min_repaired_area_ratio = 0.1
endpoint_gap_max = 0.001
flatten_bound = 0.01
near_pair_distance = 0.02
collinear_chord_tolerance = 0.00000001
max_eligible_chains = 256
max_passes = 2
max_chain_proposals = 512
max_wall_seconds = 540
```

No caller tuning is accepted: a non-null config must equal the frozen dictionary. The external worker cap remains600seconds/4096MiB; total experimental budget is parent controlled. Eligible chains are processed by ascending canonical ID. Beyond-budget candidates remain unchanged and are disclosed.

## Validation and rollback

Chains sharing incident face loops form coupled components, evaluated together. Each component has one deterministic proposal. At most two passes allow previously rejected components to be reconsidered only after other accepted components changed their neighborhood; there is no parameter search.

Affected rings must have valid raw contours, retain raw winding, remain nonzero and valid under the inherited numerical checks, and maintain endpoint closure. Repaired rings must retain at least10% of raw signed-area magnitude. All loop-containment/disjoint relationships within affected faces are compared with the raw valid arrangement; invalid raw neighborhoods cause rejection. Changed chains must be simple and stay inside the frame.

Adaptive control-hull flattening at0.01px and Shapely predicates check changed chains against all spatially neighboring unchanged chains. New crossing/overlap/unexpected-touch *pair identities* cause rollback; checking counts alone would conceal exchanged defects. A disjoint pair within0.02px is unresolved and causes rollback. Exact shared endpoints are permitted. Existing unrelated defects are retained, not converted into a global pass.

Rejected components keep their inherited geometry byte-for-byte in the output object. Accepted edits modify only `segments`; raw chains, IDs, adjacent labels, closed flags, face references, incidence and metadata remain unchanged. Every unrepaired collapse, invalid raw ring and budget omission is reported. The output status is always bounded local correction with the global gate uncertified; the parent must run independent full diagnostics.

## Code reuse and scientific limits

The module imports the earlier repository-authored geometry_eval flattening/ring helpers. It loads only the pure existing segment_area function definition from exact_area_check using the Python AST, because importing that historical script would rerun its full saved-evidence evaluation. Historical source is unchanged and no Arena code is copied.

Validation is numerical rather than a certified continuous Bézier arrangement proof. Same labels mean upstream fragmentation and missing components persist. Region area recovery may leave width, source alignment and complete visual fidelity poor. Unit-sized source faces remain unit-sized source faces: rounding their outlines must not be marketed as coherent artwork or as proof that pixel-mosaic dependence has disappeared. Existing anti-mosaic and owner-review gates remain unchanged.

## Abstract harness controls

Four independent, image-free controls passed: paired unit-L area recovery with a nested hole; a shared T-junction with unchanged endpoints/references; a new neighboring collision rejected with exact rollback; and a nonunit collapse deliberately unrepaired with no grid fallback. These test infrastructure behavior, not benchmark generalization. No benchmark was run by this agent before parent protocol freeze.
