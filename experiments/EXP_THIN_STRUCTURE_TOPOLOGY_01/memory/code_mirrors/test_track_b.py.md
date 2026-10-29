# مرآة الكود التفصيلية: `test_track_b.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_track_b.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_track_b.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `67` (`Lines 1–67`)
- **بصمة الملف (`SHA-256`):** `541ac3664ace6d59cd2825f9414a8c176047dff2ab84fd012a186c3684619832`
- **الوصف التفصيلي:** # START CHANGE AGD-THIN-TRACK-B-TEST | 2026-10-29T11:31:15Z | EDITED | Author: /root/appearance_fit

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `_line` | `function` | `Lines 6–6` | `def _line(a,b):return {'type':'L','p0':list(a),'p3':list(b)}` | رمز برمجي موثق. |
| `_chain` | `function` | `Lines 7–9` | `def _chain(key,points,labels,collapsed=False,closed=False):` | رمز برمجي موثق. |
| `_hole_graph` | `function` | `Lines 11–17` | `def _hole_graph():` | رمز برمجي موثق. |
| `GuardTests` | `class` | `Lines 19–64` | `class GuardTests(unittest.TestCase):` | رمز برمجي موثق. |
| `GuardTests.test_short_l_area_and_hole_preserved_without_grid_fallback` | `method` | `Lines 20–33` | `def test_short_l_area_and_hole_preserved_without_grid_fallback(self):` | رمز برمجي موثق. |
| `GuardTests.test_shared_t_junction_endpoints_and_reversed_references_unchanged` | `method` | `Lines 35–47` | `def test_shared_t_junction_endpoints_and_reversed_references_unchanged(self):` | رمز برمجي موثق. |
| `GuardTests.test_new_collision_is_rejected_and_original_retained` | `method` | `Lines 49–55` | `def test_new_collision_is_rejected_and_original_retained(self):` | رمز برمجي موثق. |
| `GuardTests.test_nonunit_shape_is_not_repaired_by_grid_outline` | `method` | `Lines 57–64` | `def test_nonunit_shape_is_not_repaired_by_grid_outline(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `_line` — `Lines 6–6`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `6` (`Lines 6–6`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–6`):**
```python
def _line(a,b):return {'type':'L','p0':list(a),'p3':list(b)}
```

### `_chain` — `Lines 7–9`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `9` (`Lines 7–9`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–9`):**
```python
def _chain(key,points,labels,collapsed=False,closed=False):
    return {'id':key,'adjacent_face_labels':labels,'pixel_crack_vertices':points,'closed':closed,
      'segments':[_line(points[0],points[-1])] if collapsed else [_line(a,b) for a,b in zip(points,points[1:])]}
```

### `_hole_graph` — `Lines 11–17`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `17` (`Lines 11–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–17`):**
```python
def _hole_graph():
    frame=[[0,0],[10,0],[10,10],[0,10],[0,0]];a=[4,4];c=[5,5]
    return {'width':10,'height':10,'chains':[_chain(0,frame,[1,0],closed=True),
      _chain(1,[a,[5,4],c],[2,1],True),_chain(2,[a,[4,5],c],[1,2],True)],
      'faces':{'1':[[{'chain':0,'forward':True}],[{'chain':2,'forward':True},{'chain':1,'forward':False}]],
               '2':[[{'chain':1,'forward':True},{'chain':2,'forward':False}]]},
      'incidence':[{'xy':a,'degree':2},{'xy':c,'degree':2}]}
```

