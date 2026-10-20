<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# AI Graphic Designer — Master Plan & Modular Architecture Blueprint (`MASTER_PLAN.md`)

**الحالة الحالية للمشروع (`Current Project Stage & Gate`):**
- **المرحلة (`Project Stage`):** `ARCHITECTURE_AND_GOVERNANCE_PREPARATION` (مرحلة إعداد الحوكمة والمعمارية؛ **لم يبدأ تنفيذ المنتج البرمجي بعد**).
- **حالة اعتماد المعمارية (`Architecture Approval Status`):** `NOT_APPROVED` (`PROPOSED_ONLY` — بانتظار مراجعة المالك وتجارب الجدوى).
- **بوابة المرحلة التأسيسية (`P0 Implementation Gate`):** `BLOCKED_PENDING_OWNER_APPROVAL_AND_FEASIBILITY_EXPERIMENTS`.
- **المرجع الأصلي لرؤية المالك (`Authoritative Owner Vision`):** [docs/product/OWNER_ORIGINAL_VISION.md](docs/product/OWNER_ORIGINAL_VISION.md) و[docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md](docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md).
- **مرجع تجارب الجدوى ومقارنة التقنيات:** [docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md](docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md) و[docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md](docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md).


## 1. الرؤية الهندسية الشاملة للمشروع (`System Vision`)

بناء نظام **AI Graphic Designer** يعمل كـ "مصمم جرافيك محترف يجلس على لابتوب ويستخدم أداة الـ Pen Tool بذكاء"، وليس مجرد أداة Auto-Trace تفتت الصور إلى آلاف الشظايا العشوائية. يتكون النظام من **ثلاثة أوضاع تشغيلية أساسية (Core Operational Modes)** مبنية فوق نواة هندسية موحدة (Unified Scene Graph & Clean Vector Kernel):

### الوضع الأول: توليد الصور المخطط بالطبقات (`Mode 1: Scene-Planned Image Generation`)
1. **تحليل الوصف وتخطيط الهيكل (`Prompt-to-Scene-Graph Planning`):**
   - قبل توليد الصورة النهائية، يقوم موديل التخطيط بتحليل وصف المستخدم وتحديد: عدد الطبقات (Layers)، ترتيبها من الأسفل للأعلى (`Z-Order`)، الأشكال الهندسية، الإحداثيات والأبعاد (`Bounding Boxes & Dimensions` من بكسل كذا لبكسل كذا)، وتوزيع الألوان لكل جزء.
2. **توليد معاينة الصورة الكاملة (`Full Preview Generation`):**
   - استخدام موديل توليد الصور (مثل `Nano Banana` / Gemini Image Generation أو نظيره) لإنتاج الصورة الكاملة بناءً على المخطط الهيكلي، وعرضها على العميل للموافقة (`Client Approval Gate`).
3. **توليد الطبقات المفردة وتحويلها إلى Clean SVG (`Per-Layer Generation & Clean Vectorization`):**
   - بعد موافقة العميل، يتم توليد كل طبقة على حدة بنفس المواصفات والأبعاد المحددة مسبقاً (مثل: الدرع الفضي لوحده، ثم العناصر البرتقالية والحمراء بداخله كطبقات مستقلة).
   - تحويل كل طبقة عبر محرك الـ Clean SVG إلى مسارات فيكتور نظيفة قابلة للرسم والتعديل كأنها مرسومة بـ Pen Tool، وتجميع الأجزاء المرتبطة دلالياً في Groups نظيفة مع فصل العناصر المختلفة تماماً (مثل فصل البطاطس عن العيش في طبقات مستقلة).

### الوضع الثاني: التفكيك الذكي للصور الجاهزة (`Mode 2: Magic Layers Decomposition`)
1. **التحليل البصري واستخراج شجرة الطبقات (`Visual Scene & Z-Order Analysis`):**
   - استقبال أي صورة جاهزة (سواء مولدة بأداة خارجية أو مرفوعة من المستخدم) وتحليلها لتحديد عدد الطبقات، وأي طبقة تقع تحت أو فوق الأخرى (`Occlusion & Z-Index Ordering`)، وتحديد الأبعاد والمنحنيات (`Curves & Pixel Bounds`) من اليمين للشمال ومن أعلى لأسفل.
