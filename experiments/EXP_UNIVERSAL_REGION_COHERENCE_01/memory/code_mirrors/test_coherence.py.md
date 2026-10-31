# مرآة الكود التفصيلية: `test_coherence.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_coherence.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_coherence.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `64` (`Lines 1–64`)
- **بصمة الملف (`SHA-256`):** `2597199e426c2f894ba0da835427d5ab74cce11e66053f8f26e5c9a5d213827b`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-COHERENCE-TEST | 2026-10-31T11:07:29Z | EDITED | Author: coherence_control

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `bundle` | `function` | `Lines 15–18` | `def bundle(points,tid=0):` | رمز برمجي موثق. |
| `CoherenceTests` | `class` | `Lines 21–60` | `class CoherenceTests(unittest.TestCase):` | رمز برمجي موثق. |
| `CoherenceTests.assert_anchors` | `method` | `Lines 22–26` | `def assert_anchors(self,before,after):` | رمز برمجي موثق. |
| `CoherenceTests.test_circle` | `method` | `Lines 27–32` | `def test_circle(self):` | رمز برمجي موثق. |
| `CoherenceTests.test_jaggy_staircase` | `method` | `Lines 33–38` | `def test_jaggy_staircase(self):` | رمز برمجي موثق. |
| `CoherenceTests.test_thin_L_corner` | `method` | `Lines 39–43` | `def test_thin_L_corner(self):` | رمز برمجي موثق. |
| `CoherenceTests.test_shared_junction` | `method` | `Lines 44–48` | `def test_shared_junction(self):` | رمز برمجي موثق. |
| `CoherenceTests.test_closed_hole_nesting` | `method` | `Lines 49–54` | `def test_closed_hole_nesting(self):` | رمز برمجي موثق. |
| `CoherenceTests.test_missing_provenance_explicit_rollback` | `method` | `Lines 55–57` | `def test_missing_provenance_explicit_rollback(self):` | رمز برمجي موثق. |
| `CoherenceTests.test_quality_is_separate` | `method` | `Lines 58–60` | `def test_quality_is_separate(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `bundle` — `Lines 15–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `18` (`Lines 15–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–18`):**
```python
def bundle(points,tid=0):
    p=np.asarray(points,float);fit=fit_trace(p,periodic=False)
    assert fit['chains'],fit
    return [dict(c,trace_id=tid) for c in fit['chains']],dict(trace_id=tid,source_points_xy=p.tolist())
```

### `CoherenceTests` — `Lines 21–60`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `60` (`Lines 21–60`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–60`):**
```python
class CoherenceTests(unittest.TestCase):
    def assert_anchors(self,before,after):
        for a,b in zip(before,after):
            ca=np.asarray(a['curves']);cb=np.asarray(b['curves'])
            self.assertTrue(np.array_equal(ca[0,0],cb[0,0]));self.assertTrue(np.array_equal(ca[-1,-1],cb[-1,-1]))
            self.assertEqual(a['closed'],b['closed']);self.assertEqual(a['partition_ids'],b['partition_ids'])
    def test_circle(self):
        t=np.linspace(0,2*np.pi,97);p=np.c_[30+15*np.cos(t),30+15*np.sin(t)];p[-1]=p[0]
        a,s=bundle(p);b,audit=refine(a,[s]);self.assert_anchors(a,b)
        self.assertTrue(np.array_equal(np.asarray(b[0]['curves'])[0,0],np.asarray(b[0]['curves'])[-1,-1]))
        for row in audit['chains']:
            for part in row.get('partitions',[]):self.assertLessEqual(part['deviation']['numerical_upper_envelope_px'],.6)
    def test_jaggy_staircase(self):
        p=[[0.,0.]]
        for k in range(20):p.extend([[k+1.,k+0.],[k+1.,k+1.]])
        a,s=bundle(p);b,audit=refine(a,[s]);self.assert_anchors(a,b)
        self.assertLessEqual(sum(len(x['curves']) for x in b),sum(len(x['curves']) for x in a))
        self.assertEqual(len(audit['chains']),len(a))
    def test_thin_L_corner(self):
        p=np.r_[np.c_[np.arange(0,11),np.zeros(11)],np.c_[np.full(10,10),np.arange(1,11)]]
        a,s=bundle(p);b,_=refine(a,[s]);self.assert_anchors(a,b)
        vertices=np.concatenate([np.asarray(x['curves'])[:,0] for x in b]+[np.asarray(b[-1]['curves'])[-1,-1:]])
        self.assertTrue(np.any(np.all(vertices==[10,0],axis=1)))
    def test_shared_junction(self):
        a,s=bundle([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]])
        c,t=bundle([[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7]],1)
        before=a+c;after,_=refine(before,[s,t]);self.assert_anchors(before,after)
        self.assertTrue(np.array_equal(np.asarray(after[0]['curves'])[-1,-1],np.asarray(after[1]['curves'])[0,0]))
    def test_closed_hole_nesting(self):
        theta=np.linspace(0,2*np.pi,65)
        outer=np.c_[30+20*np.cos(theta),30+20*np.sin(theta)];outer[-1]=outer[0]
        inner=np.c_[30+7*np.cos(-theta),30+7*np.sin(-theta)];inner[-1]=inner[0]
        a,s=bundle(outer);c,t=bundle(inner,1);before=a+c;after,_=refine(before,[s,t]);self.assert_anchors(before,after)
        self.assertTrue(Polygon(polyline(after[0]['curves'])).contains(Polygon(polyline(after[1]['curves']))))
    def test_missing_provenance_explicit_rollback(self):
        a,s=bundle([[k,0] for k in range(10)]);a[0].pop('partition_ids');before=copy.deepcopy(a)
        b,audit=refine(a,[s]);self.assertEqual(b,before);self.assertEqual(audit['chains'][0]['reason'],'missing_partition_provenance')
    def test_quality_is_separate(self):
        a,s=bundle([[k,0] for k in range(10)]);q=curve_quality(a[0]['curves'])
        self.assertIn('sampled_curvature_p95',q);self.assertIn('length_fraction_cubic_span_le2px',q)
```

