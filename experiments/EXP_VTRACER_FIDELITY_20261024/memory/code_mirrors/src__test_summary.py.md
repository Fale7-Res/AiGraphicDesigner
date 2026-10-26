# مرآة الكود التفصيلية: `src/test_summary.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/test_summary.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/test_summary.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `24` (`Lines 1–24`)
- **بصمة الملف (`SHA-256`):** `88725453f11b8e3c362e679b1b016c9b3910ee22e78f2f05c2935b8af6b8bacf`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SummaryTests` | `class` | `Lines 9–21` | `class SummaryTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SummaryTests.test_fixed_tiles_detect_concentrated_error` | `method` | `Lines 10–16` | `def test_fixed_tiles_detect_concentrated_error(self):` | رمز برمجي موثق. |
| `SummaryTests.test_incomplete_evidence_does_not_write_summary` | `method` | `Lines 17–21` | `def test_incomplete_evidence_does_not_write_summary(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SummaryTests` — `Lines 9–21`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `21` (`Lines 9–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–21`):**
```python
class SummaryTests(unittest.TestCase):
    def test_fixed_tiles_detect_concentrated_error(self):
        source=np.zeros((16,16,3),np.uint8);pred=source.copy();pred[:4,:4]=100
        result=local_errors(source,pred,[(1.5,1.5)])
        self.assertEqual(result['tile_rmse_worst'],100)
        self.assertEqual(result['tile_rmse_median'],0)
        self.assertGreater(result['seed_center_rmse'],0)
        self.assertEqual(local_errors(source,source)['tile_rmse_worst'],0)
    def test_incomplete_evidence_does_not_write_summary(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'inputs').mkdir();(root/'protocol.json').write_text('{}')
            with self.assertRaises(ValueError):collect(root,root/'out')
            self.assertFalse((root/'out').exists())
```

### `SummaryTests.test_fixed_tiles_detect_concentrated_error` — `Lines 10–16`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `16` (`Lines 10–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–16`):**
```python
    def test_fixed_tiles_detect_concentrated_error(self):
        source=np.zeros((16,16,3),np.uint8);pred=source.copy();pred[:4,:4]=100
        result=local_errors(source,pred,[(1.5,1.5)])
        self.assertEqual(result['tile_rmse_worst'],100)
        self.assertEqual(result['tile_rmse_median'],0)
        self.assertGreater(result['seed_center_rmse'],0)
        self.assertEqual(local_errors(source,source)['tile_rmse_worst'],0)
```

### `SummaryTests.test_incomplete_evidence_does_not_write_summary` — `Lines 17–21`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `21` (`Lines 17–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–21`):**
```python
    def test_incomplete_evidence_does_not_write_summary(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'inputs').mkdir();(root/'protocol.json').write_text('{}')
            with self.assertRaises(ValueError):collect(root,root/'out')
            self.assertFalse((root/'out').exists())
```
