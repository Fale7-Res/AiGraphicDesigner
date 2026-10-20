---
trigger: always_on
description: "Independent persistent subagent findings system, isolated per-subagent WAL/finding files, append-only parent review events, and verified promotion into authoritative documentation."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:38Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# نظام المكتشفات المستقل للـ Sub-Agents والترقية الموثقة (`Subagent Findings & Verified Promotion Rules`)

**الحالة:** إلزامي دائماً (`ALWAYS_ON`).

## 1. الغرض وفلسفة العزل (`Why Independent Subagent Findings?`)

لمنع ضياع المكتشفات التفصيلية التي يتوصل إليها كل Sub-Agent، ولمنع تعارض الكتابة المتوازية (`Parallel Write Collisions`) عندما يعمل أكثر من Sub-Agent في نفس الوقت:
1. **عزل ملفات الـ WAL والمكتشفات لكل Sub-Agent ولكل مهمة:**
   - **يُحظر تماماً** على الـ Sub-Agents المتوازية التعديل المباشر في ملف مشترك واحد في نفس اللحظة.
   - يكتب كل Sub-Agent سجل خطواته الفوري في ملف معزول خاص به:
     `memory/session/subagent_wals/<subagent_id>__<task_id>.wal.md`
   - ويسجل كل اكتشاف مهم (`Finding`) فوراً في ملف JSON معزول خاص به:
     `memory/findings/entries/<task_id>__<subagent_id>__<finding_id>.json`
2. **قفل ملكية الملفات (`Subagent Ownership Locks`):**
   - قبل انطلاق أي Sub-Agent، يسجل الـ Parent Agent نطاق الملفات المسموح له بتعديلها في `memory/findings/subagent_ownership_locks.json`. يُمنع وجود قفلين نشطين (`ACTIVE`) لوكيلين مختلفين على نفس الملف في نفس الوقت.

## 2. الحقول الإلزامية لكل اكتشاف (`Mandatory Finding Schema`)

يجب أن يحتوي كل ملف اكتشاف في `memory/findings/entries/` على الحقول التالية (ويتم التحقق منها آلياً عبر `tools/findings_guard/manage_findings.py`):
- `finding_id`: معرف فريد (مثل `FND-20261017-001`).
- `task_id`: معرف المهمة (مثل `TASK-GOV-001`).
- `subagent_id`: اسم الـ Sub-Agent المكتشف (مثل `qa-reviewer-auditor`).
- `created_at`: طابع زمني بصيغة UTC ISO-8601.
- `source_file_paths`: قائمة غير فارغة بمسارات الملفات المصدرية التي استند إليها الاكتشاف.
- `line_ranges`: قائمة نطاقات الأسطر الدقيقة لكل ملف (`{"file": "...", "start_line": 1, "end_line": 25}`).
- `source_revisions`: قائمة بصمات `SHA-256` للملفات المصدرية وقت الفحص (`{"file": "...", "sha256": "..."}`).
- `evidence`: الدليل النصي أو المقتطف أو القياس الفعلي المستخرج من المصدر.
- `confidence`: درجة الثقة (`HIGH` | `MEDIUM` | `LOW`).
- `proposed_action`: الإجراء المقترح أو التعديل المطلوب ترقيته للوثائق المعتمدة.
- `current_approval_state`: حالة المراجعة الحالية (`PENDING_PARENT_REVIEW` | `APPROVED_FOR_PROMOTION` | `PROMOTED` | `REJECTED` | `NEEDS_REVISION`).
- `review_events`: مصفوفة إلحاقية فقط (`Append-Only Array`) لأحداث المراجعة من الـ Parent Agent.
- `promotion_record`: سجل الترقية إلى الوثائق المعتمدة (أو `null` قبل الترقية).

## 3. المراجعة المستقلة من الـ Parent Agent والترقية الإلزامية (`Parent Review & Promotion Lifecycle`)

1. **مراجعة الـ Parent Agent المستقلة (`Independent Parent Review`):**
   - يقوم الـ Parent Agent (`orchestrator-planner`) بمراجعة ملفات المكتشفات المعزولة، ويضيف حدث مراجعة إلحاقي (`Append-Only Review Event`) عبر:
     `python tools/findings_guard/manage_findings.py review --finding FND-... --reviewer orchestrator-planner --decision APPROVED_FOR_PROMOTION|REJECTED|NEEDS_REVISION`
   - **حظر الاعتماد الذاتي (`No Self-Approval`):** لا يجوز للـ Sub-Agent الذي أنشأ الاكتشاف أن يعتمد اكتشافه بنفسه (`reviewer_agent != subagent_id`).
   - **إلزامية سبب الرفض (`Explicit Rejection Reason`):** إذا كان القرار `REJECTED` أو `NEEDS_REVISION`، يجب تسجيل سبب صريح وغير فارغ في `rejection_reason`.
2. **الترقية الموثقة وعدم الحذف (`Verifiable Promotion & Non-Deletion Invariant`):**
   - كل اكتشاف يحصل على `APPROVED_FOR_PROMOTION` **يجب** ترقيته فعلياً إلى الوثيقة المعتمدة المستهدفة (`target_documents`) وتسجيل ترقيته عبر `manage_findings.py promote` قبل إغلاق المهمة.
   - إذا وُجد اكتشاف بحالة `APPROVED_FOR_PROMOTION` لم تتم ترقيته (`Unpromoted Approved Finding`)، فإن أداة `verify_brain_sync.py` ترفض إغلاق المهمة.
   - **يُحظر حذف أي ملف اكتشاف بعد ترقيته أو رفضه (`retained_after_promotion: true`)**؛ تبقى جميع المكتشفات وسجلات مراجعتها محفوظة كأثر تدقيقي دائم، ويُبنى السجل المجمع `memory/findings/FINDINGS_LEDGER.md` آلياً عبر `manage_findings.py compile-ledger`.
