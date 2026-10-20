# سجل القرارات المعمارية والتصميمية وحالات الاعتماد (`memory/decisions/DECISION_LOG.md`)

**حالة المشروع الحالية (`Current Project Gate`):**
- `PROJECT_STAGE`: `ARCHITECTURE_AND_GOVERNANCE_PREPARATION`
- `ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED` (`PROPOSED_ONLY`)
- `P0_IMPLEMENTATION_GATE`: `BLOCKED_PENDING_OWNER_APPROVAL_AND_FEASIBILITY_GATES`

## 1. دلالات حالات الاعتماد القياسية السبعة (`Canonical 7-State Approval Semantics`)

يُحظر خلط متطلبات المالك بالمقترحات التقنية للـ AI. يخضع كل سجل في هذا الملف لإحدى الحالات السبع التالية حصراً:
1. **`OWNER_REQUIREMENT`:** متطلب أصلي منصوص عليه صراحةً من المالك في `docs/product/OWNER_ORIGINAL_VISION.md` أو في توجيهاته المباشرة.
2. **`PROPOSED`:** حل تقني، أو تصميم معماري، أو اختيار مكتبة مقترح من الـ AI ولم يعمده المالك ولم يُثبت تجريبياً بعد.
3. **`UNDER_RESEARCH`:** قيد البحث أو بانتظار تنفيذ تجربة جدوى تقنية (`EXP-01..05`).
4. **`TECHNICALLY_REVIEWED`:** تمت مراجعته هندسياً أو التحقق منه باختبارات الحوكمة الآلية، لكنه ينتظر اعتماد المالك (`OWNER_APPROVED`) إذا كان قراراً معمارياً.
5. **`EXPERIMENTALLY_VALIDATED`:** أُثبتت جدواه بتجربة عملية قابلة للتكرار حققت معايير القبول الكمية (`IoU / SSIM / Node Count / Latency`).
6. **`OWNER_APPROVED`:** اعتمده المالك صراحةً بتفويض موثق (`Authorized Owner Event`).
7. **`REJECTED`:** مرفوض من المالك أو ثبت عدم جدواه تجريبياً (يبقى محفوظاً في السجل التاريخي مع سبب الرفض).

## 2. السجل النشط المعتمد بعد التدقيق (`Active Canonical Decision & Requirement Register — 2026-10-17`)

