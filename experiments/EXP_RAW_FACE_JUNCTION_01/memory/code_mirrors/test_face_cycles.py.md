# مرآة الكود التفصيلية: `test_face_cycles.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_face_cycles.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_face_cycles.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `27` (`Lines 1–27`)
- **بصمة الملف (`SHA-256`):** `ee46737e0a78e46df76a858b4cee4abb9f3fa3ef0eeb55a0102ce8f691d93e00`
- **الوصف التفصيلي:** # START CHANGE AGD-RAWFACE-TEST-FACE-CYCLES | 2026-10-29T12:20:15Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `FaceWalkTests` | `class` | `Lines 6–23` | `class FaceWalkTests(unittest.TestCase):` | رمز برمجي موثق. |
| `FaceWalkTests.test_pinched_triangles_preserve_every_directed_reference` | `method` | `Lines 7–12` | `def test_pinched_triangles_preserve_every_directed_reference(self):` | رمز برمجي موثق. |
| `FaceWalkTests.test_no_silent_open_walk_fix` | `method` | `Lines 13–14` | `def test_no_silent_open_walk_fix(self):` | رمز برمجي موثق. |
| `FaceWalkTests.test_reversed_references_and_hole_winding_not_reoriented` | `method` | `Lines 15–17` | `def test_reversed_references_and_hole_winding_not_reoriented(self):` | رمز برمجي موثق. |
| `FaceWalkTests.test_degenerate_cycle_is_retained_not_pruned` | `method` | `Lines 18–20` | `def test_degenerate_cycle_is_retained_not_pruned(self):` | رمز برمجي موثق. |
| `FaceWalkTests.test_budget_is_fail_closed` | `method` | `Lines 21–23` | `def test_budget_is_fail_closed(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `FaceWalkTests` — `Lines 6–23`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `23` (`Lines 6–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–23`):**
```python
class FaceWalkTests(unittest.TestCase):
    def test_pinched_triangles_preserve_every_directed_reference(self):
        raw={0:np.array([[0,0],[2,0],[1,1],[0,0]]),1:np.array([[0,0],[-2,0],[-1,-1],[0,0]])}
        refs=[{'chain':0,'forward':True},{'chain':1,'forward':True}];saved=copy.deepcopy(refs)
        pieces,n=split_closed_walk(refs,raw)
        self.assertEqual(n,1);self.assertEqual(len(pieces),2);self.assertEqual(refs,saved)
        self.assertEqual(collections.Counter((x['chain'],x['forward']) for p in pieces for x in p),collections.Counter((x['chain'],x['forward']) for x in refs))
    def test_no_silent_open_walk_fix(self):
        with self.assertRaises(ValueError):split_closed_walk([{'chain':0,'forward':True}],{0:np.array([[0,0],[1,0]])})
    def test_reversed_references_and_hole_winding_not_reoriented(self):
        raw={0:np.array([[0,0],[1,0],[0,1],[0,0]])};refs=[{'chain':0,'forward':False}]
        pieces,n=split_closed_walk(refs,raw);self.assertEqual(pieces,[refs]);self.assertEqual(n,0)
    def test_degenerate_cycle_is_retained_not_pruned(self):
        raw={0:np.array([[0,0],[1,0],[0,0]])};refs=[{'chain':0,'forward':True}]
        pieces,n=split_closed_walk(refs,raw);self.assertEqual(pieces,[refs])
    def test_budget_is_fail_closed(self):
        raw={0:np.array([[0,0],[1,0],[0,0]]),1:np.array([[0,0],[0,1],[0,0]])}
        with self.assertRaises(ValueError):split_closed_walk([{'chain':0,'forward':True},{'chain':1,'forward':True}],raw,max_splits=0)
```

### `FaceWalkTests.test_pinched_triangles_preserve_every_directed_reference` — `Lines 7–12`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `12` (`Lines 7–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–12`):**
```python
    def test_pinched_triangles_preserve_every_directed_reference(self):
        raw={0:np.array([[0,0],[2,0],[1,1],[0,0]]),1:np.array([[0,0],[-2,0],[-1,-1],[0,0]])}
        refs=[{'chain':0,'forward':True},{'chain':1,'forward':True}];saved=copy.deepcopy(refs)
        pieces,n=split_closed_walk(refs,raw)
        self.assertEqual(n,1);self.assertEqual(len(pieces),2);self.assertEqual(refs,saved)
        self.assertEqual(collections.Counter((x['chain'],x['forward']) for p in pieces for x in p),collections.Counter((x['chain'],x['forward']) for x in refs))
```

### `FaceWalkTests.test_no_silent_open_walk_fix` — `Lines 13–14`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `14` (`Lines 13–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–14`):**
```python
    def test_no_silent_open_walk_fix(self):
        with self.assertRaises(ValueError):split_closed_walk([{'chain':0,'forward':True}],{0:np.array([[0,0],[1,0]])})
```

### `FaceWalkTests.test_reversed_references_and_hole_winding_not_reoriented` — `Lines 15–17`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `17` (`Lines 15–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–17`):**
```python
    def test_reversed_references_and_hole_winding_not_reoriented(self):
        raw={0:np.array([[0,0],[1,0],[0,1],[0,0]])};refs=[{'chain':0,'forward':False}]
        pieces,n=split_closed_walk(refs,raw);self.assertEqual(pieces,[refs]);self.assertEqual(n,0)
```

### `FaceWalkTests.test_degenerate_cycle_is_retained_not_pruned` — `Lines 18–20`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `20` (`Lines 18–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–20`):**
```python
    def test_degenerate_cycle_is_retained_not_pruned(self):
        raw={0:np.array([[0,0],[1,0],[0,0]])};refs=[{'chain':0,'forward':True}]
        pieces,n=split_closed_walk(refs,raw);self.assertEqual(pieces,[refs])
```

### `FaceWalkTests.test_budget_is_fail_closed` — `Lines 21–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `23` (`Lines 21–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–23`):**
```python
    def test_budget_is_fail_closed(self):
        raw={0:np.array([[0,0],[1,0],[0,0]]),1:np.array([[0,0],[0,1],[0,0]])}
        with self.assertRaises(ValueError):split_closed_walk([{'chain':0,'forward':True},{'chain':1,'forward':True}],raw,max_splits=0)
```
