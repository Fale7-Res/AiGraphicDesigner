---
trigger: always_on
description: "Multi-agent and Sub-agent orchestration protocol: mandates decomposing tasks across specialized sub-agents with disjoint file locks and requiring an independent Reviewer Sub-Agent audit before completion."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "TASK-COLLAB-ENG-01", "last_edited_at_utc": "2026-10-17T09:38:32Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# بروتوكول تنسيق الـ Sub-Agents والمراجعة المستقلة الإلزامية (`Sub-Agent Orchestration & Independent Review Rules`)

**الحالة:** إلزامي دائماً (`ALWAYS_ON`).

## 1. لماذا نقسم المهام على Sub-Agents بدل تنفيذ كل شيء في الـ Main Thread؟

عندما يقوم Agent واحد في محادثة واحدة بكتابة الكود، وتجربته، ومراجعته، وتحديث الذاكرة لمهمة كبيرة:
1. يمتلئ الـ Context Window سريعاً وتحدث عمليات Compaction متكررة تفقد التفاصيل.
2. يقع الـ Agent في انحياز التأكيد (`Confirmation Bias`) فلا يرى الأخطاء أو الدوال المكررة التي كتبها بنفسه.

## 2. هيكلية فريق الـ Sub-Agents في المشروع (`.agents/agents/`)

يتكون الفريق البرمجي في مشروع **AI Graphic Designer** من الأدوار التالية:

| اسم الـ Sub-Agent | ملف التعريف في `.agents/agents/` | الدور والمسؤولية | صلاحية التعديل |
| :--- | :--- | :--- | :--- |
| **Orchestrator / Planner** | `orchestrator-planner.md` | تحليل طلب المستخدم، قراءة `memory/`، تقسيم المهمة إلى وحدات عمل غير متداخلة، وتوزيعها على الـ Sub-Agents ثم دمج النتائج. | يحدث ملفات `memory/session/` و`MASTER_PLAN.md` فقط. |
| **Scene & Vision Specialist** | `scene-and-vision-agent.md` | بناء وتعديل موديولات تخطيط الـ Scene Graph، توليد الصور بالطبقات، وفصل العناصر بـ SAM 2 / Grounding DINO وحساب الـ Z-Order والـ Amodal Inpainting. | يكتب في نطاق ملفات الرؤية والتوليد المحددة له فقط. |
| **Vector & Typography Specialist** | `vector-and-typography-agent.md` | بناء وتعديل محرك الـ Clean SVG، التبسيط اللوني، تجميع `<g>` (العنصر + الظل)، منع تفتيت الفلافل/البطاطس، ومحرك الخطوط (`Smart Typography`). | يكتب في نطاق ملفات الـ Vector والـ Typography فقط. |
| **Full-Stack & Canvas Specialist** | `fullstack-canvas-agent.md` | بناء وتعديل الـ FastAPI Backend، عقود الـ API، وواجهة الـ React/TypeScript Interactive Vector Canvas. | يكتب في نطاق الـ API والـ UI المحدد له فقط. |
| **Performance & Resource Optimization Specialist** | `performance-optimization-specialist.md` | قياس استهلاك المعالج والذاكرة (CPU/RAM/VRAM)، تدقيق التعقيد الخوارزمي، ومنع الاختناق الحراري على لابتوب المالك دون التضحية بالدقة البصرية. | يكتب في نطاق أدوات القياس وسجلات التيليميتري وملفات الأداء المحددة له. |
| **Independent QA Reviewer & Auditor** | `qa-reviewer-auditor.md` | **مراجع مستقل إلزامي (Read-Only + Audit Report):** يفتش وراء الـ Sub-Agents المنفذين، يفحص الكود بالكامل، يتأكد من عدم وجود دوال مكررة، ويطابق أرقام الأسطر في `memory/code_mirrors/` و`FUNCTION_REGISTRY.md`. | قراءة وفحص وتشغيل أدوات التحقق فقط (`No Direct Feature Edits`). |

## 3. قواعد منع اللخبطة والتعارض بين الـ Sub-Agents (`Zero-Conflict Concurrency Rules`)

1. **ملكية الملفات الحصرية في الجولة الواحدة (`Disjoint File Ownership Lock`):**
   - **يُحظر تماماً** تشغيل اثنين من الـ Sub-Agents في نفس الوقت لتعديل نفس الملف البرمجي أو نفس ملف المرآة.
   - يجب أن يحدد الـ Orchestrator لكل Sub-Agent قائمة صريحة بالملفات المسموح له بكتابتها (`Allowed Write Scope`) والملفات المسموح له بقراءتها فقط (`Read-Only Scope`).
2. **تمرير السياق الصريح عند الاستدعاء (`Explicit Context Handoff Packet`):**
   - بما أن الـ Sub-Agent في Antigravity يبدأ بنافذة سياق معزولة (`Clean Slate`)، يجب أن يتضمن أمر استدعائه (`invoke_subagent`) دائماً:
     - الهدف الدقيق للمهمة الفرعية ومعايير قبولها.
     - قائمة الملفات التي يجب عليه قراءتها بالكامل (`Full-File Read`).
     - قائمة الدوال الموجودة مسبقاً في `memory/FUNCTION_REGISTRY.md` التي يجب عليه استخدامها وعدم إعادة اختراعها.
     - إلزامه بتشغيل `python tools/memory_guard/sync_code_mirrors.py --write` وتحديث ملفات المرآة الخاصة بالملفات التي عدّلها قبل أن ينهي عمله.

