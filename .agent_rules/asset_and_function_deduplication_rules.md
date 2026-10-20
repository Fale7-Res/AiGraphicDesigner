---
trigger: always_on
description: "Code symbol discovery, 3-level deduplication taxonomy (Exact-Name, Structural AST Similarity, Semantic Duplication), source file authority over mirrors, and visual asset SHA-256 deduplication."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "IMPORTED_LEGACY", "last_change_id": "BASELINE-IMPORT", "last_edited_at_utc": null, "last_editor": "governance-baseline", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد اكتشاف الرموز، وتصنيف التكرار الثلاثي، ومرجعية الكود الأصلي (`Code Discovery, Deduplication Taxonomy & Asset Reuse Rules`)

**الحالة:** إلزامي دائماً (`ALWAYS_ON`).

## 1. مرجعية الملفات البرمجية الأصلية (`Source Code Authority Invariant`)

1. **ملفات الكود المصدرية الكاملة (`Full Source Files`) هي المرجع التنفيذي الوحيد (`Sole Implementation Authority`):**
   - ملفات المرآة المولدة في `memory/code_mirrors/*.md` وسجل `memory/FUNCTION_REGISTRY.md` هي **واجهات ذاكرة وفهرسة للقراءة والتنقل** يتم توليدها آلياً من الكود الفعلي عبر `tools/memory_guard/sync_code_mirrors.py --write`.
   - **يُحظر تماماً** التعامل مع ملفات المرآة كنسخ كود مستقلة يتم تعديل الكود بداخلها يدوياً، أو السماح ببقائها قديمة (`Stale`) بعد تعديل الكود الأصلي.

## 2. الاستخراج الشامل للرموز البرمجية (`Comprehensive AST Symbol Discovery`)

تقوم أداة `tools/memory_guard/sync_code_mirrors.py` باستخراج وتوثيق جميع الرموز البرمجية في كل من **Python** و**TypeScript / JavaScript** مع نطاق الأسطر الدقيق (`Lines Start–End`) والمقتطف الفعلي، ويشمل ذلك:
- الدوال المستقلة المتزامنة وغير المتزامنة (`Top-level Functions & Async Functions`).
- الكلاسات وجميع دوالها الداخلية (`Classes & Class Methods: instance, classmethod, staticmethod, getters/setters`).
- الدوال والكلاسات المتداخلة (`Nested Functions & Nested Classes` مع اسم النطاق الأب المؤهل مثل `OuterFunc.inner_helper` أو `ClassName.method_name`).
- دوال الأسهم وتعبيرات الدوال في TS/JS (`Arrow Functions & Function Expressions: const fn = (...) => {...}`).
- التصريحات المصدّرة في TS/JS (`Exported Declarations: export function, export class, export const, export interface, export type`).

## 3. المستويات الثلاثة لتكرار الكود وحدود الأتمتة (`Three-Tier Deduplication Taxonomy`)

لمنع الادعاءات المبالغ فيها وضمان الدقة الهندسية، يميز نظام الحوكمة بصرامة بين ثلاثة أنواع من التكرار البرمجي:

| نوع التكرار (`Duplication Level`) | التعريف الدقيق | كيف يُكتشف في نظامنا؟ | هل الكشف آلي بالكامل؟ |
| :--- | :--- | :--- | :--- |
| **1. تكرار الاسم المطابق (`Exact-Name Duplication`)** | وجود دالتين أو كلاسين بنفس الاسم (`Symbol Name`) عبر ملفات المشروع (باستثناء نقاط الدخول القياسية الموثقة مثل `main` أو تطبيقات الـ Interface الموروثة). | فحص حتمي (`Deterministic AST Check`) في `sync_code_mirrors.py` و`verify_brain_sync.py`. | **نعم (100% آلي ويوقف البناء فوراً `Blocking Error`).** |
| **2. التشابه الهيكلي للـ AST (`Structural AST Similarity`)** | دالتان بأسماء مختلفة لكن لهما نفس البنية الهيكلية لشجرة الكود (`Normalized AST Skeleton`: نفس تسلسل الحلقات والشروط والاستدعاءات وعدد المعاملات بعد تجريد أسماء المتغيرات). | فحص بصمة الهيكل المجرد (`Normalized AST Structural Fingerprint`) في `sync_code_mirrors.py` يرصد الدوال ذات التشابه الهيكلي المرتفع (`>= 0.85`). | **آلي كمرشح تحذيري (`Automated Heuristic Candidate`)** يوجب مراجعة الـ Agent أو المراجع المستقل. |
| **3. التكرار الدلالي الوظيفي (`Semantic Duplication`)** | دالتان مكتوبتان بخوارزميتين أو هيكليتين مختلفتين تماماً لكنهما تؤديان نفس الغرض في المجال (مثل دالة تحسب تقاطع مضلعين هندسياً ودالة أخرى تحسب تقاطع قناعين بالـ NumPy لنفس الغرض). | **لا يُدّعى أنه آلي بالكامل.** يُمنع عبر: (1) البحث الإلزامي في أوصاف `memory/FUNCTION_REGISTRY.md` قبل كتابة أي دالة، و(2) تفتيش الـ Sub-Agent المراجع (`qa-reviewer-auditor`). | **لا (يتطلب مراجعة سجل الوظائف في `FUNCTION_REGISTRY.md` وتدقيق المراجع المستقل).** |

## 4. منع تكرار معالجة الأصول البصرية (`Visual Asset SHA-256 Deduplication`)

- كل صورة أصلية أو طبقة مولدة تُحفظ ببصمة `SHA-256`؛ ويُحظر إعادة تشغيل الـ Segmentation أو إعادة رسم الـ SVG للطبقات التي لم تتغير بصمتها أو معاملاتها أثناء تعديل طبقة أخرى.
