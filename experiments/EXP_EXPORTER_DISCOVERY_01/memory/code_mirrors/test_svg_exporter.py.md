# مرآة الكود التفصيلية: `test_svg_exporter.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_svg_exporter.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_svg_exporter.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `180` (`Lines 1–180`)
- **بصمة الملف (`SHA-256`):** `2448d694bb6d2def95c305ea85e385c0204078607d004d6df893109917b8ea35`
- **الوصف التفصيلي:** # START CHANGE AGD-EXPORTER-TESTS | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `parse_path` | `function` | `Lines 15–47` | `def parse_path(data):` | Interpret emitted absolute M/L/C/Z without serializer helper reuse. |
| `line_chain` | `function` | `Lines 50–53` | `def line_chain(identifier, points, closed=False):` | رمز برمجي موثق. |
| `graph` | `function` | `Lines 56–57` | `def graph(chains, loops=None):` | رمز برمجي موثق. |
| `ref` | `function` | `Lines 60–61` | `def ref(identifier, forward=True):` | رمز برمجي موثق. |
| `paths` | `function` | `Lines 64–65` | `def paths(svg):` | رمز برمجي موثق. |
| `svg_data` | `function` | `Lines 68–70` | `def svg_data(data, regions=True):` | رمز برمجي موثق. |
| `SemanticTests` | `class` | `Lines 73–136` | `class SemanticTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SemanticTests.test_precision_control_is_explicit_and_default_roundtrips` | `method` | `Lines 74–79` | `def test_precision_control_is_explicit_and_default_roundtrips(self):` | رمز برمجي موثق. |
| `SemanticTests.test_single_open_and_closed_preserve_corners` | `method` | `Lines 81–88` | `def test_single_open_and_closed_preserve_corners(self):` | رمز برمجي موثق. |
| `SemanticTests.test_independent_subpaths_hole_nested_evenodd` | `method` | `Lines 90–95` | `def test_independent_subpaths_hole_nested_evenodd(self):` | رمز برمجي موثق. |
| `SemanticTests.test_embedded_closed_chain_has_own_explicit_closure` | `method` | `Lines 97–104` | `def test_embedded_closed_chain_has_own_explicit_closure(self):` | رمز برمجي موثق. |
| `SemanticTests.test_reverse_cubic_controls_and_implicit_closure_order` | `method` | `Lines 106–111` | `def test_reverse_cubic_controls_and_implicit_closure_order(self):` | رمز برمجي موثق. |
| `SemanticTests.test_shared_boundary_repeated_junctions_preserved` | `method` | `Lines 113–121` | `def test_shared_boundary_repeated_junctions_preserved(self):` | رمز برمجي موثق. |
| `SemanticTests.test_mixed_open_closed_and_input_immutable` | `method` | `Lines 123–126` | `def test_mixed_open_closed_and_input_immutable(self):` | رمز برمجي موثق. |
| `SemanticTests.test_fail_closed_disconnected_unsupported_nonfinite_open_face` | `method` | `Lines 128–136` | `def test_fail_closed_disconnected_unsupported_nonfinite_open_face(self):` | رمز برمجي موثق. |
| `RendererTests` | `class` | `Lines 139–176` | `class RendererTests(unittest.TestCase):` | رمز برمجي موثق. |
| `RendererTests.test_actual_resvg_known_canonical_fixtures` | `method` | `Lines 140–176` | `def test_actual_resvg_known_canonical_fixtures(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `parse_path` — `Lines 15–47`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `47` (`Lines 15–47`)
- **الوظيفة:** Interpret emitted absolute M/L/C/Z without serializer helper reuse.
- **الكود الفعلي (`Lines 15–47`):**
```python
def parse_path(data):
    """Interpret emitted absolute M/L/C/Z without serializer helper reuse.

    Records every geometric segment including implicit Z closure and subpath
    origins; fails on unknown commands or syntax instead of ignoring them.
    """
    token_pattern = r'[MLCZ]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?'
    tokens = re.findall(token_pattern, data)
    residue = re.sub(token_pattern, '', data)
    if residue.strip(' ,\t\r\n'):
        raise ValueError('Unknown SVG syntax')
    segments, starts, closes = [], [], []
    at = 0; current = origin = None
    while at < len(tokens):
        command = tokens[at]; at += 1
        if command not in 'MLCZ':
            raise ValueError('Explicit commands required')
        if command == 'Z':
            if current is None: raise ValueError('Z without subpath')
            closes.append((current, origin))
            if current != origin: segments.append(('L', (current, origin)))
            current = origin
            continue
        size = 6 if command == 'C' else 2
        coords = [float(x) for x in tokens[at:at+size]]; at += size
        if len(coords) != size: raise ValueError('Incomplete SVG command')
        points = tuple(zip(coords[::2], coords[1::2]))
        if command == 'M':
            current = origin = points[0]; starts.append(origin)
        else:
            if current is None: raise ValueError('Draw before M')
            segments.append((command, (current,) + points)); current = points[-1]
    return {'segments': segments, 'origins': starts, 'closes': closes}
