# مرآة الكود التفصيلية: `test_oracle.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_oracle.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_oracle.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `68` (`Lines 1–68`)
- **بصمة الملف (`SHA-256`):** `5887523b46c0593d7c7f68c621b1fd3ec97eda0d690ae8e4d84652f6bf8b3c24`
- **الوصف التفصيلي:** # START CHANGE AGD-BOTTLENECK-ORACLE-TEST | 2026-10-27T15:30:59Z | CREATED | Author: /root/appearance_fit

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `OracleTests` | `class` | `Lines 13–63` | `class OracleTests(unittest.TestCase):` | رمز برمجي موثق. |
| `OracleTests.test_saved_oracle_artifact_geometry_and_gradient_limits` | `method` | `Lines 14–30` | `def test_saved_oracle_artifact_geometry_and_gradient_limits(self):` | رمز برمجي موثق. |
| `OracleTests.test_saved_native_mse_matches_actual_render` | `method` | `Lines 32–48` | `def test_saved_native_mse_matches_actual_render(self):` | رمز برمجي موثق. |
| `OracleTests.test_init_preserves_every_geometry_attribute_and_solid_paint` | `method` | `Lines 50–63` | `def test_init_preserves_every_geometry_attribute_and_solid_paint(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `OracleTests` — `Lines 13–63`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `63` (`Lines 13–63`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–63`):**
```python
class OracleTests(unittest.TestCase):
    def test_saved_oracle_artifact_geometry_and_gradient_limits(self):
        results = Path(__file__).parent / "results/oracle"
        if not results.exists():
            self.skipTest("Oracle outputs not generated")
        for folder in results.iterdir():
            if not folder.is_dir():
                continue
            signatures = []
            for name in ("oracle_truth", "oracle_init", "oracle_C", "oracle_D"):
                root = ET.parse(folder / f"{name}.svg").getroot()
                signatures.append([dict((k,v) for k,v in path.attrib.items() if k != "fill") for path in root.iter(f"{{{SVG}}}path")])
                self.assertFalse(list(root.iter(f"{{{SVG}}}image")))
            self.assertTrue(all(signature == signatures[0] for signature in signatures))
            root = ET.parse(folder / "oracle_D.svg").getroot()
            for kind in ("linearGradient", "radialGradient"):
                for gradient in root.iter(f"{{{SVG}}}{kind}"):
                    self.assertLessEqual(len(list(gradient)), 4)

    def test_saved_native_mse_matches_actual_render(self):
        results = Path(__file__).parent / "results/oracle"
        if not results.exists():
            self.skipTest("Oracle outputs not generated")
        for folder in results.iterdir():
            if not folder.is_dir():
                continue
            record = json.loads((folder / "result.json").read_text())
            if "oracle_truth" in record["conditions"]:
                self.assertEqual(record["conditions"]["oracle_truth"]["metrics"]["white"]["mse"], 0)
                self.assertTrue(record["ground_truth_reuse"]["fresh_native_svg_check_performed"])
                self.assertTrue(record["representability"]["all_regions_refitted_from_samples"])
            source = np.asarray(Image.open(folder / "source.png").convert("RGB"), dtype=float)
            for condition in ("oracle_init", "oracle_C", "oracle_D"):
                render = np.asarray(Image.open(folder / condition / "white.png").convert("RGB"), dtype=float)
                self.assertEqual(float(np.mean((source - render) ** 2)), record["conditions"][condition]["metrics"]["white"]["mse"])
            self.assertEqual(hashlib.sha256((folder / "oracle_truth.svg").read_bytes()).hexdigest(), record["ground_truth_reuse"]["svg_sha256"])

    def test_init_preserves_every_geometry_attribute_and_solid_paint(self):
        source = f'<svg xmlns="{SVG}" width="20" height="20"><defs><linearGradient id="g"><stop offset="0" stop-color="#000"/></linearGradient></defs><path d="M0 0H20V20H0Z" fill="#abcdef"/><path transform="translate(1 2)" fill-rule="evenodd" d="M1 1L5 1L5 5Z" fill="url(#g)"/></svg>'
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/"a.svg", Path(directory)/"b.svg"
            a.write_text(source)
            self.assertEqual(flat_initialization(a, b), [1])
            original, changed = ET.parse(a).getroot(), ET.parse(b).getroot()
            old_paths, new_paths = list(original.iter(f"{{{SVG}}}path")), list(changed.iter(f"{{{SVG}}}path"))
            self.assertEqual(len(old_paths), len(new_paths))
            for old, new in zip(old_paths, new_paths):
                self.assertEqual({k:v for k,v in old.attrib.items() if k != "fill"}, {k:v for k,v in new.attrib.items() if k != "fill"})
            self.assertEqual(new_paths[0].get("fill"), "#abcdef")
            self.assertEqual(new_paths[1].get("fill"), "#777777")
            self.assertEqual(len(list(changed.iter(f"{{{SVG}}}linearGradient"))), 0)
```