2. **الفصل الدلالي وإكمال الأجزاء المخفية (`Semantic Segmentation & Amodal Inpainting`):**
   - فصل كل عنصر بدقة البكسل (مثلاً عبر SAM 2 + Grounding DINO) مع إكمال الأجزاء المخفية من الطبقات السفلية (`Amodal Completion`) حتى تُرسم الطبقة السفلية كشكل هندسي كامل ونظيف بدون ثقوب مكان الطبقات العلوية.
3. **البناء التصاعدي والمطابقة البصرية (`Bottom-Up Reconstruction & 50% Opacity / IoU Verification`):**
   - بناء الطبقات من الطبقة السفلية للأعلى طبقة تلو الأخرى.
   - بعد رسم كل طبقة كـ SVG، يقوم **Visual QA Critic Agent** بتركيبها فوق الصورة الأصلية بشفافية `50% Opacity` مع حساب مقاييس التطابق الهندسي (`IoU` و`SSIM` وخريطة فروق البكسلات `Pixel Diff Map`)؛ لا ينتقل للطبقة التالية إلا بعد التأكد من تطابق الأبعاد والمنحنيات.
4. **التعامل الذكي مع النصوص (`Smart Typography Resolution`):**
   - عند اكتشاف نص داخل الصورة، يسأل النظام المستخدم (أو يتبع تفضيله المحدد):
     - **الخيار أ:** رسم النص كـ Vector مطابق 100% لشكل الحروف في الصورة مع الاحتفاظ بهوية الـ Style.
     - **الخيار ب:** البحث عن أقرب خط (`Font Matching`) وتحويله إلى نص حي قابل للكتابة، وإن لم يوجد خط مطابق يتم رسمه مع استخلاص خصائص الهوية البصرية للخط (`Stroke Width, Terminals, Curvature, Color/Gradient`) لإعادة استخدامها عند أي تعديل مستقبلي.

### الوضع الثالث: التعديل الجراحي على الطبقات والنصوص (`Mode 3: Layer-Aware Vector & Text Editing`)
1. **التفكيك المسبق (`Magic Layers First-Pass`):**
   - تطبيق خطوات الـ Magic Layers والـ Clean Design كخطوة تأسيسية لفهم بنية التصميم بالكامل.
2. **تنفيذ تعديلات العميل بدقة على الطبقات (`Surgical Art-Layer Mutation`):**
   - تطبيق تعديلات المستخدم مباشرة على طبقة الـ Vector المستهدفة (`Art Layer` أو `<g>` Group) دون إفساد باقي الطبقات.
3. **إعادة رسم النصوص بنفس هوية الخط (`Identity-Preserving Glyph Redrawing`):**
   - إذا طلب المستخدم تعديل كلمة أو نص، يعيد النظام رسم النص الجديد بنفس الـ Font Style Identity (نفس السمك، الانحناءات، الألوان، والظلال) ويصدر النتيجة النهائية بصيغة **Clean SVG** عالية الجودة جاهزة لبرامج Adobe Illustrator وFigma وPhotoshop.

## 2. القاعدة الهندسية الحاكمة للـ Clean SVG (`The Clean Graphic Designer Rule`)

لتجنب مشكلة تشظي الألوان في أدوات الذكاء الاصطناعي التقليدية (مثل تفتيت قرص الفلافل أو البطاطس إلى مئات القطع الصغيرة بسبب تدرجات الإضاءة، أو دمج جزء من البطاطس مع جزء من العيش في طبقة واحدة):

