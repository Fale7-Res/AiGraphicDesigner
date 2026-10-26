<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-25T15:03:37Z"}
END_DOC_PROVENANCE -->
# Exact VTracer version, parameter semantics and color contract

This experiment tests **Python distribution `vtracer==1.0.0a4`**, whose installed native module reports **`1.0.0-alpha.4`**. The source snapshots were fetched through the GitHub connector at the explicit tag `1.0.0-alpha.4`, not inferred from a current unpinned README. `reference/installed_vtracer.json` records distribution/module versions and the native extension SHA256. This is a prerelease engine; the benchmark does not establish release stability.

Primary sources are preserved verbatim under `reference/vtracer_1.0.0-alpha.4/`; `reference/vtracer_sources.json` gives repository paths, exact Git blob hashes and URLs. Relevant direct sources:

- [Python API README](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer-py/README.md)
- [Core configuration](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer/src/config.rs)
- [Python binding implementation](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer-py/src/lib.rs)
- [Color clustering](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer/src/frontend/color_cluster.rs)
- [Transparency keying](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer/src/frontend/keying.rs)
- [SVG serializer](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer/src/svg.rs)

## Mapping the owner's settings

| Owner UI setting | Exact Python configuration | Meaning verified in source |
|---|---|---|
| Clustering: Color | `clustering="color-cluster"` | Hierarchical color clustering; aliases `color` and `colorcluster` also parse. Alternative algorithms are `bw` and `watershed`. |
| Color Precision: 8 | `color_precision=8` | Significant bits per RGB channel. The frontend passes a precision loss of `8 - color_precision`; eight means zero dropped bits for comparisons. It does not guarantee every output pixel's original color or geometry. |
| Gradient Step: 0 | `layer_difference=0` | Hierarchical color-layer difference threshold, **not an SVG gradient stop count**. Zero also sets diagonal clustering connectivity to true. Therefore zero-versus-nonzero is not a pure color-tolerance ablation. |
| Compositing: Stacked | `hierarchical="stacked"` | Independently trace solid layer masks in painter's order; parent shapes are not punched into holes. Overdraw supplies coverage. |
| Filter Speckle: 0 | `filter_speckle=0` | Configuration is a side length whose square becomes the area threshold. Zero disables the color frontend's thin/thread-like rejection and changes the clustering hierarchy; it is not merely a final removal filter. |
| Curve Fitting: Spline | `mode="spline"` | Corner detection and cubic Bézier fitting. `polygon` and exact pixel-lattice `pixel` are separate supported alternatives. |
| Simplify: 1.5 | `simplify=1.5` | Post-fit curve simplification tolerance in pixels; refits smooth cubic runs while retaining corners. `None` or zero disables the pass. Pixel/polygon polylines are unaffected by this pass. |
| Path Precision: 0 | `path_precision=0` | Decimal places in coordinates. With default `optimize=1`, a geometry quantization/cleanup pass occurs before serialization, so this is not just cosmetic text shortening. |

Other settings are explicitly logged in the search configuration: defaults are corner threshold60 degrees, length threshold4px, ten refinement iterations, splice threshold45 degrees, no fixed palette or auto color-count cap, and optimize1. Optimize0 disables the quantization/cleanup pass and uses absolute commands, but serialization precision still rounds coordinates. Optimize2 additionally enables shorthand path serialization. No optimization level is a quality guarantee.

The exact Python interface is `vtracer.Config(**settings).convert_file(input_path, output_path)`; `convert_bytes` and `convert_pixels(raw_rgba, width, height)` also exist. `Config.__repr__` does not print every relevant field (notably simplify), so the experiment stores the actual parameter dictionaries rather than relying on repr alone.

## Cutout and watershed are real alternatives

In this tag, cutout is a mosaic with shared boundaries fitted once for adjacent faces. This is materially different from treating the old re-clustered cutout implementation as equivalent. Shared mathematical boundaries do not by themselves prove identical anti-aliasing in every SVG renderer; native renders remain the evidence.

Watershed builds a hierarchy on a four-adjacency pixel graph and uses `watershed_detail` to select the cut. Higher detail retains more regions; the code maps detail exponentially toward a target region count. Color precision and layer difference do not drive that frontend. In watershed cutout, merging uses a separate tolerance `max((255 - detail)/8, 2)` with integer division. It would be misleading to label changes to inactive color parameters as a watershed search.

The current IR supports **solid color paints only** (`Paint::Solid` in `ir.rs`). Smooth-looking gradients and reflections are approximated by colored shapes. The presence of a setting called Gradient Step does not mean the exported SVG contains analytical linear or radial gradients.

No 0.6.x wheel was installed or benchmarked. The new API, simplify control and shared-boundary cutout must not be assumed to exist or behave identically in old Python examples. The owner's precise browser/app build is unknown; these tests map the stated settings onto the explicitly tested 1.0.0a4 engine and do not claim byte-identical reproduction of an unspecified manual trial.

## Color and alpha: measured contract, not assumed support

The Python binding decodes through Rust `image` and converts to RGBA8, or accepts raw RGBA bytes. No explicit ICC-to-sRGB conversion appears in the inspected binding. Therefore profile conversion is a caller responsibility; the benchmark must inventory input profiles and must not silently treat profiled RGB as already canonical. Current benchmark images were inventoried by the benchmark worker as RGB without embedded ICC profiles. Numeric RGB is treated as sRGB for this research.

The color-cluster frontend implements heuristic keying of fully transparent pixels. It does not provide general continuous-alpha reproduction. Watershed computes RGB statistics without preserving input alpha in the inspected paths. The serializer writes solid hex fills, not arbitrary source alpha.

`src/test_color_contract.py` tests the installed engine with four 16×16 fixtures under both color-cluster and watershed, in pixel mode. Every result uses the same native Inkscape renderer at16×16 and the same white-compositing evaluator. Source PNGs, exported SVGs, native PNG renders and the complete negative result are retained in `reports/color_contract/`.

| Fixture / route | Color-cluster RMSE against source on white | Watershed RMSE | Interpretation |
|---|---:|---:|---|
| Uniform half-alpha red, raw RGBA | 103.695 | 103.695 | Both output opaque red; partial alpha is lost. |
| Red alpha ramp, raw RGBA | 122.195 | 122.195 | Continuous alpha not reconstructed. |
| Fully transparent red, raw RGBA | Process failure | 208.207 | Color clustering panics with divide-by-zero; watershed paints opaque red. |
| Four opaque sRGB patches, raw RGBA | 0.000 | 0.000 | Basic primary/gray colors and dimensions preserved in this fixture. |
| All four fixtures explicitly composited on white before tracing | 0.000 each | 0.000 each | Validates this bounded opaque-white preparation contract, not preservation of editable transparency. |

The native exception is `pyo3_runtime.PanicException`, not an ordinary Python `Exception`; process isolation preserves the failure without crashing the research driver. Diagnostic tests assert the preparation contract and retain raw-alpha failures rather than silently calling them successful conversions. Passing these small fixtures does not validate arbitrary ICC profiles, transparent artwork, every color space or every renderer.

To reproduce separately without replacing supplied audit artifacts:

```bash
python src/test_color_contract.py --output reproduction/color_contract
```

## License and distribution scope

The tagged Python Cargo manifest and installed package metadata state `MIT OR Apache-2.0`. The repository's fetched root LICENSE contains the MIT grant, including commercial use/distribution subject to retaining copyright and permission notices. That exact license is preserved with the snapshots. No paid API or model license is required for this classical engine. This records VTracer's inspected license evidence; distribution of a complete product must also preserve notices and check the exact bundled dependencies and build artifacts.
