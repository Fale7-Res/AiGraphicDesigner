<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T09:38:50Z", "last_action": "CREATED", "last_change_id": "TASK-COLLAB-ENG-01", "last_edited_at_utc": "2026-10-17T09:38:50Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T09:38:50Z"}
END_DOC_PROVENANCE -->
# عقد ومواصفات استقبال مجموعة البيانات البصرية المستقلة (`Dataset Ingestion Contract`)

**الحالة:** معتمد كعقد تدقيق واستقبال رسمي (`ACTIVE_INGESTION_CONTRACT`)  
**المصدر المعتمد:** يزودنا بها المالك حصرياً عبر ChatGPT (`OWNER_PROVIDED_VIA_CHATGPT`)  
**حالة الجاهزية الحالية:** **`PENDING_OWNER_UPLOAD — NOT_READY`** (لم يتم رفع الصور بعد؛ يُحظر تزييف أي أصل أو استبداله بصور عشوائية).

---

## 1. هيكلية مجلدات الاستقبال (`Ingestion Directory Layout`)

```text
benchmarks/datasets/
├── DATASET_INGESTION_CONTRACT.md            # هذه الوثيقة
├── pending_chatgpt_suite/                   # مجلد الحفظ والاستقبال
│   ├── easy/                                # المستوى السهل (DS12-E01..E03)
│   ├── medium/                              # المستوى المتوسط (DS12-M01..M03)
│   ├── hard/                                # المستوى الصعب (DS12-H01..H03)
│   └── extreme/                             # المستوى المعقد والخط العربي (DS12-X01..X03)
└── holdout_set/                             # مجموعة الاختبار المحجوبة (3 صور محجوبة)
```

---

## 2. جدول تعريف الأصول الـ 12 المرجعية (`The 12-Image Benchmark Suite`)

| رمز الأصل (`Asset ID`) | مستوى الصعوبة (`Tier`) | طبيعة التصميم والتحدي المعماري | مستهدف الطبقات | حالة الاستقبال |
| :--- | :--- | :--- | :--- | :---: |
| **`DS12-E01`** | **Easy** | شارة هندسية مسطحة بحواف حادة وألوان مصمتة. | 2–3 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-E02`** | **Easy** | أيقونة متجهية بتدرج لوني خطي بسيط وظل ناعم. | 3–4 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-E03`** | **Easy** | درع حماية متماثل مع إطار بارز وعنصر مركزي. | 3–4 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-M01`** | **Medium** | ملصق شفاف ثلاثي الأبعاد مع ظلال ساقطة وانعكاسات. | 4–6 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-M02`** | **Medium** | كائنات متداخلة جزئياً مع مسار قص (`clipPath`) محدد. | 5–7 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-M03`** | **Medium (Holdout)** | تصميم شارة ترويجية مع طبقات متعددة متراكبة (محجوبة للتقييم النهائي). | 5–7 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-H01`** | **Hard** | طبق فلافل مقرمش مع حبيبات السمسم وحواف عضوية غير منتظمة. | 6–9 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-H02`** | **Hard** | شطيرة برجر متعددة الطبقات مع خضار متعرج وقطع محجوبة خلفية. | 7–10 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-H03`** | **Hard (Holdout)** | سلة مقبلات مع صوص سائل وأطعمة متشابكة (محجوبة للتقييم النهائي). | 8–12 طبقة | `PENDING_OWNER_UPLOAD` |
| **`DS12-X01`** | **Extreme** | شعار تجاري معقد يدمج الخط العربي المركب (الثلث/الديواني) مع تشكيل دقيق. | 6–10 طبقات | `PENDING_OWNER_UPLOAD` |
| **`DS12-X02`** | **Extreme** | بوستر إعلاني متعدد النصوص العربية والإنجليزية مع خلفيات لونية حية. | 8–14 طبقة | `PENDING_OWNER_UPLOAD` |
| **`DS12-X03`** | **Extreme (Holdout)** | هوية بصرية كاملة تجمع التيبوجرافي العربي والأشكال الهندسية والظلال (محجوبة). | 10–16 طبقة | `PENDING_OWNER_UPLOAD` |

---

## 3. الشروط الفنية والمعايير الإلزامية لكل أصل (`Asset Validation Invariants`)

1. **صيغة ودقة الصورة النقطية الأصلية (`Source Raster Requirements`):**
   - الصيغة المقبولة: `.png` أو `.webp` ذات ضغط عديم الفقد (Lossless).
   - الأبعاد: لا تقل عن $1024 \times 1024$ بكسل (المثالي $2048 \times 2048$).
   - البصمة الرقمية: توثيق بصمة `SHA-256` فور الاستلام لمنع أي تعديل أو تبديل لاحق.
2. **ملف البيانات الوصفية المرافق (`Metadata Schema: <asset_id>.meta.json`):**
   لكل أصل، يجب إرفاق ملف JSON يحتوي على:
   ```json
   {
     "asset_id": "DS12-H01",
     "difficulty_tier": "HARD",
     "title": "Crunchy Falafel Platter",
     "source_provider": "ChatGPT",
     "received_at_utc": "2026-10-XX...",
     "sha256": "...",
     "dimensions": {"width": 2048, "height": 2048},
     "expected_layers": [
       {"layer_id": "L01", "name": "Plate_Base", "z_index": 0},
       {"layer_id": "L02", "name": "Falafel_Balls", "z_index": 1},
       {"layer_id": "L03", "name": "Sesame_Batch", "z_index": 2}
     ],
     "typography_present": false,
     "holdout_asset": false
   }
   ```
3. **الفصل بين مستويات الحقيقة الأرضية (`Ground-Truth Separation`):**
   - **المرجع النقطي (`Raw Visual Reference`):** الصورة القادمة من المالك دون تعديل.
   - **الأقنعة الدلالية المفحوصة (`Verified Semantic Masks`):** أقنعة ثنائية لكل طبقة معتمدة بشكل مستقل.
   - **المتجه المرجعي (`Ground-Truth Clean SVG`):** ملف SVG مرجعي عالي النقاء لمقارنة عدد العقد وجودة المنحنيات.
4. **حظر الخلط مع اختبارات الـ Unit Tests (`No Synthetic Substitution`):**
   - يُمنع منعاً باتاً استبدال هذه الأصول الـ 12 بالعينات المصطنعة البسيطة المستخدمة في `tests/fixtures/`.
   - لا تصبح المجموعة `READY` للقياس المعماري إلا بعد اكتمال رفع الملفات وتدقيقها من المراجع المستقل `qa-reviewer-auditor`.