```

### `line_chain` — `Lines 50–53`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `53` (`Lines 50–53`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 50–53`):**
```python
def line_chain(identifier, points, closed=False):
    return {'id': identifier, 'closed': closed, 'adjacent_face_labels': [0,1],
            'pixel_crack_vertices': points,
            'segments': [{'type':'L','p0':a,'p3':b} for a,b in zip(points, points[1:])]}
```

### `graph` — `Lines 56–57`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `56` إلى السطر `57` (`Lines 56–57`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 56–57`):**
```python
def graph(chains, loops=None):
    return {'width':64,'height':64,'chains':chains,'faces':{'1':loops or []}}
```

### `ref` — `Lines 60–61`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `60` إلى السطر `61` (`Lines 60–61`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 60–61`):**
```python
def ref(identifier, forward=True):
    return {'chain':identifier,'forward':forward}
```

### `paths` — `Lines 64–65`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `64` إلى السطر `65` (`Lines 64–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 64–65`):**
```python
def paths(svg):
    return [parse_path(e.attrib['d']) for e in ET.fromstring(svg)]
```

### `svg_data` — `Lines 68–70`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `68` إلى السطر `70` (`Lines 68–70`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 68–70`):**
```python
def svg_data(data, regions=True):
    attributes = 'fill="black" fill-rule="evenodd"' if regions else 'fill="none" stroke="#607d8b" stroke-width="0.35"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><path {attributes} d="{data}"/></svg>'
```

