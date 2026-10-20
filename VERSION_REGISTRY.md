<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "EDITED", "last_change_id": "TASK-V04-CHALLENGER-REVIEW", "last_edited_at_utc": "2026-10-18T00:25:26Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# السجل المركزي لإصدارات المعمارية التجريبية (`VERSION_REGISTRY.md`)

**الحالة:** معتمد كمرجعية حوكمية رئيسية لتتبع الإصدارات المعمارية المتعددة (`ACTIVE_VERSION_REGISTRY`)  
**حالة اعتماد المعمارية الشاملة:** غير معتمدة بعد (`NOT_APPROVED — PROPOSED_FOR_OWNER_REVIEW`)  
**المبادئ الحاكمة:**
1. **عدم التفوق التلقائي للإصدار الأحدث:** الإصدار الأحدث ليس أفضل بالضرورة؛ المعيار الوحيد للاختيار هو النتائج القياسية الصارمة والمثبتة تجريبياً في `benchmarks/RESULTS_MATRIX.md`.
2. **عزل الكود والمرايا:** كل إصدار يمتلك مجلده المستقل بالكامل تحت `versions/` مع ملفات الكود، الاختبارات، الاعتماديات، التوثيق، وسجل الدوال، والمرايا تحت `docs/CODE_MIRRORS/`.
3. **حفظ التجارب غير الناجحة:** لا يُحذف أي إصدار فاشل؛ الفشل الهندسي الموثق هو أساس حماية المشروع من تكرار الأخطاء.
4. **حظر الدمج بدون قرار:** يُحظر نقل أو دمج وظائف بين الإصدارات دون قرار رسمي معتمد في `memory/decisions/DECISION_LOG.md`.
5. **استراتيجية التطوير الهجينة المحكومة وتسلسل القياس على اللابتوب:** يبدأ العمل بإثبات شريحة رأسية دنيا متكاملة وقابلة للقياس في `version-01` محلياً، ثم يُسمح لـ `version-02` و`version-03` بالعمل بالتوازي في بيئات معزولة، مع إلزامية تسلسل القياسات الثقيلة على لابتوب المالك لمنع الاختناق الحراري وتشتت الموارد (انظر تفاصيل الإجراءات في [`docs/governance/MULTI_AGENT_COLLABORATION_AND_VERSION_STRATEGY.md`](docs/governance/MULTI_AGENT_COLLABORATION_AND_VERSION_STRATEGY.md)).

---

## 1. جدول الإصدارات المعمارية المقيدة (`Registered Architecture Versions`)

| Version ID | Architecture Hypothesis | Purpose | Current Status | Source Directory | Dependencies | Benchmark Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`version-01`** | **Sequential Pipeline Monolith:** خط أنابيب متسلسل يعتمد على التكميم اللوني في فضاء LAB وملاءمة شنايدر لبيزييه واستكمال الأقنعة بـ LaMa. | إثبات جدوى المعالجة المتسلسلة المباشرة بأبسط بنية هندسية ممكنة. | `PROPOSED_EXPERIMENTAL_SKELETON` | `versions/version-01/` | PyTorch, torchvision, opencv-python, numpy, shapely | `benchmarks/RESULTS_MATRIX.md` (*PENDING*) |
| **`version-02`** | **Hierarchical Scene Graph & Vector Optimization:** تمثيل التصميم عبر `Design IR` المنفصل مع توحيد المسارات بالاتحاد البوليني ومسارات القص `<clipPath>` لحصر الظلال. | تحقيق أعلى درجة قابلية للتعديل اليدوي ومنع تفتيت الفيكتور للأطعمة والأشكال المعقدة. | `PROPOSED_EXPERIMENTAL_SKELETON` | `versions/version-02/` | PyTorch, shapely, rtree, svgelements, pydantic | `benchmarks/RESULTS_MATRIX.md` (*PENDING*) |
| **`version-03`** | **Diffusion Latent Decomposition & Dual-Path Typography:** تفكيك الطبقات في الفضاء الكامن لشبكات الانتشار مع مسار مزدوج للخط العربي يجمع بين المنحنيات ومطابقة الخطوط. | اختبار قدرات نماذج الانتشار الحديثة في فهم العمق الدلالي ومعالجة الخط العربي المركب. | `PROPOSED_EXPERIMENTAL_SKELETON` | `versions/version-03/` | diffusers, transformers, torch, fonttools, uharfbuzz | `benchmarks/RESULTS_MATRIX.md` (*PENDING*) |
| **`version-04-claude-challenger`** | **Adaptive Surface Quadtree Grid + Edge Residual Vector Overlay:** شبكة رباعية تكيفية من 9,000 مستطيل بتدرجات رتبة-1 محلية، مع مسارات بكسلية متجهة على الحواف المكتشفة بـ Canny. | تقييم مقارن مستقل مقدم من المالك لاختبار السقف الإحصائي للدقة البصرية مقابل القابلية للتعديل الفيكتوري الاحترافي. | `EXPERIMENTAL_CHALLENGER_EVALUATED` | `versions/version-04-claude-challenger/` | numpy, opencv-python, scipy | متوسط PSNR: 28.04 dB، SSIM: 0.883، MSE: 109.52. 9,000 مستطيل، 1,111-5,268 مسار نقطي، 0 منحنيات بيزييه. دقة بصرية فائقة / انعدام القابلية للتعديل الاحترافي. |


