---
trigger: always_on
description: "Google Antigravity IDE/App/CLI specific operating rules: strictly prohibits partial snippet reads before editing files, enforces full-file reads, and governs Antigravity tools, hooks, and plugins."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد التشغيل داخل بيئة Google Antigravity وحظر القراءة الجزئية (`Antigravity Full-File Read & IDE Rules`)

**الحالة:** إلزامي دائماً (`ALWAYS_ON`).

## 1. حظر القراءة الجزئية للملفات (`Strict Prohibition of Partial File Reads`)

من أخطر المشاكل التي تحدث في **Google Antigravity** أن يقوم الـ Agent باستدعاء أداة `view_file` مع تحديد نطاق ضيق جداً (`StartLine` و`EndLine` لبضعة أسطر فقط) أو يكتفي بنتائج `grep_search`، ثم يبني افتراضات خاطئة حول باقي محتوى الملف، مما يؤدي إلى:
- تكرار دالة موجودة بالفعل في نفس الملف في أسطر لم يقرأها.
- كسر الـ Imports أو المتغيرات المشتركة في أعلى أو أسفل الملف.
- كتابة كود يتعارض مع المنطق الموجود في النصف الآخر من الملف.

### القاعدة الإلزامية (`The Full-File Read Mandate`):
1. **قراءة الملف بالكامل قبل أي تعديل أو بناء عليه:**
   - عندما تقرر تعديل أي ملف برمجي أو الاعتماد على منطقه الداخلي، **يجب قراءة الملف كاملاً من السطر `1` إلى آخر سطر في الملف**.
   - إذا كان الملف أقل من `800` سطر: استدعِ `view_file(AbsolutePath=...)` **بدون** تمرير `StartLine` أو `EndLine` (أو من `1` إلى `800`) لقراءة الملف كاملاً دفعة واحدة.
   - إذا كان الملف أكبر من `800` سطر: اقرأه في شرائح متتابعة كاملة (`1–800`، ثم `801–1600`، وهكذا) حتى تصل إلى نهاية الملف الفعلي قبل إجراء أي تعديل.
2. **مراجعة المرآة وسجل الدوال جنباً إلى جنب مع القراءة الكاملة:**
   - قبل التعديل، اقرأ ملف المرآة المقابل في `memory/code_mirrors/` لتعرف فوراً جميع الملفات الأخرى التي تتأثر بهذا الملف (`Upstream Callers` و`Downstream Callees`)، واقرأ الملفات المتأثرة بالكامل إذا كان التعديل يغير توقيع دالة أو عقد بيانات (`Contract / DTO`).
3. **حظر إنشاء ملفات ضخمة غير قابلة للقراءة الكاملة (`File Size Ceiling`):**
   - قسّم الكود البرمجي إلى ملفات معيارية واضحة بحيث لا يتجاوز أي ملف برمجي مفرد `400–600` سطر إلا للضرورة القصوى، ليبقى كل ملف قابلاً للقراءة الكاملة في استدعاء `view_file` واحد داخل Antigravity!

## 2. التوافق مع خصائص Antigravity (`Rules, Skills, Subagents, Hooks`)

1. **YAML Frontmatter إلزامي في `.agents/rules/*.md`:**
   - تتجاهل بيئة Antigravity أي ملف داخل `.agents/rules/` إذا لم يبدأ بـ YAML frontmatter صالح يحتوي على `trigger: always_on | model_decision | glob | manual` و`description`. جميع ملفات القواعد في هذا المشروع مجهزة بـ Frontmatter متوافق 100%.
2. **استخدام الـ Custom Subagents عبر `invoke_subagent`:**
   - توجد تعريفات الـ Subagents الجاهزة في `.agents/agents/`. عند استدعاء أي Subagent، مرر له في الـ Prompt مسارات ملفات الذاكرة ذات الصلة (`memory/session/CURRENT_TASK_CHECKPOINT.md` وملفات المرآة المطلوبة) لأن كل Subagent يبدأ بنافذة سياق نظيفة ومعزولة (`Context Isolation`).
3. **احترام الـ Lifecycle Hooks (`.agents/hooks.json`):**
   - يحتوي المشروع على `.agents/hooks.json` الذي يشغل فحص تزامن الذاكرة (`verify_brain_sync.py`)؛ لا تحاول تعطيل الـ Hooks أو الالتفاف عليها.
