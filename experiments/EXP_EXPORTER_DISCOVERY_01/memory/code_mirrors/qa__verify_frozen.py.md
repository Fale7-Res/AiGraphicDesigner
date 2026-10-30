# مرآة الكود التفصيلية: `qa/verify_frozen.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/verify_frozen.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/verify_frozen.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `25` (`Lines 1–25`)
- **بصمة الملف (`SHA-256`):** `978556f9eb84e24b1fe1bf06a364b5b91815d1b78395db511b6da909d34ed618`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `visit` | `function` | `Lines 11–17` | `def visit(obj):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `visit` — `Lines 11–17`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `17` (`Lines 11–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–17`):**
```python
def visit(obj):
    if isinstance(obj,dict):
        if 'path' in obj and 'sha256' in obj:checks.append({'path':obj['path'],'expected':obj['sha256'],'actual':digest(obj['path'])})
        else:
            for value in obj.values():visit(value)
    elif isinstance(obj,list):
        for value in obj:visit(value)
```
