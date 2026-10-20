# مرآة الكود التفصيلية: `tools/memory_guard/session_start_hook.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/session_start_hook.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/session_start_hook.py`
- **الدور المعماري (`Architectural Role`):** Antigravity Lifecycle Hook — SessionStart Memory Recall
- **إجمالي عدد الأسطر (`Total Lines`):** `28` (`Lines 1–28`)
- **بصمة الملف (`SHA-256`):** `c5a8df233d11714dbc2b49bdc5937f8f5e87b8b719be6cd8cc11caa5c98a2b0d`
- **الوصف التفصيلي:** سكربت يعمل تلقائياً عند حدث SessionStart في Google Antigravity ليحقن رسالة تذكير للـ Agent بقراءة الذاكرة الحية (MEMORY_INDEX.md وCURRENT_TASK_CHECKPOINT.md وACTIVE_SESSION_WAL.md) قبل أي خطوة.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `.agents/hooks.json (Antigravity SessionStart Event via stdin)` | بيانات الجلسة الحالية (conversationId, workspacePaths) | يعمل تلقائياً عند فتح أي محادثة جديدة في Antigravity. |
| **يرمي إلى (`Throws To`)** | `Antigravity Agent Trajectory (stdout JSON injectSteps)` | رسالة نظام توجيهية تلزم الـ Agent بقراءة الذاكرة الحية وقراءة الملفات كاملة | تمنع بدء الجلسة بدون استرجاع السياق. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `main` | `function` | `Lines 7–24` | `def main() -> None:` | تقرأ مدخلات حدث SessionStart من stdin وتطبع كائن JSON يحتوي على injectSteps لتوجيه الـ Agent نحو ملفات الذاكرة. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `main` — `Lines 7–24`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `24` (`Lines 7–24`)
- **الوظيفة:** تقرأ مدخلات حدث SessionStart من stdin وتطبع كائن JSON يحتوي على injectSteps لتوجيه الـ Agent نحو ملفات الذاكرة.
- **الكود الفعلي (`Lines 7–24`):**
```python
def main() -> None:
    """Read SessionStart payload from stdin and output systemMessage reminder on stdout."""
    _ = sys.stdin.read()
    response = {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": (
                        "MANDATORY STARTUP PROTOCOL: Read memory/MEMORY_INDEX.md, "
                        "memory/session/CURRENT_TASK_CHECKPOINT.md, and memory/session/ACTIVE_SESSION_WAL.md "
                        "before executing any task. Always read source files in full (Line 1 to end) "
                        "and check memory/FUNCTION_REGISTRY.md before writing functions."
                    )
                }
            }
        ]
    }
    print(json.dumps(response, ensure_ascii=False))
```
