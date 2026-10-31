# مرآة الكود التفصيلية: `qa/test_independent_pilot.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/test_independent_pilot.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/test_independent_pilot.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `29` (`Lines 1–29`)
- **بصمة الملف (`SHA-256`):** `ac005bab7c61abf988877a33aa4b94fe52efa8ff188519a3ed0f50aae6463c84`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `IndependentPilotParserAudit` | `class` | `Lines 12–23` | `class IndependentPilotParserAudit(unittest.TestCase):` | رمز برمجي موثق. |
| `IndependentPilotParserAudit.test_reject_duplicate_keys_nonfinite_or_nested_overflow` | `method` | `Lines 13–19` | `def test_reject_duplicate_keys_nonfinite_or_nested_overflow(self):` | رمز برمجي موثق. |
| `IndependentPilotParserAudit.test_valid_json_is_data_not_execution` | `method` | `Lines 21–23` | `def test_valid_json_is_data_not_execution(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `IndependentPilotParserAudit` — `Lines 12–23`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `23` (`Lines 12–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–23`):**
```python
class IndependentPilotParserAudit(unittest.TestCase):
    def test_reject_duplicate_keys_nonfinite_or_nested_overflow(self):
        for text in ['{"roi":[0,0,1,1],"roi":[0,0,0.5,0.5]}',
                     '{"value":NaN}', '{"value":Infinity}',
                     '['*1100+'0'+']'*1100,
                     '{"value":"'+'x'*2048+'"}']:
            with self.subTest(prefix=text[:30]),self.assertRaises(ValueError):
                strict_call_arguments(text)

    def test_valid_json_is_data_not_execution(self):
        parsed = strict_call_arguments('{"command":"do not execute","trace_ids":[1,2]}')
        self.assertEqual(parsed,{'command':'do not execute','trace_ids':[1,2]})
```

### `IndependentPilotParserAudit.test_reject_duplicate_keys_nonfinite_or_nested_overflow` — `Lines 13–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `19` (`Lines 13–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–19`):**
```python
    def test_reject_duplicate_keys_nonfinite_or_nested_overflow(self):
        for text in ['{"roi":[0,0,1,1],"roi":[0,0,0.5,0.5]}',
                     '{"value":NaN}', '{"value":Infinity}',
                     '['*1100+'0'+']'*1100,
                     '{"value":"'+'x'*2048+'"}']:
            with self.subTest(prefix=text[:30]),self.assertRaises(ValueError):
                strict_call_arguments(text)
```

### `IndependentPilotParserAudit.test_valid_json_is_data_not_execution` — `Lines 21–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `23` (`Lines 21–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–23`):**
```python
    def test_valid_json_is_data_not_execution(self):
        parsed = strict_call_arguments('{"command":"do not execute","trace_ids":[1,2]}')
        self.assertEqual(parsed,{'command':'do not execute','trace_ids':[1,2]})
```
