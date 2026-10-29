<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:50:14Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T07:02:02Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:50:14Z"}
END_DOC_PROVENANCE -->
# Reproduction and evidence policy

Architecture remains **NOT_APPROVED**. This is a geometry-only, fixed-label experiment. Do not rerun the prior140-candidate search or fit new appearance.

## Inputs and external comparison code

Use the existing repository images listed in inputs/manifest.json. Their source and common opaque working PNG hashes are frozen. No image is resized. Continuous alpha is outside this study.

Arena is an external comparator with unresolved redistribution rights. The owner ZIP must have SHA256 `e0549964698d696694f671a8343fcc020a3ec6bb30dc273b92d1a6fb4e330fd9`. Its verified extraction resides at `$Work\arena_review\geometry_only_v2`. Do not overwrite that extraction or vendor its implementation. Original files remain unchanged. The fine-feature fixture and114 derived evidence files are local-only; external/LOCAL_EVIDENCE_MANIFEST.json records their paths, sizes and hashes. The local review package includes them for the owner's inspection, not as a redistribution license.

## Environment

Recorded versions are in reports/environment.json. Use an isolated Python3.14 environment and install requirements.txt there. Keep virtual environments, Rust toolchains, vendor caches, renderer binaries and build products outside the repository. resvg0.49.0 is expected at `$Work\resvg\resvg.exe`.

The native adapter is pinned by adapter/Cargo.lock and upstream commit2500df76b5aea0ac22d15296b22722442f825c5b. Build and test it using a Windows Rust toolchain:

```powershell
$Repo = 'C:\Users\Mohamed\Desktop\AiGraphicDesigner'
$Exp = Join-Path $Repo 'experiments\EXP_COMPLETE_GEOMETRY_ISOLATION_01'
$Work = 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'
$env:AGD_ISOLATION_WORK = $Work
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
$env:CARGO_TARGET_DIR = Join-Path $Work 'geometry_rust\target'
cargo test --locked --release --manifest-path "$Exp\adapter\Cargo.toml"
if ($LASTEXITCODE -ne 0) { throw 'Native tests failed' }
cargo build --locked --release --manifest-path "$Exp\adapter\Cargo.toml"
if ($LASTEXITCODE -ne 0) { throw 'Native build failed' }
```

This session used an isolated GNU toolchain. Cargo's Schannel network access failed, so official packages were downloaded over normal verified Python HTTPS, checked against locked SHA256 values and supplied through Cargo's supported offline directory source. No TLS checks or security controls were bypassed. Ordinary owner-terminal Cargo access may work directly.

## Saved-output verification

Use the isolated Python executable in place of `python` below. The session executable is `$Work\agd-native\Scripts\python.exe`; Shapely was installed in `$Work\geometry-deps`, not globally.

```powershell
Set-Location -LiteralPath $Exp
python -m unittest -v test_isolation.py
python audit_raw_labels.py
python exact_area_check.py
```

The seven Python tests check metric behavior, raw-to-common mapping rejection, native ring closure, frozen-policy safeguards and an actual resvg-rendered shared-boundary/hole fixture. Rust has six interface tests including all81 two-by-two three-label maps. These tests are infrastructure checks, not reconstruction acceptance.

## Full matrix — only if reproduction is needed

**Do not run these just to view saved results.** Existing candidate hashes are checked before resume. Unknown or changed existing targets cause an error rather than silent reuse or overwrite. For an independent fresh execution, use a separate cloned experiment/output root and a new external work directory; retain the frozen protocol and evaluator files unchanged.

```powershell
python isolation.py prepare
python run_matrix.py
python analyze_matrix.py
python validate_geometry.py
python final_diagnostics.py
python make_overlays.py
python package_evidence.py
```

`prepare` recreates deterministic common working images; inspect their frozen hashes before proceeding. `run_matrix` never reads evaluator annotations. Its native children are capped at600s/4096MiB, while all Arena tasks share one600s monitored batch. The measured matrix upper CPU bound is below the frozen7200s budget. Reports document build/setup separately and distinguish sampled memory from guaranteed peaks.

`analyze_matrix` retains original graph-assembly diagnostics. `validate_geometry` performs the primary common-face comparison without changing control points. `final_diagnostics` checks numerical coverage and actual4× visible microgeometry. `package_evidence` creates actual SVG viewport renders and HTML; it does no fitting. The evaluator-only source correspondence used for known foreground masks is fixed, not candidate selection.

## Measurement corrections and limitations

Final common-face metrics and injective24-bit label checks supersede preliminary diagnostics. The original palette repeated every200 labels, and an early measurement omitted implicit native-ring SVG closepath. Preserved preliminary files are explicitly labeled, never a second successful result. Native candidate control points were not refitted.

Shield annotations are approximate AI-authored traces independently reviewed by another agent. Their uncertainty exceeds1px, so the strict complete-crown gate remains NOT_ESTABLISHED. Known geometry metrics use actual8× truth renders, not exact analytic contour distances. Raw common faces can themselves be invalid. Exact polynomial area confirmation independently agrees with the24 collapse counts; numerical intersection/coverage checks are not certified arrangement proofs.

Visible microgeometry intervals are empirical: antialias mixtures remain unclassified, and a blended color could rarely equal an ID color. No blanket fine-detail ROI exemption is applied. Actual high-zoom SVG renders, not enlarged source raster pixels, provide the visual evidence.

## Size-aware publication

Preserve source, pinned dependency metadata, tests, frozen references, labels, candidate graphs, SVGs, representative/native/zoom PNGs, metrics, logs, negative findings and reports. Ordinary Git stores this bounded package; every file is checked against GitHub's50MiB warning and100MiB block. Generated binaries, environments, caches and secrets are excluded.

Unknown-rights external fixture evidence stays local with an explicit manifest and ZIP retrieval requirement. It is not silently omitted or represented as publicly downloadable. If future evidence exceeds ordinary Git limits, use a versioned release/artifact store with SHA256 manifests; never delete historical evidence or rewrite Git history to reduce size.
