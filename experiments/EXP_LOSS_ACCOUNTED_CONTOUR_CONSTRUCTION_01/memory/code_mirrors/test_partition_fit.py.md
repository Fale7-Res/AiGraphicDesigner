# مرآة الكود التفصيلية: `test_partition_fit.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_partition_fit.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_partition_fit.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `71` (`Lines 1–71`)
- **بصمة الملف (`SHA-256`):** `840a498fc0f8261d44fcf01eb44ce3eac1efe084f1184723c3d5e420f94106fb`
- **الوصف التفصيلي:** # START CHANGE AGD-LOSS-CONTOUR-TEST | 2026-10-30T08:41:02Z | CREATED | Author: contour_partition

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PartitionFitTests` | `class` | `Lines 9–67` | `class PartitionFitTests(unittest.TestCase):` | رمز برمجي موثق. |
| `PartitionFitTests.assert_accounted` | `method` | `Lines 10–14` | `def assert_accounted(self,p,result):` | رمز برمجي موثق. |
| `PartitionFitTests.test_circle_periodic_closed` | `method` | `Lines 16–24` | `def test_circle_periodic_closed(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_square_sharp_corners` | `method` | `Lines 26–30` | `def test_square_sharp_corners(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_long_contour_no_lost_edges` | `method` | `Lines 32–37` | `def test_long_contour_no_lost_edges(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_open_junction_endpoints_and_same_conditions` | `method` | `Lines 39–42` | `def test_open_junction_endpoints_and_same_conditions(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_nested_loop_winding` | `method` | `Lines 44–47` | `def test_nested_loop_winding(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_budget_rejection_is_explicit` | `method` | `Lines 49–53` | `def test_budget_rejection_is_explicit(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_deadline_ledger` | `method` | `Lines 55–58` | `def test_deadline_ledger(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_short_trace_and_duplicate_explicit` | `method` | `Lines 60–62` | `def test_short_trace_and_duplicate_explicit(self):` | رمز برمجي موثق. |
| `PartitionFitTests.test_two_source_junction_traces_keep_same_endpoint` | `method` | `Lines 64–67` | `def test_two_source_junction_traces_keep_same_endpoint(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PartitionFitTests` — `Lines 9–67`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `67` (`Lines 9–67`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–67`):**
```python
class PartitionFitTests(unittest.TestCase):
    def assert_accounted(self,p,result):
        self.assertAlmostEqual(result['accepted_length_px']+result['rejected_length_px'],np.linalg.norm(np.diff(p,axis=0),axis=1).sum(),places=8)
        edges=[]
        for row in result['ledger']:edges.extend(range(row['lo'],row['hi']))
        self.assertEqual(edges,list(range(len(p)-1)))

    def test_circle_periodic_closed(self):
        t=np.linspace(0,2*np.pi,181);p=np.column_stack([20*np.cos(t),20*np.sin(t)]);p[-1]=p[0]
        q=construct(p,'Q');self.assert_accounted(p,q)
        self.assertTrue(q['closed_retained']);self.assertEqual(len(q['chains']),1)
        c=np.array(q['chains'][0]['curves']);self.assertTrue(np.array_equal(c[0,0],c[-1,3]))
        self.assertGreater(signed_area(flattened(c))*signed_area(p),0)
        for left,right in zip(c,np.concatenate([c[1:],c[:1]])):
            a=left[3]-left[2];b=right[1]-right[0]
            if np.linalg.norm(a)*np.linalg.norm(b)>1e-9:self.assertLess(abs(np.cross(a,b))/(np.linalg.norm(a)*np.linalg.norm(b)),1e-6)

    def test_square_sharp_corners(self):
        p=np.array([[0.,0.],[20,0],[20,20],[0,20],[0,0]])
        q=construct(p,'Q');self.assert_accounted(p,q);self.assertTrue(q['closed_retained'])
        c=np.array(q['chains'][0]['curves']);self.assertEqual(len(c),4)
        for v in p[:-1]:self.assertTrue(any(np.array_equal(v,a) for a in c[:,0]))

    def test_long_contour_no_lost_edges(self):
        x=np.linspace(0,300,601);p=np.column_stack([x,3*np.sin(x/35)])
        q=construct(p,'P');self.assert_accounted(p,q)
        self.assertEqual(q['rejected_length_px'],0)
        self.assertGreater(len(q['ledger']),8);self.assertEqual(len(q['chains']),1)
        self.assertTrue(all(r['length_px']<=32.000001 for r in q['ledger']))

    def test_open_junction_endpoints_and_same_conditions(self):
        p=np.array([[3.,4.],[6,4],[8,7],[11,10],[16,10]])
        a=construct(p,'P');b=construct(p,'Q');self.assertEqual(a['chains'],b['chains'])
        c=np.array(a['chains'][0]['curves']);self.assertTrue(np.array_equal(c[0,0],p[0]));self.assertTrue(np.array_equal(c[-1,-1],p[-1]))

    def test_nested_loop_winding(self):
        for radius,orientation in [(20,1),(8,-1)]:
            t=np.linspace(0,orientation*2*np.pi,121);p=np.column_stack([radius*np.cos(t),radius*np.sin(t)]);p[-1]=p[0]
            q=construct(p,'Q');self.assertTrue(q['closed_retained']);self.assertEqual(np.sign(signed_area(flattened(np.array(q['chains'][0]['curves'])))),orientation)

    def test_budget_rejection_is_explicit(self):
        x=np.linspace(0,200,401);p=np.column_stack([x,np.sin(x/25)])
        q=construct(p,'P',maximum_trace_cubics=1);self.assert_accounted(p,q)
        self.assertGreater(q['rejected_length_px'],0)
        self.assertTrue(any(r['reason']=='original_trace_cubic_budget' for r in q['ledger']))

    def test_deadline_ledger(self):
        p=np.column_stack([np.arange(101),np.zeros(101)])
        q=construct(p,'Q',deadline=time.monotonic()-1);self.assert_accounted(p,q)
        self.assertEqual(q['accepted_length_px'],0);self.assertTrue(all(r['reason']=='arm_wall_budget' for r in q['ledger']))

    def test_short_trace_and_duplicate_explicit(self):
        for p,reason in [(np.array([[0.,0.],[1,0]]),'short_chain'),(np.array([[0.,0.],[0,0],[9,0]]),'duplicate_adjacent_points')]:
            q=construct(p);self.assert_accounted(p,q);self.assertEqual(q['reason'],reason)

    def test_two_source_junction_traces_keep_same_endpoint(self):
        paths=[np.array([[0.,0.],[3,0],[8,0]]),np.array([[0.,0.],[0,3],[0,8]])]
        curves=[construct(p)['chains'][0]['curves'] for p in paths]
        self.assertEqual(curves[0][0][0],curves[1][0][0])
```

### `PartitionFitTests.assert_accounted` — `Lines 10–14`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `14` (`Lines 10–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–14`):**
```python
    def assert_accounted(self,p,result):
        self.assertAlmostEqual(result['accepted_length_px']+result['rejected_length_px'],np.linalg.norm(np.diff(p,axis=0),axis=1).sum(),places=8)
        edges=[]
        for row in result['ledger']:edges.extend(range(row['lo'],row['hi']))
        self.assertEqual(edges,list(range(len(p)-1)))
```

### `PartitionFitTests.test_circle_periodic_closed` — `Lines 16–24`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `24` (`Lines 16–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–24`):**
```python
    def test_circle_periodic_closed(self):
        t=np.linspace(0,2*np.pi,181);p=np.column_stack([20*np.cos(t),20*np.sin(t)]);p[-1]=p[0]
        q=construct(p,'Q');self.assert_accounted(p,q)
        self.assertTrue(q['closed_retained']);self.assertEqual(len(q['chains']),1)
        c=np.array(q['chains'][0]['curves']);self.assertTrue(np.array_equal(c[0,0],c[-1,3]))
        self.assertGreater(signed_area(flattened(c))*signed_area(p),0)
        for left,right in zip(c,np.concatenate([c[1:],c[:1]])):
            a=left[3]-left[2];b=right[1]-right[0]
            if np.linalg.norm(a)*np.linalg.norm(b)>1e-9:self.assertLess(abs(np.cross(a,b))/(np.linalg.norm(a)*np.linalg.norm(b)),1e-6)
```

### `PartitionFitTests.test_square_sharp_corners` — `Lines 26–30`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `30` (`Lines 26–30`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–30`):**
```python
    def test_square_sharp_corners(self):
        p=np.array([[0.,0.],[20,0],[20,20],[0,20],[0,0]])
        q=construct(p,'Q');self.assert_accounted(p,q);self.assertTrue(q['closed_retained'])
        c=np.array(q['chains'][0]['curves']);self.assertEqual(len(c),4)
        for v in p[:-1]:self.assertTrue(any(np.array_equal(v,a) for a in c[:,0]))
```

### `PartitionFitTests.test_long_contour_no_lost_edges` — `Lines 32–37`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `37` (`Lines 32–37`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–37`):**
```python
    def test_long_contour_no_lost_edges(self):
        x=np.linspace(0,300,601);p=np.column_stack([x,3*np.sin(x/35)])
        q=construct(p,'P');self.assert_accounted(p,q)
        self.assertEqual(q['rejected_length_px'],0)
        self.assertGreater(len(q['ledger']),8);self.assertEqual(len(q['chains']),1)
        self.assertTrue(all(r['length_px']<=32.000001 for r in q['ledger']))
```

### `PartitionFitTests.test_open_junction_endpoints_and_same_conditions` — `Lines 39–42`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `42` (`Lines 39–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–42`):**
```python
    def test_open_junction_endpoints_and_same_conditions(self):
        p=np.array([[3.,4.],[6,4],[8,7],[11,10],[16,10]])
        a=construct(p,'P');b=construct(p,'Q');self.assertEqual(a['chains'],b['chains'])
        c=np.array(a['chains'][0]['curves']);self.assertTrue(np.array_equal(c[0,0],p[0]));self.assertTrue(np.array_equal(c[-1,-1],p[-1]))
```

### `PartitionFitTests.test_nested_loop_winding` — `Lines 44–47`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `47` (`Lines 44–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–47`):**
```python
    def test_nested_loop_winding(self):
        for radius,orientation in [(20,1),(8,-1)]:
            t=np.linspace(0,orientation*2*np.pi,121);p=np.column_stack([radius*np.cos(t),radius*np.sin(t)]);p[-1]=p[0]
            q=construct(p,'Q');self.assertTrue(q['closed_retained']);self.assertEqual(np.sign(signed_area(flattened(np.array(q['chains'][0]['curves'])))),orientation)
```

### `PartitionFitTests.test_budget_rejection_is_explicit` — `Lines 49–53`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `53` (`Lines 49–53`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–53`):**
```python
    def test_budget_rejection_is_explicit(self):
        x=np.linspace(0,200,401);p=np.column_stack([x,np.sin(x/25)])
        q=construct(p,'P',maximum_trace_cubics=1);self.assert_accounted(p,q)
        self.assertGreater(q['rejected_length_px'],0)
        self.assertTrue(any(r['reason']=='original_trace_cubic_budget' for r in q['ledger']))
```

### `PartitionFitTests.test_deadline_ledger` — `Lines 55–58`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `55` إلى السطر `58` (`Lines 55–58`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 55–58`):**
```python
    def test_deadline_ledger(self):
        p=np.column_stack([np.arange(101),np.zeros(101)])
        q=construct(p,'Q',deadline=time.monotonic()-1);self.assert_accounted(p,q)
        self.assertEqual(q['accepted_length_px'],0);self.assertTrue(all(r['reason']=='arm_wall_budget' for r in q['ledger']))
```

### `PartitionFitTests.test_short_trace_and_duplicate_explicit` — `Lines 60–62`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `60` إلى السطر `62` (`Lines 60–62`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 60–62`):**
```python
    def test_short_trace_and_duplicate_explicit(self):
        for p,reason in [(np.array([[0.,0.],[1,0]]),'short_chain'),(np.array([[0.,0.],[0,0],[9,0]]),'duplicate_adjacent_points')]:
            q=construct(p);self.assert_accounted(p,q);self.assertEqual(q['reason'],reason)
```

### `PartitionFitTests.test_two_source_junction_traces_keep_same_endpoint` — `Lines 64–67`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `64` إلى السطر `67` (`Lines 64–67`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 64–67`):**
```python
    def test_two_source_junction_traces_keep_same_endpoint(self):
        paths=[np.array([[0.,0.],[3,0],[8,0]]),np.array([[0.,0.],[0,3],[0,8]])]
        curves=[construct(p)['chains'][0]['curves'] for p in paths]
        self.assertEqual(curves[0][0][0],curves[1][0][0])
```
