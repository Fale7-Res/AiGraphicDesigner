---
trigger: model_decision
description: "Rules for cataloging reference images, test designs, fonts, and SVG benchmarks in docs/ASSET_AND_EXPERIMENT_CATALOG.md."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:31Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد فهرسة الأصول البصرية وتجارب الـ SVG (`Inspected Assets & SVG Benchmark Catalog Rules`)

*يحدد هذا الملف فهرسة الأصول البصرية وتجارب التحقق من جودة الرسم القابل للتعديل.*

`docs/ASSET_AND_EXPERIMENT_CATALOG.md` هو السجل الحي لجميع الصور المرجعية، وحالات الاختبار القياسية (مثل حالة "ساندوتش الفلافل والبطاطس"، وحالة "الدرع الفضي بتفاصيل برتقالية وحمراء"، وحالات النصوص العربية والإنجليزية)، وملفات الـ SVG المرجعية.

عند إضافة أي صورة اختبار أو حالة مرجعية جديدة لتحسين خوارزميات الفصل أو الـ Clean SVG:
1. تُعطى معرّفاً قياسياً ثنائي الأرقام على الأقل (`A01`, `A02`...).
2. يُسجل مسارها، بصمة `SHA-256`، أبعادها بالبكسل (`Width x Height`)، عدد الطبقات المتوقع (`Expected Clean Layers`)، والتحدي البصري الذي تختبره (مثلاً: `Shadow Fragmentation`, `Color Bleeding between Bread and Potato`, `Curved Arabic Typography`).
3. تُسجل نتائج الفحص البصري (`IoU`, `SSIM`, `Anchor Node Count`) قبل وبعد أي تعديل في الخوارزمية لضمان عدم حدوث تراجع (`Regression`) في جودة الـ SVG.
