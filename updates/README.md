<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# حزم المراجعة التراكمية المستقلة (`updates/README.md`)

مجلد مخصص لتوليد حزم المراجعة المستقلة عن Git.
- لتوليد حزمة تحديث جديدة بعد التحقق من الذاكرة والفهرس:
  `python3 -B tools/review_updates/export_updates.py export`
- للتحقق من سلامة الحزمة:
  `python3 -B tools/review_updates/export_updates.py validate --update UPDATE-0001`
- لتأكيد مراجعة الحزمة من قبل المالك (لا يُنفذ تلقائياً أبداً):
  `python3 -B tools/review_updates/export_updates.py acknowledge --update UPDATE-0001 --by Owner --note "Reviewed" --confirm-reviewed`
