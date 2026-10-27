<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T09:03:45Z", "last_action": "CREATED", "last_change_id": "ADAPTIVE-DELIVERY", "last_edited_at_utc": "2026-10-27T09:03:45Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T09:03:45Z"}
END_DOC_PROVENANCE -->
# Install and verify

Extract directly into your local AiGraphicDesigner root. Only experiments/EXP_ADAPTIVE_VTRACER_20261027/ is added. Existing path collision: extract separately for review; do not overwrite. Requires existing committed EXP_VTRACER_FIDELITY_20261024.

Read README.md for dependency install, four unit tests and conversion commands. Open index.html for all18 native comparison reports. Check reports/ARTIFACT_CLOSURE.json errors is empty, reports/tests_final.log is OK, and verify DELIVERY_MANIFEST.json hashes. Manifest lists everypayload except itself (selfhash is impossible); ZIP CRC validates it.

After review, from projectroot:

```bash
git add experiments/EXP_ADAPTIVE_VTRACER_20261027
git commit -m "[AGD-ASTRA-RESEARCH] Add adaptive multi-mode fidelity optimizer and18input evidence"
git push origin main
```

No successfulremote push was available in research environment. Do not duplicate a commit if integrating a provided localcommit separately. Architecture NOT_APPROVED.
