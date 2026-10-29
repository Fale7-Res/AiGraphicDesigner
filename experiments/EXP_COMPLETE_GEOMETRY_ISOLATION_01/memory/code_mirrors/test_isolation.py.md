# مرآة الكود التفصيلية: `test_isolation.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_isolation.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_isolation.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `69` (`Lines 1–69`)
- **بصمة الملف (`SHA-256`):** `5b6975bd375e1c7cf43a74b9e161b8e28229184013649f4bd393395177b1a33e`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-TEST-ISOLATION | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `GeometryIsolationTests` | `class` | `Lines 7–65` | `class GeometryIsolationTests(unittest.TestCase):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_cubic_flattening_analytic_parabola` | `method` | `Lines 8–13` | `def test_cubic_flattening_analytic_parabola(self):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_ring_area_detects_collapsed_cell` | `method` | `Lines 15–17` | `def test_ring_area_detects_collapsed_cell(self):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_distance_is_symmetric_and_exposes_missing_detail` | `method` | `Lines 19–23` | `def test_distance_is_symmetric_and_exposes_missing_detail(self):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_svg_preserves_shared_reversal_hole` | `method` | `Lines 25–43` | `def test_svg_preserves_shared_reversal_hole(self):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_common_face_mapping_rejects_changed_boundaries` | `method` | `Lines 45–52` | `def test_common_face_mapping_rejects_changed_boundaries(self):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_only_closed_rings_gain_svg_closure` | `method` | `Lines 54–58` | `def test_only_closed_rings_gain_svg_closure(self):` | رمز برمجي موثق. |
| `GeometryIsolationTests.test_protocol_prevents_truth_selection` | `method` | `Lines 60–65` | `def test_protocol_prevents_truth_selection(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `GeometryIsolationTests` — `Lines 7–65`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `65` (`Lines 7–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–65`):**
```python
class GeometryIsolationTests(unittest.TestCase):
    def test_cubic_flattening_analytic_parabola(self):
        # Quadratic x=t,y=tÂ² elevated to cubic, analytic distance check.
        p=np.array([[0,0],[1/3,0],[2/3,1/3],[1,1]],float)
        from shapely.geometry import LineString,Point
        line=LineString(flatten_cubic(p,epsilon=.001))
        self.assertLessEqual(max(line.distance(Point(t,t*t)) for t in np.linspace(0,1,501)),.00101)

    def test_ring_area_detects_collapsed_cell(self):
        self.assertEqual(signed_area([[0,0],[1,0],[1,1],[0,1],[0,0]]),1.)
        self.assertEqual(signed_area([[0,0],[1,1],[0,0]]),0.)

    def test_distance_is_symmetric_and_exposes_missing_detail(self):
        a=np.array([[0,0],[1,0],[10,0]],float);b=a[:2]
        r=compare_samples(a,b)
        self.assertEqual(r['a_recall_at_1px'],2/3)
        self.assertGreater(r['symmetric_p95_px'],1)

    def test_svg_preserves_shared_reversal_hole(self):
        graph={'width':4,'height':4,'chains':[],'faces':{'1':[[{'chain':0,'forward':True}],[{'chain':1,'forward':False}]],'2':[[{'chain':1,'forward':True}]]}}
        for i,p in enumerate([[[0,0],[4,0],[4,4],[0,4],[0,0]],[[1,1],[3,1],[3,3],[1,3],[1,1]]]):
            graph['chains'].append({'id':i,'closed':True,'adjacent_face_labels':[0,1] if i==0 else [1,2],
              'pixel_crack_vertices':p,'segments':[{'type':'L','p0':a,'p3':b} for a,b in zip(p,p[1:])]})
        from xml.etree import ElementTree as ET
        xml=ET.fromstring(svg_graph(graph,regions=True,foreground={1}))
        path=next(iter(xml));self.assertEqual(path.attrib['fill-rule'],'evenodd')
        self.assertNotIn('image',ET.tostring(xml).decode())
        self.assertEqual(path.attrib['d'].count('M'),2)
        import subprocess,tempfile
        from pathlib import Path
        from isolation import WORK
        from PIL import Image
        with tempfile.TemporaryDirectory(dir=WORK) as folder:
            src=Path(folder)/'hole.svg';png=src.with_suffix('.png');src.write_text(ET.tostring(xml,encoding='unicode'))
            subprocess.run([str(WORK/'resvg/resvg.exe'),str(src),str(png)],check=True,capture_output=True)
            alpha=np.asarray(Image.open(png).convert('RGBA'))[...,3]
            self.assertEqual(alpha[1,1],0);self.assertEqual(alpha[0,0],255)

    def test_common_face_mapping_rejects_changed_boundaries(self):
        from common_geometry import normalize_to_common_faces
        a={'chains':[{'id':0,'adjacent_face_labels':[1,2],'pixel_crack_vertices':[[0,0],[1,0]],'segments':[]}]}
        b={'chains':[{'id':9,'adjacent_face_labels':[1,2],'pixel_crack_vertices':[[1,0],[0,0]],'segments':[]}]}
        result=normalize_to_common_faces(a,b)
        self.assertTrue(result['normalization']['chain_mapping'][0]['reversed'])
        b['chains'][0]['pixel_crack_vertices']=[[1,1],[0,0]]
        with self.assertRaises(KeyError):normalize_to_common_faces(a,b)

    def test_only_closed_rings_gain_svg_closure(self):
        from geometry_eval import chain_points
        ch={'closed':False,'segments':[{'type':'L','p0':[0,0],'p3':[1,1]}]}
        self.assertEqual(len(chain_points(ch)),2)
        ch['closed']=True;self.assertEqual(len(chain_points(ch)),3)

    def test_protocol_prevents_truth_selection(self):
        from pathlib import Path
        p=json.loads((Path(__file__).parent/'protocol.json').read_text())
        self.assertIn('No candidate',p['policy']['truth_selection'])
        self.assertEqual(p['architecture'],'NOT_APPROVED')
        self.assertEqual(p['budgets']['combinations_max_per_case'],4)
