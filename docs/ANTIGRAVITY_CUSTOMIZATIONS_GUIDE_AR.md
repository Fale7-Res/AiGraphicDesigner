<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# الدليل الشامل لقسم Customizations في Google Antigravity (`ANTIGRAVITY_CUSTOMIZATIONS_GUIDE_AR.md`)

هذا الدليل يجيب بالتفصيل الدقيق عن سؤالك حول ما يوجد داخل قائمة **`Customizations`** في بيئة **Google Antigravity**، وماذا يجب أن تحمّل وتفعّل منها (خصوصاً `Gemini API` و`Google Antigravity SDK`) لخدمة مشروع **AI Graphic Designer**.

## 1. ماذا يوجد داخل قائمة `Customizations` في Antigravity؟

تتكون قائمة `Customizations` (التي تفتحها من قائمة `…` أو `⚙️ Settings -> Customizations` في Antigravity) من 6 أقسام رئيسية:

| القسم داخل `Customizations` | وظيفته الحقيقية في Antigravity | كيف جهزناه لك داخل هذا الـ ZIP؟ |
| :--- | :--- | :--- |
| **1. Build with Google / Plugins (Marketplace)** | متجر الإضافات الرسمية المدمجة في Antigravity (مثل إضافة **Gemini API / `gemini-skills`**). تمنح الـ Agent أحدث معرفة رسمية بكيفية كتابة كود Gemini API وموديلات الصور (`Nano Banana`) والـ Antigravity SDK بدون هلوسة بـ APIs قديمة. | **نعم، حمّلها وفعّلها فوراً!** (التفاصيل بالأسفل). |
| **2. Rules (`Workspace & Global Rules`)** | القواعد الدائمة التي يقرأها Antigravity تلقائياً من `AGENTS.md` و`GEMINI.md` ومجلد `.agents/rules/*.md`. تفرض عليه قراءة الملفات كاملة وتحديث الذاكرة. | مجهزة بالكامل في `.agents/rules/` و`.agent_rules/` بـ YAML Frontmatter متوافق 100%. |
| **3. Custom Subagents (`Agents`)** | تعريفات الـ Sub-Agents المتخصصين الذين يعملون بالتوازي وبسياق معزول (`Orchestrator`, `Vision`, `Vector`, `Fullstack`, `QA Reviewer`). | مجهزة بالكامل في `.agents/agents/*.md` وتظهر تلقائياً عند كتابة `/agents`. |
| **4. Agent Skills (`Skills`)** | حزم مهارات إجرائية (`SKILL.md`) يستدعيها الـ Agent تلقائياً أو عبر أمر `/` لتنفيذ خطوات معقدة مثل مزامنة مرآة الكود وأرقام الأسطر. | مجهزة في `.agents/skills/` (`sync-brain-and-mirrors` و`subagent-review-cycle`). |
| **5. Lifecycle Hooks (`Hooks`)** | سكربتات تعمل تلقائياً عند بداية الجلسة (`SessionStart`) أو قبل توقف الـ Agent (`Stop`) لإجباره على فحص تزامن الذاكرة قبل التوقف. | مجهزة في `.agents/hooks.json` ومربوطة بسكربتات الفحص في `tools/memory_guard/`. |
| **6. MCP Servers (`MCP`)** | ربط قواعد بيانات أو أدوات خارجية عبر Model Context Protocol. | اختيارية؛ لا تحتاج لتحميل MCP خارجي حالياً لأن أدوات الفحص المحلية مدمجة في `tools/`. |

## 2. هل يجب تحميل `Gemini API` و`Google Antigravity SDK`؟ ولماذا؟

**الإجابة القاطعة: نعم، كلاهما مفيد جداً لمشروعك تحديداً، وإليك السبب الهندسي الدقيق لكل واحد منهما:**

### أولاً: إضافة `Gemini API` (الموجودة تحت `Customizations -> Build with Google Plugins`)
- **ما هي؟** هي حزمة المهارات الرسمية من جوجل (`google-gemini/gemini-skills` وتحديداً مهارة `gemini-api-dev`).
- **لماذا كانت الـ Agents تهلوس بدونها؟** موديلات الذكاء الاصطناعي قد تستخدم مكتبات قديمة ملغاة (مثل `google-generativeai` القديمة بدلاً من حزمة `google-genai` الحديثة أو `Interactions API`). وفقاً لاختبارات جوجل الرسمية، تفعيل هذه الإضافة يرفع دقة كتابة كود الـ API إلى **96%**.
- **كيف تفيد مشروع AI Graphic Designer تحديداً؟**
  1. تحتوي على الكود الصحيح والحديث لتشغيل موديلات توليد الصور وتعديلها (بما فيها **`Nano Banana`** الذي ذكرته في فكرتك!).
  2. تحتوي على الكود الصحيح للـ **Structured Outputs (`Pydantic JSON Schemas`)** الذي سنستخدمه لإخراج مخطط الـ `Scene Graph` والأبعاد والـ `Z-Order` بدقة.
- **كيف تفعلها؟**
  - من واجهة Antigravity: افتح `Settings (⚙️) -> Customizations -> Build with Google Plugins` واضغط تحميل/تفعيل لـ **Gemini API**.
  - أو من الـ Terminal داخل Antigravity CLI:
    `agy plugin install https://github.com/google-gemini/gemini-skills`

### ثانياً: حزمة `Google Antigravity SDK` (`pip install google-antigravity`)
- **ما هي؟** هي الـ SDK البرمجية بلغة Python (`from google.antigravity import Agent, LocalAgentConfig`) لبناء وتشغيل أنظمة Multi-Agent مبرمجة داخل تطبيقك نفسه.
- **كيف تفيد مشروع AI Graphic Designer؟**
  - في مشروعك، أنت لا تستخدم Antigravity فقط كـ IDE تكتب به الكود، بل **منتجك نفسه (AI Graphic Designer)** يحتاج بداخل الـ Backend الخاص به إلى تشغيل Sub-Agents (واحد يخطط الـ Layers، وواحد يرسم الـ SVG، وواحد يعمل فحص الـ 50% Opacity).
  - الـ `Google Antigravity SDK` و`Gemini API Interactions` يوفران لك داخل كود الـ Python الخاص بمشروعك نظام Subagents جاهز، وStructured Output، وHooks بدون أن تبني محرك الـ Agent Loop من الصفر.
