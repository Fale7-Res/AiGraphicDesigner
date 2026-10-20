---
trigger: model_decision
description: "Clean Architecture and modular boundary rules for the AI Graphic Designer system across Scene Graph, Image Generation, Magic Layers, Clean SVG, Smart Typography, Visual Critic, and Canvas UI."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد المعمارية النظيفة وحدود الموديولات (`Clean Architecture & Module Boundary Rules`)

**الحالة (`Approval Status`):** `PROPOSED_ARCHITECTURAL_BASELINE` (مقترح معماري قيد التحضير؛ لا يُعد `OWNER_APPROVED` لتنفيذ المنتج إلا بعد اجتياز بوابات `docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md` وموافقة المالك الموثقة في `memory/decisions/DECISION_LOG.md`).

## 1. استراتيجية المعمارية (`Modular Monolith + AI Pipeline Workers`)

يُبنى المشروع كمعمارية **Modular Monolith** بحدود صارمة (Clean Architecture)، مع فصل واضح بين:
- **نواة المجال الهندسي (`Domain / Scene Graph & Vector Kernel`):** تحتوي على الكيانات الهندسية (`SceneGraph`, `LayerNode`, `GroupNode`, `BezierPath`, `TypographyStyleDNA`, `BoundingBox`) وقواعد النظافة الهندسية دون أي اعتماد على مكتبات HTTP أو قواعد بيانات أو واجهات المستخدم.
- **طبقة التطبيقات وحالات الاستخدام (`Application / Use Cases & Orchestration`):** تدير تدفقات الأوضاع الثلاثة (توليد الصور بالطبقات، تفكيك الـ Magic Layers، والتعديل الجراحي على الطبقات والنصوص) وتنسق بوابات التحقق البصري (`Visual QA Gates`).
- **طبقة البنية التحتية ومشغلات الذكاء الاصطناعي (`Infrastructure / AI & CV Adapters`):** تحتوي على محولات استدعاء موديلات الصور (مثل `Nano Banana` / Gemini API)، وموديلات الفصل (SAM 2 / Grounding DINO)، ومكتبات معالجة الـ Curves والـ SVG (`DiffVG`, `VTracer`, `OpenCV`, ` Shapely / Clipper`)، والتخزين.
- **طبقة العرض والـ Canvas التفاعلي (`Presentation / FastAPI + React Vector Canvas`):** تعرض شجرة الطبقات، ومعاينة الـ 50% Opacity، وأدوات الـ Pen Tool وتعديل النصوص.

## 2. اتجاه الاعتماديات (`Dependency Direction Rules`)

| الطبقة (`Layer`) | ماذا تملك (`Owns`) | الاعتماديات المسموحة (`Allowed Dependencies`) |
| :--- | :--- | :--- |
| **Domain (`src/domain/`)** | كيانات الـ Scene Graph، قواعد تجميع الـ `<g>`، معادلات الـ Bounding Box، قواعد الـ Z-Order، ومعايير نظافة الـ SVG | مكتبات اللغة القياسية والرياضيات البحتة فقط؛ ممنوع استيراد FastAPI أو DB أو API خارجي. |
| **Application (`src/application/`)** | حالات الاستخدام (`GenerateLayeredDesign`, `DecomposeMagicLayers`, `EditLayerOrText`, `VerifyLayerOverlay`)، العقود (`Ports / Interfaces`)، والـ DTOs | طبقة الـ `Domain` فقط. |
| **Infrastructure (`src/infrastructure/`)** | محولات موديلات الـ AI، محركات الـ Segmentation، الـ Inpainting، الـ OCR/Font Matching، قاعدة البيانات، وتخزين الملفات | تطبق Interfaces طبقة الـ `Application` وتعتمد على `Domain`. |
| **Presentation (`src/api/`, `web/`)** | نقاط النهاية (`FastAPI Endpoints`)، والتحقق من المدخلات، وواجهة الـ Canvas التفاعلية | تتحدث مع `Application` عبر عقود صريحة (`DTOs`)؛ لا تستدعي موديلات الـ AI أو قاعدة البيانات مباشرة من الـ UI. |

## 3. قواعد ملكية البيانات والتفاعل بين الموديولات (`Module Ownership & Data Flow`)

1. **الـ Scene Graph هو مصدر الحقيقة الهندسي الموحد (`Single Geometric Source of Truth`):**
   - سواء دخل المستخدم من وضع **Image Generation** أو وضع **Magic Layers** أو وضع **Image Editing**، يجب أن يتحول التصميم إلى كائن `SceneGraph` قياسي وموحد قبل توليد أو تعديل كود الـ SVG.
2. **فصل المعاينة السريعة عن المخرجات المعتمدة (`Preview vs. Authoritative Vector Output`):**
   - في وضع توليد الصور، لا يتم تشغيل خط أنابيب توليد الطبقات المفردة وتحويلها إلى Clean SVG إلا بعد اجتياز بوابة موافقة العميل (`Client Preview Approval`) أو طلب صريح، لتوفير الوقت والموارد.
   - في وضع الـ Magic Layers، لا يتم اعتماد الطبقة رقم `N+1` إلا بعد اجتياز الطبقة رقم `N` لبوابة المطابقة البصرية (`Visual QA Gate`).
3. **توثيق العلاقات في الذاكرة (`Mandatory Data-Flow Documentation`):**
   - أي ارتباط جديد بين ملفين عبر هذه الطبقات يجب تسجيله فوراً في `memory/FILE_RELATIONSHIPS_GRAPH.md` وفي ملفات المرآة داخل `memory/code_mirrors/`.
