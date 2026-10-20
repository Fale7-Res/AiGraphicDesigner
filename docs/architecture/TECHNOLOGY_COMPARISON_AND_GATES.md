<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# مصفوفة مقارنة البدائل التقنية وبوابات الاعتماد (`docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md`)

**الحالة:** `PROPOSED_COMPARISON_MATRIX` — لا يوجد أي التزام نهائي (`Final Technology Commitment`) بأي مكتبة أو إطار عمل قبل مقارنة البدائل واجتياز تجارب الجدوى (`EXP-01..05`) وموافقة المالك (`OWNER_APPROVED`).

## مقارنة البدائل التقنية لكل مكون في المشروع

| المكون المعماري (`Component`) | الخيار المقترح أ (`Option A`) | الخيار المقترح ب (`Option B`) | الخيار المقترح ج (`Option C`) | معيار المفاضلة (`Selection Criteria`) | الحالة الحالية (`Status`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. توليد الصور المخطط بالطبقات (`Image Generation Model`)** | `Gemini Image Generation / Nano Banana` (عبر `google-genai`) | `Flux.1 / SDXL + ControlNet Layer Conditioning` | `Hybrid: Gemini Planner + Local Diffusion` | دقة الالتزام بالأبعاد المحددة مسبقاً للطبقة، التكلفة لكل تصميم، والسرعة. | `PROPOSED` (ينتظر قرار المالك و`EXP-02`) |
| **2. فصل الطبقات (`Semantic Segmentation`)** | `SAM 2 + Grounding DINO` | `Florence-2 + SAM 2` | `Mask2Former / HQ-SAM` | دقة فصل الحدود المتقاربة لونياً (البطاطس والعيش `EXP-01`) واستهلاك الـ GPU. | `UNDER_RESEARCH` (`EXP-01`) |
| **3. تحويل الـ Vector النظيف (`Clean SVG Tracer`)** | `Morphological Quantizer + Shapely Union + VTracer + Curve Fitter` | `DiffVG (Differentiable Vector Graphics)` | `Potrace + Custom Polygon Simplifier` | نظافة منحنيات Bézier، قلة عدد النقاط (`Anchor Points`)، وسرعة المعالجة (`EXP-02`). | `UNDER_RESEARCH` (`EXP-02`) |
| **4. إكمال الطبقات السفلية (`Amodal Inpainting`)** | `LaMa (Large Mask Inpainting)` خفيف وسريع | `Geometric Contour Extrapolation` (للأشكال الهندسية المنتظمة) | `Diffusion / Gemini Inpainting` (للتفاصيل المعقدة) | سرعة الاستكمال ونظافة الشكل الهندسي الناتج تحت الطبقة العلوية (`EXP-03`). | `UNDER_RESEARCH` (`EXP-03`) |
| **5. واجهة الرسم التفاعلية (`Interactive Vector Canvas UI`)** | `React + TypeScript + Paper.js` (متخصص في عمليات الـ Bézier والـ Boolean Operations) | `React + TypeScript + Fabric.js` | `React + TypeScript + Custom SVG DOM Canvas` | دعم تحرير نقاط التحكم (`Pen Tool Handles`)، وعرض شجرة `<g>`، وسلاسة سلايدر `50% Opacity`. | `PROPOSED` (ينتظر قرار المالك) |
| **6. إطار عمل الـ Backend (`Backend & Orchestration`)** | `Python 3.12 + FastAPI + Pydantic v2` (تكامل مباشر مع مكتبات الـ AI والـ CV) | `Node.js/TypeScript BFF + Python AI Worker` | `Go/NET API + Python gRPC AI Worker` | تقليل تعقيد اللغات وسهولة مشاركة عقود الـ `SceneGraph` مع محركات الرؤية. | `PROPOSED` (ينتظر قرار المالك) |
