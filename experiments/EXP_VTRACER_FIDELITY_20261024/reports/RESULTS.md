<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-25T15:03:37Z"}
END_DOC_PROVENANCE -->
# VTracer fidelity search: measured results

These are native source-size SVG renders. Best means the highest fixed multi-metric score among the bounded tested candidates, not a global optimum. Pixel geometry remains eligible under the owner fidelity-first instruction; it is not clean scalable reconstruction.

| Image | Owner SSIM | Best spline SSIM | Best ranked SSIM | Best mode | Original V04 | Repaired V04 | Best recent internal |
|---|---:|---:|---:|---|---:|---:|---:|
| A01_shield | 0.9079 | 0.9120 | 0.9563 | pixel | 0.9151 | 0.8290 | 0.8455 (coherent_stroke_80) |
| A02_falafel | 0.9179 | 0.8860 | 0.9971 | pixel | 0.8720 | 0.6870 | not available |
| A03_burger_layers | 0.8928 | 0.9188 | 0.9780 | pixel | 0.8906 | 0.6998 | 0.6881 (automatic_no_merge) |
| A04_fries_shadows | 0.9383 | 0.9414 | 0.9927 | pixel | 0.8565 | 0.7474 | not available |
| A05_orange_juice_transparency | 0.9109 | 0.8899 | 0.9680 | pixel | 0.8811 | 0.7810 | 0.7872 (coherent_contour_80) |
| A06_tomatoes_organic | 0.8895 | 0.8919 | 0.9975 | pixel | 0.8616 | 0.6437 | not available |
| A07_wrapped_sandwich_occlusion | 0.9169 | 0.9631 | 0.9977 | pixel | 0.8847 | 0.7172 | not available |
| A08_latte_texture | 0.9371 | 0.9412 | 0.9860 | pixel | 0.8731 | 0.7704 | not available |
| A09_arabic_calligraphy | 0.8975 | 0.9037 | 0.9639 | pixel | 0.8826 | 0.8023 | not available |
| A10_restaurant_logo | 0.9276 | 0.9360 | 0.9856 | pixel | 0.8920 | 0.7933 | 0.8547 (coherent_stroke_80) |
| A11_chocolate_cake_texture | 0.9068 | 0.9040 | 0.9943 | pixel | 0.8849 | 0.7002 | not available |
| A12_ramadan_ad_composition | 0.8625 | 0.8655 | 0.9857 | pixel | 0.9030 | 0.6464 | not available |

## All12 mean metrics

| Condition | SSIM | PSNR dB | Edge F1 | DeltaE76 mean | High-pass RMSE sigma1 | Worst tile RMSE mean |
|---|---:|---:|---:|---:|---:|---:|
| owner | 0.9088 | 26.490 | 0.9403 | 3.575 | 8.532 | 18.205 |
| best_spline | 0.9128 | 29.942 | 0.9429 | 2.082 | 6.079 | 14.006 |
| best | 0.9836 | 42.605 | 0.9881 | 0.690 | 0.740 | 7.124 |
| original | 0.8831 | 28.044 | 0.8680 | 3.130 | 5.166 | 16.339 |
| repair | 0.7348 | 21.763 | 0.7747 | 6.863 | 12.324 | 30.552 |
| frozen_common | 0.9836 | 42.605 | 0.9881 | 0.690 | 0.740 | 7.124 |

## Frozen common preset: held-out eight only

The common preset was chosen from13shared pilot configurations on A01/A03/A05/A10, frozen, then evaluated on A02/A04/A06/A07/A08/A09/A11/A12 before their per-image tuning. Those images were previously known historical benchmarks, but their current results did not choose the common preset. This is a small held-out configuration test, not unseen-domain validation.

```json
{
  "clustering": "color-cluster",
  "color_precision": 8,
  "corner_threshold": 60,
  "filter_speckle": 0,
  "hierarchical": "stacked",
  "layer_difference": 0,
  "length_threshold": 4.0,
  "max_iterations": 10,
  "mode": "pixel",
  "optimize": 1,
  "path_precision": 0,
  "simplify": null,
  "splice_threshold": 45
}
```