---

## 2. السجلات التفصيلية لكل إصدار (`Detailed Version Profiles`)

---

### إصدار المعمارية: `version-01`
- **معرف الإصدار (`Version ID`):** `version-01`
- **الفرضية المعمارية (`Architecture Hypothesis`):** خط أنابيب متسلسل مباشر (Sequential Monolithic Pipeline) يعتمد على خوارزمية شنايدر لملاءمة منحنيات بيزييه بعد التكميم اللوني في فضاء CIELAB، مع استخدام SAM 2 للتجزئة واستكمال الأشكال المحجوبة بـ LaMa، يحقق زمن معالجة سريع وتعقيداً معمارياً منخفضاً.
- **الغرض (`Purpose`):** تأسيس خط أساس مرجعي (Baseline) لقياس الأداء ودقة المنحنيات ومقارنة المعماريات الأكثر تعقيداً به.
- **الحالة الحالية (`Current Status`):** `PROPOSED_EXPERIMENTAL_SKELETON` (هيكل تجريبي مقترح بانتظار اعتماد المالك).
- **المجلد المصدري (`Source Directory`):** `versions/version-01/`
- **الاعتماديات الرئيسية (`Dependencies`):** `torch>=2.4.0`, `opencv-python>=4.10.0`, `numpy>=1.26.0`, `shapely>=2.0.0`.
- **ملف إعدادات التجارب (`Experiment Configuration`):** `versions/version-01/experiments/EXPERIMENT_CONFIG.json`
- **ملخص نتائج القياس (`Benchmark Results`):** بانتظار تشغيل التجارب بعد الاعتماد؛ مسجلة في `benchmarks/RESULTS_MATRIX.md`.
- **القيود المعروفة (`Known Limitations`):**
  - صعوبة التعامل مع التدرجات الناعمة المعقدة دون ظهور خطوط لونية حادة (Banding).
  - احتمالية تفتت مسارات الظلال الملتصقة في الأطعمة المتشابكة مثل الفلافل.
- **القرارات المعمارية المرتبطة (`Important Decisions`):** [DEC-VER01-001] اختيار فضاء CIELAB كمعيار وحيد للمسافة اللونية $\Delta E$.
- **مكتشفات المراجعين (`Reviewer Findings`):** أشار مراجع الفيكتور إلى أن خط الأنابيب المتسلسل يفتقر إلى آلية تراجع تفاعلية عند فشل ملاءمة المنحنيات.
- **التوصية أو سبب الرفض (`Recommendation / Rejection Reason`):** احتفاظ به كخط أساس مرجعي إلزامي (`Authoritative Baseline`) للمقارنة العادلة.

---

