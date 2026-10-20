<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T02:07:56Z", "last_action": "CREATED", "last_change_id": "TASK-UPDATE-SYS-CORRECTION-01", "last_edited_at_utc": "2026-10-18T02:07:56Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-18T02:07:56Z"}
END_DOC_PROVENANCE -->
# تقرير حادثة حوكمية وهندسية: خط الأساس المصطنع وحزم التحديثات غير المكتملة (`INCIDENT-UPDATE-BASELINE-01`)

**معرف الحادثة:** `INCIDENT-UPDATE-BASELINE-01`  
**تاريخ الرصد والتوثيق:** 2026-10-18T01:55:00Z  
**الجهة الراصدة:** المالك المستقل عبر التدقيق الفيزيائي للأرشيف المصدر (`Owner Independent Inspection`)  
**المشروع:** AI Graphic Designer  
**الحالة:** `CONFIRMED — UNDER_CORRECTION`  
**مستوى الخطورة:** `CRITICAL (P0 — Correctness, Trust & Security Failure)`  

---

## 1. التوصيف الدقيق للمشكلة (`Incident Description`)
أظهر الفحص المستقل للأرشيف المصدر `AGD_UPDATE_0001_20261018T012312Z.zip` أنه يحتوي على:
- `24 ADD`
- `0 MODIFY`
- `0 DELETE`
- `0 RENAME`
- `0 EXCLUSIONS`

على الرغم من أن المهمة السابقة (`TASK-V04-V09-CORRECTION-01` و `TASK-UPDATE-SYS-01`) تضمنت تعديلات جوهرية على ملفات كود وتوثيق وفهارس حوكمية كانت موجودة مسبقاً في المستودع (مثل `tools/project_catalog/build_catalog.py` و `verify_catalog.py` و `VERSION_REGISTRY.md` و `memory/session/CURRENT_TASK_CHECKPOINT.md` و `memory/session/ACTIVE_SESSION_WAL.md` و `DOCUMENT_PROVENANCE.json` و `FUNCTION_REGISTRY.md` و `PROJECT_FILE_CATALOG.md` وغيرها)، إلا أن الأرشيف أسقط هذه التعديلات بالكامل ولم يعكس سوى الملفات المنشأة حديثاً.

---

## 2. التحليل الجذري للسبب (`Root Cause Analysis`)
حدث الخلل نتيجة تسلسل تنفيذي غير سليم في بناء خط الأساس:
1. تم إنجاز التعديلات البرمجية والتوثيقية أولاً في مساحة العمل.
2. تم استدعاء أمر تهيئة الأساس `init-baseline` بعد إتمام التعديلات، مما أدى لمسح بيئة العمل وهي معدلة بالفعل وتسميتها `BASE_20261018_INITIAL`.
3. تم نسخ هذا الجرد إلى `BASE_PRE_TASK_SNAPSHOT`، ثم حُذفت منه مسارات الملفات الجديدة فقط (الكود الجديد لنظام التحديث ووثائق المقترحات المعمارية الجديدة)، مع إبقاء بصمات الملفات المعدلة كما هي في الحالة الراهنة.
4. تم إسناد طابع زمني مصطنع بأثر رجعي لهذا الأساس المعاد تركيبه يدوياً.
5. عند تشغيل مقارن الفروقات `InventoryDiffer` لحساب دلتا الأرشيف، وجد المقارن أن بصمات SHA-256 للملفات المعدلة متطابقة تماماً بين الأساس المصطنع والهدف الراهن، فصنفها كـ `UNCHANGED`، واختفت كافة التعديلات القائمة من الأرشيف.

**النتيجة الهندسية:** خط الأساس يجب أن يمثل حالة مستودع حقيقية كانت موجودة تاريخياً بالفعل، ولا يجوز مطلقاً هندسته عكسياً أو استنتاجه من بيئة عمل معدلة.

---

## 3. الأصول والحزم المتأثرة (`Affected Artifacts`)
1. **خطوط الأساس المصطنعة:**
   - `tools/update_packages/registry/baselines/BASE_PRE_TASK_SNAPSHOT.json`: وُسمت كـ `INVALID_FABRICATED_BASELINE` / `UNTRUSTED`.
   - `tools/update_packages/registry/baselines/BASE_20261018_INITIAL.json`: وُسمت كـ `INVALID_FABRICATED_BASELINE` / `UNTRUSTED`.
   *(تم الاحتفاظ بملفاتهما في السجل كأثر تدقيقي وتاريخي دائم دون حذف، مع حظر استخدامهما أو اعتمادهما في أي تصدير).*
2. **حزم التحديث المصدرة:**
   - `exports/updates/AGD_UPDATE_0001_20261018T012312Z.zip`: وُسمت كـ `INCOMPLETE / UNTRUSTED_FOR_RECONSTRUCTION`.
   - `exports/updates/AGD_UPDATE_0002_20261018T012318Z.zip`: وُسمت كـ `INCOMPLETE / UNTRUSTED_FOR_RECONSTRUCTION`.

---

## 4. خطة التصحيح والمعالجة الشاملة (`Remediation Plan`)
1. **تصحيح سياسة الأساسات:**
   - التصريح الشفاف بأنه لا يوجد مستودع Git محلي أو أرشيف تاريخي شامل للمستودع قبل المهمة الأخيرة على الجهاز.
   - إنشاء خط أساس أصيل ومعلن وصريح (`NEW BOOTSTRAP SNAPSHOT`) دون أي فبركة لطوابع زمنية أو سجلات Git.
2. **سد الثغرات الأمنية في المسارات (Security Path Traversal):**
   - تعديل `verifier.py` و `applier.py` لتدقيق كافة الحقول القادمة من المانيفست (`entry.path`, `payload_path`, `renamed_from`) وحظر `..` والمسارات المطلقة ومحركات الأقراص وأسماء UNC وحظر أي مسار خارج المستودع.
3. **تصحيح فحص شمولية الأساس (Strict Base Inventory Validation):**
   - منع نجاح التطبيق (`dry-run` أو الفعلي) على مجلد غير متطابق؛ وفرض فحص شمولية جرد الأساس كاملاً لكافة الملفات المشروطة قبل كتابة أي ملف.
4. **التطبيق التبادلي الحقيقي (Transactional Atomic Apply):**
   - تطبيق التحديثات عبر Staging مؤقت، مع أخذ نسخ احتياطية للملفات المستهدفة وإجراء التراجع الكامل (`Atomic Rollback`) بنسبة 100% في حال حدوث أي خطأ، بحيث لا تترك أي ملفات مشوهة.
5. **ضبط الماسح ومكافحة التجاهل الصامت (Fail-Closed Scanner):**
   - منع تجاهل أخطاء `(OSError, PermissionError)` وإعلان الفشل الصريح، ورصد التعديلات المتزامنة أثناء التصدير.
6. **بناء الاختبارات الصارمة الإلزامية وتصدير الحزمة المصححة:**
   - بناء الاختبارات السلبية الـ 4 المحددة من المالك وإعادة تشغيل جناح الاختبارات واختبار القبول الشامل.