### `SemanticTests` — `Lines 73–136`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `73` إلى السطر `136` (`Lines 73–136`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 73–136`):**
```python
class SemanticTests(unittest.TestCase):
    def test_precision_control_is_explicit_and_default_roundtrips(self):
        value=1.2345678901234567
        g=graph([line_chain(0,[[value,2],[4,5]])])
        self.assertEqual(paths(svg_graph(g))[0]['origins'][0][0],value)
        self.assertEqual(paths(svg_graph(g,precision=8))[0]['origins'][0][0],float(format(value,'.8g')))
        with self.assertRaises(ValueError):svg_graph(g,precision=6)

    def test_single_open_and_closed_preserve_corners(self):
        points = [[2,2],[20,2],[20,15]]
        for raw in (False,True):
            opened = paths(svg_graph(graph([line_chain(1,points)]),raw=raw))[0]
            self.assertEqual(opened['closes'],[])
            closed = paths(svg_graph(graph([line_chain(1,points,True)]),raw=raw))[0]
            self.assertEqual(closed['segments'][-1],('L',((20.,15.),(2.,2.))))
            self.assertEqual(closed['closes'],[((2.,2.),(2.,2.))])

    def test_independent_subpaths_hole_nested_evenodd(self):
        contours = [[[2,2],[60,2],[60,60],[2,60]],[[12,12],[50,12],[50,50],[12,50]],[[24,24],[38,24],[38,38],[24,38]]]
        g=graph([line_chain(i,p+[p[0]],True) for i,p in enumerate(contours)],[[ref(i)] for i in range(3)])
        data=paths(svg_graph(g,regions=True,foreground={1}))[0]
        self.assertEqual(len(data['origins']),3)
        self.assertTrue(all(a==b for a,b in data['closes']))

    def test_embedded_closed_chain_has_own_explicit_closure(self):
        # A->J, complete little closed loop at J, then J->A.
        g=graph([line_chain(0,[[2,2],[20,20]]),line_chain(1,[[20,20],[30,20],[30,30]],True)],[[ref(0),ref(1),ref(0,False)]])
        data=paths(svg_graph(g,regions=True))[0]
        self.assertIn(('L',((30.,30.),(20.,20.))),data['segments'])
        self.assertNotIn(('L',((30.,30.),(2.,2.))),data['segments'])
        self.assertEqual(data['origins'],[(2.,2.)])
        self.assertEqual(len(data['closes']),1)

    def test_reverse_cubic_controls_and_implicit_closure_order(self):
        chain={'id':0,'closed':True,'adjacent_face_labels':[0,1], 'pixel_crack_vertices':[[10,10],[30,20]],
               'segments':[{'type':'C','p0':[10,10],'p1':[12,4],'p2':[29,8],'p3':[30,20]}]}
        g=graph([chain],[[ref(0,False)]])
        segments=paths(svg_graph(g,regions=True))[0]['segments']
        self.assertEqual(segments,[('L',((10.,10.),(30.,20.))),('C',((30.,20.),(29.,8.),(12.,4.),(10.,10.)))])

    def test_shared_boundary_repeated_junctions_preserved(self):
        chains=[line_chain(0,[[5,5],[30,5],[30,30]]),line_chain(1,[[30,30],[5,30],[5,5]]),line_chain(2,[[30,30],[55,30],[55,5],[30,5]])]
        # Shared chain is an independent vertical edge, consumed in opposite directions.
        chains[0]=line_chain(0,[[30,5],[30,30]])
        chains[1]=line_chain(1,[[30,30],[5,30],[5,5],[30,5]])
        g=graph(chains);g['faces']={'1':[[ref(0),ref(1)]],'2':[[ref(0,False),ref(2,False)]]}
        data=paths(svg_graph(g,regions=True))
        self.assertIn(('L',((30.,5.),(30.,30.))),data[0]['segments'])
        self.assertIn(('L',((30.,30.),(30.,5.))),data[1]['segments'])

    def test_mixed_open_closed_and_input_immutable(self):
        g=graph([line_chain(0,[[1,1],[10,1]]),line_chain(1,[[20,20],[30,20],[25,30]],True)])
        before=copy.deepcopy(g);p=paths(svg_graph(g))
        self.assertFalse(p[0]['closes']);self.assertEqual(len(p[1]['closes']),1);self.assertEqual(g,before)

    def test_fail_closed_disconnected_unsupported_nonfinite_open_face(self):
        g=graph([line_chain(0,[[2,2],[4,4]])],[[ref(0)]])
        with self.assertRaises(ValueError):svg_graph(g,regions=True)
        g['chains'][0]['segments'].append({'type':'L','p0':[5,5],'p3':[2,2]})
        with self.assertRaises(ValueError):svg_graph(g)
        g['chains'][0]['segments'][0]['type']='Q'
        with self.assertRaises(ValueError):svg_graph(g)
        g['chains'][0]['segments']=[{'type':'L','p0':[float('nan'),2],'p3':[3,3]}]
        with self.assertRaises(ValueError):svg_graph(g)
```

### `SemanticTests.test_precision_control_is_explicit_and_default_roundtrips` — `Lines 74–79`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `74` إلى السطر `79` (`Lines 74–79`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 74–79`):**
```python
    def test_precision_control_is_explicit_and_default_roundtrips(self):
        value=1.2345678901234567
        g=graph([line_chain(0,[[value,2],[4,5]])])
        self.assertEqual(paths(svg_graph(g))[0]['origins'][0][0],value)
        self.assertEqual(paths(svg_graph(g,precision=8))[0]['origins'][0][0],float(format(value,'.8g')))
        with self.assertRaises(ValueError):svg_graph(g,precision=6)
```

