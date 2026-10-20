# مرآة الكود التفصيلية: `tools/memory_guard/stop_gate_hook.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/stop_gate_hook.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/stop_gate_hook.py`
- **الدور المعماري (`Architectural Role`):** Antigravity Lifecycle Hook — Stop Gate Memory Verifier
- **إجمالي عدد الأسطر (`Total Lines`):** `34` (`Lines 1–34`)
- **بصمة الملف (`SHA-256`):** `50873ab418a67ebda8cdba2be720d81ddeb30f5f278ce365728090c8df6382b0`
- **الوصف التفصيلي:** سكربت يعمل تلقائياً عند حدث Stop في Google Antigravity ليشغل فحص تزامن الذاكرة (verify_brain_sync.py)؛ وإذا وجد أن الـ Agent عدّل كوداً دون تحديث أرقام الأسطر في المرآة أو ترك دالة مكررة، يمنعه من التوقف (decision: continue) ويطلب منه تحديث الذاكرة أولاً.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `.agents/hooks.json (Antigravity Stop Event via stdin) + verify_brain_sync.py` | حالة توقف الـ Agent ونتيجة فحص تزامن الذاكرة | يضمن عدم انتهاء أي جلسة بذاكرة غير متزامنة مع الكود. |
| **يرمي إلى (`Throws To`)** | `Antigravity Execution Loop (stdout JSON decision: allow/continue)` | قرار السماح بالتوقف أو إرجاع الـ Agent لتحديث مرآة الكود والـ WAL | يحمي المشروع آلياً من نسيان توثيق التعديلات. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `main` | `function` | `Lines 11–30` | `def main() -> None:` | تشغل فحص verify_brain_sync.py عند محاولة الـ Agent التوقف، وترجع decision='continue' إذا كان هناك خلل في تزامن الذاكرة. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `main` — `Lines 11–30`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `30` (`Lines 11–30`)
- **الوظيفة:** تشغل فحص verify_brain_sync.py عند محاولة الـ Agent التوقف، وترجع decision='continue' إذا كان هناك خلل في تزامن الذاكرة.
- **الكود الفعلي (`Lines 11–30`):**
```python
def main() -> None:
    """Run verify_brain_sync.py on Stop event; force agent to continue if out of sync."""
    _ = sys.stdin.read()
    proc = subprocess.run(
        [sys.executable, str(HERE / "verify_brain_sync.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print(json.dumps({
            "decision": "continue",
            "reason": (
                "External Brain Sync Check Failed! Run `python tools/memory_guard/sync_code_mirrors.py --write` "
                "and update memory/code_mirrors/ and memory/session/ACTIVE_SESSION_WAL.md before stopping. "
                f"Details: {proc.stdout.strip()}"
            ),
        }, ensure_ascii=False))
    else:
        print(json.dumps({"decision": "allow"}, ensure_ascii=False))
```
