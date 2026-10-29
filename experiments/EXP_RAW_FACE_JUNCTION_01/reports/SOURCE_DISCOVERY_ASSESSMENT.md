<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T12:20:20Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T12:20:20Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T12:20:20Z"}
END_DOC_PROVENANCE -->
# Separate source-driven discovery feasibility assessment

Architecture NOT_APPROVED; geometry NOT_ACCEPTED. This is an independent assessment, not a replacement geometry engine or appearance experiment.

## What the inherited negative result establishes

The complete owner vision was read. Image generation, professional editable SVG, typography including Arabic, semantic organization, Magic Layers and visual QA remain authoritative future requirements.

The preceding thin study's `track_a.py` is an endpoint reconnection operator, not general discovery: skeleton degree-one endpoints must have a usable three-step tangent, compatible whole-label mean Lab, a shared gap label, and a supported short path. Isolated missing marks, a completely absent crown band, a merged material interface, and singleton fragments have no suitable proposal interface. The report verifies zero accepted fine-feature bridges, zero Arabic bridges and three Shield bridges outside the crown. Lowering color thresholds would not remove the central representational limitation.

`track_b.py` starts from existing chains and faces. It cannot propose absent boundaries either. Raw-face repair and discovery must therefore remain separate hypotheses. Improving face validity can enable trustworthy refinement, but cannot create information that was discarded before assembly.

## Comparison and ranking for the next discovery question

| Method | Information and benefit | Principal limitation | Feasibility and judgment |
|---|---|---|---|
| Multiscale color-boundary evidence with subpixel localization | Source RGB/Lab gradients can identify transitions even where existing labels merge them. Linked subpixel points can avoid literal staircase output. | Illumination and texture also produce edges; weak or blurred contours may be absent. Edge chains do not imply closed faces or physical material boundaries. | Highest immediate information gain. Existing scikit-image can test source evidence; mature Canny/Devernay is a later controlled subpixel baseline. |
| Signed ridges/valleys with width and paired-boundary support | Responses can identify thin structures without requiring an existing component endpoint. Centerlines are a better candidate representation for some narrow artwork. | A ridge is not two recovered contours or an exact width. Metallic highlights and shadows can look like structure. Junction response and variable-width behavior need independent tests. | Complementary evidence probe now; width/junction-aware construction needs a separately approved study. |
| Marker/region-driven segmentation followed by shared graph construction | Region ownership supplies adjacency and enclosed regions, allowing consistent common edges. Color helps detect internal subdivisions. | Marker placement decides whether missing regions can be born. Watershed can oversegment shading or lose shallow boundaries. Random walker cannot invent an unseeded phase automatically. | Viable later hybrid, but rerunning global segmentation now confounds the fixed-label raw-face question. |
| Existing pixel-equivalent SVG as the main discovery source | Contains detailed appearance transitions and can help audit the visual ceiling. | It adds no independent signal over the original sampled image; cell adjacency largely reconstructs the same lattice, gradients and noise. Parsing tiny paths adds cost and topology ambiguities. | Retain as visual ceiling, not primary geometry evidence. |
| Exact/shared planar arrangement of candidate curves | Separates incidence topology from curve embedding; can consistently split intersections and track faces. | It will faithfully arrange incorrect/missing input boundaries too. Exact numerical predicates do not decide semantic correctness or whether an edge is shading. | Important eventual assembly tool, not a boundary detector. CGAL evaluation would introduce C++/license/integration work beyond a tiny evidence probe. |
| Joint differentiable rendering | Later image feedback can move geometry toward an appearance objective. | Missing topology, ownership and texture can still be wrong; photometric objectives may reward microgeometry. Adds optimization variables before useful missing-boundary evidence has been isolated. | Defer for this geometry-only question. No neural or hosted dependency is justified. |

The strongest prospective combination is source multiscale boundary evidence plus complementary ridge/width evidence, then conservative region birth/splitting or explicit strokes and a validated shared graph. That is an engineering hypothesis, not an approved full implementation. Photographs will require ambiguity labels and detail/appearance reasoning; logos and lettering provide a more decisive first geometry test.

