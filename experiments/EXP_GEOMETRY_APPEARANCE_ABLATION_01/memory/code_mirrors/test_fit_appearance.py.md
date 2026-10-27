# مرآة الكود التفصيلية: `test_fit_appearance.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_fit_appearance.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_fit_appearance.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `86` (`Lines 1–86`)
- **بصمة الملف (`SHA-256`):** `53bb075bb9d01054b9f226f8d91a465343dc43e53369cd06cf38559a55ef32e9`
- **الوصف التفصيلي:** # START CHANGE EXP-GEOMETRY-APPEARANCE-01 | 2026-10-27T14:43:00Z | CREATED | Author: /root/appearance_fit

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `AppearanceTests` | `class` | `Lines 18–81` | `class AppearanceTests(unittest.TestCase):` | رمز برمجي موثق. |
| `AppearanceTests.test_alpha_squared_weighted_flat` | `method` | `Lines 19–25` | `def test_alpha_squared_weighted_flat(self):` | رمز برمجي موثق. |
| `AppearanceTests.test_basis_partition_and_clamp` | `method` | `Lines 27–32` | `def test_basis_partition_and_clamp(self):` | رمز برمجي موثق. |
| `AppearanceTests.test_affine_transform_order` | `method` | `Lines 34–38` | `def test_affine_transform_order(self):` | رمز برمجي موثق. |
| `AppearanceTests.test_linear_render_geometry_and_translation` | `method` | `Lines 41–42` | `def test_linear_render_geometry_and_translation(self):` | رمز برمجي موثق. |
| `AppearanceTests.test_radial_render_and_holdout` | `method` | `Lines 45–46` | `def test_radial_render_and_holdout(self):` | رمز برمجي موثق. |
| `AppearanceTests._control` | `method` | `Lines 48–81` | `def _control(self, kind):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `AppearanceTests` — `Lines 18–81`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `81` (`Lines 18–81`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–81`):**
```python
class AppearanceTests(unittest.TestCase):
    def test_alpha_squared_weighted_flat(self):
        xy = np.array([[0., 0.], [1., 0.], [2., 0.], [3., 0.]])
        rgb = np.array([[0., 0., 0.], [255., 255., 255.], [51., 51., 51.], [51., 51., 51.]])
        flat, selected, diagnostic = _fit_region(xy, rgb, np.array([0, 1]), np.array([2]), np.array([3]), time.monotonic() + 10, np.array([1., .25, 1., 1.]))
        np.testing.assert_allclose(flat["colors"], [[51., 51., 51.]])
        self.assertEqual(selected["kind"], "flat")
        self.assertAlmostEqual(diagnostic["selected_test_mse"], 0.)

    def test_basis_partition_and_clamp(self):
        b = _basis(np.array([-2., 0, .2, .7, 1, 2]), 4)
        np.testing.assert_allclose(b.sum(axis=1), 1)
        self.assertTrue(np.all(b >= 0))
        np.testing.assert_allclose(b[0], [1, 0, 0, 0])
        np.testing.assert_allclose(b[-1], [0, 0, 0, 1])

    def test_affine_transform_order(self):
        matrix = _matrix("translate(10 5) scale(2,3)")
        np.testing.assert_allclose(matrix @ [1, 2, 1], [12, 11, 1])
        with self.assertRaises(ValueError):
            _matrix("nonsense(1)")

    @unittest.skipUnless(os.environ.get("AGD_RENDERER_EXE"), "Actual resvg executable required")
    def test_linear_render_geometry_and_translation(self):
        self._control("linear")

    @unittest.skipUnless(os.environ.get("AGD_RENDERER_EXE"), "Actual resvg executable required")
    def test_radial_render_and_holdout(self):
        self._control("radial")

    def _control(self, kind):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            baseline = folder / "baseline.svg"
            geometry = '<g transform="translate(8,6)"><path transform="translate(2,3)" d="M -10 -9 L 54 -9 L 54 55 L -10 55 Z" fill="#777777"/></g>'
            baseline.write_text(f'<svg xmlns="{SVG}" width="64" height="64">{geometry}</svg>', encoding="utf-8")
            if kind == "linear":
                gradient = '<linearGradient id="ref" gradientUnits="userSpaceOnUse" x1="-10" y1="0" x2="54" y2="0"><stop offset="0" stop-color="#14283c"/><stop offset="1" stop-color="#dcaa78"/></linearGradient>'
            else:
                gradient = '<radialGradient id="ref" gradientUnits="userSpaceOnUse" cx="22" cy="23" r="45"><stop offset="0" stop-color="#f0dfc0"/><stop offset="1" stop-color="#203040"/></radialGradient>'
            source = folder / "source.svg"
            source.write_text(f'<svg xmlns="{SVG}" width="64" height="64"><defs>{gradient}</defs>{geometry.replace(chr(35)+"777777", "url(#ref)")}</svg>', encoding="utf-8")
            png = folder / "source.png"
            subprocess.run([os.environ["AGD_RENDERER_EXE"], str(source), str(png)], check=True, capture_output=True)
            c, d, info = folder / "c.svg", folder / "d.svg", folder / "diagnostic.json"
            result = fit_svg(png, baseline, c, d, info, deadline_seconds=30)
            cpaths, dpaths = _paths(ET.parse(c).getroot()), _paths(ET.parse(d).getroot())
            self.assertEqual(len(cpaths), len(dpaths))
            for (cp, cm), (dp, dm) in zip(cpaths, dpaths):
                self.assertEqual({k: v for k, v in cp.attrib.items() if k != "fill"}, {k: v for k, v in dp.attrib.items() if k != "fill"})
                np.testing.assert_equal(cm, dm)
            stops = ET.parse(d).getroot().findall(f".//{{{SVG}}}stop")
            self.assertTrue(2 <= len(stops) <= 4)
            region = result["regions"][0]
            self.assertGreater(region["test_count"], 0)
            self.assertLess(region["selected_test_mse"], region["flat_test_mse"] * .1)
            self.assertLessEqual(region["optimizer_evaluations"], 100)
            for svg in (c, d):
                subprocess.run([os.environ["AGD_RENDERER_EXE"], str(svg), str(svg.with_suffix(".png"))], check=True, capture_output=True)
            reference = np.asarray(Image.open(png).convert("RGB"), dtype=float)
            crender = np.asarray(Image.open(c.with_suffix(".png")).convert("RGB"), dtype=float)
            drender = np.asarray(Image.open(d.with_suffix(".png")).convert("RGB"), dtype=float)
            self.assertLess(np.mean((drender-reference)**2), np.mean((crender-reference)**2) * .1)
            self.assertEqual(json.loads(info.read_text())["path_count"], 1)
```

