---
name: sync-brain-and-mirrors
description: "Synchronizes code files with their 1:1 Markdown mirrors in memory/code_mirrors/, updates exact line numbers (StartLine-EndLine) and verbatim snippets in memory/FUNCTION_REGISTRY.md, and validates zero duplicate functions."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:41Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# Skill: Sync External Brain & Codebase Mirrors (`sync-brain-and-mirrors`)

اتبع هذه الخطوات في كل مرة تنشئ أو تعدل فيها أي ملف برمجي في المشروع:

## الخطوة 1: تشغيل المزامن الآلي لأرقام الأسطر والمقتطفات
شغّل الأمر التالي في الطرفية لتوليد/تحديث أرقام الأسطر الدقيقة (`Lines Start–End`) ومقتطفات الكود الفعلي وفحص الدوال المكررة:
```bash
python tools/memory_guard/sync_code_mirrors.py --write
```

## الخطوة 2: استكمال الوصف الدلالي وخريطة العلاقات (`بياخد منين وبيرمي فين`)
افتح ملف المرآة في `memory/code_mirrors/<file_path>.md` وتأكد من تعبئة:
1. الغرض التفصيلي من الملف وكل دالة بداخله (بالعربية الواضحة مع المصطلحات التقنية الدقيقة).
2. جدول العلاقات (`Upstream Inputs / Callers` و`Downstream Outputs / Callees`).
3. تحديث `memory/FILE_RELATIONSHIPS_GRAPH.md` و`PROJECT_FILE_CATALOG.md` إذا تغيرت العلاقات أو أُضيف ملف جديد.

## الخطوة 3: تشغيل التحقق الإلزامي
```bash
python tools/memory_guard/verify_brain_sync.py
python tools/project_catalog/verify_catalog.py
```
لا تنتقل للخطوة التالية إلا إذا أرجع الفحصان `0 errors`.
