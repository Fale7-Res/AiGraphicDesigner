# مرآة الكود التفصيلية: `test_region_integration.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_region_integration.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_region_integration.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `114` (`Lines 1–114`)
- **بصمة الملف (`SHA-256`):** `5e38babadb18d6efe6e1f55c61b32de06137c327b48c74cc130defbb527fb58d`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-REGION-R | 2026-10-31T11:07:29Z | EDITED | Author: region_integration

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `line` | `function` | `Lines 15–17` | `def line(a,b):` | رمز برمجي موثق. |
| `path` | `function` | `Lines 20–20` | `def path(points):return {'curves':[line(a,b) for a,b in zip(points,points[1:])]}` | رمز برمجي موثق. |
| `square` | `function` | `Lines 23–23` | `def square(x,y,s):return path([(x,y),(x+s,y),(x+s,y+s),(x,y+s),(x,y)])` | رمز برمجي موثق. |
| `RegionTests` | `class` | `Lines 26–111` | `class RegionTests(unittest.TestCase):` | رمز برمجي موثق. |
| `RegionTests.run_case` | `method` | `Lines 27–32` | `def run_case(self,items):` | رمز برمجي موثق. |
| `RegionTests.test_single_square_closed` | `method` | `Lines 34–37` | `def test_single_square_closed(self):` | رمز برمجي موثق. |
| `RegionTests.test_open_stroke_preserved` | `method` | `Lines 39–42` | `def test_open_stroke_preserved(self):` | رمز برمجي موثق. |
| `RegionTests.test_shared_junction_square` | `method` | `Lines 44–49` | `def test_shared_junction_square(self):` | رمز برمجي موثق. |
| `RegionTests.test_hole_and_interior_island_all_atomic` | `method` | `Lines 51–56` | `def test_hole_and_interior_island_all_atomic(self):` | رمز برمجي موثق. |
| `RegionTests.test_dangling_t_no_invented_region` | `method` | `Lines 58–60` | `def test_dangling_t_no_invented_region(self):` | رمز برمجي موثق. |
| `RegionTests.test_crossing_rejected_not_deleted` | `method` | `Lines 62–65` | `def test_crossing_rejected_not_deleted(self):` | رمز برمجي موثق. |
| `RegionTests.test_tangent_ambiguity_rejected` | `method` | `Lines 67–69` | `def test_tangent_ambiguity_rejected(self):` | رمز برمجي موثق. |
| `RegionTests.test_exact_no_snapping` | `method` | `Lines 71–73` | `def test_exact_no_snapping(self):` | رمز برمجي موثق. |
| `RegionTests.test_numerical_selfintersection_rejected` | `method` | `Lines 75–77` | `def test_numerical_selfintersection_rejected(self):` | رمز برمجي موثق. |
| `RegionTests.test_curved_loop_exact_cubics` | `method` | `Lines 79–85` | `def test_curved_loop_exact_cubics(self):` | رمز برمجي موثق. |
| `RegionTests.test_collinear_overshoot_not_flattened_to_chord` | `method` | `Lines 87–95` | `def test_collinear_overshoot_not_flattened_to_chord(self):` | رمز برمجي موثق. |
| `RegionTests.test_real_resvg_nested_atomic_faces_1_4_16` | `method` | `Lines 97–111` | `def test_real_resvg_nested_atomic_faces_1_4_16(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `line` — `Lines 15–17`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `17` (`Lines 15–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–17`):**
```python
def line(a,b):
    a=np.array(a,float);b=np.array(b,float)
    return [a.tolist(),(a+(b-a)/3).tolist(),(a+2*(b-a)/3).tolist(),b.tolist()]
```

### `path` — `Lines 20–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `20` (`Lines 20–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–20`):**
```python
def path(points):return {'curves':[line(a,b) for a,b in zip(points,points[1:])]}
```

### `square` — `Lines 23–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `23` (`Lines 23–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–23`):**
```python
def square(x,y,s):return path([(x,y),(x+s,y),(x+s,y+s),(x,y+s),(x,y)])
```

