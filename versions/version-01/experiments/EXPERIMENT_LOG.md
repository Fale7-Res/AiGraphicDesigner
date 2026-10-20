<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "EDITED", "last_change_id": "TASK-V01-CORRECTION-01", "last_edited_at_utc": "2026-10-17T18:21:15Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# Experiment Execution Log: Version 01 (`EXPERIMENT_LOG.md`)

**الإصدار:** `version-01`  
**الحالة:** معلق بانتظار اعتماد المالك لتجارب الجدوى (`PENDING_OWNER_FEASIBILITY_APPROVAL`)  
**مبدأ النزاهة:** لا توجد نتائج مفبركة؛ تُسجل القياسات الحقيقية فقط بعد تنفيذ الاستدلال الفعلي.

---

## 1. سجل التجارب المخططة (`Planned Experiments`)

| المعرف | الأصل | الهدف المرجو | العتاد المخطط | الحالة |
| :--- | :--- | :--- | :--- | :--- |
| `EXP-VER01-A01` | `A01` درع الهوية | قياس عدد العقد وزمن الاستجابة لملاءمة المنحنيات الهندسية. | RTX 4090 (24GB) | `PENDING_APPROVAL` |
| `EXP-VER01-A02` | `A02` طبق الفلافل | اختبار صمود خوارزمية شنايدر ضد تفتت مسارات الظلال الملتصقة. | RTX 4090 (24GB) | `PENDING_APPROVAL` |
| `EXP-VER01-A03` | `A03` البرجر المعقد | قياس دقة استكمال الطبقات المحجوبة عبر LaMa. | RTX 4090 (24GB) | `PENDING_APPROVAL` |
| `EXP-VER01-A04` | `A04` الخط العربي | تقييم جودة المنحنيات المتصلة للأحرف والتشكيل. | RTX 4090 (24GB) | `PENDING_APPROVAL` |

---

## 2. سجل التجارب المنفذة فعلياً (`Executed Experiments`)

### `EXP-V01-PRELIM-01` — الاختبارات البصرية الأولية على الصور الـ 12 (`PRELIMINARY_VISUAL_TESTS`)
- **تاريخ التنفيذ:** 2026-10-17T09:53:18Z
- **العتاد المنفذ عليه:** المعالج المركزي للابتوب الشخصي (Local Windows CPU / Zero Cloud GPU / Zero API Cost).
- **مجموعة البيانات المستخدمة:** الصور الـ 12 الأولية المقتطعة في `AI_Graphic_Designer_Test_Images_Initial_12/` (ليست Benchmark نهائي).
- **التقرير والمخرجات الموثقة:**
  - التقرير الشامل: `experiments/preliminary_visual_tests/PRELIMINARY_VISUAL_TESTS_REPORT.md`
  - مصفوفة القياس: `experiments/preliminary_visual_tests/results_summary.json`
  - ملفات الـ SVG المولدة: 12 ملفاً في `experiments/preliminary_visual_tests/outputs/` (`A01` إلى `A12`)
- **المقاييس الحسابية الإجمالية:**
  - عدد الصور: 12 صورة
  - إجمالي المسارات: 1,896 مساراً
  - إجمالي العقد: 28,478 عقدة
  - إجمالي زمن التنفيذ: 2,703.4 مللي ثانية (~2.7 ثانية)
  - إجمالي حجم ملفات الـ SVG: 1.44 ميجابايت
- **الحالة والنتيجة:** `COMPLETED_PRELIMINARY_TESTS` — نجاح تقني دون انهيار برمجي، مع كشف وتوثيق 5 أنماط فشل هندسية جوهرية (انفجار المسارات، فقدان الشفافية، تشوه الخط العربي، غياب الاستكمال المحجوب، وانهيار التجميع الدلالي) تقدم دليلاً تجريبياً قاطعاً على حتمية حلول `version-02` و`version-03`.

### `EXP-V01-CORRECTION-01` — دورة تصحيح الدقة البصرية وتحديث مخرجات الصور الـ 12 (`VISUAL_CORRECTION_CYCLE`)
- **تاريخ التنفيذ:** 2026-10-17T21:20:00Z
- **العتاد المنفذ عليه:** المعالج المركزي للابتوب الشخصي (Local Windows CPU / Zero Cloud GPU / Zero Paid APIs).
- **مجموعة البيانات:** الصور الـ 12 الأولية في `AI_Graphic_Designer_Test_Images_Initial_12/`.
- **التقرير والمخرجات الموثقة:**
  - التقرير الشامل: `experiments/fidelity_diagnostics/VERSION_01_VISUAL_CORRECTION_CYCLE_REPORT.md`
  - مصفوفة القياس المحدثة: `experiments/fidelity_diagnostics/all_12_rerun_metrics.json`
  - مخرجات SVG المحدثة الـ 12: `experiments/preliminary_visual_tests/outputs/` (`A01` إلى `A12` محدثة بالكامل)
  - الصور المصيرة المرجعية الـ 12: `experiments/fidelity_diagnostics/rendered_pngs/`
- **المقاييس الحسابية الإجمالية:**
  - عدد الصور: 12 صورة
  - إجمالي المسارات: 7,781 مساراً
  - إجمالي العقد: 133,647 عقدة
  - إجمالي زمن المعالجة: 4,157.8 مللي ثانية (~4.1 ثانية)
  - متوسط PSNR: 18.19 dB (أعلى دقة: A05 بـ 20.75 dB و A01 بـ 19.91 dB)
  - متوسط SSIM: 0.6218 (أعلى تشابه: A01 بـ 0.7679 و A10 بـ 0.7641)
  - إجمالي حجم ملفات SVG: 6.81 ميجابايت
- **الحالة والنتيجة:** `COMPLETED_CORRECTION_CYCLE` — تحديث كافة ملفات SVG الـ 12، فض تباين إحصائيات A01 (139 مساراً و 3,368 منحنى C فعلياً)، تصحيح مقياس استرجاع الذهب (Recall = 68.0%, Precision = 73.7%, IoU = 54.8%)، تثبيت البذرة العشوائية الحتمية لضمان 100% تطابق بايتي، وإثبات أن التدهور البصري بنسبة 72-85% ينشأ من التقطيع المضلعي وشروخ الحدود التحت-بكسلية.


