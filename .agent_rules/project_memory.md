---
trigger: always_on
description: "Master persistent project memory rule routing agents to the structured memory/ bank, active checkpoints, and codebase mirrors."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# دستور الذاكرة الدائمة للمشروع (`Project Memory & Continuation Governance`)

**تاريخ التأسيس:** 17 أكتوبر 2026
**المشروع:** AI Graphic Designer (Image Generation + Magic Layers + Clean SVG + Smart Typography + Layer-Aware Editing)

## 1. هيكلة الذاكرة الخارجية الحية (`Tiered External Brain Architecture`)

بدلاً من تكديس آلاف الأسطر في ملف واحد يتعرض للـ Truncation، تنقسم ذاكرة المشروع إلى 5 طبقات منظمة داخل مجلد `memory/`:

1. **الفهرس العام للذاكرة (`memory/MEMORY_INDEX.md`):**
   - نقطة الدخول الأولى لأي مطور أو Agent جديد؛ يشرح المشروع، وما تم إنجازه، وما هو مخطط، وكيف تصل لأي معلومة في ثوانٍ.
2. **ذاكرة الجلسة الحية ومضاد الـ Compaction (`memory/session/`):**
   - `CURRENT_TASK_CHECKPOINT.md`: يسجل حالة المهمة الحالية من بداية المحادثة، الخطوات المنجزة، والخطوة المتبقية التالية.
   - `ACTIVE_SESSION_WAL.md`: سجل الكتابة المسبقة الفوري (Write-Ahead Log) الذي يمنع ضياع أي تفصيلة أثناء الـ Context Compaction.
3. **مرآة الكود التفصيلية بالسطر والمقتطف (`memory/code_mirrors/`):**
   - ملف Markdown لكل ملف برمجي في المشروع يوثق كل دالة، أرقام أسطرها (`Lines Start–End`)، الكود الفعلي، وعلاقات الملف (`بياخد منين وبيرمي فين`).
4. **السجل المركزي للدوال وخريطة العلاقات (`memory/FUNCTION_REGISTRY.md` & `memory/FILE_RELATIONSHIPS_GRAPH.md`):**
   - يمنع تكرار أي دالة في المشروع، ويوفر خريطة شاملة لتدفق البيانات بين الـ Backend والـ AI Pipeline والـ Vector Engine والـ Frontend Canvas.
5. **سجل القرارات المعمارية والتصميمية (`memory/decisions/DECISION_LOG.md`):**
   - يحفظ كل قرار تقني أو معماري تم اتخاذه مع سببه وتاريخه حتى لا يعيد Agent مستقبلي نقضه أو تغييره بالخطأ.

## 2. روتين استلام وتسليم المهام لأي Agent (`Agent Handoff Protocol`)

- **عند الدخول (`On Entry`):** اقرأ `memory/MEMORY_INDEX.md` ثم `memory/session/CURRENT_TASK_CHECKPOINT.md` و`memory/session/ACTIVE_SESSION_WAL.md`.
- **أثناء العمل (`During Execution`):** سجل كل خطوة واكتشاف فوراً في `ACTIVE_SESSION_WAL.md`، واقرأ أي ملف كود بالكامل قبل تعديله.
- **عند الإغلاق (`Before Stop`):** شغّل `sync_code_mirrors.py --write`، حدّث `CURRENT_TASK_CHECKPOINT.md`، مرّر التعديلات على `qa-reviewer-auditor`، ثم شغّل `verify_brain_sync.py` و`verify_catalog.py`.
