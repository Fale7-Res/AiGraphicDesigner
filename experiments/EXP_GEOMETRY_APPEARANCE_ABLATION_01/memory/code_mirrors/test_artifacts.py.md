# مرآة الكود التفصيلية: `test_artifacts.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_artifacts.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_artifacts.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `72` (`Lines 1–72`)
- **بصمة الملف (`SHA-256`):** `5e70ee1b30a8f87c8bef1243cb6f4665016d2d4035a71cdecfb27f8a222fcd98`
- **الوصف التفصيلي:** """Independent artifact contract checks; no trace/search reruns."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `geometry_tree` | `function` | `Lines 10–18` | `def geometry_tree(node):` | رمز برمجي موثق. |
| `SavedAblationTests` | `class` | `Lines 20–69` | `class SavedAblationTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SavedAblationTests.setUpClass` | `method` | `Lines 22–24` | `def setUpClass(cls):` | رمز برمجي موثق. |
| `SavedAblationTests.test_complete_frozen_suite_and_artifact_hashes` | `method` | `Lines 25–31` | `def test_complete_frozen_suite_and_artifact_hashes(self):` | رمز برمجي موثق. |
| `SavedAblationTests.test_strict_b_c_d_geometry_and_alpha_mask_identity` | `method` | `Lines 32–36` | `def test_strict_b_c_d_geometry_and_alpha_mask_identity(self):` | رمز برمجي موثق. |
| `SavedAblationTests.test_svg_safety_gradient_capacity_and_png_integrity` | `method` | `Lines 37–52` | `def test_svg_safety_gradient_capacity_and_png_integrity(self):` | رمز برمجي موثق. |
| `SavedAblationTests.test_saved_actual_white_mse_and_alpha` | `method` | `Lines 53–62` | `def test_saved_actual_white_mse_and_alpha(self):` | رمز برمجي موثق. |
| `SavedAblationTests.test_zoom_evidence_and_known_control_geometry` | `method` | `Lines 63–69` | `def test_zoom_evidence_and_known_control_geometry(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `geometry_tree` — `Lines 10–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `18` (`Lines 10–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–18`):**
```python
def geometry_tree(node):
    tag=node.tag.rsplit('}',1)[-1]
    if tag in ['linearGradient','radialGradient']:return None
    if tag=='mask':return ET.tostring(node,encoding='unicode')
    attributes=dict(node.attrib)
    if tag=='path':attributes.pop('fill',None)
    children=[v for c in node if (v:=geometry_tree(c)) is not None]
    if tag=='defs' and not children:return None
    return [node.tag,attributes,children]
```

### `SavedAblationTests` — `Lines 20–69`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `69` (`Lines 20–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–69`):**
```python
class SavedAblationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'inputs/manifest.json').read_text())
        cls.cases=cls.manifest['cases']
    def test_complete_frozen_suite_and_artifact_hashes(self):
        self.assertEqual(len(self.cases),9)
        for case in self.cases:
            for key in ['source','reference','geometry','ground_truth_svg']:
                if key in case:self.assertEqual(hashlib.sha256(Path(case[key]).read_bytes()).hexdigest(),case[key+'_sha256'])
            result=json.loads((ROOT/'results'/case['id']/'result.json').read_text())
            for name,row in result['conditions'].items():self.assertEqual(hashlib.sha256((ROOT/'results'/case['id']/name/'output.svg').read_bytes()).hexdigest(),row['sha256'])
    def test_strict_b_c_d_geometry_and_alpha_mask_identity(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id'];trees=[ET.parse(folder/name/'output.svg').getroot() for name in 'BCD']
            self.assertEqual(geometry_tree(trees[0]),geometry_tree(trees[1]),case['id'])
            self.assertEqual(geometry_tree(trees[1]),geometry_tree(trees[2]),case['id'])
    def test_svg_safety_gradient_capacity_and_png_integrity(self):
        for path in (ROOT/'results').rglob('*.svg'):
            root=ET.parse(path).getroot();ids={e.get('id') for e in root.iter() if e.get('id')}
            for e in root.iter():
                tag=e.tag.rsplit('}',1)[-1]
                self.assertNotIn(tag,['image','foreignObject','script','filter'],str(path))
                for k,v in e.attrib.items():
                    if k.rsplit('}',1)[-1]=='href':self.assertTrue(v.startswith('#'),str(path))
                    if v.startswith('url('):self.assertIn(v[5:-1],ids,str(path))
                if tag in ['linearGradient','radialGradient']:
                    stops=list(e);self.assertLessEqual(len(stops),4);self.assertGreaterEqual(len(stops),2)
                    offsets=[float(s.get('offset')) for s in stops];self.assertEqual(offsets,sorted(offsets))
                    self.assertEqual(e.get('gradientUnits'),'userSpaceOnUse')
                    if tag=='radialGradient':self.assertGreater(float(e.get('r')),0)
        for path in (ROOT/'results').rglob('*.png'):
            with Image.open(path) as im:im.verify()
    def test_saved_actual_white_mse_and_alpha(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id'];result=json.loads((folder/'result.json').read_text());source=Image.open(folder/'source.png').convert('RGBA')
            a=np.asarray(source)
            ref=np.asarray(Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')).astype(float)
            for name,row in result['conditions'].items():
                b=np.asarray(Image.open(folder/name/'white.png').convert('RGB')).astype(float)
                self.assertAlmostEqual(float(((ref-b)**2).mean()),row['metrics']['white']['mse'],places=10)
                alpha=np.asarray(Image.open(folder/name/'render.png').convert('RGBA'))[:,:,3]
                self.assertAlmostEqual(float(np.abs(a[:,:,3].astype(float)-alpha).mean()),row['alpha_mae'],places=10)
    def test_zoom_evidence_and_known_control_geometry(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id']
            for crop in ['worst_error','center']:
                for scale in [1,4,16]:self.assertTrue((folder/f'{crop}_{scale}x.png').is_file())
            if case['known_vector']:
                g=json.loads((folder/'known_geometry.json').read_text());self.assertTrue(0<=g['foreground_iou_4x']<=1)
```

### `SavedAblationTests.setUpClass` — `Lines 22–24`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `24` (`Lines 22–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–24`):**
```python
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'inputs/manifest.json').read_text())
        cls.cases=cls.manifest['cases']
```

### `SavedAblationTests.test_complete_frozen_suite_and_artifact_hashes` — `Lines 25–31`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `31` (`Lines 25–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–31`):**
```python
    def test_complete_frozen_suite_and_artifact_hashes(self):
        self.assertEqual(len(self.cases),9)
        for case in self.cases:
            for key in ['source','reference','geometry','ground_truth_svg']:
                if key in case:self.assertEqual(hashlib.sha256(Path(case[key]).read_bytes()).hexdigest(),case[key+'_sha256'])
            result=json.loads((ROOT/'results'/case['id']/'result.json').read_text())
            for name,row in result['conditions'].items():self.assertEqual(hashlib.sha256((ROOT/'results'/case['id']/name/'output.svg').read_bytes()).hexdigest(),row['sha256'])
```

### `SavedAblationTests.test_strict_b_c_d_geometry_and_alpha_mask_identity` — `Lines 32–36`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `36` (`Lines 32–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–36`):**
```python
    def test_strict_b_c_d_geometry_and_alpha_mask_identity(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id'];trees=[ET.parse(folder/name/'output.svg').getroot() for name in 'BCD']
            self.assertEqual(geometry_tree(trees[0]),geometry_tree(trees[1]),case['id'])
            self.assertEqual(geometry_tree(trees[1]),geometry_tree(trees[2]),case['id'])
```

### `SavedAblationTests.test_svg_safety_gradient_capacity_and_png_integrity` — `Lines 37–52`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `37` إلى السطر `52` (`Lines 37–52`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 37–52`):**
```python
    def test_svg_safety_gradient_capacity_and_png_integrity(self):
        for path in (ROOT/'results').rglob('*.svg'):
            root=ET.parse(path).getroot();ids={e.get('id') for e in root.iter() if e.get('id')}
            for e in root.iter():
                tag=e.tag.rsplit('}',1)[-1]
                self.assertNotIn(tag,['image','foreignObject','script','filter'],str(path))
                for k,v in e.attrib.items():
                    if k.rsplit('}',1)[-1]=='href':self.assertTrue(v.startswith('#'),str(path))
                    if v.startswith('url('):self.assertIn(v[5:-1],ids,str(path))
                if tag in ['linearGradient','radialGradient']:
                    stops=list(e);self.assertLessEqual(len(stops),4);self.assertGreaterEqual(len(stops),2)
                    offsets=[float(s.get('offset')) for s in stops];self.assertEqual(offsets,sorted(offsets))
                    self.assertEqual(e.get('gradientUnits'),'userSpaceOnUse')
                    if tag=='radialGradient':self.assertGreater(float(e.get('r')),0)
        for path in (ROOT/'results').rglob('*.png'):
            with Image.open(path) as im:im.verify()
```

### `SavedAblationTests.test_saved_actual_white_mse_and_alpha` — `Lines 53–62`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `53` إلى السطر `62` (`Lines 53–62`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 53–62`):**
```python
    def test_saved_actual_white_mse_and_alpha(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id'];result=json.loads((folder/'result.json').read_text());source=Image.open(folder/'source.png').convert('RGBA')
            a=np.asarray(source)
            ref=np.asarray(Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')).astype(float)
            for name,row in result['conditions'].items():
                b=np.asarray(Image.open(folder/name/'white.png').convert('RGB')).astype(float)
                self.assertAlmostEqual(float(((ref-b)**2).mean()),row['metrics']['white']['mse'],places=10)
                alpha=np.asarray(Image.open(folder/name/'render.png').convert('RGBA'))[:,:,3]
                self.assertAlmostEqual(float(np.abs(a[:,:,3].astype(float)-alpha).mean()),row['alpha_mae'],places=10)
```

### `SavedAblationTests.test_zoom_evidence_and_known_control_geometry` — `Lines 63–69`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `63` إلى السطر `69` (`Lines 63–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 63–69`):**
```python
    def test_zoom_evidence_and_known_control_geometry(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id']
            for crop in ['worst_error','center']:
                for scale in [1,4,16]:self.assertTrue((folder/f'{crop}_{scale}x.png').is_file())
            if case['known_vector']:
                g=json.loads((folder/'known_geometry.json').read_text());self.assertTrue(0<=g['foreground_iou_4x']<=1)
```
