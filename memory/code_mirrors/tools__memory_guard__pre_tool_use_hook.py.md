# مرآة الكود التفصيلية: `tools/memory_guard/pre_tool_use_hook.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/pre_tool_use_hook.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/pre_tool_use_hook.py`
- **الدور المعماري (`Architectural Role`):** Antigravity Lifecycle Hook — PreToolUse Owner Gate
- **إجمالي عدد الأسطر (`Total Lines`):** `35` (`Lines 1–35`)
- **بصمة الملف (`SHA-256`):** `69cc6c7b11e25f07531907e44470aae628822166eb99d2b2362e30d85b11eb38`
- **الوصف التفصيلي:** سكربت يعمل عند حدث PreToolUse في Google Antigravity لاعتراض أي محاولة من الـ Agent لتشغيل أوامر اعتماد المالك (manage_approvals.py authorize أو export_updates.py acknowledge) وإجبار النظام على طلب تأكيد المستخدم التفاعلي (decision: force_ask).

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `.agents/hooks.json (PreToolUse stdin payload)` | تفاصيل أمر run_command المقترح تنفيذه | يمنع الـ Agent من التوقيع نيابة عن المالك. |
| **يرمي إلى (`Throws To`)** | `Antigravity Permission Engine (stdout decision: force_ask / allow)` | قرار إجبار سؤال المستخدم أو السماح للأوامر العادية | يضيف طبقة حماية وقت التشغيل لمنع الاعتماد الذاتي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `main` | `function` | `Lines 7–31` | `def main() -> None:` | تفحص الأمر الممرر في PreToolUse وترجع decision='force_ask' إذا كان يستدعي بوابة اعتماد المالك. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `main` — `Lines 7–31`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `31` (`Lines 7–31`)
- **الوظيفة:** تفحص الأمر الممرر في PreToolUse وترجع decision='force_ask' إذا كان يستدعي بوابة اعتماد المالك.
- **الكود الفعلي (`Lines 7–31`):**
```python
def main() -> None:
    """Inspect run_command tool calls and require explicit user confirmation on owner-only gates."""
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        payload = {}
    tool_call = payload.get("toolCall", {})
    args = tool_call.get("args", {})
    cmd_line = str(args.get("CommandLine") or args.get("command") or "")

    if "manage_approvals.py" in cmd_line and "authorize" in cmd_line:
        print(json.dumps({
            "decision": "force_ask",
            "reason": "Owner-only governance gate: AI agents cannot self-approve architecture transitions without explicit interactive owner authorization.",
        }, ensure_ascii=False))
        return
    if "export_updates.py" in cmd_line and "acknowledge" in cmd_line:
        print(json.dumps({
            "decision": "force_ask",
            "reason": "Owner-only review gate: AI agents cannot self-acknowledge review packages.",
        }, ensure_ascii=False))
        return

    print(json.dumps({"decision": "allow"}, ensure_ascii=False))
```
