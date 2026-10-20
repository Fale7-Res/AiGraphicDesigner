<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T07:03:27Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# Google Antigravity Workspace Instructions (`GEMINI.md`)

هذا الملف يعمل بالتكامل المباشر مع `@AGENTS.md` لتوجيه بيئة **Google Antigravity** (App / IDE / CLI / SDK).

## القواعد الفورية النشطة دائماً في Antigravity (`Always-On Core Directives`)

1. **استدعاء الذاكرة الحية عند البداية (`Startup Brain Recall`):**
   - اقرأ `@memory/MEMORY_INDEX.md` و`@memory/session/CURRENT_TASK_CHECKPOINT.md` و`@memory/session/ACTIVE_SESSION_WAL.md` فور بدء الجلسة أو بعد أي Context Compaction (~135k tokens).
2. **القراءة الكاملة للملفات (`Full-File Read Enforcement`):**
   - عند استخدام أداة `view_file` على أي ملف كود ستقوم بتعديله أو البناء عليه، **يُحظر** قراءة مقتطف جزئي فقط وافتراض باقي الكود. اقرأ الملف بالكامل (من السطر `1` إلى نهاية الملف) وتحقق من مرآته في `@memory/code_mirrors/` وسجل الدوال في `@memory/FUNCTION_REGISTRY.md`.
3. **التسجيل الفوري (`Write-Ahead Memory`):**
   - سجل كل اكتشاف أو تعديل أو قرار فوراً في `@memory/session/ACTIVE_SESSION_WAL.md` قبل الانتقال للخطوة التالية.
4. **مزامنة أرقام الأسطر والكود والعلاقات (`Mirror & Line-Number Sync`):**
   - بعد أي عملية `write_to_file` أو `replace_file_content` أو `multi_replace_file_content` على ملف برمجي، شغّل أداة:
     `python tools/memory_guard/sync_code_mirrors.py --write`
     وحدث وصف الدوال وأرقام أسطرها (`Lines Start–End`) ومقتطف الكود وعلاقات الملف (`بياخد منين وبيرمي فين`)، ثم تحقق عبر:
     `python tools/memory_guard/sync_rules.py --write`
     `python tools/findings_guard/manage_findings.py compile-ledger`
     `python tools/memory_guard/verify_brain_sync.py`
5. **العمل عبر الـ Sub-Agents والمراجع المستقل (`Subagent Teamwork & Audit`):**
   - استخدم الـ Custom Subagents المعرّفة في `.agents/agents/` لتوزيع المهام، ولا تغلق أي مهمة برمجية قبل تمريرها على الـ Subagent المراجع `@.agents/agents/qa-reviewer-auditor.md`.

للتفاصيل الكاملة، اتبع دستور المشروع في `@AGENTS.md` والقواعد التفصيلية داخل `.agents/rules/` و`.agent_rules/`.

## Mandatory code/comment timestamps and Markdown provenance

Before any source-code addition or edit, read [Code & Document Change Provenance](docs/governance/CODE_AND_DOCUMENT_CHANGE_PROVENANCE.md). Record matched `START CHANGE` / `END CHANGE` language-valid comments around each coherent authored/edited code region with real UTC date+time, `CREATED`/`EDITED`, change ID and agent identity. For mutable human-authored Markdown, maintain `DOC_PROVENANCE` and the document change ledger; never invent legacy creation dates. Run `python tools/governance/change_tracking.py verify` before final delivery. No references to external/preceding projects are needed to operate this repository.