### `SemanticTests.test_single_open_and_closed_preserve_corners` — `Lines 81–88`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `81` إلى السطر `88` (`Lines 81–88`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 81–88`):**
```python
    def test_single_open_and_closed_preserve_corners(self):
        points = [[2,2],[20,2],[20,15]]
        for raw in (False,True):
            opened = paths(svg_graph(graph([line_chain(1,points)]),raw=raw))[0]
            self.assertEqual(opened['closes'],[])
            closed = paths(svg_graph(graph([line_chain(1,points,True)]),raw=raw))[0]
            self.assertEqual(closed['segments'][-1],('L',((20.,15.),(2.,2.))))
            self.assertEqual(closed['closes'],[((2.,2.),(2.,2.))])
```

### `SemanticTests.test_independent_subpaths_hole_nested_evenodd` — `Lines 90–95`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `90` إلى السطر `95` (`Lines 90–95`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 90–95`):**
```python
    def test_independent_subpaths_hole_nested_evenodd(self):
        contours = [[[2,2],[60,2],[60,60],[2,60]],[[12,12],[50,12],[50,50],[12,50]],[[24,24],[38,24],[38,38],[24,38]]]
        g=graph([line_chain(i,p+[p[0]],True) for i,p in enumerate(contours)],[[ref(i)] for i in range(3)])
        data=paths(svg_graph(g,regions=True,foreground={1}))[0]
        self.assertEqual(len(data['origins']),3)
        self.assertTrue(all(a==b for a,b in data['closes']))
```

### `SemanticTests.test_embedded_closed_chain_has_own_explicit_closure` — `Lines 97–104`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `97` إلى السطر `104` (`Lines 97–104`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 97–104`):**
```python
    def test_embedded_closed_chain_has_own_explicit_closure(self):
        # A->J, complete little closed loop at J, then J->A.
        g=graph([line_chain(0,[[2,2],[20,20]]),line_chain(1,[[20,20],[30,20],[30,30]],True)],[[ref(0),ref(1),ref(0,False)]])
        data=paths(svg_graph(g,regions=True))[0]
        self.assertIn(('L',((30.,30.),(20.,20.))),data['segments'])
        self.assertNotIn(('L',((30.,30.),(2.,2.))),data['segments'])
        self.assertEqual(data['origins'],[(2.,2.)])
        self.assertEqual(len(data['closes']),1)
```

### `SemanticTests.test_reverse_cubic_controls_and_implicit_closure_order` — `Lines 106–111`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `106` إلى السطر `111` (`Lines 106–111`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 106–111`):**
```python
    def test_reverse_cubic_controls_and_implicit_closure_order(self):
        chain={'id':0,'closed':True,'adjacent_face_labels':[0,1], 'pixel_crack_vertices':[[10,10],[30,20]],
               'segments':[{'type':'C','p0':[10,10],'p1':[12,4],'p2':[29,8],'p3':[30,20]}]}
        g=graph([chain],[[ref(0,False)]])
        segments=paths(svg_graph(g,regions=True))[0]['segments']
        self.assertEqual(segments,[('L',((10.,10.),(30.,20.))),('C',((30.,20.),(29.,8.),(12.,4.),(10.,10.)))])
```

### `SemanticTests.test_shared_boundary_repeated_junctions_preserved` — `Lines 113–121`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `113` إلى السطر `121` (`Lines 113–121`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 113–121`):**
```python
    def test_shared_boundary_repeated_junctions_preserved(self):
        chains=[line_chain(0,[[5,5],[30,5],[30,30]]),line_chain(1,[[30,30],[5,30],[5,5]]),line_chain(2,[[30,30],[55,30],[55,5],[30,5]])]
        # Shared chain is an independent vertical edge, consumed in opposite directions.
        chains[0]=line_chain(0,[[30,5],[30,30]])
        chains[1]=line_chain(1,[[30,30],[5,30],[5,5],[30,5]])
        g=graph(chains);g['faces']={'1':[[ref(0),ref(1)]],'2':[[ref(0,False),ref(2,False)]]}
        data=paths(svg_graph(g,regions=True))
        self.assertIn(('L',((30.,5.),(30.,30.))),data[0]['segments'])
        self.assertIn(('L',((30.,30.),(30.,5.))),data[1]['segments'])
```

