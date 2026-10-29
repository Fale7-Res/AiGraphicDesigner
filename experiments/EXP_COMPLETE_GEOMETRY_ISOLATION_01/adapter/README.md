<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:50:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Native VTracer geometry bridge

Research adapter only; production architecture remains `NOT_APPROVED`. No Arena implementation is copied. VTracer public graph and spline APIs are reused unchanged; the JSON/face-reference bridge is newly authored here. Upstream VTracer is MIT OR Apache-2.0, pinned to release1.0.0-alpha.4 and source commit2500df76b5aea0ac22d15296b22722442f825c5b. Exact registry package checksums are recorded in Cargo.lock.

## Commands

`agd_geometry segment request.json output.json`

The request contains integer width/height and flat row-major RGBA8 bytes in `rgba`. Every alpha byte must be255. Defaults: `detail:192`, `min_area:0`. The adapter calls raw WatershedHierarchy build/cut, flattens the partition and remaps IDs densely to1..N. Zero is reserved outside and white working-background pixels remain a normal nonzero region. No color-similarity compositor merge is performed.

`agd_geometry fit request.json output.json`

The request contains width/height and flat row-major integer `labels`. Both initializers must consume the same frozen labels. Zero means outside, positive IDs identify regions. The adapter does not merge, recolor, refine or infer new regions. It calls BoundaryGraph::extract and unmodified SplineSegmentFitter defaults, fitting each canonical shared chain once.

Normalized output contains:

- `chains`: id, adjacent_face_labels, pixel_crack_vertices, closed and segments. Each segment is `L` with p0/p3 or `C` with p0/p1/p2/p3.
- `faces`: label-keyed lists of closed loops, each loop containing ordered `{chain,forward}` references.
- `incidence`: pixel-crack vertices with xy and degree.
- Extra diagnostics include native nodes, connected patches, native fitted geometry type, unchanged library version and source commit. `merges_disabled:true` is explicit.

The face bridge walks the public canonical graph using its left-region/right-turn convention and records8-connected same-label patches separately. It raises errors on a failed or repeated face walk; it does not silently replace curves. Native polyline outputs are retained as explicit native geometry, not relabeled as cubics. Export does not certify absence of fitted-curve crossings or raster seams; independent geometry QA must assess these properties.

## Build and tests

With an installed Windows Rust GNU or MSVC toolchain:

```
cargo test --locked --release
cargo build --locked --release
```

Build products should be directed outside the repository using CARGO_TARGET_DIR. This session uses an isolated work/geometry_rust Rustup/Cargo installation, with no global PATH modification. Cargo's native Schannel registry request failed under the execution identity. Official crates were downloaded using ordinary Python HTTPS, verified against official registry/upstream-lock SHA256 checksums, then supplied to Cargo's supported offline directory-source mechanism. No TLS checks or repository protections were disabled. Temporary toolchain, vendor cache and executable are not repository source artifacts.

The tiny-map Rust harness tests are infrastructure checks, not candidate benchmarks. Meaningful source-image execution must wait for the parent's reference freeze. Coordinate convention is raster x-right/y-down, with pixel corners integer and pixel centers offset0.5. Frame chains remain for face closure and should be excluded from source-boundary distance where protocol specifies.

## Sources and licensing

- [Pinned VTracer source](https://github.com/visioncortex/vtracer/tree/2500df76b5aea0ac22d15296b22722442f825c5b)
- [Public graph API](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer/src/mosaic/graph.rs)
- [Public spline fitter](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/crates/vtracer/src/mosaic/fit.rs)
- [Upstream license declaration](https://github.com/visioncortex/vtracer/blob/1.0.0-alpha.4/Cargo.toml)

The adapter is new research glue, not a claim that VTracer is approved production architecture or that a shared graph establishes correct scene boundaries.
