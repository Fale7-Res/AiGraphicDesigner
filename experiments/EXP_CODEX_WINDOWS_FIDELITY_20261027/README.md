<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T10:42:21Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T10:44:03Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T10:42:21Z"}
END_DOC_PROVENANCE -->
# Native Windows fidelity research extension

Architecture **NOT_APPROVED**. Read [technical assessment](reports/TECHNICAL_ASSESSMENT.md). Historical experiments are preserved.

The original adaptive entry point cannot import on Windows (`resource`). Use this experiment's `optimizer.py`; its candidate generation and selection are AST-equivalent to the inherited source. Renderer selection is explicit, with no silent fallback. Measured renderer is resvg 0.49.0; Inkscape startup was not validated locally.

## Reproduce

Create an isolated Python 3.14 environment and install `requirements-windows.txt`. The measured environment used system site packages with only pinned VTracer installed locally; `reports/environment.json` records effective versions. A fresh minimal environment with these Windows pins has not been separately validated.

Download the official [resvg 0.49.0 Windows archive](https://github.com/linebender/resvg/releases/download/v0.49.0/resvg-win-x86_64.zip), SHA-256 `38af9631b37e61118a32a5ef31e6be6af083eda63b4c17ffc4fdc63e449277df`, and extract locally. Do not commit runtimes or virtual environments.

PowerShell, from this experiment directory (substitute your environment executable):

```powershell
$env:PYTHONDONTWRITEBYTECODE = "1"
$env:AGD_RENDERER = "resvg"
$env:AGD_RENDERER_EXE = "C:\path\to\resvg.exe"
python run_inherited_tests.py
python verify_portability.py
python optimizer.py --input ..\EXP_VTRACER_FIDELITY_20261024\inputs\A03_burger_layers.png --output fresh_burger --max-candidates 24 --max-seconds 240
python optimizer.py --input inputs\N01_local_gradient_shapes.png --output fresh_local --max-candidates 24 --max-seconds 240
python validate_local.py --saved
python validate_local.py --case A03_burger_layers
python verify_alpha_geometry.py
python alpha_optimizer.py --input inputs\N02_local_soft_alpha.png --output fresh_alpha --max-candidates 13 --max-seconds 240
python scoped_governance.py --mirrors --documents
```

Use new empty destinations. `--repeat` refuses prior reproduction evidence. Local validation paths reference delivered `results/`; single-image fresh CLI output remains independently inspectable via ranking/config/render files.

`alpha_optimizer.py` is experimental: opaque RGB search then source-alpha vector mask; multiple-background metrics are post-selection. It does not change the inherited default. Read its result and limitations before use. Native comparison PNGs and actual SVGs live in each result directory. All trial failures and successful candidates are retained. No semantic/clean-vector or production-architecture claim is made.