### `SemanticTests.test_mixed_open_closed_and_input_immutable` — `Lines 123–126`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `123` إلى السطر `126` (`Lines 123–126`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 123–126`):**
```python
    def test_mixed_open_closed_and_input_immutable(self):
        g=graph([line_chain(0,[[1,1],[10,1]]),line_chain(1,[[20,20],[30,20],[25,30]],True)])
        before=copy.deepcopy(g);p=paths(svg_graph(g))
        self.assertFalse(p[0]['closes']);self.assertEqual(len(p[1]['closes']),1);self.assertEqual(g,before)
```

### `SemanticTests.test_fail_closed_disconnected_unsupported_nonfinite_open_face` — `Lines 128–136`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `128` إلى السطر `136` (`Lines 128–136`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 128–136`):**
```python
    def test_fail_closed_disconnected_unsupported_nonfinite_open_face(self):
        g=graph([line_chain(0,[[2,2],[4,4]])],[[ref(0)]])
        with self.assertRaises(ValueError):svg_graph(g,regions=True)
        g['chains'][0]['segments'].append({'type':'L','p0':[5,5],'p3':[2,2]})
        with self.assertRaises(ValueError):svg_graph(g)
        g['chains'][0]['segments'][0]['type']='Q'
        with self.assertRaises(ValueError):svg_graph(g)
        g['chains'][0]['segments']=[{'type':'L','p0':[float('nan'),2],'p3':[3,3]}]
        with self.assertRaises(ValueError):svg_graph(g)
```

