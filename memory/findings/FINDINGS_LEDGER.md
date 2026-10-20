# السجل الموحد لمكتشفات الـ Sub-Agents وحالة مراجعتها وترقيتها (`memory/findings/FINDINGS_LEDGER.md`)

> **ملاحظة آلية (`Auto-Generated Ledger`):** يُبنى هذا الملف آلياً عبر `python3 tools/findings_guard/manage_findings.py compile-ledger` من ملفات المكتشفات المعزولة في `memory/findings/entries/*.json`. لا تعدل هذا الملف يدوياً، ولا تحذف أي اكتشاف بعد ترقيته.

- **إجمالي المكتشفات المسجلة:** `3`

## جدول المكتشفات والترقية (`Subagent Findings & Promotion Table`)

| رقم الاكتشاف (`ID`) | المهمة (`Task`) | الـ Sub-Agent | المصادر والأسطر (`Source & Lines`) | درجة الثقة | الحالة (`State`) | المراجع (`Parent Reviewer`) | الوثائق المرقّى إليها (`Promoted Targets`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FND-20261017-001` | `TASK-GOV-HARDENING` | `qa-reviewer-auditor` | `docs/product/OWNER_ORIGINAL_VISION.md` (`L1–L12`), `memory/decisions/DECISION_LOG.md` (`L1–L35`) | `HIGH` | `PROMOTED` | `orchestrator-planner` | `memory/decisions/DECISION_LOG.md` |
| `FND-20261017-002` | `TASK-GOV-HARDENING` | `vector-and-typography-agent` | `docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md` (`L1–L68`), `docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md` (`L1–L29`) | `HIGH` | `PROMOTED` | `orchestrator-planner` | `docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md` |
| `FND-20261017-003` | `TASK-V01-CORRECTION-01` | `vector-and-typography-agent` | `versions/version-01/src/pipeline.py` (`L128–L130`) | `HIGH` | `PROMOTED` | `orchestrator-planner` | `versions/version-01/docs/ARCHITECTURE.md` |

## تفاصيل المكتشفات وسجل المراجعة الإلحاقي (`Detailed Findings & Append-Only Reviews`)

### `FND-20261017-001` — بواسطة `qa-reviewer-auditor` (المهمة: `TASK-GOV-HARDENING`)
- **ملف السجل المعزول:** `memory/findings/entries/TASK-GOV-HARDENING__qa-reviewer-auditor__FND-20261017-001.json`
- **تاريخ الإنشاء:** `2026-10-17T08:20:00Z`
- **الدليل (`Evidence`):** Initial decision table used generic APPROVED status for both owner product rules and AI-proposed technical implementations, and lacked a standalone verbatim owner vision file.
- **الإجراء المقترح (`Proposed Action`):** Preserve verbatim Arabic prompt in docs/product/OWNER_ORIGINAL_VISION.md and record append-only audit event DEC-REV-20261017-01 in memory/decisions/DECISION_LOG.md separating OWNER_REQUIREMENT from PROPOSED and UNDER_RESEARCH.
- **الحالة الحالية:** `PROMOTED`
- **سجل أحداث المراجعة الإلحاقي (`Append-Only Review Events`):**
  - `REV-20261017-001` (2026-10-17T08:21:00Z): المراجع `orchestrator-planner` -> القرار `APPROVED_FOR_PROMOTION` | السبب/الملاحظة: Verified against owner governance hardening requirements 1 and 3.
- **سجل الترقية (`Promotion Record`):** تمت الترقية بتاريخ `2026-10-17T08:22:00Z` إلى `['memory/decisions/DECISION_LOG.md']` (محفوظ بعد الترقية: `True`).

### `FND-20261017-002` — بواسطة `vector-and-typography-agent` (المهمة: `TASK-GOV-HARDENING`)
- **ملف السجل المعزول:** `memory/findings/entries/TASK-GOV-HARDENING__vector-and-typography-agent__FND-20261017-002.json`
- **تاريخ الإنشاء:** `2026-10-17T08:20:30Z`
- **الدليل (`Evidence`):** Semantic pixel separation under color similarity (Potato vs Bread) and non-fragmented Clean SVG <g> reconstruction (Falafel/Potato shadows) are high-risk capabilities that require empirical benchmarking before final stack commitment.
- **الإجراء المقترح (`Proposed Action`):** Establish mandatory feasibility experiments EXP-01 through EXP-05 with quantitative IoU/SSIM/Node-count pass criteria in docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md.
- **الحالة الحالية:** `PROMOTED`
- **سجل أحداث المراجعة الإلحاقي (`Append-Only Review Events`):**
  - `REV-20261017-002` (2026-10-17T08:21:30Z): المراجع `orchestrator-planner` -> القرار `APPROVED_FOR_PROMOTION` | السبب/الملاحظة: Verified against owner requirement 6 (Architecture and Feasibility Gates).
- **سجل الترقية (`Promotion Record`):** تمت الترقية بتاريخ `2026-10-17T08:22:30Z` إلى `['docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md']` (محفوظ بعد الترقية: `True`).

### `FND-20261017-003` — بواسطة `vector-and-typography-agent` (المهمة: `TASK-V01-CORRECTION-01`)
- **ملف السجل المعزول:** `memory/findings/entries/TASK-V01-CORRECTION-01__vector-and-typography-agent__FND-20261017-003.json`
- **تاريخ الإنشاء:** `2026-10-17T18:05:58.651518+00:00`
- **الدليل (`Evidence`):** cluster_areas.sort globally by pixel count violates local topological enclosure, inverting layer order in nested shapes and text.
- **الإجراء المقترح (`Proposed Action`):** Implement topological enclosure DAG and Kahn's topological sort for layer ordering, and silhouette-constrained dilation for seam trapping.
- **الحالة الحالية:** `PROMOTED`
- **سجل أحداث المراجعة الإلحاقي (`Append-Only Review Events`):**
  - `REV-FND-20261017-003-001` (2026-10-17T19:11:47.763082+00:00): المراجع `orchestrator-planner` -> القرار `APPROVED_FOR_PROMOTION` | السبب/الملاحظة: Approved: Topological enclosure and silhouette trapping are valid findings for Iteration 07 experiments
- **سجل الترقية (`Promotion Record`):** تمت الترقية بتاريخ `2026-10-17T19:18:14.926962+00:00` إلى `['versions/version-01/docs/ARCHITECTURE.md']` (محفوظ بعد الترقية: `True`).
