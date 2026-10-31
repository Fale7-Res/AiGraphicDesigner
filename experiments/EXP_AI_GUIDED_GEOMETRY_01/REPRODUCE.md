<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:16:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:16:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:16:24Z"}
END_DOC_PROVENANCE -->
# Reproduction without live API calls

Use the existing isolated runtime, from the original Codex workspace:

```powershell
Set-Location -LiteralPath 'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth'
& '.\work\agd-native\Scripts\python.exe' 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01\replay_saved_session.py' --case K01_linear_corner_hole --condition M
```

This exact command was validated. The existing `work/agentic_geometry/owner_replay/K01_linear_corner_hole/M` contains its proof and intentionally cannot be overwritten. For a fresh owner replay choose another saved case/condition or a separate empty workspace replica. The script checks exact final geometry and semantic-decision hashes. Event durations/hashes may differ; no provider is used. Every one of the seven M replays is already preserved under each case/replay_M.

Unit tests (no real network):

```powershell
& '.\work\agd-native\Scripts\python.exe' -m unittest discover -s 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01' -p 'test_*.py' -v
```

Dry-run provider request into a NEW named folder (no credentials/network):

```powershell
& '.\work\agd-native\Scripts\python.exe' 'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01\groq_pilot.py' --session-label owner_dryrun_01
```

The identifier accepts only letters/numbers/underscores and never a path. It creates a new `C_dry_run_owner_dryrun_01` under the fixed Burger case; repeated identical labels refuse overwrite. No key is read and no API request is made. `C_dry_run_final_validation` already preserves a successful final-code dry-run.

Dependencies already installed: Python3.14.2, NumPy2.4.4, SciPy1.18.1, skimage0.26, OpenCV4.14, Pillow12.1.1, psutil7.2.2, Shapely2.2 under work/geometry-deps, resvg0.49 under work/resvg. No SDK/model installation is needed. Runtime cwd/work paths are explicit trusted application configuration, not model arguments. Source and constructor pins are in protocol.json; keep historical imports unchanged.

`run_sessions.py` builds the frozen matrix only into empty folders and should not be rerun on delivered evidence. To reproduce the entire matrix, use a separate clone/workspace and configure its experiment destination; do not delete/overwrite delivered output. Evaluation uses independent refs only after construction. The first-party H03 sourceSVG is evaluator-only; do not use it to construct curves. No private FineFeatures assets are used in this cycle.

Live inference is NOT enabled by these commands. The explicit --live switch additionally requires recent trusted account free-plan/quota/model/no-charge proof and authorized image hashes. A dynamic second preview requires reviewed authorization; no automatic wildcard permission. Never place account proof or keys in this repository. Do not reuse the exposed chat credential. No paid request is approved.