### `CoherenceTests.assert_anchors` — `Lines 22–26`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `26` (`Lines 22–26`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–26`):**
```python
    def assert_anchors(self,before,after):
        for a,b in zip(before,after):
            ca=np.asarray(a['curves']);cb=np.asarray(b['curves'])
            self.assertTrue(np.array_equal(ca[0,0],cb[0,0]));self.assertTrue(np.array_equal(ca[-1,-1],cb[-1,-1]))
            self.assertEqual(a['closed'],b['closed']);self.assertEqual(a['partition_ids'],b['partition_ids'])
```

### `CoherenceTests.test_circle` — `Lines 27–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `32` (`Lines 27–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–32`):**
```python
    def test_circle(self):
        t=np.linspace(0,2*np.pi,97);p=np.c_[30+15*np.cos(t),30+15*np.sin(t)];p[-1]=p[0]
        a,s=bundle(p);b,audit=refine(a,[s]);self.assert_anchors(a,b)
        self.assertTrue(np.array_equal(np.asarray(b[0]['curves'])[0,0],np.asarray(b[0]['curves'])[-1,-1]))
        for row in audit['chains']:
            for part in row.get('partitions',[]):self.assertLessEqual(part['deviation']['numerical_upper_envelope_px'],.6)
```

### `CoherenceTests.test_jaggy_staircase` — `Lines 33–38`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `33` إلى السطر `38` (`Lines 33–38`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 33–38`):**
```python
    def test_jaggy_staircase(self):
        p=[[0.,0.]]
        for k in range(20):p.extend([[k+1.,k+0.],[k+1.,k+1.]])
        a,s=bundle(p);b,audit=refine(a,[s]);self.assert_anchors(a,b)
        self.assertLessEqual(sum(len(x['curves']) for x in b),sum(len(x['curves']) for x in a))
        self.assertEqual(len(audit['chains']),len(a))
```

### `CoherenceTests.test_thin_L_corner` — `Lines 39–43`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `43` (`Lines 39–43`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–43`):**
```python
    def test_thin_L_corner(self):
        p=np.r_[np.c_[np.arange(0,11),np.zeros(11)],np.c_[np.full(10,10),np.arange(1,11)]]
        a,s=bundle(p);b,_=refine(a,[s]);self.assert_anchors(a,b)
        vertices=np.concatenate([np.asarray(x['curves'])[:,0] for x in b]+[np.asarray(b[-1]['curves'])[-1,-1:]])
        self.assertTrue(np.any(np.all(vertices==[10,0],axis=1)))
```

### `CoherenceTests.test_shared_junction` — `Lines 44–48`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `48` (`Lines 44–48`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–48`):**
```python
    def test_shared_junction(self):
        a,s=bundle([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]])
        c,t=bundle([[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7]],1)
        before=a+c;after,_=refine(before,[s,t]);self.assert_anchors(before,after)
        self.assertTrue(np.array_equal(np.asarray(after[0]['curves'])[-1,-1],np.asarray(after[1]['curves'])[0,0]))
```

### `CoherenceTests.test_closed_hole_nesting` — `Lines 49–54`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `54` (`Lines 49–54`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–54`):**
```python
    def test_closed_hole_nesting(self):
        theta=np.linspace(0,2*np.pi,65)
        outer=np.c_[30+20*np.cos(theta),30+20*np.sin(theta)];outer[-1]=outer[0]
        inner=np.c_[30+7*np.cos(-theta),30+7*np.sin(-theta)];inner[-1]=inner[0]
        a,s=bundle(outer);c,t=bundle(inner,1);before=a+c;after,_=refine(before,[s,t]);self.assert_anchors(before,after)
        self.assertTrue(Polygon(polyline(after[0]['curves'])).contains(Polygon(polyline(after[1]['curves']))))
```

### `CoherenceTests.test_missing_provenance_explicit_rollback` — `Lines 55–57`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `55` إلى السطر `57` (`Lines 55–57`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 55–57`):**
```python
    def test_missing_provenance_explicit_rollback(self):
        a,s=bundle([[k,0] for k in range(10)]);a[0].pop('partition_ids');before=copy.deepcopy(a)
        b,audit=refine(a,[s]);self.assertEqual(b,before);self.assertEqual(audit['chains'][0]['reason'],'missing_partition_provenance')
```

### `CoherenceTests.test_quality_is_separate` — `Lines 58–60`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `60` (`Lines 58–60`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 58–60`):**
```python
    def test_quality_is_separate(self):
        a,s=bundle([[k,0] for k in range(10)]);q=curve_quality(a[0]['curves'])
        self.assertIn('sampled_curvature_p95',q);self.assertIn('length_fraction_cubic_span_le2px',q)
```
