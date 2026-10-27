<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T10:42:21Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T10:48:35Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T10:42:21Z"}
END_DOC_PROVENANCE -->
# AiGraphicDesigner — local technical handoff

Assessment recorded 2026-10-27T10:42:40.607236+00:00. Global architecture: **NOT_APPROVED**. Full fidelity milestone: **not ready for unconditional owner acceptance**. Opaque native-resolution evidence is ready for owner visual review.

## Repository and evidence audited

Initial checkout was clean on `main`, commit `99f09c8`, origin `https://github.com/Fale7-Res/AiGraphicDesigner.git`. Recent research commits are `99f09c8` (adaptive) and `4ba5ed5` (fidelity), preceded by historical Version 04 repair and initial history. The complete authoritative Arabic owner vision was read. No historical implementation, owner vision, or governance document was edited.

Both requested experiments exist with source, requirements, README/reproduction instructions, reports/RESULTS/QA, configurations, candidate SVGs, renders and rankings. `reports/research_inventory.json` lists the actual files; `research_inventory_counts.json` counts them. Research was reviewed against source, not accepted from report prose. Independent QA identified the Unix-only import and the limited scope of historical tests/reproduction.

The root operational checkpoint predates the two research commits. It must not be treated as a current product readiness statement. This experiment keeps its own operational log, source provenance, code mirrors and function registry to preserve historical records.

## Native Windows readiness

The inherited adaptive entry point fails before execution: its sibling search module imports Unix-only `resource`. Global VTracer `0.6.15` also lacks the required `1.0.0a4` parameter surface. Therefore the inherited checkout did **not** work unchanged on native Windows.

This isolated extension preserves inherited candidate generation, normalization, metric formulas and selection. AST comparisons verify the selected functions. It replaces OS-specific worker/renderer plumbing, uses psutil measurements, bounds workers, and explicitly chooses its renderer. Copied helpers are justified compatibility isolation; the historical evaluator is imported unchanged. There is no major architecture rewrite or production integration.

Measured environment: native Windows 11 build 26200, Python 3.14.2, VTracer 1.0.0a4, NumPy 2.4.4, SciPy 1.18.1, Pillow 12.1.1, scikit-image 0.26.0, psutil 7.2.2, resvg 0.49.0. See `reports/environment.json`. A separate environment with exact historical package pins was installed, but native-library loads stalled and bounded test attempts timed out. Portable Inkscape 1.2.2 was obtained from its official host; version probes stalled and were stopped. **No local Inkscape success or exact-pin native reproduction is claimed.** resvg is recorded explicitly in every trial. No global package was upgraded.

## Executed validation

Four historical tests, unchanged, pass against the Windows-derived optimizer. The original direct Windows test discovery fails on `resource`; these are distinct facts. Additional checks establish search/helper AST equivalence and actual termination of a child plus grandchild on timeout. The four tests alone do not certify rendering.

All three fresh searches completed without failed candidates, each testing 19 configurations and stopping after the inherited stagnation rule. Thirteen pilots were followed by six adaptive probes. All 57 successful SVGs were independently parsed and restricted to `svg/path`, checked for embedded raster/external content, decoded at native dimensions, and had metrics and composite scores recomputed. Selected-output copies match their winning candidate files. This establishes structural and render validity for these outputs, not a full SVG specification conformance certification.

| Fresh input | Successful/tested | SSIM | PSNR dB | Search seconds | Peak sampled tree MiB |
|---|---:|---:|---:|---:|---:|
| A03_burger_layers | 19/19 | 0.997837888 | 54.3560 | 168.1 | 166.3 |
| A01_shield | 19/19 | 0.995660179 | 51.5571 | 152.6 | 131.3 |
| N01_local_gradient_shapes | 19/19 | 0.999895362 | 67.3202 | 120.2 | 106.3 |

The new diagnostic was authored locally after the handoff: 193×137 pixels with gradients, curves, fine strokes and text. Its RGBA companion adds a soft alpha field. `inputs/manifest.json` records creation, dimensions and hashes. These are genuinely new synthetic inputs; they are not new natural-photo or large-image validation.

Burger and shield select the same configuration and produce byte-identical SVGs to the historical adaptive winners. Their SSIM/PSNR reproduce the recorded values under resvg; tiny floating-point color-metric differences are retained. A separate Burger winner retrace reproduces its local SVG, PNG and metrics exactly. This does not imply that every spline candidate renders identically between resvg and Inkscape.

Independent recomputation from all twelve saved winning renders gives mean SSIM **0.9975977028220414** and mean PSNR **54.330690724073584 dB**, exactly matching the historical report. This checks saved evidence and arithmetic; only Burger and shield were freshly retraced from that twelve-case suite. The original adaptive QA reproduction had rerun the older Burger finalist, not the new adaptive winner; the fresh local run closes that representative gap.

Visual inspection of actual comparison sheets supports close native resemblance. Burger seeds, filling edges and background are preserved; the shield's broad tonal field is substantially restored. Dense source-grid geometry remains evident on enlargement. Metrics are neither Arabic OCR nor proof of semantic object boundaries.

## Highest-value next improvement: transparency

Executed two sequential 13-candidate searches on the new RGBA fixture: inherited explicit white compositing versus unassociated RGB followed by a source-alpha vector mask. See `reports/alpha_comparison.json`. Rendered alpha error fell from MAE 198.678983/255 to **0**, maximum error **0**, and exact-alpha fraction **100%**.

| Background | Flattened SSIM | Alpha-preserving SSIM | Flattened PSNR | Alpha-preserving PSNR |
|---|---:|---:|---:|---:|
| white | 0.9988710 | 0.9985586 | 51.2572 | 55.1336 |
| black | 0.1018978 | 0.9972659 | 1.6337 | 55.1336 |
| bluegray | 0.5180671 | 0.9978930 | 4.7641 | 54.8562 |

