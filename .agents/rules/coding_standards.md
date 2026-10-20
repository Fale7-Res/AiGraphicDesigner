---
trigger: model_decision
description: "Coding standards, naming conventions, strict typing, coordinate math precision, and anti-duplication discipline for AI Graphic Designer."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:37Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# معايير كتابة الكود والصرامة البرمجية (`Coding Standards & Engineering Discipline`)

## 1. قابلية الصيانة والوضوح (`Maintainability & Clean Modularity`)

1. **مسؤولية واحدة لكل ملف ولكل دالة (`Single Responsibility`):**
   - اكتب دوال صغيرة، واضحة الاسم، وتؤدي وظيفة واحدة محددة (مثلاً: `extract_semantic_masks`، `compute_z_order_graph`، `merge_adjacent_bezier_paths`، `render_opacity_comparison`).
   - لا تكتب دوال عملاقة ("God Functions") تتجاوز `60–80` سطراً، ولا ملفات تتجاوز `400–600` سطر حتى يسهل قراءتها بالكامل دائماً في Antigravity وتوثيقها بالسطر في `memory/code_mirrors/`.
2. **منع تكرار الكود والدوال (`Strict DRY via Function Registry`):**
   - قبل كتابة أي دالة مساعدة (Helper) أو رياضية، افحص `memory/FUNCTION_REGISTRY.md`. يُحظر وجود دالتين في المشروع تقومان بنفس الحساب الهندسي أو نفس تحويل الـ SVG.
3. **معايير التسمية (`Naming Conventions`):**
   - **Python (Backend / AI / Vector Engine):** أسماء الملفات والدوال والمتغيرات بـ `snake_case`، الكلاسات بـ `PascalCase`، الثوابت بـ `UPPER_SNAKE_CASE`، مع استخدام `Type Hints` إلزامية لجميع المدخلات والمخرجات (`def trace_layer(mask: np.ndarray, max_nodes: int = 32) -> SvgLayer:`).
   - **TypeScript / React (Canvas UI):** المكونات والأنواع بـ `PascalCase`، الدوال والمتغيرات بـ `camelCase`، الـ Hooks تبدأ بـ `use...`، مع تفعيل `strict: true` في `tsconfig.json`.
   - **معرّفات الـ SVG (`SVG Layer & Group IDs`):** يجب أن تكون دلالية وواضحة للمصمم البشرى (مثل `<g id="Potato" data-name="بطاطس">`، `<path id="Potato_Base">`، `<path id="Potato_Shadow">`) وليس أسماء عشوائية مبهمة مثل `path_83921_a`.

## 2. الدقة الرياضية والهندسية (`Geometric & Coordinate Correctness`)

1. **وحدات الإحداثيات (`Coordinate System Explicitness`):**
   - يجب أن يحدد كل كائن هندسي بوضوح هل إحداثياته بالبكسل المطلق (`Pixel Space: 0..W, 0..H`) أم بنسب معيارية (`Normalized Space: 0.0..1.0`) أم بوحدات `SVG viewBox`. يُحظر الخلط بين أنظمة الإحداثيات بدون دالة تحويل مسجلة.
2. **دقة الأرقام في الـ SVG (`Floating-Point Precision`):**
   - تُقرب إحداثيات مسارات الـ SVG (`d="M ... C ..."`) إلى رقمين أو ثلاثة أرقام عشرية كحد أقصى (`round(val, 2)`) لمنع تضخم حجم ملف الـ SVG مع الحفاظ على دقة Sub-pixel في برامج التصميم.
3. **معالجة الأخطاء بوضوح (`Explicit Error Taxonomy`):**
   - ميّز في الأخطاء بين: فشل موديل خارجي (`ModelInferenceError`)، عدم تطابق بصري في بوابة الـ 50% Opacity (`VisualVerificationMismatchError`)، خطأ في بنية الـ SVG (`InvalidSvgTopologyError`)، وحاجة لقرار المستخدم (`UserClarificationRequired`).

## 3. التزامن الإلزامي مع الذاكرة (`Same-Turn Memory Synchronization`)

- أي إضافة أو تعديل أو حذف لدالة أو تغيير لأرقام أسطرها في أي ملف برمجي يستوجب **في نفس المهمة** تشغيل `python tools/memory_guard/sync_code_mirrors.py --write` وتحديث ملف المرآة في `memory/code_mirrors/` و`memory/FUNCTION_REGISTRY.md` و`PROJECT_FILE_CATALOG.md`.

## Change timestamps & document provenance (mandatory)

Apply `docs/governance/CODE_AND_DOCUMENT_CHANGE_PROVENANCE.md` on every first-party source write and human-authored Markdown edit. Source code: use matched `START CHANGE` and `END CHANGE` comments with real UTC timestamp, change ID, CREATED/EDITED, and agent ID at the smallest logical change block. Markdown: update `DOC_PROVENANCE` and `memory/DOCUMENT_PROVENANCE.json` in the same task; historical unknown creation times must stay unknown. Verify with `python tools/governance/change_tracking.py verify`. Do not edit immutable owner vision, historical snapshots, generated mirrors, or JSON with invalid comments. Update code mirrors, project catalog, and findings revision ledger when applicable.