### `RegionTests` — `Lines 26–111`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `111` (`Lines 26–111`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–111`):**
```python
class RegionTests(unittest.TestCase):
    def run_case(self,items):
        before=copy.deepcopy(items);g,a=integrate(items,32,32,np.full((32,32,3),255,np.uint8))
        self.assertEqual(before,items)
        svg=svg_graph(g,regions=True);self.assertNotIn('<image',svg)
        self.assertEqual(a['integrated_paths']+a['preserved_unintegrated_paths'],len(items))
        return g,a

    def test_single_square_closed(self):
        g,a=self.run_case([square(2,2,20)])
        self.assertEqual(len(g['faces']),1);self.assertAlmostEqual(a['faces'][0]['area_px2'],400)
        self.assertEqual(a['endpoint_movement_px'],0)

    def test_open_stroke_preserved(self):
        g,a=self.run_case([path([(2,2),(12,5)])])
        self.assertFalse(g['faces']);self.assertEqual(len(g['chains']),1)
        self.assertEqual(a['unintegrated'][0]['reasons'],['open_or_dangling_unbounded_stroke'])

    def test_shared_junction_square(self):
        items=[path([(2,2),(12,2)]),path([(12,2),(22,2)]),path([(22,2),(22,22)]),path([(22,22),(12,22)]),path([(12,22),(2,22)]),path([(2,22),(2,2)]),path([(12,2),(12,22)])]
        g,a=self.run_case(items)
        self.assertEqual(len(g['faces']),2)
        self.assertEqual(sorted(g['chains'][6]['adjacent_face_labels']),[1,2])
        self.assertAlmostEqual(sum(x['area_px2'] for x in a['faces']),400)

    def test_hole_and_interior_island_all_atomic(self):
        g,a=self.run_case([square(1,1,28),square(5,5,20),square(10,10,10)])
        self.assertEqual(len(g['faces']),3)
        self.assertEqual(sorted(len(x) for x in g['faces'].values()),[1,2,2])
        self.assertAlmostEqual(sum(x['area_px2'] for x in a['faces']),784)
        self.assertTrue(all(x['semantic_hole']=='NOT_ESTABLISHED' for x in a['faces']))

    def test_dangling_t_no_invented_region(self):
        g,a=self.run_case([path([(2,10),(10,10)]),path([(10,10),(20,10)]),path([(10,10),(10,20)])])
        self.assertFalse(g['faces']);self.assertEqual(len(a['unintegrated']),3)

    def test_crossing_rejected_not_deleted(self):
        g,a=self.run_case([path([(2,2),(20,20)]),path([(2,20),(20,2)])])
        self.assertFalse(g['faces']);self.assertEqual(len(g['chains']),2)
        self.assertTrue(all('crossing_overlap_or_nonendpoint_contact' in r['reasons'] for r in a['rows']))

    def test_tangent_ambiguity_rejected(self):
        g,a=self.run_case([path([(2,2),(10,2)]),path([(2,2),(10,2),(10,10)])])
        self.assertFalse(g['faces']);self.assertTrue(all(r['reasons'] for r in a['rows']))

    def test_exact_no_snapping(self):
        g,a=self.run_case([path([(1,1),(20,1),(20,20),(1,20),(1,1.00001)])])
        self.assertFalse(g['faces']);self.assertEqual(a['endpoint_movement_px'],0)

    def test_numerical_selfintersection_rejected(self):
        g,a=self.run_case([path([(1,1),(20,20),(1,20),(20,1),(1,1)])])
        self.assertFalse(g['faces']);self.assertIn('inherited_or_fitted_selfintersection',a['rows'][0]['reasons'])

    def test_curved_loop_exact_cubics(self):
        k=.5522847498307936;cx=16;cy=16;r=10
        cc=np.array([[[1,0],[1,k],[k,1],[0,1]],[[0,1],[-k,1],[-1,k],[-1,0]],[[-1,0],[-1,-k],[-k,-1],[0,-1]],[[0,-1],[k,-1],[1,-k],[1,0]]])*r+[cx,cy]
        g,a=self.run_case([{'curves':cc.tolist()}])
        self.assertEqual(len(g['faces']),1)
        self.assertEqual([s['p1'] for s in g['chains'][0]['segments']],cc[:,1].tolist())
        self.assertAlmostEqual(a['faces'][0]['area_px2'],math.pi*r*r,delta=.2)

    def test_collinear_overshoot_not_flattened_to_chord(self):
        c=np.array([[0,0],[40,0],[-40,0],[1,0]],float)
        p=np.array(_flat(c))
        self.assertGreater(len(p),2)
        self.assertGreater(p[:,0].max(),10)
        self.assertLess(p[:,0].min(),-10)
        g,a=self.run_case([{'curves':[c.tolist()]}])
        self.assertFalse(g['faces'])
        self.assertIn('inherited_or_fitted_selfintersection',a['rows'][0]['reasons'])

    def test_real_resvg_nested_atomic_faces_1_4_16(self):
        from PIL import Image
        renderer=Path.cwd()/'work/resvg/resvg.exe'
        self.assertTrue(renderer.exists())
        g,a=self.run_case([square(1,1,28),square(5,5,20),square(10,10,10)])
        with tempfile.TemporaryDirectory() as tmp:
            svg=Path(tmp)/'atomic.svg';svg.write_text(svg_graph(g,regions=True))
            for scale in (1,4,16):
                png=Path(tmp)/f'{scale}.png'
                subprocess.run([str(renderer),'--zoom',str(scale),str(svg),str(png)],check=True,capture_output=True)
                pixels=np.asarray(Image.open(png).convert('RGBA'))
                self.assertEqual(pixels.shape[:2],(32*scale,32*scale))
                colors=[tuple(pixels[y*scale,x*scale,:3]) for x,y in [(3,3),(7,7),(15,15)]]
                self.assertEqual(len(set(colors)),3)
                self.assertTrue(all(pixels[y*scale,x*scale,3]==255 for x,y in [(3,3),(7,7),(15,15)]))
```

