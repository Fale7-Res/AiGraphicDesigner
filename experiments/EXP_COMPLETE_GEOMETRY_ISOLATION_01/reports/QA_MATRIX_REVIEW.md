<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:50:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Independent saved-matrix review — preliminary closure

Read common_geometry.py and saved matrix/graph-integrity evidence. No new engine fitting, segmentation, candidate selection or reconstruction was performed by QA.

## Independently verified

All twelve same-label pairs (six cases×two partitions) have identical input NPY SHA256 between initializers and exactly equal canonical raw unit-edge/adjacent-region dictionaries, with no duplicate unit edge. All twelve VTracer common-face graph exports use the identical Arena face references and exactly preserve native control-point coordinates, changing only segment order/orientation where required. This includes swapping cubic control points correctly on reversal. Normalization is a defensible evaluator-only isolation control, not a new fit.

Raw face ring decompositions still differ between native builders even when unit cracks and source-center filling agree. Therefore native-ring counts cannot directly isolate curve-fitting effects. Common-face metrics address that confound but inherit the chosen common face walk's flaws (e.g. invalid pinched raw rings); report both native and common-face diagnostics and do not treat the latter as a proof of a correct arrangement.

Native SVG closepath handling also matters: appending its implied closing segment in numerical measurement only for a genuinely native closed ring faithfully measures existing SVG semantics. It is not permission to pin/move open-chain endpoints or repair a candidate. Preserve preliminary measurements, name the corrected version and retain original candidate JSON/SVGs.

## Required measurement correction

The original raw region-center check uses RGB `(label*97%200+30,label*57%200+30,label*137%200+30)`. This repeats every200 labels. Shield has more than200regions, so equal colors do not prove equal region IDs. Reported zero wrong-color pixels are a useful but noninjective check. Use an injective24bit region encoding or direct face-membership label comparison before claiming exact region-ID recovery. This is an evaluator correction, requires no refit and should retain the original evidence.

## Visual and causal limits

Viewed actual saved4× Shield Arena/Arena and VTracer/VTracer SVG detail renders. Crown tips, central ornament/lobes and candidate band curves are present; extra/deformed boundaries remain. A claim that the entire crown or band is missing would overstate these visuals. A specific lower-band edge interval may be absent in a particular partition, but identify it through the frozen source-only reference and raw crack evidence, not aggregate scores alone. Approximate references cannot establish1px truth or unique semantic correspondence.

The earlier independently verified Arena signed-area degeneration remains a real initialization defect, but it does not predict VTracer automatically fixes it. Preliminary common-face metrics already show several partitions with substantial VTracer degeneration. Preserve that negative result and avoid declaring a mature fitter universally superior.

Final metric/known-control/visual-dashboard checks remain pending. Global architecture NOT_APPROVED.
