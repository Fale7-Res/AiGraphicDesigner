<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-25T15:03:37Z"}
END_DOC_PROVENANCE -->
# Historical baseline scope

Original V04 and Image-Guided Repair are freshly **rendered from exact saved SVGs** at the native source PNG dimensions with Inkscape. This does not rerun their tracing engines and does not measure their generation time. Both the SVGs and source PNGs are included in the isolated package.

The twelve source PNGs are RGB, without ICC profiles or alpha channels. For this suite, pixel values are assumed sRGB; no resampling or profile conversion occurs. Transparent SVG backgrounds are composited on white through the shared historical evaluator. This is not an alpha-preservation validation on arbitrary images.

Per-SVG records contain source/SVG SHA256, native dimensions, SSIM, PSNR, 1.5px-tolerance edge precision/recall/F1, RGB errors, mean/p95 DeltaE76, sigma1 high-pass error, actual SVG commands/elements/bytes, renderer time, parent CPU, child renderer CPU and separate parent/child memory high-water. Memory is measured in a fresh worker for each SVG and is not a simultaneous tree-RSS peak.

## Compared recent evidence

For A01, A03, A05 and A10, both Coherent Details representations and the colored-radial RGB4 representation are freshly rerendered. A03 additionally includes Automatic Geometry No-Merge. These are automatic reconstructions; the manually assisted Oracle and hand-authored shield are not mixed into the automatic benchmark. The best SSIM among these recent candidates is an image-specific historical result, not a common preset.

Historical source locations before isolated copying:

- Original: `repo_readonly/versions/version-04-claude-challenger/experiments/outputs/<case>_v04.svg`
- Repair: `repo_readonly/versions/version-04-image-guided-repair/versions/version-04-claude-challenger/experiments/outputs/<case>_v04.svg`
- Recent coherent: `experiments/EXP_COHERENT_DETAILS_20261023/results/<case>/{contour_80,stroke_80}.svg`
- Recent RGB4: `experiments/EXP_REPRESENTATION_20261023/results/<case>/rgb4.svg`
- No-Merge: `experiments/EXP_AUTO_GEOMETRY_20261021/results_no_merge_diagnostic/A03_burger_layers/artwork.svg`

There are no recent four-image-experiment outputs for the other eight benchmark cases. No recent values are extrapolated to those cases. The full Original and Repair twelve-image results remain available.

## Reproduce

```bash
python src/baselines.py --output reproduction_baselines
```

Use a fresh destination to preserve supplied evidence. `results_baselines/summary.json` is the complete machine-readable table; each case/condition also has `render.png` and `metrics.json`. Actual geometric counts matter: zero cubic segments in Original V04 does not mean zero complexity, because its rectangles and linear pixel-run paths carry substantial geometry.

## Metric correction

QA found the first baseline implementation used sigma2 high-pass filtering while VTracer search used sigma1. All baseline metrics were recomputed from the unchanged saved PNGs using the same `search.extra_metrics` function. The initial sigma2 summary is retained in `reports/initial_baseline_sigma2_summary.json` as superseded evidence; it must not be compared to VTracer sigma1. No native SVG/PNG was changed for this correction.

## Fresh native-render results

| Case | Original V04 SSIM | Repair SSIM | Best tested recent automatic SSIM | Recent condition |
|---|---:|---:|---:|---|
| A01_shield | 0.915149 | 0.829029 | 0.8455122429834949 | coherent_stroke_80 |
| A02_falafel | 0.871995 | 0.686968 | not available | not available |
| A03_burger_layers | 0.890625 | 0.699763 | 0.6880516290212012 | automatic_no_merge |
| A04_fries_shadows | 0.856548 | 0.747365 | not available | not available |
| A05_orange_juice_transparency | 0.881095 | 0.780994 | 0.7872339686628124 | coherent_contour_80 |
| A06_tomatoes_organic | 0.861581 | 0.643676 | not available | not available |
| A07_wrapped_sandwich_occlusion | 0.884710 | 0.717183 | not available | not available |
| A08_latte_texture | 0.873129 | 0.770361 | not available | not available |
| A09_arabic_calligraphy | 0.882637 | 0.802258 | not available | not available |
| A10_restaurant_logo | 0.892019 | 0.793323 | 0.8546927190231189 | coherent_stroke_80 |
| A11_chocolate_cake_texture | 0.884942 | 0.700171 | not available | not available |
| A12_ramadan_ad_composition | 0.903041 | 0.646390 | not available | not available |
