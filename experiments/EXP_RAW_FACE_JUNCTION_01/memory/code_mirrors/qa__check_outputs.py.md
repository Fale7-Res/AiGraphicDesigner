# مرآة الكود التفصيلية: `qa/check_outputs.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/check_outputs.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/check_outputs.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `37` (`Lines 1–37`)
- **بصمة الملف (`SHA-256`):** `00adc0781f4b24acd50ab42b0f817c9a61364a2352caacd18c3c81162b20762c`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `occurrence` | `function` | `Lines 12–12` | `def occurrence(g):return {f:collections.Counter((r['chain'],r['forward']) for w in rings for r in w) for f,rings in g['faces'].items()}` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `occurrence` — `Lines 12–12`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `12` (`Lines 12–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–12`):**
```python
def occurrence(g):return {f:collections.Counter((r['chain'],r['forward']) for w in rings for r in w) for f,rings in g['faces'].items()}
```