### إصدار المعمارية: `version-02`
- **معرف الإصدار (`Version ID`):** `version-02`
- **الفرضية المعمارية (`Architecture Hypothesis`):** معمارية شجرة المشهد الهرمية المتجهية (Hierarchical Scene Graph & Design IR) مع فصل منطق الرؤية عن المحرك الهندسي، واعتماد الاتحاد البوليني للمسارات المتجاورة ومسارات القص غير التدميرية (`<clipPath>`)، تضمن الحفاظ على ميزانية العقد ($\le 36$) وتمنع تفتيت المسارات في الأطعمة المتشابكة مع تمكين التعديل التفاعلي المباشر (Pen Tool handles).
- **الغرض (`Purpose`):** تلبية متطلبات المالك الصريحة بنسبة 100% في إنتاج ملفات Clean SVG مقسمة لمجموعات دلالية تحاكي رسم المصمم المحترف.
- **الحالة الحالية (`Current Status`):** `PROPOSED_EXPERIMENTAL_SKELETON` (هيكل تجريبي مقترح بانتظار اعتماد المالك).
- **المجلد المصدري (`Source Directory`):** `versions/version-02/`
- **الاعتماديات الرئيسية (`Dependencies`):** `torch>=2.4.0`, `shapely>=2.0.0`, `rtree>=1.3.0`, `svgelements>=1.9.0`, `pydantic>=2.8.0`.
- **ملف إعدادات التجارب (`Experiment Configuration`):** `versions/version-02/experiments/EXPERIMENT_CONFIG.json`
- **ملخص نتائج القياس (`Benchmark Results`):** بانتظار تشغيل التجارب بعد الاعتماد؛ مسجلة في `benchmarks/RESULTS_MATRIX.md`.
- **القيود المعروفة (`Known Limitations`):**
  - ارتفاع استهلاك المعالجة الحسابية أثناء العمليات البولينية (`Boolean Union`) على المضلعات المعقدة.
- **القرارات المعمارية المرتبطة (`Important Decisions`):** [DEC-VER02-001] عزل العمليات البولينية داخل `ProcessPoolExecutor` بسقف زمني 2.5 ثانية.
- **مكتشفات المراجعين (`Reviewer Findings`):** أيد مراجعو النظم والفيكتور هذه المعمارية كمرشح واعد يحقق توازناً هندسياً ممتازاً بين الدقة البصرية ونظافة الفيكتور.
- **التوصية أو سبب الرفض (`Recommendation / Rejection Reason`):** مرشح رئيسي لتجارب الجدوى الأولية (Phase P0 Gate).

---

### إصدار المعمارية: `version-03`
- **معرف الإصدار (`Version ID`):** `version-03`
- **الفرضية المعمارية (`Architecture Hypothesis`):** معمارية التفكيك في الفضاء الكامن لشبكات الانتشار (Latent Diffusion Decomposition) مع دمج محرك تيبوجرافي مزدوج المسار (Dual-Path Arabic Typography) يجمع بين تحويل الحروف المتصلة إلى مسارات فيكتور دقيقة ومطابقة عائلة الخط والوزن لتوفير طبقة نصية بديلة قابلة للتحرير المباشر.
- **الغرض (`Purpose`):** تحقيق أعلى دقة بصرية في التعامل مع الصور الواقعية والشعارات والخط العربي المعقد.
- **الحالة الحالية (`Current Status`):** `PROPOSED_EXPERIMENTAL_SKELETON` (هيكل تجريبي مقترح بانتظار اعتماد المالك).
- **المجلد المصدري (`Source Directory`):** `versions/version-03/`
- **الاعتماديات الرئيسية (`Dependencies`):** `diffusers>=0.30.0`, `transformers>=4.44.0`, `torch>=2.4.0`, `fonttools>=4.53.0`, `uharfbuzz>=0.39.0`.
- **ملف إعدادات التجارب (`Experiment Configuration`):** `versions/version-03/experiments/EXPERIMENT_CONFIG.json`
- **ملخص نتائج القياس (`Benchmark Results`):** بانتظار تشغيل التجارب بعد الاعتماد؛ مسجلة في `benchmarks/RESULTS_MATRIX.md`.
- **القيود المعروفة (`Known Limitations`):**
  - ارتفاع استهلاك ذاكرة الفيديو (VRAM $\ge 14\text{ GB}$) وزمن استجابة أطول مقارنة بالمعماريتين الأخريين.
- **القرارات المعمارية المرتبطة (`Important Decisions`):** [DEC-VER03-001] تشغيل استدلال نماذج الانتشار حصرياً عبر بيئة سحابية خادمة عند الطلب (`Serverless GPU`).
- **مكتشفات المراجعين (`Reviewer Findings`):** أوصى مراجع الذكاء الاصطناعي والأمان بوضع ضوابط صارمة لاستهلاك الذاكرة ومراقبة التكلفة.
- **التوصية أو سبب الرفض (`Recommendation / Rejection Reason`):** مرشح متخصص لتقييم الحالات الحدية للخط العربي والصور الفوتوغرافية عالية التفاصيل.

