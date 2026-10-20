<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:59:14Z", "last_action": "CREATED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:59:14Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:59:14Z"}
END_DOC_PROVENANCE -->
# Version 04 — Image-Guided Repair Experiment Log

## Run sequence

1. The supplied reference image was translated into five criteria: coherent grouped appearance, true gradients, separated blur where recoverable, smoother outer contours, and fidelity without pixel-tile artifacts.
2. The previous V04 rectangular surface tessellation and source-derived Canny pixel-run stencil were reviewed and rejected as the final output representation because they followed the raster's pixel grid and produced thousands of micro-paths.
3. The current repair added boundary-aware SLIC region segmentation and merging, local multi-stop gradients, exact shared internal pixel-cell borders, and a coarse GrabCut foreground/background silhouette represented with simplified cubic paths and complementary clip paths.
4. A known synthetic 320×240 nested-shield fixture was created first and rasterized. It scored 25.00 dB PSNR, 0.9349 SSIM and 0.872 edge F1. The shadow is baked into the synthetic source, so this experiment does not prove shadow-layer recovery.
5. The full 12-image benchmark compares the committed V01 SVGs against the selected current V04 configuration at input-native dimensions using Inkscape. The complete saved rows are in `metrics/benchmark_results.csv/json` and aggregate metrics in `metrics/summary.json`.
6. Higher region budgets / increased SLIC initialization were tested separately on selected images. Some increase edge detail materially, but higher complexity increased time and file size and a full high-detail pass did not complete within the execution window. These parameters were not mixed into the selected final 12-image table.
7. The final run was resumed with `--reuse-existing-renders`: for each image, V04 was regenerated and existing raster output reused only if the new SVG bytes matched exactly and the cached render had the expected native dimensions. Existing paired renderer times were retained only for image IDs that already had those timed measurements.
8. `src/verify_outputs.py` subsequently regenerated all 12 SVGs byte-identically and confirmed XML validity, no embedded/external raster resources, valid output dimensions, and a composite silhouette clip for each file. All four unit tests pass.

## Final default summary

- Mean PSNR: 18.02 dB (V01) → 21.76 dB (V04), V04 improves 12/12.
- Mean SSIM: 0.5988 → 0.7348, V04 improves 12/12.
- Mean edge F1: 0.7556 → 0.7439, V04 improves only 5/12 and regresses on 7/12.
- Mean edge recall: 0.8392 → 0.6937, V04 regresses on 11/12. This remains a significant detail-preservation weakness.
- Mean SVG size: 590.1 KiB → 494.4 KiB; average path count rises 633 → 744.5 because surface regions are duplicated under complementary clip groups.
- Mean generation ~1.75 s/image; mean Inkscape render timings ~295 ms V04 / 270 ms V01; sampled process RSS about 181 MiB.

## Conclusion

This iteration addresses the blocky-tile artifact, source-edge pixel micro-paths, visible cracks from independent smoothing, and simple flat color islands by using genuine SVG gradients and shared internal geometry. It does not yet satisfy the image's full ask for independently editable base/shadow/highlight/blur sublayers for every semantic object. The lower edge recall/F1 in several images is an explicit remaining regression. See the detailed per-image comparison in `metrics/RESULTS_REPORT.md`.

## Scope integrity

No implementation or experimental record in Versions 01–03 was changed. The owner vision and global architecture approval status were not modified. Only V04-scoped code/outputs and governance indexes required to register this experiment were changed.
