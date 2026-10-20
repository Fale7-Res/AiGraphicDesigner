---
trigger: model_decision
description: "Testing, verification, and Definition of Done rules across Geometry, Clean SVG, Visual QA, Typography, Backend API, and Memory Synchronization."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:34Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد الاختبار والتحقق وتعريف الإنجاز (`Verification, Testing & Definition of Done`)

## 1. مستويات الاختبار الإلزامية (`Meaningful Verification Layers`)

| الطبقة / الموديول | الاختبارات المطلوبة لإثبات الكفاءة (`Meaningful Tests`) |
| :--- | :--- |
| **Scene Graph & Z-Order** | التحقق من صحة ترتيب الطبقات من الأسفل للأعلى، وعدم وجود حلقات مفرغة في شجرة الـ `<g>` Groups، وصحة أبعاد الـ Bounding Boxes. |
| **Clean SVG & Anti-Fragmentation** | اختبار أن العنصر ذو الظل (مثل البطاطس/الفلافل) يخرج كـ `<g>` منظم يحتوي على Base Shape + Shadow Shape بعدد نقاط تحكم (`Nodes`) معقول، وليس مئات الشظايا الصغيرة. |
| **Semantic Isolation (Anti-Bleeding)** | اختبار أن عنصرين متجاورين بألوان متقاربة (مثل البطاطس والعيش) يتم فصلهما في طبقتين مستقلتين بنسبة تداخل خاطئ تقترب من الصفر. |
| **Visual QA (50% Opacity / IoU)** | اختبار أن محرك المقارنة يكتشف أي انحراف في الأبعاد أو الانحناءات ويرفض الطبقة إذا قل الـ `IoU` عن الحد المسموح. |
| **Smart Typography** | اختبار مساري النص: (1) مطابقة أقرب فونت، (2) الرسم المطابق مع حفظ الـ Style Identity وإعادة رسم نص معدل بنفس السمك واللون. |
| **Memory & Catalog Sync** | تشغيل `verify_brain_sync.py` و`verify_catalog.py` للتأكد من تطابق أرقام الأسطر (`Lines Start–End`) والمقتطفات وعلاقات الملفات بنسبة 100%. |

## 2. قائمة التحقق النهائية لإنجاز أي مهمة (`Universal Definition of Done Checklist`)

لا تُعلن أي مهمة مكتملة إلا بعد تحقق جميع البنود التالية:
- [ ] تمت قراءة جميع الملفات المعدلة والملفات المرتبطة بها **قراءة كاملة (`Full-File Read`)**.
- [ ] تم تسجيل جميع المكتشفات والخطوات فوراً في `memory/session/ACTIVE_SESSION_WAL.md`.
- [ ] لا توجد أي دالة مكررة في المشروع (تم التحقق عبر `memory/FUNCTION_REGISTRY.md`).
- [ ] تم تحديث ملف المرآة لكل ملف برمجي في `memory/code_mirrors/` بأرقام الأسطر الدقيقة (`Lines Start–End`) والكود الفعلي وعلاقات الملف (`بياخد منين وبيرمي فين`).
- [ ] تم تحديث `memory/FILE_RELATIONSHIPS_GRAPH.md` و`PROJECT_FILE_CATALOG.md`.
- [ ] تم تحديث `memory/session/CURRENT_TASK_CHECKPOINT.md` و`MASTER_PLAN.md`.
- [ ] اجتاز المشروع فحص `python tools/memory_guard/verify_brain_sync.py` وفحص `python tools/project_catalog/verify_catalog.py` بصفر أخطاء.
- [ ] تمت مراجعة التعديلات بواسطة الـ Sub-Agent المراجع المستقل (`qa-reviewer-auditor`).

## Change timestamps & document provenance (mandatory)

Apply `docs/governance/CODE_AND_DOCUMENT_CHANGE_PROVENANCE.md` on every first-party source write and human-authored Markdown edit. Source code: use matched `START CHANGE` and `END CHANGE` comments with real UTC timestamp, change ID, CREATED/EDITED, and agent ID at the smallest logical change block. Markdown: update `DOC_PROVENANCE` and `memory/DOCUMENT_PROVENANCE.json` in the same task; historical unknown creation times must stay unknown. Verify with `python tools/governance/change_tracking.py verify`. Do not edit immutable owner vision, historical snapshots, generated mirrors, or JSON with invalid comments. Update code mirrors, project catalog, and findings revision ledger when applicable.
