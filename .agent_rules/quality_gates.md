---
trigger: model_decision
description: "Mandatory 12-step implementation quality gate, visual/geometric SVG QA gate, and independent reviewer sub-agent audit before marking any task complete."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:36Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# بوابات الجودة الإلزامية قبل إتمام أي مهمة (`Mandatory Implementation & Visual Quality Gates`)

لا يجوز لأي Agent الإبلاغ عن انتهاء مهمة برمجية (`Done / Completed`) بمجرد أن الكود "يشتغل في الحالة العادية". يجب اجتياز البوابات التالية بالكامل:

## 1. بوابة مراجعة الكود ومنع التكرار (`Code & Anti-Duplication Gate`)

1. **القراءة الكاملة ومراجعة التغييرات (`Whole-Change-Set Full Read`):**
   - مراجعة جميع الملفات التي تم تعديلها والملفات التي تستدعيها (`Callers`) أو تستدعي هي دوالها (`Callees`) عبر قراءتها كاملة.
2. **فحص عدم تكرار الدوال (`Zero Duplicated Functions Check`):**
   - التأكد عبر `memory/FUNCTION_REGISTRY.md` وأداة `verify_brain_sync.py` من عدم كتابة أي دالة مكررة الاسم أو الوظيفة في المشروع.
3. **فحص نظافة الكود (`Maintainability & Modularity`):**
   - عدم وجود أرقام سحرية غير مفسرة (`Magic Constants`)، أو دوال ضخمة غير مقسمة، أو كود ميت (`Dead Code`)، أو استيرادات غير مستخدمة.

## 2. بوابة الجودة الهندسية والبصرية الخاصة بـ AI Graphic Designer (`Domain Visual & Vector Gate`)

لأي كود يمس توليد الصور، أو تفكيك الطبقات (`Magic Layers`)، أو رسم وتعديل الـ `SVG`:
1. **اختبار عدم التشظي (`Anti-Fragmentation Check`):** التأكد من أن العناصر ذات التفاصيل اللونية (مثل الفلافل/البطاطس) تُجمع في `<g id="...">` نظيف يضم الشكل الأساسي والظل كقطعة نظيفة، ولا تتحول إلى مئات المسارات المشرذمة.
2. **اختبار الفصل الدلالي (`Semantic Separation Check`):** التأكد من عدم اندماج بكسلات عنصرين مختلفين (مثل البطاطس والعيش) في طبقة واحدة.
3. **اختبار المطابقة البصرية (`50% Opacity / IoU / SSIM Gate`):** التحقق من أن حساب التطابق الهندسي بين الطبقة المرسومة والصورة الأصلية يعمل بدقة ويرفض الطبقات غير المتطابقة.
4. **صحة وصلاحية كود الـ SVG (`Clean XML/SVG Validation`):** التأكد من أن ملف الـ SVG الناتج صالح قياسياً (`Valid XML`)، مرتب الـ `Z-Order` من الخلف للأمام، ويفتح في Illustrator وFigma وPhotoshop بدون أخطاء.

## 3. التسلسل الإلزامي المكون من 12 خطوة قبل الإغلاق (`12-Step Pre-Completion Sequence`)

1. قراءة الملفات المستهدفة بالكامل (`Full-File Read`).
2. تنفيذ الكود مع تسجيل الملاحظات لحظياً في `memory/session/ACTIVE_SESSION_WAL.md`.
3. تشغيل فحوصات الأنواع والـ Syntax (`Type Check / AST Parse / Linter`).
4. تشغيل الاختبارات الوظيفية والحالات السلبية والحافة (`Functional, Negative & Boundary Tests`).
5. تشغيل `python tools/memory_guard/sync_code_mirrors.py --write` لتحديث أرقام الأسطر (`Lines Start–End`) والمقتطفات في `memory/code_mirrors/` و`memory/FUNCTION_REGISTRY.md`.
6. كتابة/تحديث الوصف التفصيلي وعلاقات الملفات (`بياخد منين وبيرمي فين`) في ملف المرآة وفي `memory/FILE_RELATIONSHIPS_GRAPH.md`.
7. تحديث `PROJECT_FILE_CATALOG.md` وتشغيل `python tools/project_catalog/verify_catalog.py`.
8. تشغيل `python tools/memory_guard/verify_brain_sync.py` والتأكد من نجاحه بنسبة 100%.
9. تحديث `memory/session/CURRENT_TASK_CHECKPOINT.md` و`MASTER_PLAN.md`.
10. **استدعاء الـ Sub-Agent المراجع المستقل (`qa-reviewer-auditor`)** لمراجعة الكود والذاكرة.
11. إصلاح أي ملاحظات (`CRITICAL / HIGH / MEDIUM`) يكتشفها المراجع المستقل وإعادة الفحص.
12. تقديم التقرير النهائي للمستخدم مع ذكر الملفات المعدلة ونتائج التحقق.