### `AppearanceTests.test_alpha_squared_weighted_flat` — `Lines 19–25`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `25` (`Lines 19–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–25`):**
```python
    def test_alpha_squared_weighted_flat(self):
        xy = np.array([[0., 0.], [1., 0.], [2., 0.], [3., 0.]])
        rgb = np.array([[0., 0., 0.], [255., 255., 255.], [51., 51., 51.], [51., 51., 51.]])
        flat, selected, diagnostic = _fit_region(xy, rgb, np.array([0, 1]), np.array([2]), np.array([3]), time.monotonic() + 10, np.array([1., .25, 1., 1.]))
        np.testing.assert_allclose(flat["colors"], [[51., 51., 51.]])
        self.assertEqual(selected["kind"], "flat")
        self.assertAlmostEqual(diagnostic["selected_test_mse"], 0.)
```

### `AppearanceTests.test_basis_partition_and_clamp` — `Lines 27–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `32` (`Lines 27–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–32`):**
```python
    def test_basis_partition_and_clamp(self):
        b = _basis(np.array([-2., 0, .2, .7, 1, 2]), 4)
        np.testing.assert_allclose(b.sum(axis=1), 1)
        self.assertTrue(np.all(b >= 0))
        np.testing.assert_allclose(b[0], [1, 0, 0, 0])
        np.testing.assert_allclose(b[-1], [0, 0, 0, 1])
```

