---
trigger: always_on
description: "Write-Ahead Logging (WAL) and Anti-Compaction memory persistence protocol to prevent context loss during long sessions or automatic context compaction."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:32Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# بروتوكول الحماية من فقدان السياق أثناء الـ Compaction (`Anti-Compaction & Write-Ahead Memory Rules`)

**الحالة:** إلزامي دائماً (`ALWAYS_ON`).

## 1. تشخيص المشكلة التي يعالجها هذا البروتوكول

في جلسات البرمجة الطويلة (Vibe Coding)، يقوم النظام تلقائياً بعمل **Context Compaction** (في Antigravity يحدث تلقائياً عند حوالي `~135,000 tokens`، كما أن جودة تركيز الموديل تبدأ في التراجع عند امتلاء نافذة السياق بأكثر من 40%).
- الخطأ القاتل الذي يقع فيه الـ AI عادةً: يقرأ عشرات الملفات ويجمع ملاحظات وتفاصيل دقيقة في "ذاكرة المحادثة المؤقتة"، ويؤجل كتابة التوثيق أو الملخص إلى نهاية المهمة؛ وعندما يحدث Compaction في المنتصف، تتلخص الرسائل القديمة وتضيع التفاصيل الدقيقة (أسماء المتغيرات، أرقام الأسطر، الحالات الحدية، أسباب فشل تجربة معينة).

## 2. قاعدة التسجيل المسبق الفوري (`Write-Ahead Logging — WAL Rule`)

**يُحظر تماماً الاحتفاظ بأي اكتشاف أو قرار في ذاكرة الشات لأكثر من خطوة واحدة (Single-Turn Persistence Limit):**

1. **التسجيل أثناء العمل وليس في النهاية (`Log As You Go, Never At The End`):**
   - بمجرد أن تقرأ ملفاً، أو تكتشف سبباً لخطأ برمجي، أو تتخذ قراراً بتصميم معادلة هندسية، أو تنهي خطوة فرعية، **يجب في نفس الخطوة (Same Turn)** تسجيل هذه التفصيلة في ملف:
     `memory/session/ACTIVE_SESSION_WAL.md`
2. **ماذا يُكتب في `ACTIVE_SESSION_WAL.md`؟**
   - طابع زمني / رقم الخطوة (`Step ID`).
   - ما الذي تم فحصه أو تنفيذه بالضبط (مع مسارات الملفات وأرقام الأسطر `Lines X–Y`).
   - الحقائق الدقيقة المكتشفة (أرقام، معادلات، سلوك دالة، مدخلات ومخرجات).
   - ما الذي نجح وما الذي فشل ولماذا (لمنع إعادة تجربة حل فاشل بعد الـ Compaction).
3. **تحديث نقطة التوقف الحية (`memory/session/CURRENT_TASK_CHECKPOINT.md`):**
   - يجب أن يعكس ملف `CURRENT_TASK_CHECKPOINT.md` دائماً:
     - **هدف المحادثة الحالية من بدايتها (`Original Session Goal`).**
     - **ما تم إنجازه بالكامل حتى هذه اللحظة (`Completed Units`).**
     - **الخطوة الجارية حالياً (`Active Unit in Progress`).**
     - **الخطوات المتبقية بالترتيب (`Remaining Queue`).**
     - **أي أسئلة أو قرارات معلقة تنتظر المستخدم (`Pending User Decisions`).**

## 3. بروتوكول الاستفاقة بعد الـ Compaction أو بداية جلسة جديدة (`Post-Compaction Recovery Routine`)

عند حدوث أي Context Compaction، أو عند فتح شات جديد، أو عند استلام المهمة من قِبل Agent آخر:
1. **توقف عن التخمين:** لا تحاول استنتاج التفاصيل المفقودة من ملخص الـ Compaction المختصر.
2. **اقرأ ثلاثية الذاكرة الحية فوراً:**
   - `memory/session/CURRENT_TASK_CHECKPOINT.md`
   - `memory/session/ACTIVE_SESSION_WAL.md`
   - `memory/code_mirrors/` الخاصة بالملفات المرتبطة بالمهمة الحالية.
3. **استأنف من آخر خطوة موثقة:** أكمل العمل من حيث توقف سجل الـ WAL بدون إعادة قراءة عشوائية للمشروع وبدون نسيان أي تفصيلة تم اكتشافها في أول المحادثة.

## 4. منع تضخم ملفات القواعد الأساسية (`Context Budget Discipline`)

تفرض بيئة Google Antigravity حداً أقصى قدره **24 كيلوبايت (`24,000 bytes`)** لكل ملف قاعدة، وميزانية قدرها **20,000 توكن** لمجموع قواعد `always_on`.
- لذلك: **لا تحول `AGENTS.md` أو `GEMINI.md` إلى سجل تاريخي متراكم** (لتجنب التباس التاريخ بالوضع الحالي واستهلاك السياق بلا داعٍ).
- تبقى القواعد الدائمة في `.agent_rules/` و`.agents/rules/` رشيقة وثابتة، بينما تُكتب جميع السجلات المتغيرة، وحالات الجلسات، ومرايا الكود داخل مجلد `memory/` المخصص لذلك.

## Change timestamps & document provenance (mandatory)

Apply `docs/governance/CODE_AND_DOCUMENT_CHANGE_PROVENANCE.md` on every first-party source write and human-authored Markdown edit. Source code: use matched `START CHANGE` and `END CHANGE` comments with real UTC timestamp, change ID, CREATED/EDITED, and agent ID at the smallest logical change block. Markdown: update `DOC_PROVENANCE` and `memory/DOCUMENT_PROVENANCE.json` in the same task; historical unknown creation times must stay unknown. Verify with `python tools/governance/change_tracking.py verify`. Do not edit immutable owner vision, historical snapshots, generated mirrors, or JSON with invalid comments. Update code mirrors, project catalog, and findings revision ledger when applicable.
