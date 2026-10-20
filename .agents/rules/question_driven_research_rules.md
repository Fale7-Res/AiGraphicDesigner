---
trigger: model_decision
description: "Ambiguity resolution and question-driven decision protocol for both developer architecture decisions and runtime user design choices (such as Typography handling)."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:32Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد حسم الغموض والقرارات الموجهة بالأسئلة (`Question-Driven Resolution & Ambiguity Rules`)

*بروتوكول بحث موجّه بالأسئلة والأدلة للتخطيط العلمي والهندسي داخل AI Graphic Designer.*

## 1. متى يسأل الـ Agent المستخدم أثناء التطوير (`Development-Time Clarification`)

1. **ابحث في الذاكرة أولاً (`Check Memory First`):**
   - قبل سؤال المطور أي سؤال، ابحث في `memory/decisions/DECISION_LOG.md` و`docs/PRODUCT_VISION_AND_MODES.md` و`MASTER_PLAN.md`. لا تكرر سؤالاً تمت الإجابة عنه وتوثيقه مسبقاً.
2. **اسأل فقط عند القرارات الهيكلية الفارقة (`Structural & Product Decisions`):**
   - إذا كان هناك قرار يغير سلوك المنتج أو التكلفة (مثل اختيار مزود موديل توليد الصور الافتراضي، أو حدود التبسيط القصوى للـ Bézier Nodes)، اعرض الخيارات بوضوح مع مميزات وعيوب كل خيار، وسجّل إجابة المستخدم فوراً في `memory/decisions/DECISION_LOG.md`.

## 2. متى يسأل النظام العميل النهائي أثناء التصميم (`Runtime Designer Interaction Rules`)

يطبق النظام قاعدة **"اسأل المصمم عندما يكون القرار ذوقياً، وتصرف تلقائياً عندما يكون القرار هندسياً نظيفاً"**:
1. **قرارات تُحسم تلقائياً بدون إزعاج العميل (`Autonomous Clean Design Decisions`):**
   - فصل العناصر المستقلة (مثل البطاطس عن العيش) في طبقات منفصلة.
   - تجميع الشكل الأساسي للعنصر مع الظل الخاص به داخل `<g id="Potato">` واحد نظيف.
   - دمج شظايا اللون المتجاورة في مسار منتظم وإصلاح أي بروز خارج حدود الطبقة.
2. **قرارات يُسأل فيها العميل صراحةً (`Explicit User Choice Gates`):**
   - **بوابة الموافقة على الصورة الكاملة (`Full Image Approval Gate` في الوضع الأول):** بعد تخطيط الطبقات وتوليد الصورة الكاملة، يعرضها النظام على العميل ويطلب موافقته قبل البدء في توليد الطبقات المفردة وتحويلها لـ SVG.
   - **بوابة التعامل مع النصوص (`Smart Typography Gate` في الوضع الثاني):** عند اكتشاف نص داخل الصورة، يسأل النظام العميل:
     - *"هل تفضل رسم هذا النص كـ Vector مطابق تماماً لشكل الحروف في الصورة، أم البحث عن أقرب Font حي قابل للكتابة والتعديل؟"*
     - وإذا اختار العميل البحث عن أقرب خط ولم يوجد خط مطابق بدرجة كافية، يقوم النظام برسمه كـ Vector نظيف مع حفظ الـ Style Identity للتعديل عليه لاحقاً.
