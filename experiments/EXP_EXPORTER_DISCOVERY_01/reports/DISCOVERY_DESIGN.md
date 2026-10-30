<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T22:00:15Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T22:00:15Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T22:00:15Z"}
END_DOC_PROVENANCE -->
# Paired-flank source stroke discovery

Research hypothesis: a thin contrasting source structure may be absent from all inherited label regions but still have paired, compatible flanks. Source-only paired-flank evidence can propose continuous stroke geometry without requiring existing segmentation endpoints. This does not establish complete artwork reconstruction.

## Inputs and fixed construction

`discover(rgb)` accepts only native uint8 RGB. It receives no case identifier, segmentation labels, evaluator mask, crown annotation, reference curve, or ROI. The caller reuses the previously frozen white-composited working raster. Existing graph geometry is never modified.

The exact constants are in `discovery_strokes.CONFIG`, approved before implementation. Gaussian-smoothed Lab (sigma0.6) is evaluated at8undirected normals and flank distances1.5,2.5,4px using bilinear sampling. Both center–flank contrasts must exceed15Lab, flank disagreement must be<=12Lab, and the contrast vectors must have cosine>=0.9. This last test distinguishes a central excursion from a simple monotone transition. The score is minimum flank contrast divided by flank distance; it is not a calibrated probability of physical structure.

Directional nonmaximum suppression compares the selected score with score samples1px either side along the selected normal; ties are retained. Zhang skeletonization creates a source-support graph. Redundant diagonals are suppressed if an orthogonal intermediate support pixel exists. Maximal degree2 chains are traced between endpoints/junctions; closed loops are traced separately. Each undirected edge is visited once. Isolated source points are reported rather than converted into pixel shapes.

Each chain must be>=6px. Bilateral profiles sampled at0.25px through4.5px estimate the first half-contrast crossing on each side, linearly interpolated. Median measured chain width must be<=6px and is floored at0.5px for rendering only; the raw value remains logged. A chain with no bilateral width support is rejected.

OpenCV Douglas–Peucker epsilon0.35px reduces the native centerline. Piecewise cubic Hermite interpolation uses centered tangents except at turns>=60degrees, where independent one-sided tangents preserve the sharp corner. At most64cubic segments are allowed. Curves are sampled at32intervals/segment and the source polyline at<=0.25px intervals. Symmetric sampled nearest-neighbor deviation must be<=0.6px; otherwise reject the entire proposal. This is a sampled test, not a certified continuous Hausdorff bound. There is no pixel-polyline fallback.

Rank by median source score times length, then original chain identity; keep at most128proposals. Rejected chains and reasons are preserved, including budget rejection. Output is genuine SVG cubic stroke geometry with constant chain width, not an image, raster underlay, or source-grid rectangle mosaic. Coordinates remain native raster-derived sample centers; this implementation does not claim fully subpixel-localized centerlines.

## Independence, safety and boundaries

Proposals remain separate stroke objects and are not integrated into the inherited region graph. Consequently they cannot delete existing faces, alter its holes or source segmentation, or prove repaired region topology. Crossings between proposals and graph boundaries must be measured by the evaluator and remain unresolved unless independently justified. No fitted appearance is produced; uniform blue is a geometry-only diagnostic style.

This method can propose a previously absent thin stroke, a narrow internal band, or a loop. It cannot discover a broad missing crown region. Variable-width strokes are only approximated by a median width. Junctions may be fragmented by normal changes or NMS, and the six-pixel minimum rejects short significant ornamentation. Paired flanks can also occur in a metallic highlight, shadow, texture, or reflection. Such source-supported proposals must not automatically be called physical or structural contours.

## Rejected alternatives for this bounded test

- More permissive endpoint-joining thresholds cannot discover wholly absent structures and repeat the failed hypothesis.
- Unfiltered Canny tracing represents individual transitions, including abundant lighting/texture, without paired-width evidence; prior Shield probe already demonstrated this ambiguity.
- Luminance-only Sato ridges miss chromatic structures and still require converting a heatmap into actual curves. We use Lab profiles and output explicit strokes, while retaining ridge-class ambiguity.
- Global superpixel/region oversegmentation would change a second major variable and risk recreating many small cells.
- Neural segmentation adds weights, licenses, hardware and semantic priors without isolating the present thin-source-evidence hypothesis.
- A universal planar graph reconstruction or full variable-width stroke engine exceeds this experiment. Proposed strokes are deliberately unintegrated.

## Budget, tests, reproduction and interpretation

One configuration; four frozen source cases; max1million source pixels, externally monitored60s and512MiB per constructor. No parameter sweep or threshold relaxation after benchmark results. Synthetic tests cover no signal, a single non-stroke edge, a new source stroke without labels, determinism/input preservation, exact skeleton edge traversal, sharp-corner preservation, a closed skeleton loop, and invalid input. Initial synthetic tests found a scalar SciPy interpolation rank bug; it was corrected before any benchmark construction, without changing method or constants. Eight tests then passed.

CLI: `python discovery_strokes.py SOURCE_RGB NEW_DIRECTORY`. Directory creation refuses overwrite. Saved outputs: proposals.json containing accepted/rejected chains and configuration; proposals.svg containing accepted cubic strokes; evidence.npz containing source score, support, skeleton and selected normals. Root evaluation must add actual resvg rendering, source/reference-isolated metrics and comparison with the inherited baseline and failed endpoint method. Do not claim a crown or glyph recovered solely from additional source score support.

Primary implementation documentation: [scikit-image skeletonize](https://scikit-image.org/docs/stable/auto_examples/edges/plot_skeleton.html), [OpenCV4.13 approxPolyDP](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html). These mature primitives are reused; the paired-profile selection and bounded cubic proposal construction are first-party research hypotheses.