### `RendererTests` — `Lines 139–176`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `139` إلى السطر `176` (`Lines 139–176`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 139–176`):**
```python
class RendererTests(unittest.TestCase):
    def test_actual_resvg_known_canonical_fixtures(self):
        renderer=Path(os.environ.get('AGD_RESVG',r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\resvg\resvg.exe'))
        self.assertTrue(renderer.is_file(),'Actual resvg required; do not silently skip')
        fixtures=[]
        fixtures.append(('open',graph([line_chain(0,[[2,2],[20,2],[20,15]])]),False,'M2,2 L20,2 L20,15'))
        fixtures.append(('closed_corner',graph([line_chain(0,[[2,2],[20,2],[20,15]],True)]),False,'M2,2 L20,2 L20,15 L2,2 Z'))
        contours=[[[2,2],[60,2],[60,60],[2,60],[2,2]],[[12,12],[50,12],[50,50],[12,50],[12,12]],[[24,24],[38,24],[38,38],[24,38],[24,24]]]
        fixture=graph([line_chain(i,p,True) for i,p in enumerate(contours)],[[ref(i)] for i in range(3)])
        fixtures.append(('nested_holes',fixture,True,'M2,2 L60,2 L60,60 L2,60 L2,2 Z M12,12 L50,12 L50,50 L12,50 L12,12 Z M24,24 L38,24 L38,38 L24,38 L24,24 Z'))
        embedded=graph([line_chain(0,[[2,2],[20,20]]),line_chain(1,[[20,20],[30,20],[30,30]],True)],[[ref(0),ref(1),ref(0,False)]])
        fixtures.append(('embedded_closed',embedded,True,'M2,2 L20,20 L30,20 L30,30 L20,20 L2,2 Z'))
        reverse={'id':0,'closed':True,'adjacent_face_labels':[0,1], 'pixel_crack_vertices':[[10,10],[30,20]],
                 'segments':[{'type':'C','p0':[10,10],'p1':[12,4],'p2':[29,8],'p3':[30,20]}]}
        fixtures.append(('reversed_cubic',graph([reverse],[[ref(0,False)]]),True,'M10,10 L30,20 C29,8 12,4 10,10 Z'))
        fixtures.append(('independent_subpaths',graph([line_chain(0,[[4,4],[20,4],[20,20]],True),line_chain(1,[[40,40],[55,40],[55,55]],True)],[[ref(0)],[ref(1)]]),True,'M4,4 L20,4 L20,20 L4,4 Z M40,40 L55,40 L55,55 L40,40 Z'))
        # One stroke path can contain independent open/closed subpaths. Exact
        # pixels equal two exported path elements with identical paint.
        fixtures.append(('mixed_open_closed',graph([line_chain(0,[[2,2],[10,2]]),line_chain(1,[[20,20],[30,20],[25,30]],True)]),False,'M2,2 L10,2 M20,20 L30,20 L25,30 L20,20 Z'))
        shared=graph([line_chain(0,[[30,5],[30,30]]),line_chain(1,[[30,30],[5,30],[5,5],[30,5]]),line_chain(2,[[30,30],[55,30],[55,5],[30,5]])])
        shared['faces']={'1':[[ref(0),ref(1)]],'2':[[ref(0,False),ref(2,False)]]}
        # Separate face paints must remain separate to test source-over AA.
        shared_expected='<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><path fill="black" fill-rule="evenodd" d="M30,5 L30,30 L5,30 L5,5 L30,5 Z"/><path fill="black" fill-rule="evenodd" d="M30,30 L30,5 L55,5 L55,30 L30,30 Z"/></svg>'
        fixtures.append(('shared_boundary',shared,True,shared_expected))
        out=Path(os.environ.get('AGD_EXPORTER_FIXTURE_OUTPUT',tempfile.mkdtemp(prefix='agd_exporter_')));out.mkdir(parents=True,exist_ok=True)
        for name,g,regions,canonical in fixtures:
            generated=svg_graph(g,regions=regions,foreground={1,2} if regions else None)
            expected=canonical if canonical.startswith('<svg') else svg_data(canonical,regions)
            for suffix,svg in [('actual',generated),('canonical',expected)]:
                source=out/f'{name}_{suffix}.svg';png=out/f'{name}_{suffix}.png';source.write_text(svg,encoding='utf-8')
                subprocess.run([str(renderer),str(source),str(png)],check=True,capture_output=True)
            a=Image.open(out/f'{name}_actual.png').convert('RGBA');b=Image.open(out/f'{name}_canonical.png').convert('RGBA')
            self.assertEqual(a.tobytes(),b.tobytes(),name)
        # Independent expected pixel occupancy for the nested evenodd fixture.
        image=Image.open(out/'nested_holes_actual.png').convert('RGBA')
        self.assertEqual(image.getpixel((5,5))[3],255)
        self.assertEqual(image.getpixel((15,15))[3],0)
        self.assertEqual(image.getpixel((30,30))[3],255)
```

