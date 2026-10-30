# مرآة الكود التفصيلية: `test_stable_fit.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_stable_fit.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_stable_fit.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `31` (`Lines 1–31`)
- **بصمة الملف (`SHA-256`):** `7ca6c967138b8fa2ac4de3491c41be84a518b72bc8f89a27b5dec6ac4ba4cd8e`
- **الوصف التفصيلي:** # START CHANGE AGD-ML-FIT-CONTROL-TEST | 2026-10-30T07:59:01Z | CREATED | Author: fitting_stability

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `StableFitTests` | `class` | `Lines 8–28` | `class StableFitTests(unittest.TestCase):` | رمز برمجي موثق. |
| `StableFitTests.test_unequal_chord_cannot_create_long_short_handle` | `method` | `Lines 9–13` | `def test_unequal_chord_cannot_create_long_short_handle(self):` | رمز برمجي موثق. |
| `StableFitTests.test_sharp_corner_preserved` | `method` | `Lines 14–19` | `def test_sharp_corner_preserved(self):` | رمز برمجي موثق. |
| `StableFitTests.test_no_budget_fallback` | `method` | `Lines 20–23` | `def test_no_budget_fallback(self):` | رمز برمجي موثق. |
| `StableFitTests.test_nonfinite_rejected` | `method` | `Lines 24–25` | `def test_nonfinite_rejected(self):` | رمز برمجي موثق. |
| `StableFitTests.test_segment_distance_not_vertex_distance` | `method` | `Lines 26–28` | `def test_segment_distance_not_vertex_distance(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `StableFitTests` — `Lines 8–28`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `28` (`Lines 8–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–28`):**
```python
class StableFitTests(unittest.TestCase):
    def test_unequal_chord_cannot_create_long_short_handle(self):
        curves,_=construct(np.array([[0,0],[10,0],[11,1],[30,2]],float))
        lengths=np.linalg.norm(curves[:,3]-curves[:,0],axis=1)
        self.assertTrue(np.all(np.linalg.norm(curves[:,1]-curves[:,0],axis=1)<=lengths/3+1e-12))
        self.assertTrue(np.all(np.linalg.norm(curves[:,3]-curves[:,2],axis=1)<=lengths/3+1e-12))
    def test_sharp_corner_preserved(self):
        raw=np.array([[0,0],[2,0],[2,2]],float)
        curves,meta=fit(raw)
        self.assertIsNotNone(curves);self.assertEqual(meta['intentional_corner_count'],1)
        np.testing.assert_equal(curves[0,3],curves[1,0])
        self.assertLess(meta['numerical_upper_envelope_px'],.01)
    def test_no_budget_fallback(self):
        points=np.array([[i,i%2] for i in range(20)],float)
        curves,meta=fit(points,maximum_segments=2)
        self.assertIsNone(curves);self.assertEqual(meta['reason'],'cubic_budget')
    def test_nonfinite_rejected(self):
        self.assertIsNone(fit(np.array([[0,0],[np.nan,1]]))[0])
    def test_segment_distance_not_vertex_distance(self):
        raw=np.array([[0,0],[100,0]],float);curves,_=construct(raw)
        self.assertLess(measure(raw,curves)['curve_to_raw_max_px'],1e-10)
```

### `StableFitTests.test_unequal_chord_cannot_create_long_short_handle` — `Lines 9–13`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `13` (`Lines 9–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–13`):**
```python
    def test_unequal_chord_cannot_create_long_short_handle(self):
        curves,_=construct(np.array([[0,0],[10,0],[11,1],[30,2]],float))
        lengths=np.linalg.norm(curves[:,3]-curves[:,0],axis=1)
        self.assertTrue(np.all(np.linalg.norm(curves[:,1]-curves[:,0],axis=1)<=lengths/3+1e-12))
        self.assertTrue(np.all(np.linalg.norm(curves[:,3]-curves[:,2],axis=1)<=lengths/3+1e-12))
```

### `StableFitTests.test_sharp_corner_preserved` — `Lines 14–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `19` (`Lines 14–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–19`):**
```python
    def test_sharp_corner_preserved(self):
        raw=np.array([[0,0],[2,0],[2,2]],float)
        curves,meta=fit(raw)
        self.assertIsNotNone(curves);self.assertEqual(meta['intentional_corner_count'],1)
        np.testing.assert_equal(curves[0,3],curves[1,0])
        self.assertLess(meta['numerical_upper_envelope_px'],.01)
```

### `StableFitTests.test_no_budget_fallback` — `Lines 20–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `23` (`Lines 20–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–23`):**
```python
    def test_no_budget_fallback(self):
        points=np.array([[i,i%2] for i in range(20)],float)
        curves,meta=fit(points,maximum_segments=2)
        self.assertIsNone(curves);self.assertEqual(meta['reason'],'cubic_budget')
```

### `StableFitTests.test_nonfinite_rejected` — `Lines 24–25`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `24` إلى السطر `25` (`Lines 24–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 24–25`):**
```python
    def test_nonfinite_rejected(self):
        self.assertIsNone(fit(np.array([[0,0],[np.nan,1]]))[0])
```

### `StableFitTests.test_segment_distance_not_vertex_distance` — `Lines 26–28`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `28` (`Lines 26–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–28`):**
```python
    def test_segment_distance_not_vertex_distance(self):
        raw=np.array([[0,0],[100,0]],float);curves,_=construct(raw)
        self.assertLess(measure(raw,curves)['curve_to_raw_max_px'],1e-10)
```
