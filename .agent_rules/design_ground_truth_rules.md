---
trigger: model_decision
description: "Ground-truth visual evidence and geometric provenance rules (AI Graphic Designer visual/geometry source-evidence policy)."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:33Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد مرجعية الحقيقة البصرية والهندسية (`Design Ground-Truth & Visual Evidence Rules`)

*قواعد مستقلة لمرجعية الحقيقة البصرية والهندسية في AI Graphic Designer.*

## 1. التسلسل الهرمي لمصادر الحقيقة (`Visual & Geometric Trust Hierarchy`)

1. **في وضع Magic Layers & Image Editing:** الصورة الأصلية التي قدمها العميل (أو وافق عليها) هي **المصدر الوحيد للحقيقة البصرية (`Visual Source of Truth`)** فيما يخص الأبعاد، الألوان، مواقع العناصر بالبكسل، وشكل الحروف.
2. **في وضع Image Generation:** وصف المستخدم (`User Prompt`) متبوعاً بمخطط الـ Scene Graph المعتمد من العميل بعد معاينة الصورة الكاملة هو **المصدر الوحيد للحقيقة الهيكلية (`Structural Source of Truth`)**.
3. المخرجات الوسيطة (مثل Masks أولية غير مهذبة أو مخرجات Auto-Trace خام قبل التنظيف) هي **وسائل مساعدة للاستكشاف (`Discovery Aids`)** وليست النتيجة النهائية المعتمدة.

## 2. تصنيف الحقائق الهندسية والبصرية (`Fact & Inference Classification`)

لمنع الهلوسة البصرية أو الهندسية، يجب تمييز كل عنصر داخل `SceneGraph` وملفات الذاكرة بأحد التصنيفات الخمسة التالية:
- **`O` (`Observed Pixel/Geometry Fact`):** حقيقة مقاسة مباشرة من الصورة (مثل: اللون السائد `#D4882A`، الـ Bounding Box من `x=120..340, y=80..260`).
- **`S` (`Semantic Grouping Rule`):** علاقة دلالية مؤكدة (مثل: هذا الظل ينتمي لجروب `Potato` وليس لطبقة `Bread`).
- **`I` (`Inferred Occluded Geometry`):** جزء مستنتج عبر الـ Amodal Inpainting لأن طبقة علوية كانت تغطيه؛ يجب تمييزه كجزء مُكمّل (`Inpainted Hidden Region`).
- **`U` (`Unresolved User Preference`):** قرار تصميمي يحتاج تفضيل المستخدم (مثل: هل نرسم النص كـ Vector مطابق أم نستبدله بأقرب خط قابل للكتابة؟).
- **`P` (`Proposed Clean Vector Path`):** مسار الـ Bézier المقترح بعد التبسيط، والذي ينتظر اجتياز بوابة الـ `50% Opacity / IoU Critic` لاعتماده.

## 3. الفحص الآمن وحفظ الأصول (`Safe Asset Inspection & Provenance`)

- لا تقم أبداً بالكتابة فوق الصورة الأصلية التي رفعها المستخدم؛ احفظها ببصمة `SHA-256` في مخزن الأصول (`assets/originals/`) واشتغل على نسخ مشتقة في مجلد العمل.
- سجل لكل عملية تحويل أو تفكيك مقاييس الجودة الفعلية (`IoU`, `SSIM`, `Node Count`, `Layer Count`) في سجل التجارب والأصول ولا تدّعِ نجاح التطابق البصري بدون تشغيل أداة الفحص الفعلي.
