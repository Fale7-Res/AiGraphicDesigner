# مرآة الكود التفصيلية: `test_selection.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_selection.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_selection.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `15` (`Lines 1–15`)
- **بصمة الملف (`SHA-256`):** `cee509c6c1f66509851e776b6f79fe2be17e64f3e0f5bf3c3733d43242a49d79`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-SELECTION-TEST | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SelectionTests` | `class` | `Lines 5–13` | `class SelectionTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SelectionTests.test_deterministic_and_no_mutation` | `method` | `Lines 6–10` | `def test_deterministic_and_no_mutation(self):` | رمز برمجي موثق. |
| `SelectionTests.test_closure_is_source_only` | `method` | `Lines 11–13` | `def test_closure_is_source_only(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SelectionTests` — `Lines 5–13`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `5` إلى السطر `13` (`Lines 5–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 5–13`):**
```python
class SelectionTests(unittest.TestCase):
 def test_deterministic_and_no_mutation(self):
  rgb=np.full((24,24,3),255,dtype='uint8');rgb[5:18,10:12]=0
  traces=[dict(trace_id=9,length_px=12,source_points_xy=[[10,5],[10,17]]),dict(trace_id=2,length_px=20,source_points_xy=[[1,1],[21,1]])]
  a,rows=selection_rank(traces,rgb);b,_=selection_rank(traces,rgb)
  self.assertEqual(a,b);self.assertEqual(len(rows),2);self.assertEqual(traces[0]['trace_id'],9);self.assertEqual(a[0]['trace_id'],9)
 def test_closure_is_source_only(self):
  p=[[2,2],[12,2],[12,12],[2,12],[2,2]];t=dict(trace_id=0,length_px=40,source_points_xy=p)
  _,rows=selection_rank([t],np.zeros((16,16,3),dtype='uint8'));self.assertTrue(rows[0]['closed']);self.assertEqual(t['source_points_xy'],p)
```

### `SelectionTests.test_deterministic_and_no_mutation` — `Lines 6–10`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `10` (`Lines 6–10`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–10`):**
```python
 def test_deterministic_and_no_mutation(self):
  rgb=np.full((24,24,3),255,dtype='uint8');rgb[5:18,10:12]=0
  traces=[dict(trace_id=9,length_px=12,source_points_xy=[[10,5],[10,17]]),dict(trace_id=2,length_px=20,source_points_xy=[[1,1],[21,1]])]
  a,rows=selection_rank(traces,rgb);b,_=selection_rank(traces,rgb)
  self.assertEqual(a,b);self.assertEqual(len(rows),2);self.assertEqual(traces[0]['trace_id'],9);self.assertEqual(a[0]['trace_id'],9)
```

### `SelectionTests.test_closure_is_source_only` — `Lines 11–13`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `13` (`Lines 11–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–13`):**
```python
 def test_closure_is_source_only(self):
  p=[[2,2],[12,2],[12,12],[2,12],[2,2]];t=dict(trace_id=0,length_px=40,source_points_xy=p)
  _,rows=selection_rank([t],np.zeros((16,16,3),dtype='uint8'));self.assertTrue(rows[0]['closed']);self.assertEqual(t['source_points_xy'],p)
```
