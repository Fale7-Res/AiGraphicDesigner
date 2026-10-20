<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "CREATED", "last_change_id": "TASK-MULTI-VER-01", "last_edited_at_utc": "2026-10-17T08:58:05Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# مصفوفة القياس المعياري الرسمية عبر الإصدارات المعمارية (`Cross-Version Benchmark Results Matrix`)

**الحالة:** معتمدة كقالب قياس حي بدون أرقام مفبركة (`OFFICIAL_RESULTS_MATRIX — ZERO_FABRICATION`)  
**حالة اعتماد التجارب:** بانتظار اعتماد المالك للتجارب الأولية (`PENDING_OWNER_FEASIBILITY_APPROVAL`)  
**قاعدة الصدق التجريبي:** لا تحتوي هذه المصفوفة على أي أرقام مختلقة؛ كافة الحقول التجريبية معلقة كـ `PENDING_EXECUTION` حتى يتم الترخيص الصريح بتشغيل الاستدلال الفعلي.

---

## 1. جدول المقارنة الشامل بين الإصدارات المعمارية الثلاثة (`Comprehensive Comparison Table`)

| الإصدار المعماري (`Version ID`) | الفرضية المعمارية الأساسية (`Core Hypothesis`) | الأصل المرجعي (`Asset`) | شريط الحواف (`Trimap IoU \ge 0.90`) | النقاء الإدراكي (`LPIPS \le 0.12`) | ميزانية العقد (`Nodes \le 36`) | زمن المعالجة (`Latency \le 8.0s`) | ذروة الذاكرة (`VRAM \le 16GB`) | التكلفة التقديرية (`Cost \le $0.04`) | حالة التحقق (`Status`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`version-01`** | **Pipeline Monolith (Schneider + SAM 2 + LaMa):** خط أنابيب متسلسل مباشر يعتمد على التكميم اللوني في فضاء LAB وملاءمة بيزييه المباشرة مع استكمال حتمي للأقنعة. | `A01` درع الهوية | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-01`** | (نفس الفرضية) | `A02` طبق الفلافل | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-01`** | (نفس الفرضية) | `A03` البرجر المعقد | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-01`** | (نفس الفرضية) | `A04` الخط العربي | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-02`** | **Hierarchical Scene Graph & Vector Optimization:** فصل تمثيل التصميم (`Design IR`) عن المحرك الهندسي، واستخدام الاتحاد البوليني للمسارات (`Boolean Union`) ومسارات القص غير التدميرية (`<clipPath>`) لمنع التفتيت. | `A01` درع الهوية | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-02`** | (نفس الفرضية) | `A02` طبق الفلافل | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-02`** | (نفس الفرضية) | `A03` البرجر المعقد | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-02`** | (نفس الفرضية) | `A04` الخط العربي | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-03`** | **Diffusion Latent Decomposition & Dual-Path Typography:** تفكيك الطبقات في الفضاء الكامن لشبكات الانتشار (`Latent Attention Masks`) مع مسار مزدوج للخط العربي يجمع بين مسارات المنحنيات ومطابقة عائلة الخط. | `A01` درع الهوية | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-03`** | (نفس الفرضية) | `A02` طبق الفلافل | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-03`** | (نفس الفرضية) | `A03` البرجر المعقد | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |
| **`version-03`** | (نفس الفرضية) | `A04` الخط العربي | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | *PENDING* | `PENDING_FEASIBILITY_APPROVAL` |

---

## 2. سجل التشغيل والعتاد المقاس (`Empirical Execution Runs Log`)

*لا توجد تشغيلات فعلية بعد — بانتظار صدور موافقة المالك على خطة الأبحاث (Phase P0 Gate).*

عند بدء القياس الفعلي، سيتم توثيق كل تشغيلة بصيغة السجل التالي:
```json
{
  "run_id": "BENCH-YYYYMMDD-001",
  "version_id": "version-XX",
  "dataset_asset_id": "A0X",
  "hardware_telemetry": { ... },
  "metrics": { ... },
  "verification_status": "VERIFIED_REAL_RUN"
}
```
