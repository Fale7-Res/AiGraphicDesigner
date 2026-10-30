# مرآة الكود التفصيلية: `test_discovery_strokes.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_discovery_strokes.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_discovery_strokes.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `65` (`Lines 1–65`)
- **بصمة الملف (`SHA-256`):** `e149c2ccb123084d4a5c6141c90df7ef45eb2a2a5a53ff494450fa139ae34069`
- **الوصف التفصيلي:** # START CHANGE AGD-SOURCE-STROKES-TEST | 2026-10-29T21:58:16Z | CREATED | Author: discovery_strokes

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SourceStrokeTests` | `class` | `Lines 8–60` | `class SourceStrokeTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_uniform_has_no_candidates` | `method` | `Lines 9–12` | `def test_uniform_has_no_candidates(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_single_boundary_not_stroke` | `method` | `Lines 14–17` | `def test_single_boundary_not_stroke(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_absent_label_thin_stroke_proposal` | `method` | `Lines 19–27` | `def test_absent_label_thin_stroke_proposal(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_deterministic_geometry` | `method` | `Lines 29–32` | `def test_deterministic_geometry(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_junction_trace_edges_once` | `method` | `Lines 34–40` | `def test_junction_trace_edges_once(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_corner_fit_keeps_vertex` | `method` | `Lines 42–47` | `def test_corner_fit_keeps_vertex(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_loop_trace_closes_once` | `method` | `Lines 49–56` | `def test_loop_trace_closes_once(self):` | رمز برمجي موثق. |
| `SourceStrokeTests.test_invalid_input` | `method` | `Lines 58–60` | `def test_invalid_input(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SourceStrokeTests` — `Lines 8–60`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `60` (`Lines 8–60`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–60`):**
```python
class SourceStrokeTests(unittest.TestCase):
    def test_uniform_has_no_candidates(self):
        audit, arrays = ds.discover(np.full((32, 48, 3), 255, np.uint8))
        self.assertEqual(audit['accepted'], [])
        self.assertEqual(int(arrays['source_skeleton'].sum()), 0)

    def test_single_boundary_not_stroke(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[:, :24] = 0
        audit, _ = ds.discover(rgb)
        self.assertEqual(audit['accepted'], [])

    def test_absent_label_thin_stroke_proposal(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[15:17, 7:40] = 0
        original = rgb.copy()
        audit, _ = ds.discover(rgb)
        self.assertTrue(audit['accepted'])
        self.assertTrue(np.array_equal(original, rgb))
        self.assertTrue(all(x['width_px'] <= 6 for x in audit['accepted']))
        self.assertFalse(audit['integrated_into_shared_graph'])
        self.assertNotIn('<image', ds.svg(audit, 48, 32))

    def test_deterministic_geometry(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[15:17, 7:40] = (180, 0, 0)
        first, _ = ds.discover(rgb); second, _ = ds.discover(rgb)
        self.assertEqual(first['accepted'], second['accepted'])

    def test_junction_trace_edges_once(self):
        sk = np.zeros((9, 9), bool); sk[4, 1:8] = True; sk[1:5, 4] = True
        chains, adjacency = ds._trace(sk)
        observed = sum(len(chain)-1 for chain in chains)
        expected = sum(len(near) for near in adjacency.values())//2
        self.assertEqual(observed, expected)
        self.assertEqual(len(chains), 3)

    def test_corner_fit_keeps_vertex(self):
        points = np.array([[2., 2.], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4], [5, 5]])
        curves, meta = ds._fit(points)
        self.assertIsNotNone(curves)
        self.assertEqual(meta['intentional_corner_count'], 1)
        self.assertTrue(np.array_equal(curves[0, 3], [5, 2]))

    def test_loop_trace_closes_once(self):
        sk = np.zeros((9, 9), bool)
        sk[2, 2:7] = True; sk[6, 2:7] = True
        sk[2:7, 2] = True; sk[2:7, 6] = True
        chains, _ = ds._trace(sk)
        self.assertEqual(len(chains), 1)
        self.assertTrue(np.array_equal(chains[0][0], chains[0][-1]))
        self.assertEqual(len(chains[0])-1, 16)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            ds.discover(np.zeros((10, 10), np.uint8))
```

### `SourceStrokeTests.test_uniform_has_no_candidates` — `Lines 9–12`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `12` (`Lines 9–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–12`):**
```python
    def test_uniform_has_no_candidates(self):
        audit, arrays = ds.discover(np.full((32, 48, 3), 255, np.uint8))
        self.assertEqual(audit['accepted'], [])
        self.assertEqual(int(arrays['source_skeleton'].sum()), 0)
```

### `SourceStrokeTests.test_single_boundary_not_stroke` — `Lines 14–17`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `17` (`Lines 14–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–17`):**
```python
    def test_single_boundary_not_stroke(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[:, :24] = 0
        audit, _ = ds.discover(rgb)
        self.assertEqual(audit['accepted'], [])
```

### `SourceStrokeTests.test_absent_label_thin_stroke_proposal` — `Lines 19–27`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `27` (`Lines 19–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–27`):**
```python
    def test_absent_label_thin_stroke_proposal(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[15:17, 7:40] = 0
        original = rgb.copy()
        audit, _ = ds.discover(rgb)
        self.assertTrue(audit['accepted'])
        self.assertTrue(np.array_equal(original, rgb))
        self.assertTrue(all(x['width_px'] <= 6 for x in audit['accepted']))
        self.assertFalse(audit['integrated_into_shared_graph'])
        self.assertNotIn('<image', ds.svg(audit, 48, 32))
```

### `SourceStrokeTests.test_deterministic_geometry` — `Lines 29–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `32` (`Lines 29–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–32`):**
```python
    def test_deterministic_geometry(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[15:17, 7:40] = (180, 0, 0)
        first, _ = ds.discover(rgb); second, _ = ds.discover(rgb)
        self.assertEqual(first['accepted'], second['accepted'])
```

### `SourceStrokeTests.test_junction_trace_edges_once` — `Lines 34–40`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `40` (`Lines 34–40`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–40`):**
```python
    def test_junction_trace_edges_once(self):
        sk = np.zeros((9, 9), bool); sk[4, 1:8] = True; sk[1:5, 4] = True
        chains, adjacency = ds._trace(sk)
        observed = sum(len(chain)-1 for chain in chains)
        expected = sum(len(near) for near in adjacency.values())//2
        self.assertEqual(observed, expected)
        self.assertEqual(len(chains), 3)
```

### `SourceStrokeTests.test_corner_fit_keeps_vertex` — `Lines 42–47`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `47` (`Lines 42–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–47`):**
```python
    def test_corner_fit_keeps_vertex(self):
        points = np.array([[2., 2.], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4], [5, 5]])
        curves, meta = ds._fit(points)
        self.assertIsNotNone(curves)
        self.assertEqual(meta['intentional_corner_count'], 1)
        self.assertTrue(np.array_equal(curves[0, 3], [5, 2]))
```

### `SourceStrokeTests.test_loop_trace_closes_once` — `Lines 49–56`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `56` (`Lines 49–56`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–56`):**
```python
    def test_loop_trace_closes_once(self):
        sk = np.zeros((9, 9), bool)
        sk[2, 2:7] = True; sk[6, 2:7] = True
        sk[2:7, 2] = True; sk[2:7, 6] = True
        chains, _ = ds._trace(sk)
        self.assertEqual(len(chains), 1)
        self.assertTrue(np.array_equal(chains[0][0], chains[0][-1]))
        self.assertEqual(len(chains[0])-1, 16)
```

### `SourceStrokeTests.test_invalid_input` — `Lines 58–60`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `60` (`Lines 58–60`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 58–60`):**
```python
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            ds.discover(np.zeros((10, 10), np.uint8))
```