### `OracleTests.test_saved_oracle_artifact_geometry_and_gradient_limits` — `Lines 14–30`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `30` (`Lines 14–30`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–30`):**
```python
    def test_saved_oracle_artifact_geometry_and_gradient_limits(self):
        results = Path(__file__).parent / "results/oracle"
        if not results.exists():
            self.skipTest("Oracle outputs not generated")
        for folder in results.iterdir():
            if not folder.is_dir():
                continue
            signatures = []
            for name in ("oracle_truth", "oracle_init", "oracle_C", "oracle_D"):
                root = ET.parse(folder / f"{name}.svg").getroot()
                signatures.append([dict((k,v) for k,v in path.attrib.items() if k != "fill") for path in root.iter(f"{{{SVG}}}path")])
                self.assertFalse(list(root.iter(f"{{{SVG}}}image")))
            self.assertTrue(all(signature == signatures[0] for signature in signatures))
            root = ET.parse(folder / "oracle_D.svg").getroot()
            for kind in ("linearGradient", "radialGradient"):
                for gradient in root.iter(f"{{{SVG}}}{kind}"):
                    self.assertLessEqual(len(list(gradient)), 4)
```

### `OracleTests.test_saved_native_mse_matches_actual_render` — `Lines 32–48`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `48` (`Lines 32–48`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–48`):**
```python
    def test_saved_native_mse_matches_actual_render(self):
        results = Path(__file__).parent / "results/oracle"
        if not results.exists():
            self.skipTest("Oracle outputs not generated")
        for folder in results.iterdir():
            if not folder.is_dir():
                continue
            record = json.loads((folder / "result.json").read_text())
            if "oracle_truth" in record["conditions"]:
                self.assertEqual(record["conditions"]["oracle_truth"]["metrics"]["white"]["mse"], 0)
                self.assertTrue(record["ground_truth_reuse"]["fresh_native_svg_check_performed"])
                self.assertTrue(record["representability"]["all_regions_refitted_from_samples"])
            source = np.asarray(Image.open(folder / "source.png").convert("RGB"), dtype=float)
            for condition in ("oracle_init", "oracle_C", "oracle_D"):
                render = np.asarray(Image.open(folder / condition / "white.png").convert("RGB"), dtype=float)
                self.assertEqual(float(np.mean((source - render) ** 2)), record["conditions"][condition]["metrics"]["white"]["mse"])
            self.assertEqual(hashlib.sha256((folder / "oracle_truth.svg").read_bytes()).hexdigest(), record["ground_truth_reuse"]["svg_sha256"])
```

### `OracleTests.test_init_preserves_every_geometry_attribute_and_solid_paint` — `Lines 50–63`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `63` (`Lines 50–63`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 50–63`):**
```python
    def test_init_preserves_every_geometry_attribute_and_solid_paint(self):
        source = f'<svg xmlns="{SVG}" width="20" height="20"><defs><linearGradient id="g"><stop offset="0" stop-color="#000"/></linearGradient></defs><path d="M0 0H20V20H0Z" fill="#abcdef"/><path transform="translate(1 2)" fill-rule="evenodd" d="M1 1L5 1L5 5Z" fill="url(#g)"/></svg>'
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/"a.svg", Path(directory)/"b.svg"
            a.write_text(source)
            self.assertEqual(flat_initialization(a, b), [1])
            original, changed = ET.parse(a).getroot(), ET.parse(b).getroot()
            old_paths, new_paths = list(original.iter(f"{{{SVG}}}path")), list(changed.iter(f"{{{SVG}}}path"))
            self.assertEqual(len(old_paths), len(new_paths))
            for old, new in zip(old_paths, new_paths):
                self.assertEqual({k:v for k,v in old.attrib.items() if k != "fill"}, {k:v for k,v in new.attrib.items() if k != "fill"})
            self.assertEqual(new_paths[0].get("fill"), "#abcdef")
            self.assertEqual(new_paths[1].get("fill"), "#777777")
            self.assertEqual(len(list(changed.iter(f"{{{SVG}}}linearGradient"))), 0)
```
