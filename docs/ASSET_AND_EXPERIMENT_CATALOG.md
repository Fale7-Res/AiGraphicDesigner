<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# سجل الأصول المرجعية وحالات الاختبار القياسية (`ASSET_AND_EXPERIMENT_CATALOG.md`)

هذا السجل يوثق الحالات القياسية المرجعية (`Golden Benchmark Cases`) التي يجب أن يجتازها محرك **AI Graphic Designer**:

| الكود (`ID`) | اسم الحالة المرجعية | الوصف والتحدي الهندسي | النتيجة المطلوبة في الـ Clean SVG |
| :--- | :--- | :--- | :--- |
| `A01` | **الدرع الفضي بتفاصيل برتقالية وحمراء (`Silver Shield Badge`)** | اختبار الوضع الأول (`Image Generation`): توليد صورة درع فضي بداخله زخارف برتقالية وحمراء، ثم توليد كل طبقة لوحدها بنفس الأبعاد. | طبقة `Shield_Silver_Base` منفصلة تماماً في الأسفل، وفوقها طبقات `Inner_Orange_Crest` و`Inner_Red_Emblem` متطابقة الأبعاد كأنها مرسومة بـ Pen Tool. |
| `A02` | **قوام الفلافل والظلال المتدرجة (`Falafel Texture & Shadows`)** | اختبار منع تشظي الـ SVG (`Anti-Fragmentation`): قرص فلافل يحتوي على مناطق فاتحة وغامقة متداخلة. | عدم تحويله لمئات القطع العشوائية؛ بل تجميع الأجزاء المتجاورة في `<g id="Falafel">` يضم شكلاً أساسياً نظيفاً وطبقة ظل/إضاءة مدمجة ومنتظمة. |
| `A03` | **ساندوتش البطاطس والعيش (`Potato & Bread Sandwich`)** | اختبار منع اختلاط الطبقات ذات الألوان المتقاربة (`Anti-Bleeding`): بطاطس صفراء داخل عيش بيج/أصفر مع ظل للبطاطس. | فصل كامل: جروب `<g id="Bread">` مستقل تماماً عن جروب `<g id="Potato">` (الذي يضم البطاطس + الشادو بتاعها كقطعة واحدة نظيفة). |
| `A04` | **شعار نصي مخصص (`Custom Styled Typography Logo`)** | اختبار `Smart Typography & Editing`: صورة تحتوي على نص بستايل فونت خاص وتعديل الكلمة مع الحفاظ على الهوية. | تخيير العميل بين الرسم المطابق أو أقرب فونت، وحفظ بصمة الفونت وإعادة رسم أي نص معدل بنفس الـ Identity. |
