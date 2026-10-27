<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T14:58:15Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T15:02:38Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T14:58:15Z"}
END_DOC_PROVENANCE -->
# Fixed-geometry SVG appearance ablation — technical report

Research scope: owner-approved bounded appearance ablation only. Production architecture remains **NOT_APPROVED**. No visual-fidelity, clean-vector, Magic Layers or product milestone is approved. The complete original owner vision is unchanged.

## Outcome

Real SVG gradients help appearance fitting on fixed paths, but these results do not approach the saved high-fidelity pixel reference on textured or shaded real images. D improves full native render SSIM and MSE over C on eight of nine cases; Arabic is unchanged. Six of seven real-image cases improve, with two analytic controls reported separately. This is evidence for appearance capacity, not proof that gradients explain all micro-cell proliferation, nor proof of satisfactory geometry or generalization to arbitrary images.

The pixel baseline remains materially better. No detail paths, overlays, topology changes or control-point movement were introduced. All B/C/D ordered geometry and masks pass an independent strict tree comparison. Path count reduction was not used as a quality objective.

## Conditions and frozen protocol

A: strongest saved adaptive pixel SVG on seven real cases, reused unchanged. For the two new analytic controls only, A is one fixed inherited watershed512 pixel configuration, not an adaptive search or a claim of best possible control SVG. The original analytic SVGs are retained as ground truth.

B: existing shared-boundary watershed128 cutout spline geometry with inherited solid fills. Saved trial08 outputs were reused byte-for-byte for all seven real cases. Controls were traced once with that same configuration. C: train-only alpha²-weighted optimized flat fills. D: identical C paths, adaptive flat/linear/radial gradients, at most four equally spaced stops. A single uniform geometry setting was deliberately used, within the approved at-most-three bound; this is not an exhaustive geometry-quality sweep. It produced only 18–35 RGB paths per case.

The manifest froze sources and saved artifact hashes. One input-policy correction was necessary: rocket's raw ICC-tagged RGB was initially compared with an sRGB-normalized inherited trace. That run is invalid for comparisons and preserved under `negative_results/raw_rgb_color_confounded/`; the active manifest uses the saved normalized source. Other six real sources were verified pixel-identical to their saved prepared sources. An interrupted partial cat run is also preserved. No inherited searches were rerun. There were four new control traces total (A/B on two fixtures); all other geometry was saved evidence.

## Native-resolution results

SSIM is on white. All three background metrics, DeltaE76, highpass errors, alpha and premultiplied RGB metrics are in each `result.json`. PSNR ∞ means identical tested-resolution pixels, not an artificial 99 dB cap. MSE reduction compares C with D; it is not a milestone acceptance threshold.

| Case | A SSIM | B SSIM | C SSIM | D SSIM | A / D PSNR dB | C→D MSE reduction | RGB paths B/C/D |
|---|---:|---:|---:|---:|---:|---:|---:|
| A01_shield | 0.995660 | 0.745143 | 0.748810 | 0.815371 | 51.56 / 23.05 | 60.9% | 35 |
| G01_coffee | 0.997894 | 0.482583 | 0.485733 | 0.535965 | 54.97 / 21.68 | 37.3% | 26 |
| G03_rocket | 0.996047 | 0.628908 | 0.628724 | 0.693539 | 52.69 / 22.28 | 46.6% | 28 |
| G05_chelsea_nativecrop | 0.999823 | 0.323273 | 0.325667 | 0.395686 | 62.84 / 21.50 | 34.0% | 22 |
| G06_arabic | 0.999999 | 0.999457 | 0.999457 | 0.999457 | 73.20 / 53.32 | 0.0% | 28 |
| G07_tux | 1.000000 | 0.857916 | 0.862740 | 0.876195 | ∞ / 26.06 | 24.8% | 29 |
| G08_dice_alpha | 0.999622 | 0.819321 | 0.822009 | 0.843116 | 58.53 / 24.88 | 25.5% | 29 |
| K01_linear_corner_hole | 0.999464 | 0.918145 | 0.917900 | 0.978980 | 60.48 / 33.48 | 41.2% | 25 |
| K02_radial_shared_curves | 0.998299 | 0.817846 | 0.816981 | 0.913501 | 54.58 / 31.46 | 85.7% | 18 |

The reference-to-D gap is especially large on fur and food photography. Arabic's high score must not be read as successful geometric lettering reconstruction: the unchanged inherited alpha mask carries its shape. Neither image-specific tuning nor learned cross-image training was performed.

## Geometry and pixel-grid evidence

The shield A contains 34,617 paths; B/C/D contain 35, 1,586 cubic segments and zero RGB paths with bounds ≤1×1. Exact shared segment pairing finds 797 paired segments and 27 unpaired segments (including outer boundaries), with no segment incidence greater than two at 0.001-coordinate rounding. This is genuine reuse of shared curve coordinates, but not proof of no crossings, correct region topology or visually coherent contours. Coffee still has jagged texture-derived boundaries and artificial region divisions. Cubic commands alone do not establish professional geometry.

