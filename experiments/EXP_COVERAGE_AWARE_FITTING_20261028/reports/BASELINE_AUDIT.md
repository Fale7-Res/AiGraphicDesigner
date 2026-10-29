<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-28T05:38:04Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-28T05:38:04Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-28T05:38:04Z"}
END_DOC_PROVENANCE -->
# Inherited appearance fitter: precise baseline audit

Read complete source: `experiments/EXP_GEOMETRY_APPEARANCE_ABLATION_01/fit_appearance.py`, SHA256 `3ae12b40fb67746e393745fac5340429a05d9be69129bbbf3e362b887b7e528f`. Audit time 2026-10-28T05:17:20+00:00. This report records saved evidence; no prior fitting or rendering was repeated. Global architecture **NOT_APPROVED**.

## Actual inherited algorithm and line references

- `_paths`, lines57–67, collects visible SVG paths with accumulated affine transforms, skipping defs/masks/clip paths. It preserves paint order but provides no per-pixel continuous coverage matrix or overlap mixture.
- `_ownership`, lines70–106, replaces each path paint with a unique pseudo-random RGB integer ID (codes line76, paint override77–82), forces path opacity/fill-opacity1, and renders once using the actual renderer85–86. Exact RGB code plus exact alpha255 is required at line97. Four-neighbor same-label consensus100–102 then rejects a one-pixel local boundary band; viewport border is also rejected103–105. This is a four-neighbor erosion-style consensus, not an analytic geometric inside test. An antialiased source-over mixture generally does not equal either ID, so valid visible edge observations are deliberately discarded. Topmost opaque ownership loses contributions from covered lower paths and cannot identify translucent source-over mixtures.
- `fit_svg`, lines249–338, accepts image-aligned fixed geometry and rejects mask/clipPath/image/filter nodes, inherited style/clip/mask/filter attributes, nonunit opacity/fill-opacity, and visible strokes. Exact references: mask/content rejection lines269–270; attribute rejection271–273; opacity274–276; stroke277–278. Final alpha application belongs to its caller. It is an unmasked opaque-RGB fitting contract, not RGBA inverse rendering.
- Source alpha is read at280. Zero-alpha labels are removed283. Samples are collected only from nonnegative surviving ownership labels284–288. For each region it fits source unassociated RGB at the chosen pixel centers302–303 with **source-alpha-squared weights**304. This weighting is equivalent to a fixed-alpha RGB residual scaling under the relevant assumptions; it does not render the actual current geometry/paint composition, model alpha/coverage error, or solve inter-path source-over coupling.
- Periodic split `(x+3*y)%5` at305–306 allocates train3/5, selection1/5, test1/5. These are disjoint pixels testing interpolation, not independent blocks. Train is capped512 samples312; selection and test256 each317–318. No train sample is an antialiased rejected boundary pixel.
- No-interior/deadline branch292–300 keeps the inherited flat fill. Non-flat URL fallback would raise `Unsupported baseline flat fill`296–298. Initial synthetic geometry must therefore use ordinary dummy flat fills even when source truth uses gradients. No train samples uses all region interior as train307–311; no selection samples retains a flat mean313–315. These fallbacks are disclosed by reason fields, not evidence that those regions were optimized.
- `_fit_region`, lines130–220: flat fit is weighted least squares; gradient candidates require >=16 train, >=6 selection, and sufficient flat selection error (line167). Linear/radial families have2/3/4 equally spaced stops; at most100 evaluations (143–145) and deterministic search. Final family selection uses disjoint selection samples with an absolute0.0625 / relative1% improvement margin208–213. Test pixels only populate diagnostics214–219. Stop colors are clipped unconstrained least-squares coefficients (162–164), not a constrained optimum. Radial radius follows visible sample extent155–158, so membership in the broad radial SVG family does not imply its continuous parameterization can exactly recover every radial fixture.
- `_paint`, lines223–246, exports gradients in actual SVG with inverse accumulated geometry transforms. `fit_svg` copies the same root geometry into C/D324–329; it does not move curves. Its own documented limitations are repeated in diagnostics330–336. Every final quality claim must still use the full SVG render.

## Saved 192-level real-case diagnostics

Source is each immutable `EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/<case>/192/fitting.json`. Counts are extracted from saved records, not inferred from visual inspection. Interior fraction denominator is full tested viewport, so transparent backgrounds count in the denominator; it is not visible-area coverage. `<=5` includes zero; insufficient-selection counts are additional disclosed reasons. Flat counts include selected-flat models and fallback models.

| Case | Paths | Zero interior | Interior <=5 | Insufficient selection | Surviving interior samples | Fraction of viewport | Flat/linear/radial |
|---|---:|---:|---:|---:|---:|---:|---|
| A01_shield | 188 | 86 | 100 | 13 | 73092 | 79.55% | 123/42/23 |
| G01_coffee | 167 | 19 | 29 | 7 | 48543 | 71.22% | 54/63/50 |
| G05_chelsea_nativecrop | 184 | 5 | 6 | 1 | 43576 | 66.49% | 29/92/63 |
| G06_arabic | 176 | 175 | 175 | 0 | 17924 | 26.67% | 176/0/0 |
| G08_dice_alpha | 185 | 50 | 56 | 3 | 14988 | 19.52% | 107/42/36 |