## 4. بوابة المراجع المستقل الإلزامية (`Mandatory Reviewer Sub-Agent Gate`)

**لا يجوز إعلان انتهاء أي مهمة برمجية للمستخدم قبل مرورها بالدورة الرباعية التالية:**
1. **التقسيم (`Plan & Lock`):** يقسم الـ Orchestrator المهمة ويسجلها في `memory/session/CURRENT_TASK_CHECKPOINT.md`.
2. **التنفيذ وتحديث المرآة (`Execute & Mirror`):** ينفذ الـ Sub-Agent المختص الكود، ويقرأ الملفات كاملة، ويحدث `memory/code_mirrors/` و`memory/FUNCTION_REGISTRY.md` بأرقام الأسطر الدقيقة والمقتطفات وعلاقات الملفات.
3. **المراجعة المستقلة (`Independent Sub-Agent Audit`):** يستدعي الـ Orchestrator الـ Sub-Agent المراجع (`qa-reviewer-auditor`) ليقوم بـ:
   - قراءة الكود المعدل بالكامل ومقارنته مع ملف المرآة في `memory/code_mirrors/`.
   - التأكد من صحة أرقام الأسطر (`Lines Start–End`) ووجود الكود الفعلي وتوثيق العلاقات (`بياخد منين وبيرمي فين`).
   - التأكد من عدم وجود أي دالة مكررة في `memory/FUNCTION_REGISTRY.md`.
   - تشغيل الاختبارات وأداة `verify_brain_sync.py` وأداة `verify_catalog.py`.
4. **الإصلاح والاعتماد (`Fix & Sign-Off`):** إذا اكتشف المراجع أي خطأ أو نقص في الذاكرة أو الكود، يعيده للـ Sub-Agent المنفذ لإصلاحه، ولا تُسلم المهمة للمستخدم إلا بعد حصولها على `AUDIT_PASSED` من المراجع المستقل.


## 5. عزل الـ WAL والمكتشفات لكل Sub-Agent (`Isolated Subagent WALs & Findings Integration`)

- يلتزم كل Sub-Agent بقاعدة [.agent_rules/subagent_findings_and_promotion_rules.md](subagent_findings_and_promotion_rules.md):
  1. يكتب كل Sub-Agent ملاحظاته الفورية في ملف WAL معزول خاص به (`memory/session/subagent_wals/<subagent_id>__<task_id>.wal.md`) ولا يعدل `ACTIVE_SESSION_WAL.md` المشترك أثناء العمل المتوازي.
  2. يسجل كل Sub-Agent مكتشفاته في ملفات مستقلة تحت `memory/findings/entries/<task_id>__<subagent_id>__<finding_id>.json` شاملة المسار، نطاق الأسطر، بصمة `SHA-256`، الدليل، درجة الثقة، والإجراء المقترح.
  3. يراجع الـ Parent Agent (`orchestrator-planner`) هذه المكتشفات بشكل مستقل ويضيف قرار المراجعة الإلحاقي (`Append-Only Review Event`) ويرقي المكتشفات المعتمدة إلى الوثائق الرسمية بدون حذف سجلات المكتشفات الأصلية.

## 6. بروتوكول التواصل الحقيقي والمناظرة الهندسية (`Real Communication & Debate Protocol`)

1. **إلزامية تبادل الرسائل الفعلي (`Verifiable Inter-Agent Messaging`):**
   - يُحظر تماماً فبركة مناظرات وهمية يصيغها الـ Parent Agent منفرداً.
   - يتم التواصل بين الوكلاء باستخدام أداة `send_message` بمعرفات المحادثة (`conversationId`) الحقيقية، أو عبر وساطة الـ Parent Agent الشفافة (`Parent-Mediated Relay`) مع توثيق معرفات الوكلاء ونصوص الرسائل ومراجع الـ Transcript.
2. **شروط المناظرة الهندسية الصالحة (`Valid Debate Standard`):**
   - كل قرار جوهري يجب أن يمر بجولة اعتراض ورد حقيقية:
     - مقترح أولي مستقل مدعوم بالحسابات.
     - اعتراض صريح ومفصل من تخصص مقابل يوضح المخاطر.
     - رد وتفنيد أو تسوية هندسية مدعومة بالأدلة.
     - توصية نهائية وحفظ الخلافات العالقة في `ARCHITECTURE_DEBATE_AND_CONFLICTS.md`.
3. **دورة المهام الهندسية الكبرى (المراحل التسع A–I):**
   - الالتزام الصارم بالمراحل: `Stage A: Requirements` -> `Stage B: Independent Research` -> `Stage C: Engineering Debate` -> `Stage D: Decision Synthesis` -> `Stage E: Work Decomposition` -> `Stage F: Specialized Implementation` -> `Stage G: Independent Review` -> `Stage H: Repair & Reverify` -> `Stage I: Evidence-Based Completion` (انظر التفاصيل في [`docs/governance/MULTI_AGENT_COLLABORATION_AND_VERSION_STRATEGY.md`](../docs/governance/MULTI_AGENT_COLLABORATION_AND_VERSION_STRATEGY.md)).