### `GuardTests` — `Lines 19–64`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `64` (`Lines 19–64`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–64`):**
```python
class GuardTests(unittest.TestCase):
    def test_short_l_area_and_hole_preserved_without_grid_fallback(self):
        graph=_hole_graph();original=copy.deepcopy(graph);candidate,audit=initialize_safe(graph)
        self.assertEqual(graph,original);self.assertEqual(audit['accepted_chains'],[1,2])
        self.assertFalse(audit['unrepaired_collapses']);self.assertEqual(candidate['faces'],graph['faces'])
        self.assertEqual(candidate['incidence'],graph['incidence'])
        for chain in candidate['chains'][1:]:
            self.assertEqual(len(chain['segments']),1);self.assertEqual(chain['segments'][0]['type'],'C')
            self.assertEqual(chain['segments'][0]['p1'],chain['pixel_crack_vertices'][1])
            self.assertEqual(chain['segments'][0]['p2'],chain['pixel_crack_vertices'][1])
            self.assertEqual(chain['segments'][0]['p0'],chain['pixel_crack_vertices'][0])
            self.assertEqual(chain['segments'][0]['p3'],chain['pixel_crack_vertices'][-1])
        utilities,area=_utilities();rings,_=_ring_records(candidate,utilities,area)
        self.assertTrue(rings[('1',0)]['poly'].contains(rings[('1',1)]['poly']))
        self.assertGreater(rings[('2',0)]['area'],.1)

    def test_shared_t_junction_endpoints_and_reversed_references_unchanged(self):
        a=[4,4];c=[5,5];origin=[0,0];end=[10,10]
        graph={'width':10,'height':10,'chains':[
          _chain(0,[origin,[10,0],end],[1,0]),_chain(1,[a,[5,4],c],[2,1],True),
          _chain(2,[a,[4,5],c],[3,2],True),_chain(3,[origin,[0,10],end],[0,3]),
          _chain(4,[origin,a],[3,1]),_chain(5,[c,end],[3,1])],
          'faces':{'1':[[{'chain':0,'forward':True},{'chain':5,'forward':False},{'chain':1,'forward':False},{'chain':4,'forward':False}]],
                   '2':[[{'chain':1,'forward':True},{'chain':2,'forward':False}]],
                   '3':[[{'chain':4,'forward':True},{'chain':2,'forward':True},{'chain':5,'forward':True},{'chain':3,'forward':False}]]},
          'incidence':[{'xy':a,'degree':3},{'xy':c,'degree':3}]}
        candidate,audit=initialize_safe(graph)
        self.assertEqual(audit['accepted_chains'],[1,2]);self.assertEqual(candidate['faces'],graph['faces'])
        for key in (0,3,4,5):self.assertEqual(candidate['chains'][key],graph['chains'][key])

    def test_new_collision_is_rejected_and_original_retained(self):
        graph=_hole_graph()
        graph['chains'].append(_chain(3,[[4.7,4.125],[5,4.125]],[4,0]))
        candidate,audit=initialize_safe(graph)
        self.assertEqual(candidate,graph);self.assertFalse(audit['accepted_chains'])
        self.assertTrue(any('new_crossing'==reason['code'] for event in audit['events'] for reason in event['rejections']))
        self.assertTrue(audit['unrepaired_collapses'])

    def test_nonunit_shape_is_not_repaired_by_grid_outline(self):
        graph=_hole_graph()
        for chain in graph['chains'][1:]:
            chain['pixel_crack_vertices']=[[x*2,y*2] for x,y in chain['pixel_crack_vertices']]
            chain['segments']=[_line(chain['pixel_crack_vertices'][0],chain['pixel_crack_vertices'][-1])]
        candidate,audit=initialize_safe(graph)
        self.assertEqual(candidate,graph);self.assertEqual(audit['eligible_chains'],[])
        self.assertTrue(audit['unrepaired_collapses'])
```