| المشكلة الشائعة في أدوات الـ AI | القاعدة الحاكمة في نظامنا (`Clean Design Invariant`) |
| :--- | :--- |
| **دمج عنصرين مختلفين (مثل البطاطس والعيش) في مسار واحد لتقارب اللون الأصفر/البني** | **العزل الدلالي المسبق (`Semantic Mask Isolation`):** يتم فصل كل كيان دلالي (`Bread` مقابل `Potato` مقابل `Falafel`) في Mask مستقل تماماً قبل أي عملية تحويل لـ Vector؛ يُحظر عبور أي مسار SVG لحدود الـ Semantic Mask الخاص بالعنصر. |
| **تفتيت العنصر الواحد لمئات الشظايا بسبب الظل والنور (`Color Fragmentation`)** | **التجميع الهرمي النظيف (`Hierarchical <g> Grouping`):** يُنشأ Group باسم العنصر (مثلاً `<g id="Potato">` أو `<g id="بطاطس">` حسب لغة المستخدم) يحتوي بداخله على: 1) الشكل الأساسي الموحد (`Base Clean Shape`)، 2) طبقة الظل كقطعة نظيفة موحدة (`Shadow Shape`)، 3) طبقة الإضاءة (`Highlight Shape`). |
| **تقسيم ظل متصل يمكن رسمه كقطعة واحدة إلى عدة قطع متناثرة** | **دمج المسارات المتجاورة (`Adjacent Path Topology Union`):** أي أجزاء لونية متجاورة أو متداخلة تنتمي لنفس الوظيفة البصرية داخل نفس العنصر يتم عمل `Boolean Union + Bézier Curve Fitting` لها لتصبح مساراً واحداً منتظماً بأقل عدد ممكن من نقاط التحكم (`Anchor Points`). |
| **بروز حواف طبقة فرعية خارج حدود الشكل الأساسي (`Layer Bleeding`)** | **القص الهندسي النظيف (`Boundary Clipping & Z-Clean Check`):** بعد تجميع الأشكال، يتم فحص ما إذا كانت أي طبقة ظل أو تفصيلة قد خرجت خارج حدود الـ Base Shape، ويتم تهذيبها هندسياً (`Boolean Intersection / ClipPath`) لضمان نظافة التصميم. |

## 3. الموديولات المعمارية للمشروع (`System Modules — Non-Prescriptive Workstreams`)

يمكن للمطور أو الـ Agent البدء بأي موديول أو شريحة رأسية (Vertical Slice) بناءً على توجيه المستخدم المباشر، دون التقيد بترتيب إجباري واحد:

| كود الموديول | اسم الموديول (`Module`) | المسؤولية الأساسية | المخرجات والعقود (`Contracts`) |
| :--- | :--- | :--- | :--- |
| `M01-KERNEL` | **Scene Graph & Geometry Kernel** | تعريف الـ JSON Schemas للـ Scene Graph، الطبقات، الـ Z-Order، الـ Bounding Boxes، والمجموعات (`<g>`). | `SceneGraphSchema`, `LayerNode`, `GroupNode`, `GeometryPrimitives` |
| `M02-GEN` | **Planned Image Generation Engine** | تحليل الوصف، تخطيط الطبقات والأبعاد، توليد الصورة الكاملة (مثل Nano Banana / Gemini Image)، ثم توليد الصور المفردة لكل طبقة بعد موافقة العميل. | `PromptScenePlanner`, `FullPreviewGenerator`, `LayerAssetGenerator` |
| `M03-DECOMP` | **Magic Layers Decomposition Engine** | تحليل الصور الجاهزة، استخراج الـ Masks (SAM 2 / Grounding DINO)، ترتيب الـ Z-Order، وإكمال الأجزاء المخفية (`Amodal Inpainting`). | `SceneAnalyzer`, `LayerSegmenter`, `ZOrderSolver`, `AmodalInpainter` |
| `M04-VECTOR` | **Clean SVG & Topology Engine** | تحويل كل طبقة إلى Bézier SVG نظيف، تطبيق التبسيط اللوني، دمج الأشكال المتجاورة، إنشاء مجموعات `<g>` (عنصر + ظل)، ومنع تداخل العناصر المنفصلة. | `SemanticColorQuantizer`, `CleanBezierTracer`, `PathUnionConsolidator`, `SvgGroupBuilder` |
| `M05-TYPO` | **Smart Typography & Font Identity Engine** | اكتشاف النصوص (OCR)، تخيير المستخدم (رسم مطابق أو أقرب فونت)، استخلاص بصمة الفونت (`Font Style DNA`)، وإعادة رسم النصوص المعدلة بنفس الهوية. | `TextRegionDetector`, `FontMatcherService`, `FontStyleExtractor`, `GlyphVectorSynthesizer` |
| `M06-CRITIC` | **Visual QA & 50% Opacity Critic** | مطابقة الـ SVG المرسوم مع الصورة الأصلية طبقة بطبقة (50% Opacity Overlay + IoU + SSIM + Pixel Diff) وإرجاع إحداثيات الأخطاء لتصحيحها تلقائياً. | `OpacityOverlayRenderer`, `GeometricDiffCalculator`, `LayerVerificationGate` |
| `M07-EDIT` | **Layer-Aware Surgical Editor** | استقبال أوامر التعديل من المستخدم بعد تفكيك الصورة إلى Magic Layers، وتنفيذ التعديل على طبقة الرسم أو النص المستهدف مع الحفاظ على نظافة الـ SVG. | `EditIntentParser`, `ArtLayerMutator`, `SvgExportSerializer` |
| `M08-APP` | **Backend API & Interactive Vector Canvas UI** | واجهة المستخدم التفاعلية (عرض الطبقات، الموافقة على الصورة، مقارنة الـ 50% Opacity، تعديل الـ Anchor Points والنصوص) والـ FastAPI Backend. | `FastApiOrchestrator`, `CanvasWorkspaceUI`, `LayerTreePanel`, `IllustratorSvgExporter` |

