<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T07:04:50Z", "last_action": "CREATED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T07:04:50Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T07:04:50Z"}
END_DOC_PROVENANCE -->
# AI Graphic Designer — دليل تشغيل الحوكمة النهائية

**الحالة بتاريخ 2026-10-17T07:04:49Z:** ملفات قواعد وأدوات حوكمة فقط؛ **تنفيذ التطبيق غير مسموح بعد**، المعمارية `NOT_APPROVED`، وتجارب الجدوى `NOT_RUN`. هذا المستودع مستقل بذاته ولا يحتاج لأي مشروع آخر أو ملفات خارجية قديمة لتشغيل القواعد.

## نقطة البداية

1. افتح المجلد المستخرج في Google Antigravity على Windows أو Linux.
2. اقرأ `AGENTS.md` ثم `GEMINI.md` و`memory/MEMORY_INDEX.md` و`memory/session/CURRENT_TASK_CHECKPOINT.md`.
3. اقرأ `docs/product/OWNER_ORIGINAL_VISION.md` باعتباره مرجع المتطلبات الأصلي؛ لا تعدله أو تعدل Baseline التاريخي.
4. استخدم `docs/governance/CODE_AND_DOCUMENT_CHANGE_PROVENANCE.md` للتوثيق اللحظي لتغييرات الكود والـMarkdown.
5. راجع `memory/findings/FINDINGS_LEDGER.md` و`memory/decisions/OWNER_APPROVAL_PROVENANCE.json` قبل تنفيذ أي مهمة.

## تجهيز البيئة

- **Python 3.11+** مطلوب. على Windows جرّب `python --version`؛ لو مش متاح اضبط مفسر Python 3 في إعدادات Antigravity/الـHooks قبل التشغيل. تستدعي `.agents/hooks.json` الأمر `python` بدل افتراض توفر `python3`.
- قفل العمليات يستخدم `msvcrt` على Windows و`fcntl` على Linux/macOS، ولا يضيف ملفات Lock داخل مستودع المشروع.
- لا تحتاج مكتبات Python خارجية لتشغيل أدوات الحوكمة الأساسية. أي API/model/SDK جديد يحتاج دراسة واعتماد مستقل.

## تغيير كود — تسجيل Start/End

```python
# START CHANGE TASK-0001 | 2026-10-17T07:20:30Z | CREATED | Author: implementation-engineer
def example():
    return 1
# END CHANGE TASK-0001 | 2026-10-17T07:20:30Z | CREATED
```

- ضَع الزوج حول كل جزء منطقي تكتبه أو تعدله، بالوقت الحقيقي بصيغة UTC والتصنيف `CREATED` أو `EDITED` ومعرّف التغيير واسم الـAgent.
- في TypeScript/JavaScript استخدم `// START CHANGE` و`// END CHANGE`؛ أما JSON أو الملفات المولدة التي لا تقبل التعليقات فلا تكسر صيغتها، وسجل التغيير في Sidecar والتوثيق المرتبط بالمهمة.
- التعليقات بتوثق وقت **إجراء التغيير**، مش بالضرورة وقت أول إنشاء للكود الموجود قبل هذا النظام. أدوات الفحص بتتأكد من صحة أزواج التعليقات، أما التحقق من تغطية كل Diff فمسؤولية المراجع وGit/CI.

## تعديل Documentation — معرفة إذا الملف جديد أو متعدل

- كل Markdown بشري قابل للتعديل يحمل `DOC_PROVENANCE`، وسجل أحداث في `memory/DOCUMENT_PROVENANCE.json`.
- ملفات قبل بدء التتبع حالة `IMPORTED_LEGACY` وتواريخ الإنشاء القديمة غير المعروفة تُترك `null` حتى لا نختلق تواريخ.
- مثال إنشاء مستند Markdown جديد ثم تسجيله:

```powershell
python tools/governance/change_tracking.py edit-document --file docs/NEW.md --kind CREATED --change-id TASK-001 --editor architecture-reviewer
```

- مثال تعديل مستند مسجّل بالفعل:

```powershell
python tools/governance/change_tracking.py edit-document --file docs/NEW.md --kind EDITED --change-id TASK-002 --editor architecture-reviewer
```

- لا تطبق هذه الأداة على نص الرؤية الأصلي أو نسخ Findings التاريخية أو الملفات المولدة. اتبع بروتوكول الـPromotion/Revision عند تعديل مستند فيه معلومات معتمدة سابقًا.

## فحوص التسليم

```powershell
python tools/memory_guard/sync_rules.py --write
python tools/memory_guard/sync_code_mirrors.py --write
python tools/project_catalog/build_catalog.py --write
python tools/governance/change_tracking.py verify
python tools/findings_guard/manage_findings.py verify
python tools/memory_guard/verify_brain_sync.py
python tools/project_catalog/verify_catalog.py
python -m unittest tools.tests.test_governance_suite -v
python -m unittest tools.tests.test_final_governance -v
```

**نتائج مراجعة هذه الحزمة:** 24/24 اختبارًا أصليًا و6/6 اختبارات إضافية في بيئة Linux المعزولة، مع نجاح أدوات فحص الذاكرة والفهرس. تم اختبار انتقال الاعتماد الكامل والرجوع بعد الفشل على نسخ اصطناعية منفصلة. **اختبار واجهة Antigravity الفعلية وتشغيل Windows الأصلي ما زالا مطلوبين على جهاز المطور** قبل إعلان دعم تام.

## حدود الاعتماد

- لا يستطيع أي ملف Markdown أو SHA محلي إثبات هوية مالك المشروع ضد Agent لديه صلاحية كتابة واسعة. استخدام `--confirm-owner-authorized` وسجلات التجارب الفنية لا يكفي وحده للموافقة الموثوقة؛ استخدم مراجعة بشرية خارجية، صلاحيات Git والفروع المحمية، أو توقيعًا خارجيًا موثوقًا عند الحاجة.
- لا تحول تقارير تجارب شكلية إلى إثبات علمي. تقارير الاختبارات الاصطناعية داخل Suite محاكاة لا تعني نجاح تجربة SVG أو موديل AI.
- أي تعديل مستقبلي يحتاج تحديث مرايا الكود وسجل الملفات وتواريخ التوثيق في نفس المهمة؛ لا تُعلن PASS بدون تشغيل الأمر وفحص مخرجاته.
