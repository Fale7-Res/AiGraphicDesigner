<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "EDITED", "last_change_id": "TASK-V01-CORRECTION-01", "last_edited_at_utc": "2026-10-17T19:18:00Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# Architecture Specification: Version 01 (Sequential Pipeline Monolith)

**المعرف:** `version-01`  
**النمط المعماري:** Pipeline Monolith  
**حالة الاعتماد:** `NOT_APPROVED — PROPOSED_FOR_OWNER_REVIEW`

---

## 1. الفرضية الهندسية ومخطط تدفق البيانات (`Architecture Hypothesis & Flow`)

تعتمد معمارية `version-01` على تسلسل خطي مباشر لمعالجة الصور وتفكيكها إلى متجهات:
1. إدخال الصورة النقطية وتحديد الأقنعة الدلالية عبر SAM 2.
2. تكميم الألوان داخل كل قناع في فضاء CIELAB لتقليل الضوضاء.
3. استخراج مضلعات الحدود وملاءمتها مباشرة إلى منحنيات بيزييه عبر خوارزمية شنايدر (Schneider Bézier Fitting).
4. استكمال الأجزاء المحجوبة عمقياً عبر خوارزمية LaMa للترميم الدلالي.
5. تصدير ملف Clean SVG متسلسل.

```mermaid
flowchart LR
    InputImg[صورة الإدخال] --> SegSAM2[التجزئة بـ SAM 2]
    SegSAM2 --> QuantLAB[تكميم CIELAB]
    QuantLAB --> SchneiderFit[ملاءمة بيزييه شنايدر]
    SchneiderFit --> InpaintLaMa[استكمال المحجوب LaMa]
    InpaintLaMa --> OutputSVG[تصدير Clean SVG]
```

---

## 2. المكونات البرمجية الأساسية (`Core Components`)

- `src/geometry/bezier.py`:
  - كلاس `BezierCurve` لتمثيل المنحنيات التكعيبية.
  - دالة `fit_schneider_bezier`: تطبق خوارزمية شنايدر لتقريب مصفوفة النقاط إلى أقل عدد ممكن من مقاطع بيزييه مع الحفاظ على ميزانية العقد $\le 36$.
- `src/pipeline.py`:
  - كلاس `SequentialPipeline`: يدير تدفق البيانات المتسلسل من الإدخال حتى تصدير الـ SVG.

---

## 3. معايير القبول ونقاط الخطر (`Acceptance Gates & Risks`)

- **معيار النجاح:** اجتياز الفحص الهندسي للأصول A01 وA02 بزمن استجابة أقل من 5 ثوانٍ.
- **نقطة الخطر:** احتمالية تفتت مسارات الظلال في الأطعمة المتشابكة نظراً لغياب خطوة الاتحاد البوليني المسبقة.

---

## 4. المكتشفات التقنية المعتمدة لترتيب الطبقات وسد الشروخ (`FND-20261017-003`)

- **المرجع:** `FND-20261017-003` (ترتيب الطبقات الطوبولوجي وسد الشروخ الظلية).
- **التشخيص:** فرز العناقيد اللونيّة عالمياً بمجرد عدد البكسلات (`cluster_areas.sort`) يخل بالعلاقات المكانية للتضمين والاحتواء الطوبولوجي، مما يقلب ترتيب الطبقات في الأشكال المتداخلة والنصوص.
- **الحل المعتمد:** تطبيق مخطط الاحتواء الطوبولوجي الموجه (Topological Enclosure DAG) وفرز كان (Kahn's Topological Sort) لترتيب الطبقات، مع تمديد مقيد بالمحيط الخارجي (Silhouette-constrained dilation) لسد الشروخ البينية دون تشويه الحواف الحادة.