## 4. حالات الإنجاز والاعتماد (`Completion & Authority States`)

للحفاظ على الصرامة الهندسية ومنع الهلوسة (وفقًا لمبادئ تتبع الأدلة واستقلالية القرار)، يتم التمييز بدقة بين الحالات التالية لكل ميزة أو موديول:
- `PLANNED`: موثق كتصميم أو خطة في `MASTER_PLAN.md` ولم يبدأ تنفيذه البرمجي بعد.
- `IN_PROGRESS`: قيد التنفيذ حالياً ومُسجل في `memory/session/CURRENT_TASK_CHECKPOINT.md`.
- `IMPLEMENTED_UNVERIFIED`: كُتب الكود الخاص به، لكن لم تكتمل مراجعة الـ `qa-reviewer-auditor` أو تحديث مرآة الكود بعد.
- `VERIFIED_AND_MIRRORED`: اجتاز اختبارات الكود، وتم تحديث ملف المرآة في `memory/code_mirrors/` وسجل `memory/FUNCTION_REGISTRY.md` بأرقام الأسطر الدقيقة، وراجعه الـ Sub-Agent المراجع.
- `USER_APPROVED`: راجعه المستخدم وأكّد قبوله.

## 5. دلالات الاعتماد وبوابات الجدوى قبل تنفيذ المنتج (`Approval Semantics & Feasibility Gates`)

يفصل هذا المخطط بصرامة بين حالات المتطلبات والحلول التقنية والتنفيذ:
- `OWNER_REQUIREMENT`: متطلب أصلي من المالك في `docs/product/OWNER_ORIGINAL_VISION.md`.
- `PROPOSED`: حل تقني أو معماري مقترح من الـ AI، غير معتمد بعد من المالك.
- `UNDER_RESEARCH`: يخضع لتجارب الجدوى التقنية (`EXP-01` إلى `EXP-05`).
- `TECHNICALLY_REVIEWED`: تمت مراجعته هندسياً واختباره آلياً (مثل أدوات الحوكمة الحالية).
- `EXPERIMENTALLY_VALIDATED`: أثبتت التجارب العملية نجاحه وفق معايير `FEASIBILITY_EXPERIMENTS_AND_GATES.md`.
- `OWNER_APPROVED`: اعتمده المالك صراحةً بتفويض موثق في `memory/decisions/DECISION_LOG.md`.
- `REJECTED`: مرفوض من المالك أو ثبت عدم جدواه (يُحفظ في التاريخ مع سبب الرفض).

> **حظر الاعتماد الذاتي (`No Self-Approval Rule`):** لا يجوز لأي Agent تغيير حالة المعمارية أو المرحلة `P0` إلى `OWNER_APPROVED` أو البدء في تنفيذ كود المنتج بدون تفويض صريح وموثق من المالك.