### `RegionTests.run_case` — `Lines 27–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `32` (`Lines 27–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–32`):**
```python
    def run_case(self,items):
        before=copy.deepcopy(items);g,a=integrate(items,32,32,np.full((32,32,3),255,np.uint8))
        self.assertEqual(before,items)
        svg=svg_graph(g,regions=True);self.assertNotIn('<image',svg)
        self.assertEqual(a['integrated_paths']+a['preserved_unintegrated_paths'],len(items))
        return g,a
```

### `RegionTests.test_single_square_closed` — `Lines 34–37`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `37` (`Lines 34–37`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–37`):**
```python
    def test_single_square_closed(self):
        g,a=self.run_case([square(2,2,20)])
        self.assertEqual(len(g['faces']),1);self.assertAlmostEqual(a['faces'][0]['area_px2'],400)
        self.assertEqual(a['endpoint_movement_px'],0)
```

### `RegionTests.test_open_stroke_preserved` — `Lines 39–42`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `42` (`Lines 39–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–42`):**
```python
    def test_open_stroke_preserved(self):
        g,a=self.run_case([path([(2,2),(12,5)])])
        self.assertFalse(g['faces']);self.assertEqual(len(g['chains']),1)
        self.assertEqual(a['unintegrated'][0]['reasons'],['open_or_dangling_unbounded_stroke'])
```

### `RegionTests.test_shared_junction_square` — `Lines 44–49`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `49` (`Lines 44–49`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–49`):**
```python
    def test_shared_junction_square(self):
        items=[path([(2,2),(12,2)]),path([(12,2),(22,2)]),path([(22,2),(22,22)]),path([(22,22),(12,22)]),path([(12,22),(2,22)]),path([(2,22),(2,2)]),path([(12,2),(12,22)])]
        g,a=self.run_case(items)
        self.assertEqual(len(g['faces']),2)
        self.assertEqual(sorted(g['chains'][6]['adjacent_face_labels']),[1,2])
        self.assertAlmostEqual(sum(x['area_px2'] for x in a['faces']),400)
```

### `RegionTests.test_hole_and_interior_island_all_atomic` — `Lines 51–56`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `51` إلى السطر `56` (`Lines 51–56`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 51–56`):**
```python
    def test_hole_and_interior_island_all_atomic(self):
        g,a=self.run_case([square(1,1,28),square(5,5,20),square(10,10,10)])
        self.assertEqual(len(g['faces']),3)
        self.assertEqual(sorted(len(x) for x in g['faces'].values()),[1,2,2])
        self.assertAlmostEqual(sum(x['area_px2'] for x in a['faces']),784)
        self.assertTrue(all(x['semantic_hole']=='NOT_ESTABLISHED' for x in a['faces']))
```

### `RegionTests.test_dangling_t_no_invented_region` — `Lines 58–60`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `60` (`Lines 58–60`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 58–60`):**
```python
    def test_dangling_t_no_invented_region(self):
        g,a=self.run_case([path([(2,10),(10,10)]),path([(10,10),(20,10)]),path([(10,10),(10,20)])])
        self.assertFalse(g['faces']);self.assertEqual(len(a['unintegrated']),3)
```

### `RegionTests.test_crossing_rejected_not_deleted` — `Lines 62–65`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `62` إلى السطر `65` (`Lines 62–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 62–65`):**
```python
    def test_crossing_rejected_not_deleted(self):
        g,a=self.run_case([path([(2,2),(20,20)]),path([(2,20),(20,2)])])
        self.assertFalse(g['faces']);self.assertEqual(len(g['chains']),2)
        self.assertTrue(all('crossing_overlap_or_nonendpoint_contact' in r['reasons'] for r in a['rows']))
```

