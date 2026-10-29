# مرآة الكود التفصيلية: `test_fitter.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_fitter.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_fitter.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `70` (`Lines 1–70`)
- **بصمة الملف (`SHA-256`):** `7b94eacceb183ee38c841706308cafb5381676fa0d2b048be576e4cddfd68e44`
- **الوصف التفصيلي:** # START CHANGE AGD-COVERAGE-FITTER-TEST | 2026-10-28T05:16:21Z | EDITED | Author: /root/appearance_fit

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `FitterTests` | `class` | `Lines 15–66` | `class FitterTests(unittest.TestCase):` | رمز برمجي موثق. |
| `FitterTests._fixture` | `method` | `Lines 16–28` | `def _fixture(self, folder, alpha=False):` | رمز برمجي موثق. |
| `FitterTests.test_source_over_coefficients_recover_thin_support` | `method` | `Lines 30–44` | `def test_source_over_coefficients_recover_thin_support(self):` | رمز برمجي موثق. |
| `FitterTests.test_joint_fit_preserves_soft_alpha_gradient_and_improves_render` | `method` | `Lines 46–66` | `def test_joint_fit_preserves_soft_alpha_gradient_and_improves_render(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `FitterTests` — `Lines 15–66`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `66` (`Lines 15–66`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–66`):**
```python
class FitterTests(unittest.TestCase):
    def _fixture(self, folder, alpha=False):
        defs='<defs><linearGradient id="fixedAlpha" x1="0" y1="0" x2="64" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".15"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient><mask id="fixedMask" style="mask-type:alpha" mask-type="alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="48"><path fill="url(#fixedAlpha)" d="M0 0H64V48H0Z"/></mask></defs>' if alpha else ''
        group=' mask="url(#fixedMask)"' if alpha else ''
        paths='<path fill="#143c50" d="M0 0H64V48H0Z"/><path opacity=".5" fill="#d25a1e" d="M12 7H58V39H12Z"/><path fill="#1eb4c8" d="M30.2 3H30.8V46H30.2Z"/>'
        truth=f'<svg xmlns="{SVG}" width="64" height="48">{defs}<g{group}>{paths}</g></svg>'
        source=folder/'source.svg';source.write_text(truth)
        _render(ET.fromstring(truth),folder/'render_input.svg',folder/'source.png')
        root=ET.fromstring(truth)
        # Change only visible paint, preserving the soft alpha dependency.
        visible=root.find(f'{{{SVG}}}g')
        for path in visible:path.set('fill','#777777')
        baseline=folder/'baseline.svg';ET.ElementTree(root).write(baseline,encoding='utf-8')
        return source,baseline

    def test_source_over_coefficients_recover_thin_support(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);_,baseline=self._fixture(folder)
            metadata=build_maps(baseline,folder/'maps')
            self.assertLess(metadata['closure_max'],.02)
            self.assertLess(metadata['random_forward_rmse_bytes'],1.5)
            with np.load(folder/'maps/maps.npz') as values:
                w=values['weights'].reshape(3,48,64)
                self.assertGreater(w[2].sum(),0)
                self.assertLess(w[2].max(),1)
                self.assertAlmostEqual(float(w[1,15,20]),.5,delta=.01)
                self.assertAlmostEqual(float(w[0,15,20]),.5,delta=.01)
            self.assertEqual(build_maps(baseline,folder/'maps')['maps_npz_sha256'],metadata['maps_npz_sha256'])
            with (folder/'maps/maps.npz').open('ab') as stream:stream.write(b'corruption')
            with self.assertRaisesRegex(ValueError,'cache drift'):build_maps(baseline,folder/'maps')

    def test_joint_fit_preserves_soft_alpha_gradient_and_improves_render(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);source,baseline=self._fixture(folder,alpha=True)
            build_maps(baseline,folder/'maps')
            fit_case(folder/'source.png',baseline,baseline,folder/'maps',folder/'flat.svg',folder/'gradient.svg',folder/'fit.json',max_seconds=20)
            original=ET.parse(baseline).getroot()
            for name in ('flat','gradient'):
                root=ET.parse(folder/f'{name}.svg').getroot()
                self.assertEqual(_shape_signature(root),_shape_signature(original))
                dependency=root.find(f'.//{{{SVG}}}linearGradient[@id="fixedAlpha"]')
                self.assertIsNotNone(dependency)
                self.assertEqual(ET.tostring(dependency),ET.tostring(original.find(f'.//{{{SVG}}}linearGradient[@id="fixedAlpha"]')))
            truth=np.asarray(Image.open(folder/'source.png').convert('RGBA'),dtype=float)
            target=truth[:,:,:3]*(truth[:,:,3:4]/255.)
            initial=_render(original,folder/'initial_probe.svg',folder/'initial.png')
            fitted=_render(ET.parse(folder/'flat.svg').getroot(),folder/'final_probe.svg',folder/'final.png')
            self.assertLess(float(np.mean((fitted-target)**2)),float(np.mean((initial-target)**2))*.05)
            np.testing.assert_equal(np.asarray(Image.open(folder/'initial.png'))[:,:,3],np.asarray(Image.open(folder/'final.png'))[:,:,3])
            diagnostic=json.loads((folder/'fit.json').read_text())
            self.assertIn('untouched_test_mse',diagnostic['flat_surrogate'])
            self.assertIn('Atotal-As',diagnostic['objective'])
```

