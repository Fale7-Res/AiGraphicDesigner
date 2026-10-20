---
name: subagent-review-cycle
description: "Executes the mandatory Multi-Agent Builder -> Independent QA Reviewer Sub-Agent workflow to guarantee zero hallucinations, zero duplicate functions, and 100% accurate memory mirrors."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:42Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# Skill: Sub-Agent Execution & Independent Review Cycle (`subagent-review-cycle`)

عند تنفيذ أي مهمة برمجية أو معمارية:

## 1. مرحلة ما قبل التنفيذ (`Pre-Flight & WAL`)
1. اقرأ `memory/session/CURRENT_TASK_CHECKPOINT.md` و`memory/FUNCTION_REGISTRY.md`.
2. سجل بداية المهمة ونطاق الملفات المستهدفة في `memory/session/ACTIVE_SESSION_WAL.md`.
3. اقرأ جميع الملفات المستهدفة **قراءة كاملة (`Full-File Read`)** من السطر الأول للأخير.

## 2. مرحلة التنفيذ ومزامنة المرآة (`Implementation & Mirroring`)
1. نفّذ الكود المطلوب عبر الـ Sub-Agent المختص (`scene-and-vision-agent` أو `vector-and-typography-agent` أو `fullstack-canvas-agent`).
2. شغّل `python tools/memory_guard/sync_code_mirrors.py --write` وحدّث `PROJECT_FILE_CATALOG.md`.

## 3. مرحلة المراجعة المستقلة (`Independent Audit Gate`)
1. استدعِ الـ Sub-Agent `qa-reviewer-auditor` عبر أداة `invoke_subagent`.
2. إذا أرجع `AUDIT_RESULT: FAILED`، أصلح جميع الملاحظات وأعد تشغيل المراجعة حتى تحصل على `AUDIT_RESULT: PASSED`.