Known-control foreground-union checks at actual 4× vector render: K01 IoU 0.991077, mean directed boundary distances 0.228/0.229px, one hole preserved; K02 IoU 0.993078, 0.244/0.248px, zero holes preserved. Foreground assignment uses the known flat background and inherited B paint distance, and tests silhouette union only. Internal boundary correspondence, full intersection certification and physical-object topology remain unvalidated. These controls are analytic assets, not unfamiliar real photographs.

Arabic is a negative geometry control: 27 of 28 RGB paths have bounds ≤1×1 and the median bounding-box dimension is one pixel. The inherited mask contributes 255 level paths containing numerous pixel runs. Tux and dice also retain their inherited alpha run masks. Thus the overall transparent output is not grid-independent, even where RGB paths are larger. These cases prevent a blanket “coherent vector output” claim.

## Fitting, sample separation and limitations

Ownership is inferred by an actual unique-color SVG render; only opaque, exact-ID, four-neighbor interior samples enter fitting. Zero-alpha source samples are excluded; residuals and fitted means use alpha² weights, matching premultiplied RGB fitting under a fixed alpha. Pixel positions `(x+3y)%5` split train (0,1,2), model-selection (3), and untouched diagnostic test (4). Training and selection/test are capped per region. Geometry extent uses positions, not held-out colors. This is interpolation validation on the same image, not independent spatial holdout or out-of-distribution generalization. Full-image metrics intentionally also evaluate fitted pixels; they validate actual output rendering rather than serve as an independent statistical test set.

Models use two to four equally spaced RGB stops, explicit sRGB interpolation and transform-correct user-space coordinates. Linear orientation and radial center are refined with deterministic bounded search; radial focus equals center and radius is the sample extent. Clipped least squares is not a globally constrained optimum. The regional cap is 100 model evaluations; fitting dispatch is 540s and the full case process is capped at 600s with a sampled 4GiB tree limit. No case hit those bounds. Tiny/no-interior regions retain inherited or fitted flat fills. This does not rule out stronger appearance fitting or different stop/focal models.

Held-out diagnostics are preserved by region in `fitting.json`, summarized in `reports/heldout_summary.json`. Known linear control interior test error drops near zero while full-render MSE remains 29.21; radial control also retains much more full-render error than interior error. This supports the conclusion that omitted boundary pixels, rendering seams, shape placement and coarse region representation matter. It does not supply a rigorous percentage attribution of error to geometry versus appearance.

## Alpha and coverage defects

Identical B/C/D vector masks do not imply identical rendered alpha. C and D differ by at most one 8-bit alpha quantum on seven cases; Arabic and K01 are unchanged. More seriously, B/C/D do not preserve the desired opaque coverage or source alpha perfectly: shield D alpha MAE is 1.734/255 and maximum error 223, Tux 1.217/max72, dice 0.613/max64. These losses occur despite shared curve coordinates and the same alpha mask. Shared coordinates are insufficient to guarantee watertight antialiased painting; spline coverage defects may also contribute. We have measured the error, not uniquely identified its cause. No seam-covering underlay or geometry expansion was silently added.

## Local errors, cost and complexity

| Case | C / D worst32px tile RMSE | D cubic segments | D RGB ≤1px paths | D bytes | D native render seconds | Fit seconds | Full case seconds | Sampled peak MiB |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A01_shield | 60.001 / 47.866 | 1586 | 0 | 56,930 | 0.153 | 3.952 | 40.3 | 160.6 |
| G01_coffee | 62.076 / 51.266 | 1622 | 0 | 54,187 | 0.123 | 3.545 | 64.2 | 188.0 |
| G03_rocket | 65.693 / 54.061 | 996 | 1 | 38,173 | 0.127 | 3.127 | 45.8 | 151.3 |
| G05_chelsea_nativecrop | 41.680 / 36.182 | 1404 | 0 | 44,955 | 0.158 | 3.915 | 74.9 | 193.7 |
| G06_arabic | 1.834 / 1.834 | 6 | 27 | 182,630 | 0.192 | 0.707 | 28.4 | 146.7 |
| G07_tux | 58.771 / 29.718 | 1068 | 0 | 49,396 | 0.177 | 3.345 | 34.8 | 157.9 |
| G08_dice_alpha | 43.849 / 36.856 | 850 | 0 | 442,407 | 0.239 | 3.875 | 49.1 | 169.0 |
| K01_linear_corner_hole | 11.727 / 9.017 | 346 | 1 | 15,971 | 0.109 | 1.912 | 26.6 | 172.4 |
| K02_radial_shared_curves | 44.022 / 12.740 | 428 | 0 | 17,889 | 0.142 | 1.304 | 30.5 | 177.7 |

Full-case times include parsing the large A reference, all four native renders, diagnostics and 24 direct SVG viewport crop renders at 1×/4×/16×, not only tracing or fitting. Memory is sampled simultaneous process-tree RSS including renderer; brief peaks may be missed. Native renderer measurements and per-zoom resources are saved separately. This is CPU/native Windows evidence, not a GPU or cross-platform benchmark. Resvg 0.49.0 is the only independently working renderer here; second-renderer interoperability remains unverified.