### `GuardTests.test_short_l_area_and_hole_preserved_without_grid_fallback` — `Lines 20–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `33` (`Lines 20–33`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–33`):**
```python
    def test_short_l_area_and_hole_preserved_without_grid_fallback(self):
        graph=_hole_graph();original=copy.deepcopy(graph);candidate,audit=initialize_safe(graph)
        self.assertEqual(graph,original);self.assertEqual(audit['accepted_chains'],[1,2])
        self.assertFalse(audit['unrepaired_collapses']);self.assertEqual(candidate['faces'],graph['faces'])
        self.assertEqual(candidate['incidence'],graph['incidence'])
        for chain in candidate['chains'][1:]:
            self.assertEqual(len(chain['segments']),1);self.assertEqual(chain['segments'][0]['type'],'C')
            self.assertEqual(chain['segments'][0]['p1'],chain['pixel_crack_vertices'][1])
            self.assertEqual(chain['segments'][0]['p2'],chain['pixel_crack_vertices'][1])
            self.assertEqual(chain['segments'][0]['p0'],chain['pixel_crack_vertices'][0])
            self.assertEqual(chain['segments'][0]['p3'],chain['pixel_crack_vertices'][-1])
        utilities,area=_utilities();rings,_=_ring_records(candidate,utilities,area)
        self.assertTrue(rings[('1',0)]['poly'].contains(rings[('1',1)]['poly']))
        self.assertGreater(rings[('2',0)]['area'],.1)
```

### `GuardTests.test_shared_t_junction_endpoints_and_reversed_references_unchanged` — `Lines 35–47`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `47` (`Lines 35–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 35–47`):**
```python
    def test_shared_t_junction_endpoints_and_reversed_references_unchanged(self):
        a=[4,4];c=[5,5];origin=[0,0];end=[10,10]
        graph={'width':10,'height':10,'chains':[
          _chain(0,[origin,[10,0],end],[1,0]),_chain(1,[a,[5,4],c],[2,1],True),
          _chain(2,[a,[4,5],c],[3,2],True),_chain(3,[origin,[0,10],end],[0,3]),
          _chain(4,[origin,a],[3,1]),_chain(5,[c,end],[3,1])],
          'faces':{'1':[[{'chain':0,'forward':True},{'chain':5,'forward':False},{'chain':1,'forward':False},{'chain':4,'forward':False}]],
                   '2':[[{'chain':1,'forward':True},{'chain':2,'forward':False}]],
                   '3':[[{'chain':4,'forward':True},{'chain':2,'forward':True},{'chain':5,'forward':True},{'chain':3,'forward':False}]]},
          'incidence':[{'xy':a,'degree':3},{'xy':c,'degree':3}]}
        candidate,audit=initialize_safe(graph)
        self.assertEqual(audit['accepted_chains'],[1,2]);self.assertEqual(candidate['faces'],graph['faces'])
        for key in (0,3,4,5):self.assertEqual(candidate['chains'][key],graph['chains'][key])
```

### `GuardTests.test_new_collision_is_rejected_and_original_retained` — `Lines 49–55`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `55` (`Lines 49–55`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–55`):**
```python
    def test_new_collision_is_rejected_and_original_retained(self):
        graph=_hole_graph()
        graph['chains'].append(_chain(3,[[4.7,4.125],[5,4.125]],[4,0]))
        candidate,audit=initialize_safe(graph)
        self.assertEqual(candidate,graph);self.assertFalse(audit['accepted_chains'])
        self.assertTrue(any('new_crossing'==reason['code'] for event in audit['events'] for reason in event['rejections']))
        self.assertTrue(audit['unrepaired_collapses'])
```

### `GuardTests.test_nonunit_shape_is_not_repaired_by_grid_outline` — `Lines 57–64`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `64` (`Lines 57–64`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–64`):**
```python
    def test_nonunit_shape_is_not_repaired_by_grid_outline(self):
        graph=_hole_graph()
        for chain in graph['chains'][1:]:
            chain['pixel_crack_vertices']=[[x*2,y*2] for x,y in chain['pixel_crack_vertices']]
            chain['segments']=[_line(chain['pixel_crack_vertices'][0],chain['pixel_crack_vertices'][-1])]
        candidate,audit=initialize_safe(graph)
        self.assertEqual(candidate,graph);self.assertEqual(audit['eligible_chains'],[])
        self.assertTrue(audit['unrepaired_collapses'])
```