---

### إصدار المعمارية: `version-04-claude-challenger`
- **معرف الإصدار (`Version ID`):** `version-04-claude-challenger`
- **الفرضية المعمارية (`Architecture Hypothesis`):** الجمع بين سطح لوني تكيفي يعتمد على تقسيم رباعي متكرر (Quadtree) محكوم بالصور التكاملية وملاءمة تدرجات خطية محلية برتبة-1 عبر SVD ينتج 9,000 مستطيل `<rect>`، مع طبقة متبقيات متجهة للحواف الحادة (Canny Edge Residual Band) مشفرة كمسارات أفقية بكسلية بارتفاع 1px (`M...h...v1h...Z`)، يحقق قفزة كبرى في الدقة البصرية الإحصائية دون الاعتماد على التجزئة الدلالية.
- **الغرض (`Purpose`):** إجراء تقييم مستقل ومناظرة هندسية صارمة لمتحدي خارجي مستقل مقدم من المالك، وفصل مكاسب الدقة البصرية عن كوارث فقدان القابلية للتعديل، واستخلاص المكونات القابلة لإعادة الاستخدام والدمج.
- **الحالة الحالية (`Current Status`):** `EXPERIMENTAL_CHALLENGER_EVALUATED` (تم تقييمه واختباره وتدقيقه هندسياً كمتحدٍ مستقل).
- **المجلد المصدري (`Source Directory`):** `versions/version-04-claude-challenger/`
- **الاعتماديات الرئيسية (`Dependencies`):** `numpy>=1.24.0`, `opencv-python>=4.8.0`, `scipy>=1.11.0`.
- **ملف إعدادات التجارب (`Experiment Configuration`):** `versions/version-04-claude-challenger/experiments/EXPERIMENT_CONFIG.json`
- **ملخص نتائج القياس (`Benchmark Results`):**
  - متوسط PSNR: 28.04 dB (ارتفاع من 18.02 dB لخط أساس V01 القديم).
  - متوسط SSIM: 0.883 (ارتفاع من 0.599).
  - متوسط MSE: 109.52 (انخفاض من 1074.58).
  - زمن المعالجة: 2.1–4.8 ثوانٍ على المعالج المركزي المحلي.
  - حجم ملفات SVG: متوسط 1.22 MB لكل صورة.
- **القيود الجوهرية والعيوب القاتلة (`Critical Verified Flaws`):**
  - **انعدام تام لمنحنيات بيزييه (`Zero Bézier Curves`):** لا يحتوي على أي أمر `C` (Cubic) أو `Q` (Quadratic)؛ الهندسة عبارة عن 9,000 مستطيل محاذي للمحاور وآلاف الخطوط البكسلية المستقيمة.
  - **انعدام القابلية للتعديل اليدوي (`Zero Professional Editability`):** شجرة العناصر في Illustrator/Inkscape تتجاوز 10,000 عنصر لكل تصميم؛ تفكك الشكل الواحد (مثل شطيرة البرجر) إلى مئات المربعات وآلاف الشرائح المجهرية مما يستحيل تحريكه أو تعديل ألوانه.
  - **انعدام التجميع الدلالي والطبقات (`No Semantic Layers`):** غياب كامل لوسوم `<g>` الدلالية أو الطبقات المعنونة، وغياب أي تمييز للنصوص أو الظلال أو الانعكاسات.
- **مكتشفات المراجعين (`Reviewer Findings`):** أثبتت المناظرة الهندسية أن V04 حقق دقته البصرية العالية بترميز بكسلات الراستر فيكتورياً (Raster-in-Vector disguise)، ويوصى برفض اعتماده كمعمارية، مع استخلاص آليات تسريع الحسابات التكاملية والانحدار المكاني للتدرجات وإعادة توظيفها داخل بديل الحدود المشتركة المستوية V09.
- **التوصية أو سبب الرفض (`Recommendation / Rejection Reason`):** `REJECT_AS_ARCHITECTURE / ADAPT_SPECIFIC_TECHNIQUES` (مرفوض كمعمارية تصميمية للـ Clean SVG، ومقبول لإعادة توظيف خوارزميات تسريع الإحصاءات وتقدير التدرجات).