| رقم السجل (`ID`) | الموضوع (`Decision / Requirement Topic`) | متطلب المالك الأصلي (`Owner Requirement Status`) | الحل التقني المقترح (`Proposed Technical Approach`) | حالة الحل التقني (`Technical Status`) | حالة اعتماد المالك للمعمارية (`Owner Approval`) | التفويض / بوابة الجدوى المطلوبة (`Required Gate`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `ADR-001` | **تجميع العنصر مع الظل في `<g>` Group نظيف ومنع تشظي الـ SVG** | `OWNER_REQUIREMENT` (`OV-05`, `OV-12`) | تقليص لوني وظيفي + `Shapely Boolean Union` + `VTracer/DiffVG` داخل `<g id="Potato">`. | `UNDER_RESEARCH` | `NOT_APPROVED` (بانتظار نتائج `EXP-02` وموافقة المالك) | تنفيذ تجربة `EXP-02` على حالتي الفلافل والبطاطس (`A02`, `A03`). |
| `ADR-002` | **فصل العناصر المتقاربة لونياً (مثل البطاطس والعيش) في طبقات مستقلة** | `OWNER_REQUIREMENT` (`OV-07`) | استخراج `Semantic Instance Masks` (مرشح: `SAM 2 + Grounding DINO` أو `Florence-2`) قبل التحويل لـ Vector. | `UNDER_RESEARCH` | `NOT_APPROVED` (بانتظار نتائج `EXP-01` وموافقة المالك) | تنفيذ تجربة `EXP-01` على حالة ساندوتش البطاطس (`A03`). |
| `ADR-003` | **بوابة المطابقة البصرية الطبقيّة بشفافية `50% Opacity`** | `OWNER_REQUIREMENT` (`OV-09`) | تركيب الطبقة بشفافية 50% وحساب `IoU >= 0.92` و`SSIM` وخريطة فروق البكسلات قبل الانتقال للطبقة التالية. | `UNDER_RESEARCH` | `NOT_APPROVED` (بانتظار نتائج `EXP-04` وموافقة المالك) | تنفيذ تجربة `EXP-04` لقياس سرعة ودقة تقارب المنحنيات. |
| `ADR-004` | **تخيير المستخدم في النصوص (`Smart Typography`) وحفظ هوية الخط للتعديل** | `OWNER_REQUIREMENT` (`OV-10`, `OV-11`) | `OCR + Font Matcher` مع استخلاص `FontStyleDNA` وإعادة رسم الحروف المعدلة. | `UNDER_RESEARCH` | `NOT_APPROVED` (بانتظار نتائج `EXP-05` وموافقة المالك) | تنفيذ تجربة `EXP-05` على الشعارات النصية العربية والإنجليزية (`A04`). |
| `ADR-005` | **نظام مرآة الكود `1:1` بأرقام الأسطر والمقتطفات ومنع تكرار الدوال** | `OWNER_REQUIREMENT` (`OV-13`, `OV-14`) | أداة `sync_code_mirrors.py` (استخراج AST شامل لـ Python وTS/JS) + `verify_brain_sync.py`. | `TECHNICALLY_REVIEWED` | `OWNER_REQUIREMENT` (مفوض كقاعدة حوكمة) | اجتاز الاختبارات الإيجابية والسلبية في `test_governance_suite.py`. |
| `ADR-006` | **بروتوكول الكتابة المسبقة (`WAL`)، ونظام مكتشفات الـ Sub-Agents المستقل، وحظر القراءة الجزئية** | `OWNER_REQUIREMENT` (`OV-15`, `OV-16`, `OV-17`) | `ACTIVE_SESSION_WAL.md` + عزل `memory/findings/entries/` لكل Subagent + `manage_findings.py` + `recover_context.py`. | `TECHNICALLY_REVIEWED` | `OWNER_REQUIREMENT` (مفوض كقاعدة حوكمة) | اجتاز اختبارات التضارب والترقية والاسترجاع في `test_governance_suite.py`. |
| `ADR-007` | **المكدس التقني المقترح للتطبيق (`FastAPI + React/TS Canvas + Google GenAI`)** | `PROPOSED` (مقترح معماري لتنفيذ رؤية المالك) | مصفوفة البدائل في `docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md`. | `PROPOSED` | `NOT_APPROVED` (يتطلب موافقة صريحة من المالك) | مقارنة البدائل واعتماد المالك قبل بدء تنفيذ المنتج (`P0`). |

## 3. سجل أحداث التدقيق وتصحيح الحالات (`Append-Only Governance Audit Events`)

- **`[DEC-REV-20261017-01]` — 2026-10-17T08:19:06+03:00 — تصحيح دلالات الاعتماد وفصل متطلبات المالك عن المقترحات التقنية:**
  - **السبب:** النسخة الأولية من جدول القرارات استخدمت الكلمة العامة `APPROVED` لكل من متطلبات المالك الأصلية والحلول التقنية المقترحة من الـ AI بدون تمييز بين `OWNER_REQUIREMENT` و`PROPOSED` و`UNDER_RESEARCH`.
  - **الإجراء المتخذ:** تم الاحتفاظ بالجدول الأولي أدناه كمرجع تاريخي غير ممسوح (`Historical Baseline`)، وإضافة السجل النشط أعلاه بالدلالات السبع الصارمة، وتثبيت حالة المشروع في مرحلة `ARCHITECTURE_AND_GOVERNANCE_PREPARATION` (`NOT_APPROVED` لتنفيذ المنتج) لحين صدور موافقة المالك.

## 4. النسخة التاريخية المحفوظة للتدقيق (`Historical Baseline — Initial 2026-10-17 Table — Superseded by Section 2`)

> *محفوظة للأمانة التدقيقية (`Append-Only History`)؛ تم استبدال عمود الحالة العام `APPROVED` بالتفصيل الدقيق في القسم (2) أعلاه.*

| رقم القرار (`ID`) | التاريخ | القرار (كما سُجل مبدئياً) | الحالة المبدئية قبل التدقيق |
| :--- | :--- | :--- | :--- |
| `ADR-001` | 2026-10-17 | اعتماد التجميع الدلالي `<g>` (Base + Shadow + Highlight) بدلاً من التحويل اللوني المباشر للـ SVG | `APPROVED` *(Superseded: Requirement is `OWNER_REQUIREMENT`; algorithm is `UNDER_RESEARCH`)* |
| `ADR-002` | 2026-10-17 | العزل الدلالي المسبق بالـ Instance Masks قبل أي تحويل لـ Vector | `APPROVED` *(Superseded: Requirement is `OWNER_REQUIREMENT`; model choice is `UNDER_RESEARCH`)* |
| `ADR-003` | 2026-10-17 | بوابة التحقق البصري الطبقي (`50% Opacity Overlay + IoU/SSIM`) | `APPROVED` *(Superseded: 50% Opacity check is `OWNER_REQUIREMENT`; IoU/SSIM thresholds are `UNDER_RESEARCH`)* |
| `ADR-004` | 2026-10-17 | بوابة التخيير الذكي للنصوص (`Smart Typography Choice`) مع حفظ `Font Style DNA` | `APPROVED` *(Superseded: User prompt & style identity are `OWNER_REQUIREMENT`; implementation is `UNDER_RESEARCH`)* |
| `ADR-005` | 2026-10-17 | مرآة الكود 1:1 (`memory/code_mirrors/`) وسجل الدوال بأرقام الأسطر والمقتطفات | `APPROVED` *(Clarified: `OWNER_REQUIREMENT` & `TECHNICALLY_REVIEWED`)* |
| `ADR-006` | 2026-10-17 | بروتوكول الكتابة المسبقة (`Write-Ahead Log`) وحظر القراءة الجزئية في Antigravity | `APPROVED` *(Clarified: `OWNER_REQUIREMENT` & `TECHNICALLY_REVIEWED`)* |
| `ADR-007` | 2026-10-17 | تقسيم المهام على Sub-Agents مع مراجع مستقل إلزامي (`qa-reviewer-auditor`) | `APPROVED` *(Clarified: `OWNER_REQUIREMENT` & `TECHNICALLY_REVIEWED`)* |
