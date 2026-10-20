<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:54:02Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# الفهرس الرئيسي للذاكرة الحية للمشروع (`memory/MEMORY_INDEX.md`)

**مرحباً بك في العقل الخارجي الحي (`External Brain`) لمشروع AI Graphic Designer.**
- **المرحلة الحالية (`Project Stage`):** `ARCHITECTURE_AND_GOVERNANCE_PREPARATION` (لم يبدأ تنفيذ كود المنتج؛ المعمارية `NOT_APPROVED` وتنتظر تجارب الجدوى واعتماد المالك).
- **مرجع الرؤية الأصلية للمالك (`Authoritative Verbatim Vision`):** [docs/product/OWNER_ORIGINAL_VISION.md](../docs/product/OWNER_ORIGINAL_VISION.md) و[docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md](../docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md).

## 1. ملخص تنفيذي: ماذا نبني؟ (`What We Are Building`)

نظام **AI Graphic Designer** يعمل بعقلية مصمم جرافيك محترف يستخدم الـ `Pen Tool`، ويشمل الأوضاع الثلاثة التي نص عليها المالك في رؤيته الأصلية:
1. **الوضع الأول (`Planned-Layers Image Generation`):** تحليل الوصف -> تخطيط الطبقات والأشكال الهندسية والأبعاد والألوان -> توليد الصورة الكاملة -> موافقة العميل -> توليد كل طبقة لوحدها بنفس المواصفات -> تحويلها إلى **Clean SVG** وتجميع الأشكال المتجاورة وفصل العناصر المستقلة (مثل البطاطس عن العيش).
2. **الوضع الثاني (`Magic Layers Decomposition`):** تحليل صورة جاهزة -> تحديد عدد الطبقات وترتيب الـ `Z-Order` والأبعاد والمنحنيات -> تصميم كل طبقة من الأسفل للأعلى -> مراجعة كل طبقة بواسطة AI ثانٍ يضعها فوق الصورة الأصلية بشفافية `50% Opacity` قبل الانتقال للطبقة التالية -> التعامل الذكي مع النصوص (سؤال العميل بين الرسم المطابق أو أقرب فونت مع حفظ هوية الخط).
3. **الوضع الثالث (`Layer-Aware Vector & Text Editing`):** تطبيق Magic Layers والـ Clean Design أولاً -> تنفيذ تعديلات العميل على الـ `Art Layers` -> إعادة رسم النصوص المعدلة بنفس `Font Style Identity` -> إخراج **Clean SVG** (مع تجميع كل عنصر وظله في Group منظم مثل `<g id="Potato">`).

## 2. خريطة ملفات الذاكرة الحية ومصادر الحقيقة (`External Brain Navigation`)

| ملف الذاكرة | دوره ومسؤوليته الوحيدة (`Single Responsibility`) | طريقة التحديث |
| :--- | :--- | :--- |
| [docs/product/OWNER_ORIGINAL_VISION.md](../docs/product/OWNER_ORIGINAL_VISION.md) | النص العربي الأصلي الكامل للمالك حرفياً بدون أي تعديل (`OWNER_REQUIREMENT` Authority). | ثابت ومحمّي (`Immutable`). |
| [docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md](../docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md) | ربط عبارات المالك الأصلية (`OV-01..18`) بالمتطلبات المشتقة وبوابات الجدوى (`EXP-01..05`). | عند تحديث المتطلبات أو التجارب. |
| [memory/session/CURRENT_TASK_CHECKPOINT.md](session/CURRENT_TASK_CHECKPOINT.md) | نقطة التوقف الحية للجلسة وحالة بوابات الاعتماد الحالية. | يُحدث مع كل خطوة. |
| [memory/session/ACTIVE_SESSION_WAL.md](session/ACTIVE_SESSION_WAL.md) | سجل الكتابة المسبقة الرئيسي للـ Parent Agent. | يُحدث فوراً في نفس الخطوة. |
| `memory/session/subagent_wals/*.wal.md` | سجلات الـ WAL المعزولة لكل Sub-Agent لمنع التضارب أثناء العمل المتوازي. | يكتب كل Sub-Agent في ملفه المعزول فقط. |
| [memory/findings/FINDINGS_LEDGER.md](findings/FINDINGS_LEDGER.md) | السجل الموحد لمكتشفات الـ Sub-Agents (`memory/findings/entries/*.json`) وأحداث مراجعة الـ Parent وترقيتها. | يُجمّع آلياً عبر `manage_findings.py compile-ledger`. |
| [memory/session/RECOVERY_PACKET.json](session/RECOVERY_PACKET.json) | حزمة استرجاع السياق الحتمية بعد أي انقطاع أو `Context Compaction`. | تُولّد آلياً عبر `recover_context.py --write`. |
| [memory/FUNCTION_REGISTRY.md](FUNCTION_REGISTRY.md) | السجل المركزي لجميع الدوال والكلاسات والـ Methods والـ Arrow Functions وأرقام الأسطر. | يُولّد آلياً عبر `sync_code_mirrors.py --write`. |
| `memory/code_mirrors/*.md` | مرآة القراءة لكل ملف برمجي بأرقام الأسطر والمقتطفات وعلاقات الملف (الكود الأصلي هو المرجع التنفيذي). | تُولّد آلياً عبر `sync_code_mirrors.py --write`. |
| [memory/decisions/DECISION_LOG.md](decisions/DECISION_LOG.md) | سجل القرارات بالحالات السبع (`OWNER_REQUIREMENT`, `PROPOSED`, `UNDER_RESEARCH`, `TECHNICALLY_REVIEWED`, `EXPERIMENTALLY_VALIDATED`, `OWNER_APPROVED`, `REJECTED`). | سجل إلحاقي (`Append-Only`). |

## Change chronology / Edit audit

- Source change: `START CHANGE` / `END CHANGE` comments with UTC time, ID, and CREATED/EDITED.
- Mutable documentation: `DOC_PROVENANCE` metadata + `memory/DOCUMENT_PROVENANCE.json` events.
- Complete protocol: `docs/governance/CODE_AND_DOCUMENT_CHANGE_PROVENANCE.md`.
- Validate with `python tools/governance/change_tracking.py verify`; historical unknown timestamps must not be fabricated.
