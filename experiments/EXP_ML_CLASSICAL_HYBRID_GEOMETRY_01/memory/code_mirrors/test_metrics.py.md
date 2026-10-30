# مرآة الكود التفصيلية: `test_metrics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_metrics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_metrics.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `32` (`Lines 1–32`)
- **بصمة الملف (`SHA-256`):** `b958ad80fab5eb8c9cce7bd923caa9797d8b75ab75a7c7c7587812fe6a76e695`
- **الوصف التفصيلي:** # START CHANGE AGD-ML-METRIC-TESTS | 2026-10-30T08:20:30Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `MetricTests` | `class` | `Lines 10–29` | `class MetricTests(unittest.TestCase):` | رمز برمجي موثق. |
| `MetricTests.test_exact_and_displaced_support` | `method` | `Lines 11–14` | `def test_exact_and_displaced_support(self):` | رمز برمجي موثق. |
| `MetricTests.test_empty_support_is_failure` | `method` | `Lines 16–19` | `def test_empty_support_is_failure(self):` | رمز برمجي موثق. |
| `MetricTests.test_pixel_centers_are_explicit` | `method` | `Lines 21–23` | `def test_pixel_centers_are_explicit(self):` | رمز برمجي موثق. |
| `MetricTests.test_open_curve_has_no_implicit_closure` | `method` | `Lines 25–29` | `def test_open_curve_has_no_implicit_closure(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `MetricTests` — `Lines 10–29`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `29` (`Lines 10–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–29`):**
```python
class MetricTests(unittest.TestCase):
    def test_exact_and_displaced_support(self):
        q=np.array([[0.,0.],[10.,0.]])
        self.assertEqual(support_stats(q,q,1.25)['recall'],1.)
        self.assertEqual(support_stats(q,q+np.array([0.,2.]),1.25)['recall'],0.)

    def test_empty_support_is_failure(self):
        self.assertEqual(support_stats(np.array([[1.,1.]]),np.empty((0,2)),1.25)['recall'],0.)
        lines,points=samples_from_items([])
        self.assertEqual(lines,[]);self.assertEqual(points.shape,(0,2))

    def test_pixel_centers_are_explicit(self):
        m=np.zeros((3,4),bool);m[1,2]=True
        np.testing.assert_array_equal(xy(m),[[2.5,1.5]])

    def test_open_curve_has_no_implicit_closure(self):
        item={'curves':[[[1.,1.],[2.,1.],[3.,2.],[4.,2.]]]}
        root=ET.fromstring(svg_graph(chain_graph([item],10,10)))
        path=list(root)[0]
        self.assertNotIn('Z',path.attrib['d']);self.assertEqual(path.attrib['stroke-width'],'0.35')
```

### `MetricTests.test_exact_and_displaced_support` — `Lines 11–14`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `14` (`Lines 11–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–14`):**
```python
    def test_exact_and_displaced_support(self):
        q=np.array([[0.,0.],[10.,0.]])
        self.assertEqual(support_stats(q,q,1.25)['recall'],1.)
        self.assertEqual(support_stats(q,q+np.array([0.,2.]),1.25)['recall'],0.)
```

### `MetricTests.test_empty_support_is_failure` — `Lines 16–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `19` (`Lines 16–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–19`):**
```python
    def test_empty_support_is_failure(self):
        self.assertEqual(support_stats(np.array([[1.,1.]]),np.empty((0,2)),1.25)['recall'],0.)
        lines,points=samples_from_items([])
        self.assertEqual(lines,[]);self.assertEqual(points.shape,(0,2))
```

### `MetricTests.test_pixel_centers_are_explicit` — `Lines 21–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `23` (`Lines 21–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–23`):**
```python
    def test_pixel_centers_are_explicit(self):
        m=np.zeros((3,4),bool);m[1,2]=True
        np.testing.assert_array_equal(xy(m),[[2.5,1.5]])
```

### `MetricTests.test_open_curve_has_no_implicit_closure` — `Lines 25–29`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `29` (`Lines 25–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–29`):**
```python
    def test_open_curve_has_no_implicit_closure(self):
        item={'curves':[[[1.,1.],[2.,1.],[3.,2.],[4.,2.]]]}
        root=ET.fromstring(svg_graph(chain_graph([item],10,10)))
        path=list(root)[0]
        self.assertNotIn('Z',path.attrib['d']);self.assertEqual(path.attrib['stroke-width'],'0.35')
```