| Condition | Holdout SSIM | PSNR dB | Edge F1 | DeltaE76 | High-pass RMSE |
|---|---:|---:|---:|---:|---:|
| frozen_common | 0.9894 | 46.658 | 0.9965 | 0.290 | 0.537 |
| best | 0.9894 | 46.658 | 0.9965 | 0.290 | 0.537 |
| best_spline | 0.9121 | 30.102 | 0.9527 | 2.066 | 6.549 |
| original | 0.8773 | 28.111 | 0.8670 | 3.293 | 5.152 |
| repair | 0.7143 | 21.867 | 0.7730 | 7.168 | 11.838 |

## Complexity and search cost

All path commands include implicit repetitions and H/V/L commands. Coordinate-pair counts exclude H/V and arc implicit coordinates; do not mistake them for all free parameters. V04 rectangles are reported separately, not counted as zero geometry.

| Image | Best paths | Rectangles | All path commands | Cubics | SVG bytes | Full search wall s |
|---|---:|---:|---:|---:|---:|---:|
| A01_shield | 35815 | 0 | 271251 | 0 | 2155254 | 35.00 |
| A02_falafel | 76799 | 0 | 533696 | 0 | 4416205 | 75.26 |
| A03_burger_layers | 68942 | 0 | 461190 | 0 | 3903261 | 60.80 |
| A04_fries_shadows | 68993 | 0 | 482622 | 0 | 3979360 | 58.31 |
| A05_orange_juice_transparency | 52788 | 0 | 370091 | 0 | 3057942 | 47.08 |
| A06_tomatoes_organic | 76878 | 0 | 553745 | 0 | 4495072 | 62.20 |
| A07_wrapped_sandwich_occlusion | 80443 | 0 | 553636 | 0 | 4606222 | 45.12 |
| A08_latte_texture | 58418 | 0 | 439180 | 0 | 3488547 | 36.94 |
| A09_arabic_calligraphy | 35547 | 0 | 305626 | 0 | 2283604 | 27.18 |
| A10_restaurant_logo | 36607 | 0 | 251517 | 0 | 2098708 | 37.67 |
| A11_chocolate_cake_texture | 74609 | 0 | 513516 | 0 | 4272422 | 41.45 |
| A12_ramadan_ad_composition | 65749 | 0 | 455932 | 0 | 3775960 | 38.47 |

The CSV contains complexity for every selected historical and VTracer condition. Every trial result records generation CPU/wall time, render time and separate worker/renderer peak memory. Full search wall is the sum of isolated trial wall times; excludes comparison generation and historical SVG generation.

## Local detail evidence

Fixed4x4 tiles provide worst and median RGB RMSE for every condition in summary.json/CSV. They are spatial windows, not semantic ground truth. The Burger subset uses20historical manually confirmed seed centers,2.5pixel-radius disks at pixel centers; it never enters candidate selection.

| Burger condition | Seed-center RMSE | Worst tile RMSE |
|---|---:|---:|
| owner | 31.927 | 19.592 |
| best_spline | 0.029 | 8.927 |
| best | 0.029 | 7.335 |
| original | 6.204 | 14.082 |
| repair | 52.586 | 32.989 |
| best_recent | 40.988 | 27.567 |
| frozen_common | 0.029 | 7.335 |

## Proposed milestone numerical gates

These thresholds were research proposals recorded before benchmark results, not owner approval. Visual acceptance remains separate.

