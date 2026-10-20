---
trigger: always_on
description: "Mandatory External Brain and 1:1 Codebase Markdown Mirroring rules: every code file must have a Markdown mirror documenting all functions, exact line numbers (StartLine-EndLine), verbatim code snippets, and upstream/downstream file relationships."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:35Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# نظام الذاكرة الخارجية الحية ومرآة الكود (`External Brain & 1:1 Code Mirror Rules`)

**الحالة:** إلزامي دائماً (`ALWAYS_ON`) لجميع الـ Agents والـ Sub-Agents.

## 1. فلسفة الذاكرة الحية (`Memory, Not Documentation`)

لا تتعامل مع ملفات الـ Markdown داخل `memory/` و`PROJECT_FILE_CATALOG.md` على أنها "توثيقات إضافية يكتبها المبرمج بعد الانتهاء". هذه الملفات هي **ذاكرتك الخارجية الحية (External Working & Long-Term Brain)**.
- الهدف الأساسي: إذا مسحت المحادثة بالكامل، أو حدث Context Compaction متكرر، أو جاء مطور بشري أو Agent جديد لم يرَ المشروع من قبل، فيجب أن يستطيع من خلال قراءة ملفات `memory/` فقط أن يفهم:
  1. ماذا يفعل المشروع بالكامل وما هي معماريته.
  2. ما الذي تم بناؤه حتى الآن، وما الذي كان يجري العمل عليه، وما الذي يتبقى.
  3. أين تقع كل دالة وكل سطر برمجي مهم في المشروع بالضبط (`Lines Start–End`) وما هو نص الكود الفعلي، وكيف يتصل كل ملف بالملفات الأخرى، **دون الحاجة لقراءة آلاف أو مئات الآلاف من أسطر الكود الخام**.

## 2. قاعدة المرآة لكل ملف برمجي (`1:1 Codebase Markdown Mirroring`)

لكل ملف برمجي في المشروع (سواء `.py`، `.ts`، `.tsx`، `.js`، `.sql`، إلخ)، يجب أن يوجد ملف Markdown مقابل له في المسار:
`memory/code_mirrors/<relative_path_with_double_underscores>.md`
*(مثال: الملف `src/vector_engine/svg_cleaner.py` يقابله ملف المرآة `memory/code_mirrors/src__vector_engine__svg_cleaner.py.md`).*

يجب أن يحتوي كل ملف مرآة (`Code Mirror`) على الأقسام الخمسة الإلزامية التالية:

### أ. بطاقة تعريف الملف (`File Identity & Purpose`)
- المسار الفعلي للملف (`Source Path`)، ونوعه المعماري (`Domain / Application / AI-Pipeline / Vector-Engine / API / UI-Canvas / Tooling`).
- عدد الأسطر الإجمالي (`Total Lines`) وبصمة الملف (`SHA-256`).
- شرح تفصيلي وواضح لوظيفة الملف ولماذا هو موجود في المعمارية.

### ب. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)
جدول إلزامي يوضح بدقة:
- **من أين يأخذ البيانات (`Upstream Inputs / Imported By / Callers`):** ما هي الملفات أو الـ APIs أو قواعد البيانات أو الـ Queues التي تغذي هذا الملف بالبيانات، وما هو شكل البيانات (`Schema / DTO`) التي يستقبلها.
- **إلى أين يرمي البيانات (`Downstream Outputs / Imports / Callees`):** ما هي الملفات أو الـ Endpoints أو الواجهات (`Frontend Canvas`) أو المخازن التي يرسل إليها هذا الملف مخرجاته.
- **تأثير التعديل (`Change Impact`):** إذا تغير هذا الملف، ما هي الملفات الأخرى التي ستتأثر ويجب مراجعتها فوراً.

