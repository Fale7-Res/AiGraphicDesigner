<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-20T01:55:18Z", "last_action": "CREATED", "last_change_id": "TASK-V04-IMAGE-REPAIR-02", "last_edited_at_utc": "2026-10-20T01:55:18Z", "last_editor": "chatgpt", "tracking_started_at_utc": "2026-10-20T01:55:18Z"}
END_DOC_PROVENANCE -->
# V04 Repair — Iteration and Parameter Notes

## Default configuration selected

The final benchmark uses the laptop-friendlier configuration recorded in the output SVGs: 850 initial SLIC segments, target region counts estimated in the range 220–560, `compactness=9`, contour epsilon 1.8 px for the outer silhouette, region gradient model enabled, and a shared-edge path representation. This output is the *only* configuration summarized in `benchmark_results.csv/json` and `RESULTS_REPORT.md`.

## Higher-detail probes

Higher-density region settings were evaluated as separate exploratory experiments; their scores must not be compared as if they came from the default run without noting changed parameters:

- The `mid_tuning/results.json` probe tests the 1,000-initial-segment / 270–700 target-range candidate on A02/A05/A09/A10/A11.
- The `compactness_tuning/results.json` probe tests SLIC compactness 4/6/9 on A02/A05/A11 with higher region counts. In those test cases compactness 9 generally gave the strongest PSNR/SSIM/edge F1 of the tested values.
- Additional higher-density probes showed that additional regions can recover more edge detail for selected images, but the highest settings made the full pass too costly or inconsistent in this execution environment. These settings are not the selected default.

Example observations from recorded sweeps:

| Probe | Target regions | PSNR | SSIM | Edge recall | Edge F1 | SVG size |
|---|---:|---:|---:|---:|---:|---:|
| A02 final default | 461 | 21.79 dB | 0.687 | 0.587 | 0.661 | 624 KiB |
| A02 medium detail | 575 | 21.94 dB | 0.701 | 0.610 | 0.681 | 708 KiB |
| A02 high detail | 692 | 22.66 dB | 0.731 | 0.737 | 0.767 | 780 KiB |
| A09 final default | 220 | 21.00 dB | 0.802 | 0.917 | 0.877 | 288 KiB |
| A09 medium detail | 270 | 20.82 dB | 0.793 | 0.915 | 0.865 | 300 KiB |
| A09 high detail | 330 | 20.98 dB | 0.805 | 0.928 | 0.891 | 358 KiB |
| A11 final default | 538 | 21.08 dB | 0.700 | 0.686 | 0.761 | 688 KiB |
| A11 medium detail | 672 | 21.20 dB | 0.714 | 0.695 | 0.770 | 790 KiB |
| A11 high detail | 800 | 21.46 dB | 0.738 | 0.775 | 0.813 | 874 KiB |

These are three-image/selected-image probes, not a 12-image benchmark with a common setting. They are provided to explain the next optimization opportunity, not to replace the final same-config table.

## Selection reasoning

The owner prioritizes faithful, editable shape structure—not simply path minimization. The selected default provides consistent completion across the 12-image dataset, higher PSNR/SSIM on every image, and smaller average SVG size than Version 01. It still has documented edge recall and F1 regressions, so the next implementation should allocate additional geometry only to regions where the residual edge error is high and then optimize common boundaries as a graph. Raising the global region budget indiscriminately is not an adequate long-term fix.