```json
{
  "best": {
    "all12_ssim_ge_.95": true,
    "mean_ssim_ge_.97": true,
    "all12_psnr_ge30": false,
    "all12_edge_ge_.9": true,
    "all12_deltaE_le3": false,
    "visual_acceptance": "requires separate human review; numeric gates are not sufficient"
  },
  "best_spline": {
    "all12_ssim_ge_.95": false,
    "mean_ssim_ge_.97": false,
    "all12_psnr_ge30": false,
    "all12_edge_ge_.9": false,
    "all12_deltaE_le3": false,
    "visual_acceptance": "requires separate human review; numeric gates are not sufficient"
  },
  "frozen_common": {
    "all12_ssim_ge_.95": true,
    "mean_ssim_ge_.97": true,
    "all12_psnr_ge30": false,
    "all12_edge_ge_.9": true,
    "all12_deltaE_le3": false,
    "visual_acceptance": "requires separate human review; numeric gates are not sufficient"
  }
}
```

## Reproduction and scope

Every tested parameter set, native SVG, PNG, metric record and failure remains in its trial directory. The best spline and overall candidate configurations are in summary.json; they may be different. Full native comparison sheets and100/200/400% crop expansions are under comparisons/. Enlarged PNGs expose source-resolution defects; they are not a claim of higher-resolution truth. No OCR, semantic layers, alpha-preserving vectorization or universal preset is established.

## Separate bounded follow-up and final deliverables

The primary and frozen-common results above are unchanged. The follow-up was selected after primary evidence and a negative visible-color refit diagnostic. Its configuration was selected using the four development images, frozen, then applied once to each remaining image. It is a second, exploratory round; do not merge it into the primary held-out claim.

| Image | Final origin | SSIM | PSNR dB | Edge F1 | DeltaE76 | Total path commands |
|---|---|---:|---:|---:|---:|---|
| A01_shield | fixed_geometry_refit_visible_color_refit | 0.9567 | 24.410 | 0.9288 | 3.282 | 271251 |
| A02_falafel | posthoc_extension | 0.9978 | 53.297 | 0.9978 | 0.107 | 520939 |
| A03_burger_layers | posthoc_extension | 0.9782 | 37.651 | 0.9976 | 0.828 | 452297 |
| A04_fries_shadows | posthoc_extension | 0.9942 | 47.659 | 0.9983 | 0.195 | 467797 |
| A05_orange_juice_transparency | posthoc_extension | 0.9741 | 36.347 | 0.9750 | 0.791 | 364944 |
| A06_tomatoes_organic | posthoc_extension | 0.9985 | 57.363 | 0.9992 | 0.077 | 545459 |
| A07_wrapped_sandwich_occlusion | posthoc_extension | 0.9984 | 54.000 | 0.9997 | 0.077 | 547106 |
| A08_latte_texture | posthoc_extension | 0.9860 | 39.372 | 0.9944 | 0.422 | 424310 |
| A09_arabic_calligraphy | posthoc_extension | 0.9727 | 40.175 | 1.0000 | 0.545 | 308828 |
| A10_restaurant_logo | posthoc_extension | 0.9939 | 49.372 | 0.9999 | 0.313 | 281234 |
| A11_chocolate_cake_texture | posthoc_extension | 0.9963 | 50.885 | 0.9995 | 0.121 | 509343 |
| A12_ramadan_ad_composition | posthoc_extension | 0.9952 | 49.488 | 0.9991 | 0.202 | 459969 |

All12 final mean metrics:
```json
{
  "ssim": 0.9868562031848397,
  "psnr_db": 45.00158758754751,
  "edge_f1_1_5px": 0.9907684514803888,
  "delta_e76_mean": 0.5800326994365312,
  "highpass_rmse_sigma1": 0.640083025785066
}
```
Separate follow-up frozen8 mean metrics:
```json
{
  "ssim": 0.99240753415281,
  "psnr_db": 49.029873926635275,
  "edge_f1_1_5px": 0.9984958821875041,
  "delta_e76_mean": 0.21829448373001464,
  "highpass_rmse_sigma1": 0.44294834047938847
}
```
Final selected SVG/PNG pairs are in best_outputs/. Their JSON sidecars record exact source candidate, settings, all candidate scores and structure. Highest score remains a numerical choice subject to the separately documented visual review.
