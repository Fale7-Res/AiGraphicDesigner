# مرآة الكود التفصيلية: `test_study.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_study.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_study.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `24` (`Lines 1–24`)
- **بصمة الملف (`SHA-256`):** `ac982958b331c67389a1b53c7d3818773f83e31718b6fd6e5db0b182cb221a75`
- **الوصف التفصيلي:** # START CHANGE AGD-THIN-TEST-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `MeasurementSafeguards` | `class` | `Lines 7–20` | `class MeasurementSafeguards(unittest.TestCase):` | رمز برمجي موثق. |
| `MeasurementSafeguards.test_false_join_of_two_disjoint_structures` | `method` | `Lines 8–11` | `def test_false_join_of_two_disjoint_structures(self):` | رمز برمجي موثق. |
| `MeasurementSafeguards.test_false_split_of_one_structure` | `method` | `Lines 13–16` | `def test_false_split_of_one_structure(self):` | رمز برمجي موثق. |
| `MeasurementSafeguards.test_empty_reference_never_passes` | `method` | `Lines 18–20` | `def test_empty_reference_never_passes(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `MeasurementSafeguards` — `Lines 7–20`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `20` (`Lines 7–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–20`):**
```python
class MeasurementSafeguards(unittest.TestCase):
    def test_false_join_of_two_disjoint_structures(self):
        truth=np.zeros((8,12),bool);truth[2:6,1:4]=True;truth[2:6,8:11]=True
        pred=truth.copy();pred[3,4:8]=True
        self.assertEqual(separation_errors(truth,pred)['false_join_excess'],1)

    def test_false_split_of_one_structure(self):
        truth=np.zeros((8,12),bool);truth[2:6,1:11]=True
        pred=truth.copy();pred[:,5]=False
        self.assertEqual(separation_errors(truth,pred)['false_split_excess'],1)

    def test_empty_reference_never_passes(self):
        result=separation_errors(np.zeros((8,8),bool),np.ones((8,8),bool))
        self.assertEqual(result['status'],'EMPTY_REFERENCE_NOT_EVALUABLE')
```

### `MeasurementSafeguards.test_false_join_of_two_disjoint_structures` — `Lines 8–11`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `11` (`Lines 8–11`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–11`):**
```python
    def test_false_join_of_two_disjoint_structures(self):
        truth=np.zeros((8,12),bool);truth[2:6,1:4]=True;truth[2:6,8:11]=True
        pred=truth.copy();pred[3,4:8]=True
        self.assertEqual(separation_errors(truth,pred)['false_join_excess'],1)
```

### `MeasurementSafeguards.test_false_split_of_one_structure` — `Lines 13–16`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `16` (`Lines 13–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–16`):**
```python
    def test_false_split_of_one_structure(self):
        truth=np.zeros((8,12),bool);truth[2:6,1:11]=True
        pred=truth.copy();pred[:,5]=False
        self.assertEqual(separation_errors(truth,pred)['false_split_excess'],1)
```

### `MeasurementSafeguards.test_empty_reference_never_passes` — `Lines 18–20`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `20` (`Lines 18–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–20`):**
```python
    def test_empty_reference_never_passes(self):
        result=separation_errors(np.zeros((8,8),bool),np.ones((8,8),bool))
        self.assertEqual(result['status'],'EMPTY_REFERENCE_NOT_EVALUABLE')
```
