<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T09:01:44Z", "last_action": "EDITED", "last_change_id": "ADAPTIVE-DELIVERY", "last_edited_at_utc": "2026-10-27T09:03:13Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T09:01:44Z"}
END_DOC_PROVENANCE -->
# Adaptive fidelity findings

Architecture remains NOT_APPROVED. The chosen extension addresses a measured search-domain gap: high-detail Watershed retains lowcontrast transitions lost by the old Color clustering finalists. It reuses the same native Inkscape evaluator, score and original dimensions. No AI model, residual patches, embedded image or raster filter was added.

## Evidence

All18 inputs completed:12 historical,4 deterministic diagnostics and2 real new inputs (NASA astronaut and CC0 brick, at native512×512). Historical12 mean SSIM0.9975977, PSNR54.3307dB, edgeF1.998344, DeltaE76.205738. Previous selectedVTracer recorded mean.9868562/45.0016dB. OriginalV04 recorded mean.8831/28.04dB; repairedV04.7348/21.76dB. Those older engines were not regenerated in this run. An independent oldBurger finalist rerun produced byte-identical SVG/PNG; see reproduction_A03.json.

Shield improves from recorded.956706/24.4099dB to.995660/51.5571dB, restoring broadshadow/background tones. Burger improves.978246/37.6508 to.997838/54.3560. Calligraphy improves.9727/40.175 to.996105/52.1150. Actual native comparisons are linked from index.html; top-five candidates and50%overlay remain reviewable.

Newreal2 meanSSIM.999273. This is small transfer evidence, not universal tracing or a learned predictor. The current input itself is the optimization reference, as intended. Synthetic4 meanSSIM.999390; exactmatches have null/infinitePSNR and are excluded from finitePSNR averages. Alpha diagnostic is explicitly whitecomposited, not transparency preservation.

## What changed

13 diversepilots coverColor/Watershed/Binary andpixel/polygon/spline; applicable fields canonicalized; family-leader coordinate probes and budget/stagnation stops replace old largely inactive pixel-simplification probes. Highdetail512Watershed was absent from old pilots128/256. Perimage configs/history/failures, realSVG/renders, CPU/wall/peakmemory and fullcommands are retained. Ranking is fixed multimetric without complexitypenalty.

## Negative results and limitations

Spline/polygon andBinary candidates often lose texture or color, retained transparently in rankings. Two globally stagnant rounds can stop before latecurve/precision controls: bounded search does not establish globaloptimum. Palette/max_colors remain unsupported by this search despite availableengine controls. Broad tonal failure improved without segmentation, so no localAI is justified for this specific gap.

Dense pixel-lattice paths remain. This is genuineSVG but not cleanprofessional artwork; highnative similarity does not establish smoothzoom behavior or semantic ownership. Numeric edgeF1 is tolerant and fine-detailRMSE is not sesame detection or ArabicOCR. TransparentSVG, arbitraryICC/HDR/largeimages/nativeWindows remain unvalidated. File corruption caused by transient storage is repaired only by rerendering unchangedSVG with hashes/metricchecks recorded; it is not a new algorithm.

## Acceptance and next priority

Proposed gates: allopaque benchmark and transfercases SSIM>=.99,PSNR>=40dB,edgeF1>=.98 where meaningful,DeltaE76<=1; no raster/filtershortcut; no criticalnativevisual loss. Metrics alone cannot approve. Owner should inspect shieldshadow, bunseeds, Arabicstrokes and newphotos via index.html before accepting fidelity. Transparency prevents claiming arbitrary-input milestone completion. Next bounded technical experiment should implement and evaluate alpha-preserving color/compositing on multiple backgrounds, before cleanvector cleanup. Do not repeat indefinite colorrefit iterations.

## Complete owner vision retained

Fidelity is the current enabler only. CleanSVG grouping and geometry remain later requirements. MagicLayers needs semantic ownership, occlusion and layerrecomposition tests; plannedgeneration needs preview/layerconsistency; semanticediting needs editlocality tests; Arabic typography needs shaping, fontidentity and unseenwordediting evidence. None is delivered by these path-heavy SVGs. No productionarchitecture winner is declared.

## Recovery and Git

Latestremote verified4ba5ed56df11001b0e3050383883e7107003751a. Workspace maintenance removed prioruncommitted adaptive work; this directory is reconstructed code with fresh evidence, not recovered prioroutputs. Historicalfiles unchanged. GitCLI lacks HTTPScredentials; GitHubconnector write returned403 Resource not accessible by integration. No successfulpush is claimed. PortableZIP is the integrationfallback.