The white-background SSIM tradeoff is retained, not hidden. The prototype SVG is 1,667,681 bytes with 25,903 paths, versus 645,520 bytes and 11,052 paths for the white-composited winner. It contains only svg/defs/mask/path/g elements, no raster/filter/external content. The renderer took 0.668 seconds versus 0.386 seconds in this fixture. Selection still uses opaque RGB fidelity; alpha/background scores are post-selection evidence. This is one successful native synthetic test, not universal alpha-aware optimization. More real RGBA assets, varying sizes and independent applications remain necessary.

The inherited default explicitly rejects nonopaque inputs. Its optional `white` policy flattens them; historical U04's exact score is white appearance only. The prototype uses equal-alpha horizontal vector runs, with no embedded image or raster filter. Geometry checks cover all 256 alpha values, full opacity/transparency and checker boundaries. SVG masking semantics are supported by the [W3C masking specification](https://www.w3.org/TR/css-masking-1/#MaskElement). Actual rendering remains the deciding experiment.

Pixel-grid opacity is deliberately acceptable for current fidelity research. It does not solve smooth scaling, clean geometry, object ownership or editing. The prototype has a 1,048,576-pixel input cap. ICC conversion is implemented but arbitrary ICC/HDR/16-bit/animation support is not certified.

## Capability assessment and defects

Working and locally measured: genuine SVG generation, bounded candidate search, automatic multimetric ranking, native output rendering, saved-metric recomputation, representative deterministic tracing, new opaque synthetic input processing, and native Windows worker plumbing. The Windows extension is the tested entry point.

Incomplete: transparent-input default support in inherited code, clean professional geometry, semantic grouping/occlusion and Magic Layers, layer-aware editing, planned image generation, font identification, Arabic shaping and font-identity-preserving word editing. Historical Version 02 builds groups from supplied contours; Version 03 accepts supplied text/font/contours. Those building blocks do not implement automatic semantic decomposition or font reconstruction.

Best supported categories are opaque, modest-sized images where detailed texture and tonal variation can be retained with dense pixel-derived paths. This is an inference from the measured food/logo/calligraphy/photo research plus local diagnostic, not a comprehensive category study. Binary and smoother curve candidates often lose color or texture. Arbitrary new static opaque files can be submitted through the CLI, but universal quality and resource bounds are not established. Huge images, animation, HDR and alternate application interoperability remain unverified.

Remaining defects include pixel-grid geometry, large output size, potential zoom aliasing, shallow search/stagnation before late parameters, input failures outside candidate history, RGB-only selection for the alpha prototype, and environment startup delays. The score can prefer a result different from highest SSIM or owner preference. No complexity penalty was introduced. Performance includes worker startup/render/evaluation; trace time is separately recorded. Memory is an observed simultaneous process-tree RSS lower bound with a requested 10 ms polling delay plus enumeration overhead, not a hard OS limit or maximum possible input guarantee. The default sampled 4 GiB guard and timeout cleanup are research controls.

## Governance and acceptance

Root `change_tracking.py verify` fails historical documentation registry/provenance drift. Root `verify_brain_sync.py` and `verify_catalog.py` abort on a pre-existing non-UTF-8 file. Logs are retained under `reports/`; no repository-wide governance success is claimed. The isolated experiment's mirrors/provenance are checked separately. Historical drift is reported rather than silently repaired.

The previous Work/Astra results are useful, and representative opaque fidelity claims now have fresh local support. Further investigation is needed for transparency across real RGBA assets, broader unseen photos/designs, large inputs, renderer/editor interchange and clean scaling. The owner should inspect native Burger/shield/new-input comparisons before accepting the opaque fidelity slice. The complete milestone still needs those limits resolved or explicitly accepted. Architecture remains **NOT_APPROVED**.

The complete owner vision remains binding: planned image generation; Magic Layers with geometry, z-order and occlusion; professional SVG geometry and grouping; semantic editing; Arabic typography and font identity. Fidelity work enables those later milestones and does not replace them.

## Git delivery status

All tracked historical files remain unchanged against HEAD. Creation of the research branch was attempted with both hierarchical and flat branch names. Git metadata writes were denied even after an exact `.git` filesystem permission grant. Consequently no new commit or push is claimed; the checkout remains on `main` with the isolated experiment untracked. The requested coherent commit is prepared for the owner to perform once Git metadata writes are available:

```powershell
git switch -c codex-research-windows-fidelity-20261027
git add experiments/EXP_CODEX_WINDOWS_FIDELITY_20261027
git commit -F experiments/EXP_CODEX_WINDOWS_FIDELITY_20261027/COMMIT_MESSAGE.txt
```

Inspect branch and remote state before any push. No force push, history rewrite or unrelated file staging was attempted.

## Final closure

Independent QA verdict: **PASSED_FOR_BOUNDED_RESEARCH_WITH_DOCUMENTED_LIMITATIONS**. The aggregate scan parsed 90 SVGs and decoded 116 PNGs with zero artifact errors; the subsequently generated comparison board was also decoded and viewed by both parent and reviewer. Five rankings contain 83 successful search candidates and zero failures. Alpha equality was independently checked directly from PNG arrays. Final Git status contains only this isolated experiment; tracked changes against the original HEAD are empty.

Full source, trials, metrics and reproducibility instructions are retained at `C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_CODEX_WINDOWS_FIDELITY_20261027`. The output copies contain the assessment, QA result and selected SVG/PNG evidence. No commit or push could be completed because repository metadata writes were denied. No architecture approval is granted.
