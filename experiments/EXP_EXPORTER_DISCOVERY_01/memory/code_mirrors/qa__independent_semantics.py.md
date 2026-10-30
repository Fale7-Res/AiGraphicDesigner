# مرآة الكود التفصيلية: `qa/independent_semantics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/independent_semantics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/independent_semantics.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `55` (`Lines 1–55`)
- **بصمة الملف (`SHA-256`):** `463394502b1517a9d863c46cf9d9e3e1d8a8945ad2a55df92518c2e18338d1cb`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `interpreted` | `function` | `Lines 13–24` | `def interpreted(text):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `interpreted` — `Lines 13–24`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `24` (`Lines 13–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–24`):**
```python
def interpreted(text):
    pen=RecordingPen();parse_path(text,pen)
    current=start=None;segments=[]
    for op,args in pen.value:
        if op=='moveTo':current=start=args[0]
        elif op=='lineTo':segments.append(('L',current,args[0]));current=args[0]
        elif op=='curveTo':segments.append(('C',current,*args));current=args[-1]
        elif op=='closePath':
            if current!=start:segments.append(('L',current,start))
            current=start
        elif op!='endPath':raise AssertionError(op)
    return segments
```