### `AppearanceTests.test_affine_transform_order` — `Lines 34–38`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `38` (`Lines 34–38`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–38`):**
```python
    def test_affine_transform_order(self):
        matrix = _matrix("translate(10 5) scale(2,3)")
        np.testing.assert_allclose(matrix @ [1, 2, 1], [12, 11, 1])
        with self.assertRaises(ValueError):
            _matrix("nonsense(1)")
```

### `AppearanceTests.test_linear_render_geometry_and_translation` — `Lines 41–42`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `42` (`Lines 41–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 41–42`):**
```python
    def test_linear_render_geometry_and_translation(self):
        self._control("linear")
```

### `AppearanceTests.test_radial_render_and_holdout` — `Lines 45–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `45` إلى السطر `46` (`Lines 45–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 45–46`):**
```python
    def test_radial_render_and_holdout(self):
        self._control("radial")
```

### `AppearanceTests._control` — `Lines 48–81`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `81` (`Lines 48–81`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–81`):**
```python
    def _control(self, kind):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            baseline = folder / "baseline.svg"
            geometry = '<g transform="translate(8,6)"><path transform="translate(2,3)" d="M -10 -9 L 54 -9 L 54 55 L -10 55 Z" fill="#777777"/></g>'
            baseline.write_text(f'<svg xmlns="{SVG}" width="64" height="64">{geometry}</svg>', encoding="utf-8")
            if kind == "linear":
                gradient = '<linearGradient id="ref" gradientUnits="userSpaceOnUse" x1="-10" y1="0" x2="54" y2="0"><stop offset="0" stop-color="#14283c"/><stop offset="1" stop-color="#dcaa78"/></linearGradient>'
            else:
                gradient = '<radialGradient id="ref" gradientUnits="userSpaceOnUse" cx="22" cy="23" r="45"><stop offset="0" stop-color="#f0dfc0"/><stop offset="1" stop-color="#203040"/></radialGradient>'
            source = folder / "source.svg"
            source.write_text(f'<svg xmlns="{SVG}" width="64" height="64"><defs>{gradient}</defs>{geometry.replace(chr(35)+"777777", "url(#ref)")}</svg>', encoding="utf-8")
            png = folder / "source.png"
            subprocess.run([os.environ["AGD_RENDERER_EXE"], str(source), str(png)], check=True, capture_output=True)
            c, d, info = folder / "c.svg", folder / "d.svg", folder / "diagnostic.json"
            result = fit_svg(png, baseline, c, d, info, deadline_seconds=30)
            cpaths, dpaths = _paths(ET.parse(c).getroot()), _paths(ET.parse(d).getroot())
            self.assertEqual(len(cpaths), len(dpaths))
            for (cp, cm), (dp, dm) in zip(cpaths, dpaths):
                self.assertEqual({k: v for k, v in cp.attrib.items() if k != "fill"}, {k: v for k, v in dp.attrib.items() if k != "fill"})
                np.testing.assert_equal(cm, dm)
            stops = ET.parse(d).getroot().findall(f".//{{{SVG}}}stop")
            self.assertTrue(2 <= len(stops) <= 4)
            region = result["regions"][0]
            self.assertGreater(region["test_count"], 0)
            self.assertLess(region["selected_test_mse"], region["flat_test_mse"] * .1)
            self.assertLessEqual(region["optimizer_evaluations"], 100)
            for svg in (c, d):
                subprocess.run([os.environ["AGD_RENDERER_EXE"], str(svg), str(svg.with_suffix(".png"))], check=True, capture_output=True)
            reference = np.asarray(Image.open(png).convert("RGB"), dtype=float)
            crender = np.asarray(Image.open(c.with_suffix(".png")).convert("RGB"), dtype=float)
            drender = np.asarray(Image.open(d.with_suffix(".png")).convert("RGB"), dtype=float)
            self.assertLess(np.mean((drender-reference)**2), np.mean((crender-reference)**2) * .1)
            self.assertEqual(json.loads(info.read_text())["path_count"], 1)
```
