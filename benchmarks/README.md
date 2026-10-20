<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "CREATED", "last_change_id": "TASK-MULTI-VER-01", "last_edited_at_utc": "2026-10-17T08:58:05Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# نظام القياس المعياري المشترك عبر الإصدارات (`Cross-Version Benchmarking Architecture`)

**الحالة:** نشط معمارياً (`ACTIVE_GOVERNANCE_SPECIFICATION`)  
**حالة اعتماد التجارب:** بانتظار اعتماد المالك للتجارب الأولية (`PENDING_OWNER_FEASIBILITY_APPROVAL`)  
**سياق الحوكمة:** وثيقة المقارنة المشتركة لنظام الإصدارات المتعددة (`Multi-Version Architecture System`).

---

## 1. الغرض والمبادئ الحاكمة (`Purpose & Iron Core Principles`)

يمثل مجلد `benchmarks/` نظام القياس المعياري المشترك المحايد لكافة الإصدارات المعمارية المطورة داخل مجلد `versions/`.
في هذا المشروع البحثي، تُختبر معماريتات متعددة متنافسة (مثل `version-01`, `version-02`, `version-03`) دون أي تحيز مسبق ودون اعتبار الإصدار الأحدث متفوقاً تلقائياً.

### المبادئ الصارمة لمنع اختلاق النتائج (`Anti-Fabrication & Empirical Integrity`):
1. **حظر اختلاق الأرقام (`Zero Fabricated Results Invariant`):** يُحظر تماماً كتابة أرقام قياسية أو نسب مئوية افتراضية أو وهمية. أي قياس يُسجل في `RESULTS_MATRIX.md` يجب أن ينشأ من تشغيل حقيقي لأداة `benchmarks/harness/run_benchmark.py` مع توثيق بصمة الأصول والعتاد المستخدم.
2. **شروط عتادية ونماذج موحدة ومسجلة (`Standardized Telemetry`):** تُسجل كل تجربة بمعلومات بيئتها الدقيقة (نوع كارت الشاشة GPU، حجم ذاكرة الفيديو VRAM، إصدار CUDA، نظام التشغيل، ووقت المعالجة الفعلي).
3. **حفظ التجارب غير الناجحة (`Preservation of Failed Experiments`):** لا يُحذف أي إصدار أو تجربة أظهرت نتائج سلبية أو متدنية؛ الفشل الهندسي الموثق هو أساس استبعاد الخيارات المعمارية غير القابلة للإنتاج.
4. **حظر دمج الميزات بين الإصدارات (`Zero Cross-Version Feature Merging`):** كل إصدار يحتفظ بحدوده البرمجية المستقلة، ولا يجوز نقل أو دمج كود من إصدار لآخر دون قرار اعتمادي موثق في `memory/decisions/DECISION_LOG.md`.

---

## 2. هيكلة نظام القياس المعياري (`Benchmarking Structure`)

```
benchmarks/
├── README.md                  # الوثيقة الحالية: المعمارية والمبادئ الحاكمة
├── DATASETS.md                # توصيف أصول الاختبار الذهبية A01–A04 ومجموعة الـ 30 أصلاً
├── METRICS.md                 # المعادلات الرياضية الدقيقة والعتبات (IoU, LPIPS, Node Budget, Latency, Cost)
├── EVALUATION_PROTOCOL.md     # بروتوكول التشغيل خطوة بخطوة وإجراءات التدقيق
├── RESULTS_MATRIX.md          # مصفوفة النتائج الرسمية للمقارنة بين الإصدارات (غير مفبركة)
└── harness/                   # أدوات التشغيل الآلية
    ├── benchmark_schema.json  # مخطط JSON المعتمد لتسجيل بيانات كل تشغيلة
    └── run_benchmark.py       # سكريبت الفحص والتحقق من صحة القياسات والعتاد
```

---

## 3. الأبعاد السبعة للمقارنة المعمارية (`7 Evaluation Dimensions`)

| البعد القياسي (`Dimension`) | المقياس المعتمد (`Metric`) | الهدف المطلوب (`Target`) | طريقة القياس (`Tool/Method`) |
| :--- | :--- | :--- | :--- |
| **1. دقة الفصل والتفكيك** | `Trimap Boundary IoU (8px)` | $\ge 0.90$ عند الحواف | قناع التقييم على الحواف الملتصقة (A02, A03) |
| **2. جودة الفيكتور النظيف** | `Max Bézier Node Count` | $\le 36$ عقدة لكل مسار | فحص شجرة الـ SVG ومنع المسارات المجزأة |
| **3. النقاء الإدراكي للبصريات** | `LPIPS (AlexNet/VGG)` | $\le 0.12$ | مقارنة بصرية بين الصورة النقطية وتصيير الـ SVG |
| **4. التشابه الهيكلي للطبقات** | `SSIM` | $\ge 0.92$ | قياس التشابه الهيكلي لكل طبقة بعد إعادة التركيب |
| **5. زمن المعالجة الإجمالي** | `End-to-End Latency (s)` | $\le 8.0$ ثوانٍ | قياس زمني عبر `time.perf_counter` من الإدخال للـ SVG |
| **6. استهلاك ذاكرة العتاد** | `Peak VRAM Consumption (GB)`| $\le 16.0$ جيجابايت | قراءة مستمرة لحجم ذاكرة كارت الشاشة عبر PyTorch CUDA |
| **7. التكلفة التشغيلية لكل تصميم**| `Operating Cost per Design ($)`| $\le \$0.04$ | حساب تسعيرة الحوسبة السحابية الخادمة (Modal/RunPod) |
