# بوابات الجدوى التقنية والتجارب الإلزامية للوظائف عالية المخاطر (`docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md`)

**الحالة المعمارية الحالية (`Current Project Gate`):**
- `PROJECT_STAGE`: `ARCHITECTURE_AND_GOVERNANCE_PREPARATION`
- `ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED` (`PROPOSED_ONLY`)
- `P0_IMPLEMENTATION_GATE`: `BLOCKED_PENDING_OWNER_APPROVAL_AND_FEASIBILITY_EXPERIMENTS`

> **قاعدة حاكمة:** يُحظر اعتبار أي مقترح تقني أو اختيار مكتبة في هذا المشروع بمثابة `OWNER_APPROVED` أو `EXPERIMENTALLY_VALIDATED` قبل تنفيذ تجارب الجدوى الكمية أدناه والحصول على موافقة صريحة وموثقة من المالك.

## 1. الفصل الصارم بين المستويات الأربعة (`Four-Tier Separation Invariant`)

| المستوى (`Tier`) | الحالة القياسية (`Status Code`) | التعريف الدقيق | المرجع الحاكم (`Authoritative File`) |
| :--- | :--- | :--- | :--- |
| **1. رؤية ومتطلبات المالك** | `OWNER_REQUIREMENT` | ما نص عليه المالك حرفياً في رؤيته الأصلية (الأوضاع الثلاثة، النظافة كـ Pen Tool، جروب البطاطس + الظل، مقارنة 50% Opacity، ذكاء الخطوط، والذاكرة الحية). | `docs/product/OWNER_ORIGINAL_VISION.md` |
| **2. الحلول التقنية المقترحة** | `PROPOSED` | المعمارية، والموديلات، والمكتبات المقترحة من قِبل الـ AI (مثل SAM 2، VTracer، DiffVG، FastAPI، React Canvas) والتي لم تُختبر تجريبياً بعد ولم يعتمدها المالك. | `docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md` |
| **3. الأبحاث وتجارب الجدوى** | `UNDER_RESEARCH` / `EXPERIMENTALLY_VALIDATED` | التجارب العملية المعزولة لقياس دقة الفصل الدلالي ونظافة الـ SVG وتكلفة/سرعة الاستدعاء على الحالات المرجعية `A01–A04`. | `docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md` |
| **4. المعمارية المعتمدة للتنفيذ** | `OWNER_APPROVED` | القرارات التي راجعها المالك بعد ظهور نتائج التجارب وأصدر أمراً صريحاً باعتمادها لبدء تنفيذ المنتج. | `memory/decisions/DECISION_LOG.md` |

## 2. سجل تجارب الجدوى الإلزامية للوظائف عالية المخاطر (`Mandatory High-Risk Feasibility Experiments`)

قبل الالتزام النهائي بأي مكتبة أو معمارية لمحرك الجرافيك، يجب تنفيذ التجارب الخمس التالية وتوثيق نتائجها في `memory/findings/`:

| كود التجربة (`Experiment ID`) | المخاطرة التقنية المستهدفة (`High-Risk Capability`) | حالة الاختبار المرجعية (`Benchmark Asset`) | المرشحون للمقارنة (`Candidates to Compare`) | معايير النجاح الكمية (`Quantitative Pass Criteria`) | الحالة الحالية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EXP-01` | **الفصل الدلالي الدقيق لعناصر متقاربة اللون بدون نزيف بكسلات (`Semantic Decomposition without Color Bleeding`)** | `A03`: ساندوتش البطاطس والعيش (فصل اللون الأصفر للبطاطس عن البيج/البني للعيش). | 1) `SAM 2 + Grounding DINO`<br>2) `Florence-2 + SAM 2`<br>3) `Multimodal VLM BBox + GrabCut/Watershed` | - `Boundary IoU >= 0.92`<br>- `Cross-Layer Pixel Bleed <= 1.5%`<br>- زمن الفصل `< 4s` للصورة. | `UNDER_RESEARCH` (لم تنفذ بعد) |
| `EXP-02` | **منع تشظي الـ SVG وتجميع `<g>` (الشكل الأساسي + الظل كقطعة نظيفة) (`High-Fidelity Clean SVG & Anti-Fragmentation`)** | `A02` (الفلافل) & `A03` (البطاطس والظل بتاعها). | 1) `Morphological Quantization + Shapely Union + VTracer`<br>2) `DiffVG Differentiable Bézier Fitting`<br>3) `Potrace Multi-Pass + Douglas-Peucker Curve Fitting` | - صفر شظايا مجهرية (`0 micro-shards < 16px²`)<br>- عدد نقاط الـ Bézier (`Anchor Nodes`) لكل شكل `<= 36`<br>- تطابق بصري `SSIM >= 0.93` داخل `<g>` منظم. | `UNDER_RESEARCH` (لم تنفذ بعد) |
| `EXP-03` | **استنتاج ترتيب الطبقات (`Z-Order`) وإكمال الأجزاء المخفية (`Amodal Completion / Inpainting`)** | `A01` (الدرع الفضي وتفاصيله) & `A03` (العيش تحت البطاطس). | 1) `Depth-Anything v2 + Occlusion Graph + LaMa Inpainting`<br>2) `VLM Layer Ordering + Gemini Image Edit Inpainting`<br>3) `Geometric Convex/Spline Contour Completion` | - دقة ترتيب `Z-Order = 100%` على الحالات المرجعية<br>- اتصال وسلامة الطبقة السفلية بعد إخفاء الطبقة العلوية بدون ثقوب. | `UNDER_RESEARCH` (لم تنفذ بعد) |
| `EXP-04` | **حلقة المراجعة البصرية بشفافية `50% Opacity` وتصحيح الأبعاد التلقائي (`50% Opacity Critic Convergence`)** | `A01`, `A02`, `A03` | 1) `Programmatic Raster Overlay (CairoSVG) + IoU/Pixel-Diff Map`<br>2) `Hybrid Programmatic Diff + Vision LLM Critic` | - وصول التطابق إلى `IoU >= 0.94` خلال `<= 3` دورات تصحيح<br>- إجمالي زمن التحقق للطبقة `< 2s`. | `UNDER_RESEARCH` (لم تنفذ بعد) |
| `EXP-05` | **التعرف على الخطوط، تخيير المستخدم، وإعادة رسم النصوص بنفس الهوية (`Smart Typography & Style DNA Synthesis`)** | `A04`: شعار نصي عربي/إنجليزي بستايل خاص. | 1) `PaddleOCR/EasyOCR + Font Embedding Matcher + SVG Path Warp`<br>2) `VLM Glyph Style Extractor + Few-Shot Vector Glyph Generator` | - دقة فصل الحروف واستخلاص سمك/لون/انحناء الخط<br>- نجاح تعديل كلمة مع الحفاظ على الهوية البصرية. | `UNDER_RESEARCH` (لم تنفذ بعد) |
