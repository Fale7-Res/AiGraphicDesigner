<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# خريطة علاقات الملفات وتدفق البيانات (`memory/FILE_RELATIONSHIPS_GRAPH.md`)

توضح هذه الوثيقة الحية علاقات الملفات ببعضها في المشروع (**كل ملف بياخد منين وبيرمي فين**، وما الذي يتأثر عند تعديله). يتم تحديث هذا الجدول في نفس المهمة عند إضافة أو تعديل أي ملف.

| الملف المصدر (`Source File`) | يأخذ البيانات/القواعد من (`Takes From / Upstream`) | يرمي البيانات/المخرجات إلى (`Throws To / Downstream`) | نوع العلاقة وتأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| `AGENTS.md` & `GEMINI.md` | تعليمات المستخدم المباشرة في الجلسة | `.agent_rules/*.md`, `.agents/rules/*.md`, `.agents/agents/*.md`, `memory/MEMORY_INDEX.md` | **دستور التوجيه الرئيسي:** أي تغيير في قواعد العمل الأساسية يجب أن ينعكس هنا وفي جداول التوجيه. |
| `MASTER_PLAN.md` | `docs/PRODUCT_VISION_AND_MODES.md`, `memory/decisions/DECISION_LOG.md` | `memory/session/CURRENT_TASK_CHECKPOINT.md`, جميع موديولات `M01–M08` | **خارطة الطريق:** تحدد حدود الموديولات الثمانية ومعايير القبول لكل موديول. |
| `tools/memory_guard/sync_code_mirrors.py` | جميع الملفات البرمجية في المستودع (`*.py`, `*.ts`, `*.tsx`) + `tools/memory_guard/mirror_metadata.json` | `memory/code_mirrors/*.md`, `memory/FUNCTION_REGISTRY.md` | **محرك مرآة الكود:** يستخرج الدوال وأرقام الأسطر (`Lines Start–End`) والمقتطفات؛ أي تعديل في كود المشروع يستوجب تشغيله فوراً. |
| `tools/memory_guard/verify_brain_sync.py` | جميع الملفات البرمجية + `memory/code_mirrors/*.md` + `memory/FUNCTION_REGISTRY.md` + `.agents/rules/*.md` | `tools/memory_guard/brain_validation.json`, `tools/memory_guard/stop_gate_hook.py` | **حارس الذاكرة ومنع التكرار:** يمنع إغلاق المهمة إذا كانت أرقام الأسطر غير محدثة أو وُجدت دالة مكررة. |
| `tools/memory_guard/session_start_hook.py` | `.agents/hooks.json` (`SessionStart` stdin payload) | رسالة تذكير النظام في بداية جلسة Antigravity (`stdout injectSteps`) | **منبه بداية الجلسة:** يذكّر الـ Agent بقراءة `MEMORY_INDEX.md` و`CURRENT_TASK_CHECKPOINT.md` والـ `WAL`. |
| `tools/memory_guard/stop_gate_hook.py` | `.agents/hooks.json` (`Stop` stdin payload) + `verify_brain_sync.py` | قرار السماح بالتوقف أو إجبار الـ Agent على المتابعة لتحديث الذاكرة (`stdout decision`) | **بوابة الإغلاق في Antigravity:** تمنع نسيان تحديث الذاكرة في نهاية الجلسة. |
| `tools/project_catalog/build_catalog.py` | شجرة ملفات المستودع الفعلية + `tools/project_catalog/catalog_descriptions.json` | `PROJECT_FILE_CATALOG.md`, `tools/project_catalog/file_metadata.json`, `tools/project_catalog/relationships.json` | **باني الفهرس العام:** يوثق كل ملف في المشروع وعلاقاته المتبادلة. |
| `tools/project_catalog/verify_catalog.py` | شجرة ملفات المستودع + `PROJECT_FILE_CATALOG.md` + `tools/project_catalog/relationships.json` | `tools/project_catalog/validation.json` | **مدقق الفهرس:** يضمن `0 uncataloged files` و`0 stale paths`. |
| `tools/review_updates/export_updates.py` | جميع ملفات المشروع المملوكة (`First-Party Files`) + `updates/baselines/state.json` | `updates/packages/UPDATE-NNNN.zip`, `updates/latest/AI_DESIGNER_LATEST.zip`, `updates/UPDATE_HISTORY.md` | **مصدّر حزم المراجعة:** ينشئ نسخاً تراكمية مفحوصة بالـ SHA-256 لمراجعة المالك. |
| `make_project_zip.py` | كامل ملفات المستودع | أرشيف `.zip` شامل للمشروع | **أداة ضغط سريعة:** تجمع كامل ملفات القواعد والذاكرة والأدوات في ملف مضغوط واحد. |