### `FitterTests._fixture` — `Lines 16–28`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `28` (`Lines 16–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–28`):**
```python
    def _fixture(self, folder, alpha=False):
        defs='<defs><linearGradient id="fixedAlpha" x1="0" y1="0" x2="64" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".15"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient><mask id="fixedMask" style="mask-type:alpha" mask-type="alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="48"><path fill="url(#fixedAlpha)" d="M0 0H64V48H0Z"/></mask></defs>' if alpha else ''
        group=' mask="url(#fixedMask)"' if alpha else ''
        paths='<path fill="#143c50" d="M0 0H64V48H0Z"/><path opacity=".5" fill="#d25a1e" d="M12 7H58V39H12Z"/><path fill="#1eb4c8" d="M30.2 3H30.8V46H30.2Z"/>'
        truth=f'<svg xmlns="{SVG}" width="64" height="48">{defs}<g{group}>{paths}</g></svg>'
        source=folder/'source.svg';source.write_text(truth)
        _render(ET.fromstring(truth),folder/'render_input.svg',folder/'source.png')
        root=ET.fromstring(truth)
        # Change only visible paint, preserving the soft alpha dependency.
        visible=root.find(f'{{{SVG}}}g')
        for path in visible:path.set('fill','#777777')
        baseline=folder/'baseline.svg';ET.ElementTree(root).write(baseline,encoding='utf-8')
        return source,baseline
```

### `FitterTests.test_source_over_coefficients_recover_thin_support` — `Lines 30–44`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `44` (`Lines 30–44`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–44`):**
```python
    def test_source_over_coefficients_recover_thin_support(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);_,baseline=self._fixture(folder)
            metadata=build_maps(baseline,folder/'maps')
            self.assertLess(metadata['closure_max'],.02)
            self.assertLess(metadata['random_forward_rmse_bytes'],1.5)
            with np.load(folder/'maps/maps.npz') as values:
                w=values['weights'].reshape(3,48,64)
                self.assertGreater(w[2].sum(),0)
                self.assertLess(w[2].max(),1)
                self.assertAlmostEqual(float(w[1,15,20]),.5,delta=.01)
                self.assertAlmostEqual(float(w[0,15,20]),.5,delta=.01)
            self.assertEqual(build_maps(baseline,folder/'maps')['maps_npz_sha256'],metadata['maps_npz_sha256'])
            with (folder/'maps/maps.npz').open('ab') as stream:stream.write(b'corruption')
            with self.assertRaisesRegex(ValueError,'cache drift'):build_maps(baseline,folder/'maps')
```

### `FitterTests.test_joint_fit_preserves_soft_alpha_gradient_and_improves_render` — `Lines 46–66`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `46` إلى السطر `66` (`Lines 46–66`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 46–66`):**
```python
    def test_joint_fit_preserves_soft_alpha_gradient_and_improves_render(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);source,baseline=self._fixture(folder,alpha=True)
            build_maps(baseline,folder/'maps')
            fit_case(folder/'source.png',baseline,baseline,folder/'maps',folder/'flat.svg',folder/'gradient.svg',folder/'fit.json',max_seconds=20)
            original=ET.parse(baseline).getroot()
            for name in ('flat','gradient'):
                root=ET.parse(folder/f'{name}.svg').getroot()
                self.assertEqual(_shape_signature(root),_shape_signature(original))
                dependency=root.find(f'.//{{{SVG}}}linearGradient[@id="fixedAlpha"]')
                self.assertIsNotNone(dependency)
                self.assertEqual(ET.tostring(dependency),ET.tostring(original.find(f'.//{{{SVG}}}linearGradient[@id="fixedAlpha"]')))
            truth=np.asarray(Image.open(folder/'source.png').convert('RGBA'),dtype=float)
            target=truth[:,:,:3]*(truth[:,:,3:4]/255.)
            initial=_render(original,folder/'initial_probe.svg',folder/'initial.png')
            fitted=_render(ET.parse(folder/'flat.svg').getroot(),folder/'final_probe.svg',folder/'final.png')
            self.assertLess(float(np.mean((fitted-target)**2)),float(np.mean((initial-target)**2))*.05)
            np.testing.assert_equal(np.asarray(Image.open(folder/'initial.png'))[:,:,3],np.asarray(Image.open(folder/'final.png'))[:,:,3])
            diagnostic=json.loads((folder/'fit.json').read_text())
            self.assertIn('untouched_test_mse',diagnostic['flat_surrogate'])
            self.assertIn('Atotal-As',diagnostic['objective'])
```
