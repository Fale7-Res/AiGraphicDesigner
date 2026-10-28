# مرآة الكود التفصيلية: `test_bottlenecks.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_bottlenecks.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_bottlenecks.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `72` (`Lines 1–72`)
- **بصمة الملف (`SHA-256`):** `36d0deee61b0febd73bcff5b732723c9d92dcac44b85e388287ddba05d20e9e7`
- **الوصف التفصيلي:** """Saved-result and microgeometry contracts; no historical searches rerun."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `BottleneckTests` | `class` | `Lines 11–69` | `class BottleneckTests(unittest.TestCase):` | رمز برمجي موثق. |
| `BottleneckTests.test_complete_frozen_suite_and_native_metrics` | `method` | `Lines 12–22` | `def test_complete_frozen_suite_and_native_metrics(self):` | رمز برمجي موثق. |
| `BottleneckTests.test_geometry_held_across_fits_and_gradient_safety` | `method` | `Lines 23–32` | `def test_geometry_held_across_fits_and_gradient_safety(self):` | رمز برمجي موثق. |
| `BottleneckTests.test_correction_pairing_and_unchanged_underlying_paths` | `method` | `Lines 33–42` | `def test_correction_pairing_and_unchanged_underlying_paths(self):` | رمز برمجي موثق. |
| `BottleneckTests.test_visibility_does_not_hide_tiny_regions_or_count_occlusion` | `method` | `Lines 43–51` | `def test_visibility_does_not_hide_tiny_regions_or_count_occlusion(self):` | رمز برمجي موثق. |
| `BottleneckTests.test_monitor_timeout_is_bounded_and_reported` | `method` | `Lines 52–56` | `def test_monitor_timeout_is_bounded_and_reported(self):` | رمز برمجي موثق. |
| `BottleneckTests.test_cycle_inventory_rejects_missing_and_modified_artifacts` | `method` | `Lines 57–69` | `def test_cycle_inventory_rejects_missing_and_modified_artifacts(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `BottleneckTests` — `Lines 11–69`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `69` (`Lines 11–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–69`):**
```python
class BottleneckTests(unittest.TestCase):
    def test_complete_frozen_suite_and_native_metrics(self):
        cases=json.loads((ROOT/'inputs/manifest.json').read_text())['cases'];self.assertEqual(len(cases),7)
        for case in cases:
            b.paths_for_case(case);folder=ROOT/'results/granularity'/case['id'];data=json.loads((folder/'result.json').read_text())
            self.assertEqual(set(data['levels']),{'128','192','256'})
            for detail,row in data['levels'].items():
                for name,condition in row['conditions'].items():
                    svg=folder/detail/name/'output.svg';self.assertEqual(b.inherited.digest(svg),condition['sha256'])
                    source=Image.open(folder/'source.png').convert('RGBA');ref=Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')
                    pred=Image.open(folder/detail/name/'white.png').convert('RGB');mse=float(np.mean((np.asarray(ref,dtype=float)-np.asarray(pred,dtype=float))**2))
                    self.assertAlmostEqual(mse,condition['metrics']['white']['mse'],places=10)
    def test_geometry_held_across_fits_and_gradient_safety(self):
        from test_artifacts import geometry_tree
        for folder in (ROOT/'results/granularity').iterdir():
            for detail in ['128','192','256']:
                trees=[ET.parse(folder/detail/k/'output.svg').getroot() for k in 'BCD']
                self.assertEqual(geometry_tree(trees[0]),geometry_tree(trees[1]));self.assertEqual(geometry_tree(trees[1]),geometry_tree(trees[2]))
                for tree in trees:
                    for node in tree.iter():
                        self.assertNotIn(node.tag.rsplit('}',1)[-1],['image','script','foreignObject','filter'])
                        if node.tag.rsplit('}',1)[-1] in ['linearGradient','radialGradient']:self.assertLessEqual(len(node),4)
    def test_correction_pairing_and_unchanged_underlying_paths(self):
        allowed=['stroke','stroke-width','stroke-linejoin','stroke-linecap','paint-order']
        for folder in (ROOT/'results/corrections').iterdir():
            record=json.loads((folder/'result.json').read_text());self.assertEqual(record['baseline_detail'],192)
            baseline=ROOT/'results/granularity'/folder.name/'192/D/output.svg';self.assertEqual(b.inherited.digest(baseline),record['baseline_svg_sha256']);self.assertEqual(b.inherited.digest(folder/'output.svg'),record['sha256'])
            trees=[ET.parse(p).getroot() for p in [baseline,folder/'output.svg']]
            for tree in trees:
                for node in tree.iter():
                    for key in allowed:node.attrib.pop(key,None)
            self.assertEqual(ET.tostring(trees[0]),ET.tostring(trees[1]))
    def test_visibility_does_not_hide_tiny_regions_or_count_occlusion(self):
        with tempfile.TemporaryDirectory() as temporary:
            p=Path(temporary);source=p/'source.png';Image.new('RGB',(10,10),'white').save(source)
            bg='<path d="M0 0H10V10H0Z" fill="#111111"/>';cell='<path d="M3 3H4V4H3Z" fill="#eeeeee"/>'
            for name,paths,expected in [('visible',bg+cell,.01),('occluded',cell+bg,0.)]:
                svg=p/f'{name}.svg';svg.write_text(f'<svg xmlns="{b.SVG}" width="10" height="10">{paths}</svg>')
                record,_=b.visible_geometry(svg,source,p/name);self.assertEqual(record['paths_bbox_le1'],1)
                self.assertAlmostEqual(record['visible_alpha_weighted_area_tiny1_fraction'],expected,places=10)
                self.assertAlmostEqual(record['assigned_visible_alpha_fraction'],1.,places=10)
    def test_monitor_timeout_is_bounded_and_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            record=monitor([sys.executable,'-c','import time; time.sleep(5)'],Path(temporary)/'child.log',timeout=.15)
            self.assertEqual(record['termination_reason'],'timeout');self.assertLess(record['wall_seconds'],4)
            self.assertEqual(record['cleanup_unverified_pids'],[])
    def test_cycle_inventory_rejects_missing_and_modified_artifacts(self):
        import run_cycle
        old=run_cycle.ROOT
        try:
            with tempfile.TemporaryDirectory() as temporary:
                run_cycle.ROOT=Path(temporary);target=run_cycle.ROOT/'results/example';target.mkdir(parents=True)
                file=target/'output.svg';file.write_text('<svg/>');run_cycle.artifact_inventory(target)
                run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
                file.write_text('<svg>changed</svg>')
                with self.assertRaises(AssertionError):run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
                file.unlink()
                with self.assertRaises(AssertionError):run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
        finally:run_cycle.ROOT=old
```

### `BottleneckTests.test_complete_frozen_suite_and_native_metrics` — `Lines 12–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `22` (`Lines 12–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–22`):**
```python
    def test_complete_frozen_suite_and_native_metrics(self):
        cases=json.loads((ROOT/'inputs/manifest.json').read_text())['cases'];self.assertEqual(len(cases),7)
        for case in cases:
            b.paths_for_case(case);folder=ROOT/'results/granularity'/case['id'];data=json.loads((folder/'result.json').read_text())
            self.assertEqual(set(data['levels']),{'128','192','256'})
            for detail,row in data['levels'].items():
                for name,condition in row['conditions'].items():
                    svg=folder/detail/name/'output.svg';self.assertEqual(b.inherited.digest(svg),condition['sha256'])
                    source=Image.open(folder/'source.png').convert('RGBA');ref=Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')
                    pred=Image.open(folder/detail/name/'white.png').convert('RGB');mse=float(np.mean((np.asarray(ref,dtype=float)-np.asarray(pred,dtype=float))**2))
                    self.assertAlmostEqual(mse,condition['metrics']['white']['mse'],places=10)
```

### `BottleneckTests.test_geometry_held_across_fits_and_gradient_safety` — `Lines 23–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `32` (`Lines 23–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–32`):**
```python
    def test_geometry_held_across_fits_and_gradient_safety(self):
        from test_artifacts import geometry_tree
        for folder in (ROOT/'results/granularity').iterdir():
            for detail in ['128','192','256']:
                trees=[ET.parse(folder/detail/k/'output.svg').getroot() for k in 'BCD']
                self.assertEqual(geometry_tree(trees[0]),geometry_tree(trees[1]));self.assertEqual(geometry_tree(trees[1]),geometry_tree(trees[2]))
                for tree in trees:
                    for node in tree.iter():
                        self.assertNotIn(node.tag.rsplit('}',1)[-1],['image','script','foreignObject','filter'])
                        if node.tag.rsplit('}',1)[-1] in ['linearGradient','radialGradient']:self.assertLessEqual(len(node),4)
```

### `BottleneckTests.test_correction_pairing_and_unchanged_underlying_paths` — `Lines 33–42`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `33` إلى السطر `42` (`Lines 33–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 33–42`):**
```python
    def test_correction_pairing_and_unchanged_underlying_paths(self):
        allowed=['stroke','stroke-width','stroke-linejoin','stroke-linecap','paint-order']
        for folder in (ROOT/'results/corrections').iterdir():
            record=json.loads((folder/'result.json').read_text());self.assertEqual(record['baseline_detail'],192)
            baseline=ROOT/'results/granularity'/folder.name/'192/D/output.svg';self.assertEqual(b.inherited.digest(baseline),record['baseline_svg_sha256']);self.assertEqual(b.inherited.digest(folder/'output.svg'),record['sha256'])
            trees=[ET.parse(p).getroot() for p in [baseline,folder/'output.svg']]
            for tree in trees:
                for node in tree.iter():
                    for key in allowed:node.attrib.pop(key,None)
            self.assertEqual(ET.tostring(trees[0]),ET.tostring(trees[1]))
```

### `BottleneckTests.test_visibility_does_not_hide_tiny_regions_or_count_occlusion` — `Lines 43–51`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `43` إلى السطر `51` (`Lines 43–51`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 43–51`):**
```python
    def test_visibility_does_not_hide_tiny_regions_or_count_occlusion(self):
        with tempfile.TemporaryDirectory() as temporary:
            p=Path(temporary);source=p/'source.png';Image.new('RGB',(10,10),'white').save(source)
            bg='<path d="M0 0H10V10H0Z" fill="#111111"/>';cell='<path d="M3 3H4V4H3Z" fill="#eeeeee"/>'
            for name,paths,expected in [('visible',bg+cell,.01),('occluded',cell+bg,0.)]:
                svg=p/f'{name}.svg';svg.write_text(f'<svg xmlns="{b.SVG}" width="10" height="10">{paths}</svg>')
                record,_=b.visible_geometry(svg,source,p/name);self.assertEqual(record['paths_bbox_le1'],1)
                self.assertAlmostEqual(record['visible_alpha_weighted_area_tiny1_fraction'],expected,places=10)
                self.assertAlmostEqual(record['assigned_visible_alpha_fraction'],1.,places=10)
```

### `BottleneckTests.test_monitor_timeout_is_bounded_and_reported` — `Lines 52–56`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `52` إلى السطر `56` (`Lines 52–56`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 52–56`):**
```python
    def test_monitor_timeout_is_bounded_and_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            record=monitor([sys.executable,'-c','import time; time.sleep(5)'],Path(temporary)/'child.log',timeout=.15)
            self.assertEqual(record['termination_reason'],'timeout');self.assertLess(record['wall_seconds'],4)
            self.assertEqual(record['cleanup_unverified_pids'],[])
```

### `BottleneckTests.test_cycle_inventory_rejects_missing_and_modified_artifacts` — `Lines 57–69`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `69` (`Lines 57–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–69`):**
```python
    def test_cycle_inventory_rejects_missing_and_modified_artifacts(self):
        import run_cycle
        old=run_cycle.ROOT
        try:
            with tempfile.TemporaryDirectory() as temporary:
                run_cycle.ROOT=Path(temporary);target=run_cycle.ROOT/'results/example';target.mkdir(parents=True)
                file=target/'output.svg';file.write_text('<svg/>');run_cycle.artifact_inventory(target)
                run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
                file.write_text('<svg>changed</svg>')
                with self.assertRaises(AssertionError):run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
                file.unlink()
                with self.assertRaises(AssertionError):run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
        finally:run_cycle.ROOT=old
```
