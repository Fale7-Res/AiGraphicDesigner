# مرآة الكود التفصيلية: `test_fixtures.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_fixtures.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_fixtures.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `57` (`Lines 1–57`)
- **بصمة الملف (`SHA-256`):** `fc5d384cbc27e7a1b339739479f806952f253bafbd705df5e6ae32020571bdbd`
- **الوصف التفصيلي:** """Passive checks for frozen known-vector controls; no tracing or fitting."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `AnalyticFixtureTests` | `class` | `Lines 9–54` | `class AnalyticFixtureTests(unittest.TestCase):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.setUpClass` | `method` | `Lines 11–12` | `def setUpClass(cls):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.test_two_small_frozen_controls_and_reference_reuse` | `method` | `Lines 13–21` | `def test_two_small_frozen_controls_and_reference_reuse(self):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.test_frozen_hashes_and_real_png_decoding` | `method` | `Lines 22–28` | `def test_frozen_hashes_and_real_png_decoding(self):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.test_no_raster_or_dense_grid_and_same_initial_geometry` | `method` | `Lines 29–35` | `def test_no_raster_or_dense_grid_and_same_initial_geometry(self):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.test_gradient_stop_family_and_subpixel_features` | `method` | `Lines 36–41` | `def test_gradient_stop_family_and_subpixel_features(self):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.test_soft_alpha_is_actual_vector_mask_and_visible_in_render` | `method` | `Lines 42–46` | `def test_soft_alpha_is_actual_vector_mask_and_visible_in_render(self):` | رمز برمجي موثق. |
| `AnalyticFixtureTests.test_nonempty_freeze_target_refused` | `method` | `Lines 47–54` | `def test_nonempty_freeze_target_refused(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `AnalyticFixtureTests` — `Lines 9–54`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `54` (`Lines 9–54`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–54`):**
```python
class AnalyticFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((fixtures.ROOT/'inputs/analytic/manifest.json').read_text())
    def test_two_small_frozen_controls_and_reference_reuse(self):
        self.assertEqual(self.manifest['status'],'FROZEN_BEFORE_FITTING')
        self.assertEqual(len(self.manifest['cases']),2);self.assertEqual(len(self.manifest['existing_control_references']),2)
        for ref in self.manifest['existing_control_references']:
            self.assertEqual(hashlib.sha256(Path(ref['truth_svg']).read_bytes()).hexdigest(),ref['truth_sha256'])
            self.assertEqual(hashlib.sha256(Path(ref['source_png']).read_bytes()).hexdigest(),ref['source_sha256'])
        for case in self.manifest['cases']:
            self.assertLessEqual(case['paint_paths'],8);self.assertLessEqual(max(case['dimensions']),160)
            self.assertEqual(case['license'],'CC0-1.0')
    def test_frozen_hashes_and_real_png_decoding(self):
        for case in self.manifest['cases']:
            folder=fixtures.ROOT/Path(case['truth_svg']).parent
            for name,record in case['files'].items():
                self.assertEqual(hashlib.sha256((folder/name).read_bytes()).hexdigest(),record['sha256'])
            with Image.open(fixtures.ROOT/case['source_png']) as im:
                im.load();self.assertEqual(list(im.size),case['dimensions'])
    def test_no_raster_or_dense_grid_and_same_initial_geometry(self):
        for case in self.manifest['cases']:
            a=ET.parse(fixtures.ROOT/case['truth_svg']).getroot();b=ET.parse(fixtures.ROOT/case['initial_svg']).getroot()
            for node in a.iter():self.assertNotIn(node.tag.rsplit('}',1)[-1],('image','filter','script','foreignObject'))
            paths=[p for p in a.iter(f'{{{fixtures.SVG}}}path') if p.get('id')]
            self.assertEqual(len(paths),case['paint_paths'])
            self.assertEqual([(p.get('id'),p.get('d'),p.get('opacity'),p.get('fill-rule')) for p in paths],[(p.get('id'),p.get('d'),p.get('opacity'),p.get('fill-rule')) for p in b.iter(f'{{{fixtures.SVG}}}path') if p.get('id')])
    def test_gradient_stop_family_and_subpixel_features(self):
        for case in self.manifest['cases']:
            for gradient in case['truth_gradients']:
                stops=gradient['stops'];self.assertLessEqual(len(stops),4)
                np.testing.assert_allclose([float(s['offset']) for s in stops],np.linspace(0,1,len(stops)),atol=1e-10)
            self.assertTrue(all(0<r['nominal_perpendicular_width_px']<1 for r in case['thin_regions']))
    def test_soft_alpha_is_actual_vector_mask_and_visible_in_render(self):
        case=self.manifest['cases'][1];root=ET.parse(fixtures.ROOT/case['truth_svg']).getroot()
        self.assertEqual(len(list(root.iter(f'{{{fixtures.SVG}}}mask'))),1)
        alpha=np.asarray(Image.open(fixtures.ROOT/case['source_png']).convert('RGBA'))[:,:,3]
        self.assertGreater(int(((alpha>0)&(alpha<255)).sum()),1000);self.assertGreater(int((alpha==0).sum()),0)
    def test_nonempty_freeze_target_refused(self):
        previous=fixtures.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'inputs/analytic').mkdir(parents=True);(root/'inputs/analytic/keep.txt').write_text('keep')
            fixtures.ROOT=root
            try:
                with self.assertRaises(FileExistsError):fixtures.freeze_fixtures()
            finally:fixtures.ROOT=previous
```

### `AnalyticFixtureTests.setUpClass` — `Lines 11–12`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `12` (`Lines 11–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–12`):**
```python
    def setUpClass(cls):
        cls.manifest=json.loads((fixtures.ROOT/'inputs/analytic/manifest.json').read_text())
```

### `AnalyticFixtureTests.test_two_small_frozen_controls_and_reference_reuse` — `Lines 13–21`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `21` (`Lines 13–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–21`):**
```python
    def test_two_small_frozen_controls_and_reference_reuse(self):
        self.assertEqual(self.manifest['status'],'FROZEN_BEFORE_FITTING')
        self.assertEqual(len(self.manifest['cases']),2);self.assertEqual(len(self.manifest['existing_control_references']),2)
        for ref in self.manifest['existing_control_references']:
            self.assertEqual(hashlib.sha256(Path(ref['truth_svg']).read_bytes()).hexdigest(),ref['truth_sha256'])
            self.assertEqual(hashlib.sha256(Path(ref['source_png']).read_bytes()).hexdigest(),ref['source_sha256'])
        for case in self.manifest['cases']:
            self.assertLessEqual(case['paint_paths'],8);self.assertLessEqual(max(case['dimensions']),160)
            self.assertEqual(case['license'],'CC0-1.0')
```

### `AnalyticFixtureTests.test_frozen_hashes_and_real_png_decoding` — `Lines 22–28`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `28` (`Lines 22–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–28`):**
```python
    def test_frozen_hashes_and_real_png_decoding(self):
        for case in self.manifest['cases']:
            folder=fixtures.ROOT/Path(case['truth_svg']).parent
            for name,record in case['files'].items():
                self.assertEqual(hashlib.sha256((folder/name).read_bytes()).hexdigest(),record['sha256'])
            with Image.open(fixtures.ROOT/case['source_png']) as im:
                im.load();self.assertEqual(list(im.size),case['dimensions'])
```

### `AnalyticFixtureTests.test_no_raster_or_dense_grid_and_same_initial_geometry` — `Lines 29–35`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `35` (`Lines 29–35`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–35`):**
```python
    def test_no_raster_or_dense_grid_and_same_initial_geometry(self):
        for case in self.manifest['cases']:
            a=ET.parse(fixtures.ROOT/case['truth_svg']).getroot();b=ET.parse(fixtures.ROOT/case['initial_svg']).getroot()
            for node in a.iter():self.assertNotIn(node.tag.rsplit('}',1)[-1],('image','filter','script','foreignObject'))
            paths=[p for p in a.iter(f'{{{fixtures.SVG}}}path') if p.get('id')]
            self.assertEqual(len(paths),case['paint_paths'])
            self.assertEqual([(p.get('id'),p.get('d'),p.get('opacity'),p.get('fill-rule')) for p in paths],[(p.get('id'),p.get('d'),p.get('opacity'),p.get('fill-rule')) for p in b.iter(f'{{{fixtures.SVG}}}path') if p.get('id')])
```

### `AnalyticFixtureTests.test_gradient_stop_family_and_subpixel_features` — `Lines 36–41`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `41` (`Lines 36–41`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 36–41`):**
```python
    def test_gradient_stop_family_and_subpixel_features(self):
        for case in self.manifest['cases']:
            for gradient in case['truth_gradients']:
                stops=gradient['stops'];self.assertLessEqual(len(stops),4)
                np.testing.assert_allclose([float(s['offset']) for s in stops],np.linspace(0,1,len(stops)),atol=1e-10)
            self.assertTrue(all(0<r['nominal_perpendicular_width_px']<1 for r in case['thin_regions']))
```

### `AnalyticFixtureTests.test_soft_alpha_is_actual_vector_mask_and_visible_in_render` — `Lines 42–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `46` (`Lines 42–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–46`):**
```python
    def test_soft_alpha_is_actual_vector_mask_and_visible_in_render(self):
        case=self.manifest['cases'][1];root=ET.parse(fixtures.ROOT/case['truth_svg']).getroot()
        self.assertEqual(len(list(root.iter(f'{{{fixtures.SVG}}}mask'))),1)
        alpha=np.asarray(Image.open(fixtures.ROOT/case['source_png']).convert('RGBA'))[:,:,3]
        self.assertGreater(int(((alpha>0)&(alpha<255)).sum()),1000);self.assertGreater(int((alpha==0).sum()),0)
```

### `AnalyticFixtureTests.test_nonempty_freeze_target_refused` — `Lines 47–54`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `47` إلى السطر `54` (`Lines 47–54`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 47–54`):**
```python
    def test_nonempty_freeze_target_refused(self):
        previous=fixtures.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'inputs/analytic').mkdir(parents=True);(root/'inputs/analytic/keep.txt').write_text('keep')
            fixtures.ROOT=root
            try:
                with self.assertRaises(FileExistsError):fixtures.freeze_fixtures()
            finally:fixtures.ROOT=previous
```