```

### `GeometryIsolationTests.test_cubic_flattening_analytic_parabola` — `Lines 8–13`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `13` (`Lines 8–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–13`):**
```python
    def test_cubic_flattening_analytic_parabola(self):
        # Quadratic x=t,y=tÂ² elevated to cubic, analytic distance check.
        p=np.array([[0,0],[1/3,0],[2/3,1/3],[1,1]],float)
        from shapely.geometry import LineString,Point
        line=LineString(flatten_cubic(p,epsilon=.001))
        self.assertLessEqual(max(line.distance(Point(t,t*t)) for t in np.linspace(0,1,501)),.00101)
```

### `GeometryIsolationTests.test_ring_area_detects_collapsed_cell` — `Lines 15–17`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `17` (`Lines 15–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–17`):**
```python
    def test_ring_area_detects_collapsed_cell(self):
        self.assertEqual(signed_area([[0,0],[1,0],[1,1],[0,1],[0,0]]),1.)
        self.assertEqual(signed_area([[0,0],[1,1],[0,0]]),0.)
```

### `GeometryIsolationTests.test_distance_is_symmetric_and_exposes_missing_detail` — `Lines 19–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `23` (`Lines 19–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–23`):**
```python
    def test_distance_is_symmetric_and_exposes_missing_detail(self):
        a=np.array([[0,0],[1,0],[10,0]],float);b=a[:2]
        r=compare_samples(a,b)
        self.assertEqual(r['a_recall_at_1px'],2/3)
        self.assertGreater(r['symmetric_p95_px'],1)
```

### `GeometryIsolationTests.test_svg_preserves_shared_reversal_hole` — `Lines 25–43`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `43` (`Lines 25–43`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–43`):**
```python
    def test_svg_preserves_shared_reversal_hole(self):
        graph={'width':4,'height':4,'chains':[],'faces':{'1':[[{'chain':0,'forward':True}],[{'chain':1,'forward':False}]],'2':[[{'chain':1,'forward':True}]]}}
        for i,p in enumerate([[[0,0],[4,0],[4,4],[0,4],[0,0]],[[1,1],[3,1],[3,3],[1,3],[1,1]]]):
            graph['chains'].append({'id':i,'closed':True,'adjacent_face_labels':[0,1] if i==0 else [1,2],
              'pixel_crack_vertices':p,'segments':[{'type':'L','p0':a,'p3':b} for a,b in zip(p,p[1:])]})
        from xml.etree import ElementTree as ET
        xml=ET.fromstring(svg_graph(graph,regions=True,foreground={1}))
        path=next(iter(xml));self.assertEqual(path.attrib['fill-rule'],'evenodd')
        self.assertNotIn('image',ET.tostring(xml).decode())
        self.assertEqual(path.attrib['d'].count('M'),2)
        import subprocess,tempfile
        from pathlib import Path
        from isolation import WORK
        from PIL import Image
        with tempfile.TemporaryDirectory(dir=WORK) as folder:
            src=Path(folder)/'hole.svg';png=src.with_suffix('.png');src.write_text(ET.tostring(xml,encoding='unicode'))
            subprocess.run([str(WORK/'resvg/resvg.exe'),str(src),str(png)],check=True,capture_output=True)
            alpha=np.asarray(Image.open(png).convert('RGBA'))[...,3]
            self.assertEqual(alpha[1,1],0);self.assertEqual(alpha[0,0],255)
```

### `GeometryIsolationTests.test_common_face_mapping_rejects_changed_boundaries` — `Lines 45–52`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `45` إلى السطر `52` (`Lines 45–52`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 45–52`):**
```python
    def test_common_face_mapping_rejects_changed_boundaries(self):
        from common_geometry import normalize_to_common_faces
        a={'chains':[{'id':0,'adjacent_face_labels':[1,2],'pixel_crack_vertices':[[0,0],[1,0]],'segments':[]}]}
        b={'chains':[{'id':9,'adjacent_face_labels':[1,2],'pixel_crack_vertices':[[1,0],[0,0]],'segments':[]}]}
        result=normalize_to_common_faces(a,b)
        self.assertTrue(result['normalization']['chain_mapping'][0]['reversed'])
        b['chains'][0]['pixel_crack_vertices']=[[1,1],[0,0]]
        with self.assertRaises(KeyError):normalize_to_common_faces(a,b)
```

### `GeometryIsolationTests.test_only_closed_rings_gain_svg_closure` — `Lines 54–58`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `54` إلى السطر `58` (`Lines 54–58`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 54–58`):**
```python
    def test_only_closed_rings_gain_svg_closure(self):
        from geometry_eval import chain_points
        ch={'closed':False,'segments':[{'type':'L','p0':[0,0],'p3':[1,1]}]}
        self.assertEqual(len(chain_points(ch)),2)
        ch['closed']=True;self.assertEqual(len(chain_points(ch)),3)
```

### `GeometryIsolationTests.test_protocol_prevents_truth_selection` — `Lines 60–65`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `60` إلى السطر `65` (`Lines 60–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 60–65`):**
```python
    def test_protocol_prevents_truth_selection(self):
        from pathlib import Path
        p=json.loads((Path(__file__).parent/'protocol.json').read_text())
        self.assertIn('No candidate',p['policy']['truth_selection'])
        self.assertEqual(p['architecture'],'NOT_APPROVED')
        self.assertEqual(p['budgets']['combinations_max_per_case'],4)
```