## One bounded evidence-only probe proposed for protocol freeze

Hypothesis: some important support omitted by frozen segmentation remains detectable in the original source independently of endpoint availability. The test is whether admissible evidence exists, not whether complete geometry has been reconstructed.

Construction inputs: the four frozen working RGB images only. No case name, labels, annotations, crop ROIs or known geometry are supplied to the evidence extractor. Native dimensions; no resize or source enhancement.

Fixed operators:

1. Convert RGB/255 to Lab using the installed scikit-image version. Normalize channels as L/100, a/128, b/128.
2. On each channel run Canny at sigma 0.6 and 1.2, low threshold .04, high threshold .10, `use_quantiles=False`, `mode='reflect'`. Per-scale union over channels. Persistent support means a source-edge location is within Euclidean 1px of the other scale's union. Keep each original map and the persistence map; do not synthesize connecting paths.
3. Separately compute Sato ridge responses on L/100, sigma .7, 1.2, 2, both polarities. Preserve float responses and per-polarity maximum. Do not choose a segmentation threshold from benchmark results. If visually normalized, save the exact scale factor and label it display-only, not calibrated confidence.

Budget: four images, one fixed setting, maximum 90 wall seconds and 1024MiB sampled memory per source. No candidate geometry, label modifications, curve fitting, segmentation search, or endpoint threshold retuning. No paid APIs or new dependencies. Dense maps above 15% support trigger a clutter warning, not post-hoc threshold adjustment. Abort a failing operator branch rather than substituting another method or increasing the budget.

Outputs: source hashes, frozen operator config/version, float/binary NPZ maps, source edge/ridge overlays, timestamps, measured runtime and sampled memory, density and raw source evidence counts. Main study supplies actual geometry SVGs; these probe maps must not be exported or advertised as reconstructed artwork.

Only after construction is frozen may a separate evaluator compare the evidence to original crack boundaries: measure persistent source support farther than 2px from existing raw boundaries, show the entire image plus inherited crown/Arabic/fine-feature review areas, and preserve unsupported/misleading texture examples. This is a missing-evidence diagnostic, not precision/recall against objective structure. High counts may reflect lighting or noise; zero counts may reflect unsuitable scale/contrast, not absence of structure. Any known-vector reference comparison is evaluation-only and must use the inherited uncertainty labels.

Decision rule: coherent source evidence near a missing feature supports a later targeted region-birth/stroke-discovery experiment; it does not justify a reconstruction acceptance claim. Evidence too fragmented or dominated by shading means this simple detector is insufficient and requires a new hypothesis. Do not tune until a crown appears. No claim of false-positive rate, correct physical contour classification, complete crown recovery, or independent Arabic outline fidelity can be made from this probe.

## Primary sources checked

- Canny operator, scales and thresholds: https://scikit-image.org/docs/stable/api/skimage.feature.html
- Ridge operators and their Hessian-based purpose: https://scikit-image.org/docs/stable/api/skimage.filters.html and https://scikit-image.org/docs/0.25.x/auto_examples/edges/plot_ridge_filter.html
- Marching-squares subpixel interpolation and explicit connectivity choice: https://scikit-image.org/docs/stable/api/skimage.measure.html
- Marker-controlled watershed and random walker: https://scikit-image.org/docs/stable/api/skimage.segmentation
- scikit-image BSD-3-Clause distribution terms: https://scikit-image.org/docs/stable/license.html
- Canny/Devernay peer-reviewed implementation produces chained subpixel edge points; its provided source is AGPL-3.0-or-later, so do not silently copy into product code: https://www.ipol.im/pub/art/2017/216/
- Arrangement topology/geometry separation and DCEL concepts: https://cgal.geometryfactory.com/CGAL/doc/main/Arrangement_on_surface_2/index.html

Published subpixel localization performance is not an accuracy guarantee on these source images. The probe initially uses existing pixel Canny maps and ridge responses; it does not claim to implement or validate the Devernay method. A later subpixel baseline must test coordinate convention, blur/noise assumptions and corners independently.