## Visual findings and failures

- Shield: D restores broad metallic and red shading, but outer silhouette details, inner band placement, crown and localized reflections differ.
- Coffee: the broad cup/saucer shading improves, while wood grain, spoon highlights and precise cup/handle contours disappear. The worst residual is not excused by the 26-path output.
- Rocket: smoke and sky shading improve after color normalization, but thin structures and localized smoke contours are missing.
- Cat native crop: gradients cannot recreate fur, whisker-scale transitions and eye detail on 22 regions. It is the weakest real case and receives the same dashboard prominence.
- Arabic: no gain; fixed alpha masks largely determine visible shape, and tiny RGB cell geometry persists.
- Tux/dice: RGB gradients help, but contours, reflections and bright local highlights remain wrong; dice's worst-error 16× crop shows a missing specular highlight. Alpha is still a pixel-run representation and coverage is imperfect.
- Analytic controls: smooth fills are recovered substantially better, but geometry-induced bands and seams remain visible. These are not successful replacements for the ground-truth SVGs.

## Validation and preservation

Five fitter tests pass, including actual transformed linear/radial SVG rendering and alpha² weighting. Five dedicated artifact tests pass: frozen hashes and complete nine-case suite, strict B/C/D ordered geometry/mask identity, SVG safety/≤4 gradient stops and PNG decoding, independent recomputed native MSE/alpha, and zoom/known-control evidence. Independent QA and scoped governance outputs are attached separately. Two repeated actual renders (shield A and K01 D) are pixel-identical, so their repeated native renderer noise was zero in this bounded check. Renderer determinism is not optimizer repeatability across all machines.

The prior generalization closure reuses 140 candidates without retracing, verifies 213 SVGs/553 PNGs and all eight unchanged winners, and provides six saved-evidence tests and visual sheets. It demonstrated no reconstruction improvement. Its seven independent original images and eight cases are not eight independent data sources. Historical implementations and owner vision are unchanged.

## Technical conclusion and next decision

1. **Appearance capacity:** supported within this bounded experiment. Gradients improve fixed-geometry native fidelity on eight cases, including six real cases.
2. **Coherent geometry:** only partial evidence. Shared coordinates and large RGB paths are useful, but seams, shape errors, jagged boundaries and the Arabic micro-cell case prevent acceptance.
3. **Approach to pixel reference:** not achieved. The remaining PSNR/SSIM and localized error gaps are substantial, including on known-vector controls.
4. **Generalization:** limited evidence across the stated categories; it does not establish arbitrary-image performance, native full-size source performance or typography reconstruction.

Keep the gradient fitter as an experimental component. A wholesale replacement of VTracer or a new neural geometry engine is not justified by this single coarse configuration. The next recommended decision is a bounded **coverage-and-geometry granularity study**: diagnose shared-edge alpha/seam errors independently, include the known source SVG geometry as an oracle control to separate appearance capacity from region discovery, compare a small uniform range of existing spline granularities using this same appearance fitter, and explicitly check control silhouettes, local feature retention and cell-scale distributions. Existing strongest saved spline candidates should be included as contextual controls. This would distinguish excessive coarsening and rasterization defects from a deeper reconstruction-method limitation without assuming a new engine is necessary.

Constrained alternating geometry/appearance refinement deserves investigation after those controls establish valid coverage and useful geometry granularity. It should retain shared boundaries, restrict displacement near evidence-supported contours and accept moves only on actual local/global render improvements; simply nudging the current coarse boundaries cannot invent missing texture or reflections. Do not implement that next stage without the owner's next decision.

Rejected for this cycle: adding micro-paths to inflate scores (invalidates hypothesis), global unrestricted joint optimization (scope expansion and topology risk), diffusion-curve rendering/raster fallback (SVG portability and raster prohibition), and treating path count alone as quality. More complicated gradients alone cannot recover missing localized highlights, disconnected features or texture on a fixed inadequate partition. No production architecture, full Clean SVG or Magic Layers implementation was started.


## Governance and publication boundary

Independent QA passes bounded execution and evidence; scoped code mirrors/provenance pass (four new Python files, 41 symbols). Root-wide governance does not pass: document registry/catalog drift remains, and root brain/catalog verification encounters a pre-existing non-UTF8 generalization WAL (byte0x97); root README also has a pre-existing UTF-16 BOM. Historical encodings/governance files were preserved. New documents are UTF-8. Root check logs and exit statuses are retained in reports/root_*.log and root_governance_checks.json. Scope-local success is not a claim that root governance is healthy.

Local and remote main were c9bd9d95c680e1404165025915ed1739050ede74 at start. .git still has explicit DENY write ACLs; no Git writes or pushes were attempted again. Owner-run publishing instructions and a SHA256 inventory accompany the delivered review package. No changes are claimed committed or published.
