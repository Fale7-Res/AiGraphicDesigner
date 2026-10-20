<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# مواصفات محرك الخطوط الذكي والتعديل الجراحي (`SMART_TYPOGRAPHY_AND_EDITING_SPEC.md`)

## 1. سير عمل التعامل الذكي مع النصوص (`Smart Typography Pipeline`)

عندما يكتشف النظام وجود طبقة نصية (`Text Region`) أثناء تفكيك الصورة في وضع **Magic Layers** أو **Image Editing**:

### المرحلة أ: الاكتشاف والتحليل البصري للنص (`Text Detection & Style DNA Extraction`)
1. تحديد الـ `Bounding Box` وقناع الحروف (`Glyph Masks`) واتجاه الكتابة (`RTL` للعربية أو `LTR` للإنجليزية).
2. استخلاص **بصمة هوية الخط (`Font Style Identity DNA`)**:
   - `stroke_weight_profile`: متوسط سمك الخط ونسبة التباين بين الخطوط الرأسية والأفقية.
   - `terminal_style`: شكل نهايات الحروف (`Rounded`, `Sharp`, `Serif`, `Calligraphic`).
   - `fill_and_effects`: لون التعبئة، التدرج اللوني (`Linear/Radial Gradient`)، حدود الحرف (`Stroke`)، والظل (`Drop/Inner Shadow`).
   - `baseline_curve`: خط الأساس الذي تجلس عليه الحروف (مستقيم أم منحني/قوسي).

### المرحلة ب: بوابة تخيير العميل (`User Typography Decision Gate`)
يسأل النظام العميل السؤال الواضح التالي:
1. **الخيار الأول (`EXACT_VECTOR_DRAW`):** *"رسم النص كأشكال Vector مطابقة 100% للصورة الأصلية مع حفظ ستايل الفونت للتعديل المستقبلي."*
2. **الخيار الثاني (`MATCH_LIVE_FONT`):** *"البحث عن أقرب خط (`Font`) مطابق لتحويله إلى نص حي؛ وفي حال عدم وجود خط بنفس الشكل بالضبط، يقوم النظام برسمه كـ Vector نظيف."*

### المرحلة ج: التعديل على النص بنفس الهوية (`Identity-Preserving Text Editing`)
- عندما يطلب العميل في وضع **Editing** تغيير الكلمة المكتوبة (مثلاً تغيير كلمة في لوجو أو بوستر):
  - يستخدم النظام بصمة الهوية المحفوظة (`Font Style Identity DNA`) والخط المطابق أو مولد الحروف (`Few-Shot Glyph Vector Synthesizer`) لرسم الكلمة الجديدة بنفس سمك الحروف، ونفس الانحناءات، ونفس الألوان والظلال، ويضعها في نفس المسار (`Baseline Curve`) داخل الـ `<g id="Typography_Group">` في ملف الـ SVG.
