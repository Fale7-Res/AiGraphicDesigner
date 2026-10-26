<!-- DOC_PROVENANCE
{"created_at_utc": null, "tracking_started_at_utc": "2026-10-25T15:05:18.618308+00:00", "last_edited_at_utc": "2026-10-25T15:05:18.618308+00:00", "last_action": "EDITED", "last_change_id": "VTRACER-DELIVERY", "last_editor": "parent"}
END_DOC_PROVENANCE -->
# Consolidated research installation

Architecture NOT_APPROVED. The ZIP uses project-root-relative paths with no extra AiGraphicDesigner wrapper. It adds only:

- `experiments/EXP_VTRACER_FIDELITY_20261024/`
- `updates/DELIVERY_VTRACER_20261025/`

Four prior packages are not duplicated because their accessible files have no undelivered delta. See `reports/RECOVERY_COVERAGE.md`. Your local incorporation state cannot be verified remotely.

## Extract and verify safely

If both directories are absent, extract directly into your local AiGraphicDesigner project root using **never overwrite** mode. For possible collisions, extract into a temporary staging directory instead and run:

```bash
python /path/to/staging/updates/DELIVERY_VTRACER_20261025/install_delivery.py
python /path/to/staging/updates/DELIVERY_VTRACER_20261025/install_delivery.py --destination /path/to/AiGraphicDesigner
```

The first command verifies every manifest entry. The second skips identical files and copies differing collisions into a new `updates/REVIEW_COLLISIONS_VTRACER_<UTC>/` directory, preserving relative paths. It never overwrites existing files. A symlink or a regular file blocking an intermediate directory stops installation safely; resolve it manually. Review the printed conflict list. No collision in the available repository snapshot establishes nothing about your unseen local filesystem.

## Dependencies and reproduction

From the project root:

```bash
python updates/DELIVERY_VTRACER_20261025/install_delivery.py
cd experiments/EXP_VTRACER_FIDELITY_20261024
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
inkscape --version
python -m unittest discover -s src -p 'test*.py'
python reproduce.py --destination ../EXP_VTRACER_REPRODUCTION_LOCAL --run
```

Measured environment: Python3.12, Linux, Inkscape1.2.2. Use Linux/WSL and install Inkscape/Cairo with your OS package manager. Native Windows and different renderer versions are unverified. Dependencies are pinned; virtual environments and downloaded binaries are excluded. No model/API costs are required. Allow several GB for extraction plus a fresh reproduction.

The reproduction destination must not exist. Omit `--run` to prepare only. The launcher copies source/data to a fresh location and executes primary search, frozen holdouts, historical renders, fixed-geometry refits, clustering controls, summaries, renderer checks and color diagnostics. Its preparation/refusal behavior was tested; all underlying stages were executed previously, while the new whole launcher was not redundantly replayed at delivery.

## Evidence and checklist

- Verify ZIP integrity and manifest hashes.
- Review any reported installation collisions.
- Read `reports/REPORT.md`, `RESULTS.md`, `QA_AUDIT.md`, `RECOVERY_COVERAGE.md`.
- Inspect `best_outputs/` and `comparisons_final/`, especially shield shadow, juice, cup and Arabic lettering.
- Run research tests and optionally reproduce in a fresh directory.
- Review dense pixel-derived geometry: genuine SVG is not automatically clean scalable artwork.
- Keep architecture NOT_APPROVED and the fidelity milestone unpassed.

`DELIVERY_MANIFEST.json` lists every archive path, size, hash, status, experiment and role. All files have ordinary byte SHA-256 except the manifest self-entry: `canonical_manifest_self_v1` hashes sorted compact JSON after setting only its own size to0 and hash to null. This explicit convention avoids impossible self-referential byte hashing; actual manifest size is checked separately. Archive byte SHA-256 is supplied outside the archive. No signature or approval is implied.

## Optional Git commands — owner only, after review

From your local project root, verify branch/remote and file sizes before staging:

```bash
git status --short
git branch --show-current
git remote -v
git add -- experiments/EXP_VTRACER_FIDELITY_20261024 updates/DELIVERY_VTRACER_20261025
git diff --cached --stat
git commit -m "Add bounded VTracer fidelity research and evidence"
git push origin main
```

Only push when the reviewed commit is on your intended local main branch and origin is your repository. The assistant did not create branches, commit, push or merge. These instructions do not change that prohibition.
