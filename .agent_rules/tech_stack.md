---
trigger: model_decision
description: "Technology stack baseline and library guidelines for AI Graphic Designer (Python AI/CV pipeline, Google GenAI/Antigravity SDK, Clean SVG vector engine, and React/TypeScript Canvas UI)."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# خط الأساس التقني وإدارة الحالة (`Technology Baseline & State Management`)

**الحالة (`Approval Status`):** `PROPOSED / UNDER_RESEARCH` — لا توجد أي التزامات تقنية نهائية (`No Final Technology Commitments`) قبل إجراء المقارنات التجريبية في `docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md` وتجارب الجدوى `EXP-01..05` في `docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md` وموافقة المالك (`OWNER_APPROVED`).

## 1. المكدس التقني المقترح (`Proposed Tech Stack`)

| المجال (`Area`) | التقنيات والمكتبات المقترحة (`Baseline`) | الدور والغرض في المشروع |
| :--- | :--- | :--- |
| **AI & LLM Orchestration** | `google-genai` (Gemini API SDK) + `google-antigravity` SDK | تخطيط الـ Scene Graph، توليد الصور (مثل Nano Banana / Gemini Image)، التحليل البصري (Vision QA)، وتنسيق الـ Agents. |
| **Segmentation & Z-Order** | `SAM 2` (Segment Anything 2) + `Grounding DINO` + `Depth-Anything v2` | فصل العناصر بدقة البكسل (البطاطس عن العيش) وترتيب الـ Z-Order من الخلف للأمام. |
| **Amodal Inpainting** | `LaMa` / `Diffusers Inpainting` / Gemini Image Edit | إكمال الأجزاء المخفية من الطبقات السفلية تحت الطبقات العلوية قبل رسمها كـ SVG. |
| **Clean Vectorization & Geometry** | `VTracer` / `DiffVG` + `Shapely` + `PyClipper` + `svgpathtools` + `OpenCV` + `scikit-image` | التبسيط اللوني الدلالي، دمج الأشكال المتجاورة (`Boolean Union`)، تنعيم منحنيات Bézier، وقص الزوائد (`Boundary Clipping`). |
| **Smart Typography** | `PaddleOCR` / `EasyOCR` + `FontTools` + `HarfBuzz` (لدعم العربية والـ RTL) | اكتشاف النصوص، مطابقة أقرب فونت، استخلاص بصمة الـ Style، وتحويل الحروف إلى مسارات SVG نظيفة. |
| **Visual QA Critic** | `scikit-image` (`SSIM`) + `NumPy` (`IoU` & Pixel Diff) + `CairoSVG` / `resvg` | تحويل الـ SVG المرسوم إلى صورة، عمل مقارنة `50% Opacity` وحساب نسبة التطابق الهندسي آلياً. |
| **Backend API & Queue** | `Python 3.12+` + `FastAPI` + `Pydantic v2` + `Celery / ARQ` (اختياري للمهام الثقيلة) | تقديم APIs سريعة وموثقة بـ Schemas صارمة لإدارة جلسات التصميم والطبقات. |
| **Frontend Interactive Canvas** | `React 19` + `TypeScript (Strict)` + `Paper.js` أو `Fabric.js` / `Konva` + `Tailwind CSS` | واجهة مصمم جرافيك تفاعلية: شجرة الطبقات والـ `<g>` Groups، أداة Pen Tool، سلايدر مقارنة 50% Opacity، وتصدير SVG. |
| **Database & Storage** | `PostgreSQL` أو `SQLite` (للتطوير المحلي) + مخزن ملفات محلي/سحابي للأصول | حفظ مشاريع التصميم، نسخ الـ Scene Graph، وبصمات الأصول (`SHA-256`). |

## 2. قواعد إدارة الحالة (`State Management Separation`)

1. **حالة الـ Scene Graph المعتمدة (`Authoritative Server Scene Graph`):** تُحفظ في الـ Backend وتضم شجرة الطبقات المعتمدة التي اجتازت فحص الـ Visual QA.
2. **حالة الـ Canvas التفاعلية (`Interactive Canvas State`):** تدير التحريك السريع، وتعديل نقاط الـ Bézier (`Anchor Handles`)، وتغيير الشفافية (`50% Opacity Slider`) في المتصفح بسلاسة (`60 FPS`) ثم تزامن التعديلات مع الـ Scene Graph.
3. **حظر خلط الحسابات الهندسية بالـ UI:** عمليات دمج المسارات (`Boolean Union`) وفصل البكسلات وحساب الـ IoU تتم عبر دوال هندسية نقية ومختبرة، وليس عبر كود عشوائي داخل مكونات الـ React.