### `RendererTests.test_actual_resvg_known_canonical_fixtures` — `Lines 140–176`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `140` إلى السطر `176` (`Lines 140–176`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 140–176`):**
```python
    def test_actual_resvg_known_canonical_fixtures(self):
        renderer=Path(os.environ.get('AGD_RESVG',r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\resvg\resvg.exe'))
        self.assertTrue(renderer.is_file(),'Actual resvg required; do not silently skip')
        fixtures=[]
        fixtures.append(('open',graph([line_chain(0,[[2,2],[20,2],[20,15]])]),False,'M2,2 L20,2 L20,15'))
        fixtures.append(('closed_corner',graph([line_chain(0,[[2,2],[20,2],[20,15]],True)]),False,'M2,2 L20,2 L20,15 L2,2 Z'))
        contours=[[[2,2],[60,2],[60,60],[2,60],[2,2]],[[12,12],[50,12],[50,50],[12,50],[12,12]],[[24,24],[38,24],[38,38],[24,38],[24,24]]]
        fixture=graph([line_chain(i,p,True) for i,p in enumerate(contours)],[[ref(i)] for i in range(3)])
        fixtures.append(('nested_holes',fixture,True,'M2,2 L60,2 L60,60 L2,60 L2,2 Z M12,12 L50,12 L50,50 L12,50 L12,12 Z M24,24 L38,24 L38,38 L24,38 L24,24 Z'))
        embedded=graph([line_chain(0,[[2,2],[20,20]]),line_chain(1,[[20,20],[30,20],[30,30]],True)],[[ref(0),ref(1),ref(0,False)]])
        fixtures.append(('embedded_closed',embedded,True,'M2,2 L20,20 L30,20 L30,30 L20,20 L2,2 Z'))
        reverse={'id':0,'closed':True,'adjacent_face_labels':[0,1], 'pixel_crack_vertices':[[10,10],[30,20]],
                 'segments':[{'type':'C','p0':[10,10],'p1':[12,4],'p2':[29,8],'p3':[30,20]}]}
        fixtures.append(('reversed_cubic',graph([reverse],[[ref(0,False)]]),True,'M10,10 L30,20 C29,8 12,4 10,10 Z'))
        fixtures.append(('independent_subpaths',graph([line_chain(0,[[4,4],[20,4],[20,20]],True),line_chain(1,[[40,40],[55,40],[55,55]],True)],[[ref(0)],[ref(1)]]),True,'M4,4 L20,4 L20,20 L4,4 Z M40,40 L55,40 L55,55 L40,40 Z'))
        # One stroke path can contain independent open/closed subpaths. Exact
        # pixels equal two exported path elements with identical paint.
        fixtures.append(('mixed_open_closed',graph([line_chain(0,[[2,2],[10,2]]),line_chain(1,[[20,20],[30,20],[25,30]],True)]),False,'M2,2 L10,2 M20,20 L30,20 L25,30 L20,20 Z'))
        shared=graph([line_chain(0,[[30,5],[30,30]]),line_chain(1,[[30,30],[5,30],[5,5],[30,5]]),line_chain(2,[[30,30],[55,30],[55,5],[30,5]])])
        shared['faces']={'1':[[ref(0),ref(1)]],'2':[[ref(0,False),ref(2,False)]]}
        # Separate face paints must remain separate to test source-over AA.
        shared_expected='<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><path fill="black" fill-rule="evenodd" d="M30,5 L30,30 L5,30 L5,5 L30,5 Z"/><path fill="black" fill-rule="evenodd" d="M30,30 L30,5 L55,5 L55,30 L30,30 Z"/></svg>'
        fixtures.append(('shared_boundary',shared,True,shared_expected))
        out=Path(os.environ.get('AGD_EXPORTER_FIXTURE_OUTPUT',tempfile.mkdtemp(prefix='agd_exporter_')));out.mkdir(parents=True,exist_ok=True)
        for name,g,regions,canonical in fixtures:
            generated=svg_graph(g,regions=regions,foreground={1,2} if regions else None)
            expected=canonical if canonical.startswith('<svg') else svg_data(canonical,regions)
            for suffix,svg in [('actual',generated),('canonical',expected)]:
                source=out/f'{name}_{suffix}.svg';png=out/f'{name}_{suffix}.png';source.write_text(svg,encoding='utf-8')
                subprocess.run([str(renderer),str(source),str(png)],check=True,capture_output=True)
            a=Image.open(out/f'{name}_actual.png').convert('RGBA');b=Image.open(out/f'{name}_canonical.png').convert('RGBA')
            self.assertEqual(a.tobytes(),b.tobytes(),name)
        # Independent expected pixel occupancy for the nested evenodd fixture.
        image=Image.open(out/'nested_holes_actual.png').convert('RGBA')
        self.assertEqual(image.getpixel((5,5))[3],255)
        self.assertEqual(image.getpixel((15,15))[3],0)
        self.assertEqual(image.getpixel((30,30))[3],255)
```
