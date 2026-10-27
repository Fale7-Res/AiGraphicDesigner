# مرآة الكود التفصيلية: `test_optimizer.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_optimizer.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_optimizer.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `39` (`Lines 1–39`)
- **بصمة الملف (`SHA-256`):** `ec61254f4ffb67e6814fb98709b884110dd828846f624bd441a154197e8cbd4a`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `OptimizerTests` | `class` | `Lines 10–36` | `class OptimizerTests(unittest.TestCase):` | رمز برمجي موثق. |
| `OptimizerTests.test_surface` | `method` | `Lines 11–16` | `def test_surface(self):` | رمز برمجي موثق. |
| `OptimizerTests.test_effective_settings` | `method` | `Lines 17–22` | `def test_effective_settings(self):` | رمز برمجي موثق. |
| `OptimizerTests.test_input_and_history` | `method` | `Lines 23–29` | `def test_input_and_history(self):` | رمز برمجي موثق. |
| `OptimizerTests.test_budget_and_failure_record` | `method` | `Lines 30–36` | `def test_budget_and_failure_record(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `OptimizerTests` — `Lines 10–36`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `36` (`Lines 10–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–36`):**
```python
class OptimizerTests(unittest.TestCase):
    def test_surface(self):
        self.assertEqual({c['clustering'] for c in pilots()},{'color-cluster','watershed','bw'})
        self.assertEqual(pilots()[0],OWNER)
        for c in pilots():
            vtracer.Config(**c)
            for n in neighborhood(c):vtracer.Config(**n)
    def test_effective_settings(self):
        c=OWNER|{'mode':'pixel'}
        self.assertEqual(canonical(c),canonical(c|{'simplify':.25}))
        c=OWNER|{'clustering':'bw','hierarchical':'cutout'}
        self.assertIn('layer_difference',canonical(c))
        self.assertNotIn('color_precision',canonical(c))
    def test_input_and_history(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);Image.new('RGBA',(16,16),(255,0,0,100)).save(p/'a.png')
            with self.assertRaises(ValueError):optimize(p/'a.png',p/'out')
            (p/'out').mkdir();(p/'out/sentinel').write_text('preserve')
            with self.assertRaises(FileExistsError):optimize(p/'a.png',p/'out')
            self.assertEqual((p/'out/sentinel').read_text(),'preserve')
    def test_budget_and_failure_record(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);Image.new('RGB',(16,16),'white').save(p/'a.png')
            def failed(*args):return {'status':'failed','error':'test failure','config':args[2]}
            with patch('optimizer.run_trial',side_effect=failed):r=optimize(p/'a.png',p/'out',13,60)
            self.assertEqual(len(r['failed']),13);self.assertEqual(r['ranked'],[])
            self.assertTrue((p/'out/ranking.json').is_file())
```

### `OptimizerTests.test_surface` — `Lines 11–16`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `16` (`Lines 11–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–16`):**
```python
    def test_surface(self):
        self.assertEqual({c['clustering'] for c in pilots()},{'color-cluster','watershed','bw'})
        self.assertEqual(pilots()[0],OWNER)
        for c in pilots():
            vtracer.Config(**c)
            for n in neighborhood(c):vtracer.Config(**n)
```

### `OptimizerTests.test_effective_settings` — `Lines 17–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `22` (`Lines 17–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–22`):**
```python
    def test_effective_settings(self):
        c=OWNER|{'mode':'pixel'}
        self.assertEqual(canonical(c),canonical(c|{'simplify':.25}))
        c=OWNER|{'clustering':'bw','hierarchical':'cutout'}
        self.assertIn('layer_difference',canonical(c))
        self.assertNotIn('color_precision',canonical(c))
```

### `OptimizerTests.test_input_and_history` — `Lines 23–29`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `29` (`Lines 23–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–29`):**
```python
    def test_input_and_history(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);Image.new('RGBA',(16,16),(255,0,0,100)).save(p/'a.png')
            with self.assertRaises(ValueError):optimize(p/'a.png',p/'out')
            (p/'out').mkdir();(p/'out/sentinel').write_text('preserve')
            with self.assertRaises(FileExistsError):optimize(p/'a.png',p/'out')
            self.assertEqual((p/'out/sentinel').read_text(),'preserve')
```

### `OptimizerTests.test_budget_and_failure_record` — `Lines 30–36`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `36` (`Lines 30–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–36`):**
```python
    def test_budget_and_failure_record(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);Image.new('RGB',(16,16),'white').save(p/'a.png')
            def failed(*args):return {'status':'failed','error':'test failure','config':args[2]}
            with patch('optimizer.run_trial',side_effect=failed):r=optimize(p/'a.png',p/'out',13,60)
            self.assertEqual(len(r['failed']),13);self.assertEqual(r['ranked'],[])
            self.assertTrue((p/'out/ranking.json').is_file())
```