### ج. فهرس الدوال والكلاسات داخل الملف (`Functions & Classes Table`)
جدول سريع يدرج كل دالة (`Function / Method`) وكل كلاس (`Class`) داخل الملف، مع:
- اسم الدالة/الكلاس.
- نطاق الأسطر الدقيق من سطر كذا إلى سطر كذا (`Lines Start–End`).
- المدخلات والمخرجات (`Parameters & Return Type`).
- وظيفة الدالة بالتفصيل لمنع إعادة كتابتها أو تكرارها في مكان آخر.

### د. التوثيق السطري والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)
**قاعدة صارمة:** أي دالة أو منطق برمجي أو ثابت مهم يُذكر في ملف المرآة يجب أن يُكتب معه:
1. **نطاق الأسطر الدقيق (`Lines X–Y`)** كما هو موجود فعلياً في ملف الكود.
2. **مقتطف الكود الفعلي (`Verbatim Code Block`)**: توقيع الدالة والمنطق الفعلي (أو الكود الكامل للدوال القصيرة؛ مثلاً لو دالة تطبع `print("hello world")` في الأسطر من 1 إلى 5، يُكتب: `Lines 1–5` متبوعاً ببلوك الكود الفعلي بالضبط).

مثال للتنسيق الإلزامي داخل ملف المرآة:
```markdown
#### الدالة `merge_adjacent_shadow_paths` — `Lines 14–28`
- **الوظيفة:** تدمج مسارات الظل المتجاورة داخل نفس طبقة العنصر (مثل ظل البطاطس) في مسار Bézier واحد نظيف لمنع تفتيت الـ SVG.
- **تأخذ من:** `src/vector_engine/color_quantizer.py` (`quantize_layer_regions`, `Lines 45–82`).
- **ترمي إلى:** `src/vector_engine/svg_group_builder.py` (`build_semantic_group`, `Lines 19–60`).
- **الكود الفعلي (`Lines 14–28`):**
```python
def merge_adjacent_shadow_paths(paths: list[SvgPath], tolerance_px: float = 1.5) -> list[SvgPath]:
    # يجمع المسارات المتداخلة أو المتجاورة في مسار واحد نظيف
    merged = boolean_union(paths, distance_threshold=tolerance_px)
    return [fit_clean_bezier(poly, max_nodes=24) for poly in merged]
```
```

## 3. السجل المركزي للدوال (`memory/FUNCTION_REGISTRY.md`)

بالإضافة لملفات المرآة الفردية، يتم تحديث `memory/FUNCTION_REGISTRY.md` في نفس المهمة ليكون الفهرس الموحد لكل دالة في المشروع.
- **حظر تكرار الدوال (`Zero Duplicate Functions Rule`):** قبل كتابة أي دالة جديدة في أي ملف، **يجب** البحث في `memory/FUNCTION_REGISTRY.md`. إذا كانت هناك دالة موجودة تؤدي نفس الوظيفة (حتى لو باسم مختلف مثل `calculate_iou` و`compute_mask_iou`)، يُحظر إنشاء دالة ثانية؛ يجب استيراد الدالة الموجودة واستخدامها.

## 4. الأتمتة والتحقق الإلزامي (`Automated Mirror Sync & Verification`)

لتجنب أي خطأ بشري أو نسيان من الـ Agent في حساب أرقام الأسطر بعد تعديل الكود:
1. بعد أي تعديل في الكود، شغّل الأداة:
   `python tools/memory_guard/sync_code_mirrors.py --write`
   تقوم هذه الأداة بقراءة شجرة الكود (AST)، وتحديث أرقام الأسطر (`Lines Start–End`) والمقتطفات الفعلية تلقائياً في `memory/code_mirrors/` و`memory/FUNCTION_REGISTRY.md`، وتكشف أي دوال مكررة.
2. املأ أو حدّث الوصف الدلالي وعلاقات الملف (`بياخد منين وبيرمي فين`).
3. شغّل أداة التحقق الإلزامية قبل إنهاء المهمة:
   `python tools/memory_guard/verify_brain_sync.py`
   لا تُعتبر المهمة مكتملة إذا أرجعت هذه الأداة أي خطأ (`Exit Code != 0`).