Across these five saved cases, 335 of 900 regions have zero surviving interior samples. This count is dominated by Arabic175/176, where zero-alpha exclusion also removes many paths in invisible background space. It would be incorrect to interpret every zero-interior path as a visible thin feature or to attribute every failure to erosion alone. Shield86/188 zero-interior regions show that hard ownership/consensus materially restricts fitting even outside that transparent-background example. Shape granularity, visibility, alpha, occlusion, sample erosion and true regional scale remain confounded unless inspected separately.

## What this establishes and does not establish

The old loop optimizes regional interior observations while the decisive final render includes partial coverages, shared-edge antialiasing, source-over order, fixed masks and overlaps. This objective mismatch is a plausible bottleneck, supported by implementation and saved sample attrition. It is not yet proof that coverage-aware fitting closes the fidelity gap, nor that geometry is adequate.

For new known controls the old baseline adapter must strip masks and path/group opacity only from a temporary RGB fitting input; the final old/new conditions must restore identical original mask and opacity. It must preserve geometry/order/fill-rule and disclose that old ownership still treats regions as opaque. A translucent source composite is not a region's true unassociated paint color; fitting it independently and restoring opacity can apply mixing twice. Do not silently compare an opaque baseline with a masked proposed method, or call baseline-adapter restrictions a new method's success.

The new analytic controls retain compact true geometry, known paint family, subpixel colored regions, shared curves, sharp corners, holes, local edge highlights and known opacity/mask mixtures. A fixed true-geometry paint oracle tests representation/renderer reachability independently of optimization. Existing K01/K02 analytic references are reused by hash; no tracing or new reference rendering is needed. Synthetic controls are targeted causal diagnostics, not substitutes for the five saved real-image cases or proof of generalization.

## Frozen saved-diagnostic references

```json
[
  {
    "case": "A01_shield",
    "paths": 188,
    "zero_interior": 86,
    "interior_le5": 100,
    "insufficient_selection": 13,
    "interior_samples": 73092,
    "viewport_pixels": 91881,
    "interior_fraction": 0.7955072321807556,
    "flat": 123,
    "linear": 42,
    "radial": 23,
    "diagnostic_relative": "experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/A01_shield/192/fitting.json",
    "diagnostic_sha256": "62ce9e993d2053a640f613158e691a53fde4ba7a367cdd68334576d839dd02e8"
  },
  {
    "case": "G01_coffee",
    "paths": 167,
    "zero_interior": 19,
    "interior_le5": 29,
    "insufficient_selection": 7,
    "interior_samples": 48543,
    "viewport_pixels": 68160,
    "interior_fraction": 0.7121919014084507,
    "flat": 54,
    "linear": 63,
    "radial": 50,
    "diagnostic_relative": "experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/G01_coffee/192/fitting.json",
    "diagnostic_sha256": "40935ba4f49b52fafa6cf0fcd049c278bf068265fddc032432532d85b2eef4dd"
  },
  {
    "case": "G05_chelsea_nativecrop",
    "paths": 184,
    "zero_interior": 5,
    "interior_le5": 6,
    "insufficient_selection": 1,
    "interior_samples": 43576,
    "viewport_pixels": 65536,
    "interior_fraction": 0.6649169921875,
    "flat": 29,
    "linear": 92,
    "radial": 63,
    "diagnostic_relative": "experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/G05_chelsea_nativecrop/192/fitting.json",
    "diagnostic_sha256": "f6ebe064c60199bcaefd51df447ff98b236e7e6b156acdde05ec7df229b45c0c"
  },
  {
    "case": "G06_arabic",
    "paths": 176,
    "zero_interior": 175,
    "interior_le5": 175,
    "insufficient_selection": 0,
    "interior_samples": 17924,
    "viewport_pixels": 67200,
    "interior_fraction": 0.26672619047619045,
    "flat": 176,
    "linear": 0,
    "radial": 0,
    "diagnostic_relative": "experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/G06_arabic/192/fitting.json",
    "diagnostic_sha256": "bbdb9169ffe7f47fd9e44d8a6ec076cffca4a2a0836e8bb058d8370640c998c6"
  },
  {
    "case": "G08_dice_alpha",
    "paths": 185,
    "zero_interior": 50,
    "interior_le5": 56,
    "insufficient_selection": 3,
    "interior_samples": 14988,
    "viewport_pixels": 76800,
    "interior_fraction": 0.19515625,
    "flat": 107,
    "linear": 42,
    "radial": 36,
    "diagnostic_relative": "experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/G08_dice_alpha/192/fitting.json",
    "diagnostic_sha256": "72ff500bfec3bcb38eda84cec93658f09da5f210ad97dabe5b50dbb8aa788bf2"
  }
]
```
