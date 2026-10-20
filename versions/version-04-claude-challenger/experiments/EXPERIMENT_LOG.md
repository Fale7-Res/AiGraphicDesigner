<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T00:24:17Z", "last_action": "CREATED", "last_change_id": "CHALLENGER-V04-IMPORT", "last_edited_at_utc": "2026-10-18T00:24:17Z", "last_editor": "owner-claude-import", "tracking_started_at_utc": "2026-10-18T00:24:17Z"}
END_DOC_PROVENANCE -->
# Version 04 — Experiment Log

## Sequence

1. **Pre-implementation proposal recorded.** `docs/TECHNICAL_PROPOSAL.md` compares shared-boundary topology-aware regions + adaptive Bézier curves against adaptive vector-surface tessellation. Strategy B was selected before writing the implementation.
2. **S00 synthetic known geometry.** A deterministic 320×240 known geometry composite included a rounded plaque, nested shield shapes, gold border, red inset, highlight patch, ring/hole, two tiny marks, and a pre-composited soft shadow. The 9,000-cell surface-only SVG scored 22.15 dB PSNR / 0.8547 SSIM. A separately labelled edge-band hybrid scored 25.61 dB / 0.8947 SSIM. These results demonstrate only a synthetic smoke test, not semantic layer inference.
3. **A01 budget sweep before full benchmark.** On the surface-only shield run, 1k / 2.5k / 5k / 9k cells produced 21.69 / 23.04 / 24.11 / 24.46 dB PSNR, SSIM 0.7491 / 0.7940 / 0.8307 / 0.8536, and SVG size 114 / 199 / 344 / 586 KiB. Improvement tails off as the budget increases; the subsequent edge-band overlay is evaluated separately.
4. **Visual review rejected surface-only as final.** Its pixel scores improved versus V01, but calligraphy and logo edges visibly stair-stepped. Most edge-recall values for the base surface remained inferior to the source. The method was not kept as the final benchmark representation.
5. **Edge-band iteration.** Add a 1× dilated 3×3 Canny residual in five-bit-per-channel RGB, grouping same-color horizontal pixel runs into SVG path objects. Quantization was swept over A02/A09/A10/A12 for 4/5/6/8 bits; 5 bits was chosen as a size/quality compromise, not claimed globally optimal.
6. **Final same-renderer benchmark.** All 12 committed V01 SVGs and all 12 V04 hybrid SVGs were rendered by Inkscape at the source PNG dimensions. Results are in `metrics/benchmark_results.csv/json`, `metrics/summary.json`, paired timings in `metrics/render_performance.csv`, and the report in `metrics/RESULTS_REPORT.md`.
7. **Independent artifact verification.** `src/verify_outputs.py` re-generated each final SVG, parsed its XML, checked for embedded raster images/external image references, and verified rendered dimensions. `metrics/verification.json` reports byte-identical output on all 12 images.
8. **Unit tests.** Four small CPU tests pass for cell-budget bounds, constant fill behavior, SVG validity/no raster image, and deterministic hybrid edge residual generation.

## Final metric snapshot

| Measure | Version 01 baseline mean | Version 04 hybrid mean | Better / losses |
|---|---:|---:|---|
| MSE | 1074.58 | 109.52 | V04 better 12/12 |
| PSNR | 18.02 dB | 28.04 dB | V04 better 12/12 |
| SSIM | 0.5988 | 0.8831 | V04 better 12/12 |
| Edge precision (1 px) | 0.7072 | 0.8330 | V04 better 10/12; losses A09, A10 |
| Edge recall (1 px) | 0.8392 | 0.9853 | V04 better 12/12 |
| Edge F1 (1 px) | 0.7556 | 0.9009 | V04 better 12/12 |
| Small-edge component recall proxy | 0.7826 | 0.9741 | V04 better 11/12; loss A04 |
| Foreground IoU proxy | 0.9211 | 0.9629 | V04 better 12/12 |

## Explicit trade-offs / unresolved failures

- V04 mean SVG size is 1,223.9 KiB compared with 590.1 KiB for V01; average path count is 2,839 rather than 633, and each image has 9,000 rectangle leaves. The current output is therefore worse as a compact, semantic, professionally editable document.
- A09 calligraphy and A10 restaurant logo show lower edge precision despite a small edge-F1 gain; A04's small-edge-component recall proxy is lower. These are reported rather than suppressed.
- The edge correction is source-derived. The better metrics should be interpreted as a fidelity/complexity trade-off, not as proof that unknown geometry was semantically inferred.
- No SAM 2 / LaMa stage, custom model training, paid APIs, or cloud GPU was used. The inspected Version 01 pipeline does not implement SAM 2 / LaMa either.

## Governance

Version 04 outputs and documents are isolated under `versions/version-04-claude-challenger/`. Version 01–03 implementation and original experiment artifacts were not edited. The owner vision and global architecture approval state were not edited.
