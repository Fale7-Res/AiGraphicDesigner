---
trigger: manual
description: "Git-free incremental review package export and snapshot validation rules using updates/ and tools/review_updates/."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:35Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد تصدير حزم المراجعة التراكمية المستقلة (`Incremental Review Update Exports`)

*نظام مستقل لتصدير حزم مراجعة قابلة للتحقق دون الاعتماد على Git.*

## 1. الغرض وآلية العمل

يتيح مجلد `updates/` وأدوات `tools/review_updates/` إنشاء حزم مضغوطة مرقمة (`UPDATE-0001.zip`, `UPDATE-0002.zip`...) تحتوي على جميع ملفات القواعد، والذاكرة الحية (`memory/`)، والكود، والفهارس بعد التحقق من سلامتها.

1. لإنشاء حزمة تحديث جديدة بعد إتمام مهمة والتحقق من الذاكرة:
   `python -B tools/review_updates/export_updates.py export`
2. للتحقق من سلامة الحزمة وبصمات الملفات (`SHA-256`):
   `python -B tools/review_updates/export_updates.py validate --update UPDATE-0001`
3. توجد ثلاث حالات منفصلة في `updates/baselines/state.json`:
   - `LOCAL_SCAN_BASELINE`: حالة الملفات المحلية على القرص.
   - `EXPORTED_UPDATE`: آخر حزمة تم تصديرها والتحقق منها.
   - `REVIEWER_ACKNOWLEDGED_BASELINE`: آخر حزمة أكد المستخدم استلامها ومراجعتها (لا يتم تشغيل `acknowledge` تلقائياً أبداً بدون أمر صريح من المستخدم).