### `RegionTests.test_tangent_ambiguity_rejected` — `Lines 67–69`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `67` إلى السطر `69` (`Lines 67–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 67–69`):**
```python
    def test_tangent_ambiguity_rejected(self):
        g,a=self.run_case([path([(2,2),(10,2)]),path([(2,2),(10,2),(10,10)])])
        self.assertFalse(g['faces']);self.assertTrue(all(r['reasons'] for r in a['rows']))
```

### `RegionTests.test_exact_no_snapping` — `Lines 71–73`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `71` إلى السطر `73` (`Lines 71–73`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 71–73`):**
```python
    def test_exact_no_snapping(self):
        g,a=self.run_case([path([(1,1),(20,1),(20,20),(1,20),(1,1.00001)])])
        self.assertFalse(g['faces']);self.assertEqual(a['endpoint_movement_px'],0)
```

### `RegionTests.test_numerical_selfintersection_rejected` — `Lines 75–77`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `75` إلى السطر `77` (`Lines 75–77`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 75–77`):**
```python
    def test_numerical_selfintersection_rejected(self):
        g,a=self.run_case([path([(1,1),(20,20),(1,20),(20,1),(1,1)])])
        self.assertFalse(g['faces']);self.assertIn('inherited_or_fitted_selfintersection',a['rows'][0]['reasons'])
```

### `RegionTests.test_curved_loop_exact_cubics` — `Lines 79–85`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `79` إلى السطر `85` (`Lines 79–85`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 79–85`):**
```python
    def test_curved_loop_exact_cubics(self):
        k=.5522847498307936;cx=16;cy=16;r=10
        cc=np.array([[[1,0],[1,k],[k,1],[0,1]],[[0,1],[-k,1],[-1,k],[-1,0]],[[-1,0],[-1,-k],[-k,-1],[0,-1]],[[0,-1],[k,-1],[1,-k],[1,0]]])*r+[cx,cy]
        g,a=self.run_case([{'curves':cc.tolist()}])
        self.assertEqual(len(g['faces']),1)
        self.assertEqual([s['p1'] for s in g['chains'][0]['segments']],cc[:,1].tolist())
        self.assertAlmostEqual(a['faces'][0]['area_px2'],math.pi*r*r,delta=.2)
```

### `RegionTests.test_collinear_overshoot_not_flattened_to_chord` — `Lines 87–95`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `87` إلى السطر `95` (`Lines 87–95`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 87–95`):**
```python
    def test_collinear_overshoot_not_flattened_to_chord(self):
        c=np.array([[0,0],[40,0],[-40,0],[1,0]],float)
        p=np.array(_flat(c))
        self.assertGreater(len(p),2)
        self.assertGreater(p[:,0].max(),10)
        self.assertLess(p[:,0].min(),-10)
        g,a=self.run_case([{'curves':[c.tolist()]}])
        self.assertFalse(g['faces'])
        self.assertIn('inherited_or_fitted_selfintersection',a['rows'][0]['reasons'])
```

### `RegionTests.test_real_resvg_nested_atomic_faces_1_4_16` — `Lines 97–111`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `97` إلى السطر `111` (`Lines 97–111`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 97–111`):**
```python
    def test_real_resvg_nested_atomic_faces_1_4_16(self):
        from PIL import Image
        renderer=Path.cwd()/'work/resvg/resvg.exe'
        self.assertTrue(renderer.exists())
        g,a=self.run_case([square(1,1,28),square(5,5,20),square(10,10,10)])
        with tempfile.TemporaryDirectory() as tmp:
            svg=Path(tmp)/'atomic.svg';svg.write_text(svg_graph(g,regions=True))
            for scale in (1,4,16):
                png=Path(tmp)/f'{scale}.png'
                subprocess.run([str(renderer),'--zoom',str(scale),str(svg),str(png)],check=True,capture_output=True)
                pixels=np.asarray(Image.open(png).convert('RGBA'))
                self.assertEqual(pixels.shape[:2],(32*scale,32*scale))
                colors=[tuple(pixels[y*scale,x*scale,:3]) for x,y in [(3,3),(7,7),(15,15)]]
                self.assertEqual(len(set(colors)),3)
                self.assertTrue(all(pixels[y*scale,x*scale,3]==255 for x,y in [(3,3),(7,7),(15,15)]))
```
