# مرآة الكود التفصيلية: `src/test_search.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/test_search.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/test_search.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `36` (`Lines 1–36`)
- **بصمة الملف (`SHA-256`):** `951c568cf793e39298ba7a60321f3d225e30d7bc98a2abf8f48c8e1ede57a03a`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SearchTests` | `class` | `Lines 9–32` | `class SearchTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SearchTests.test_exact_owner_mapping_and_budget` | `method` | `Lines 10–15` | `def test_exact_owner_mapping_and_budget(self):` | رمز برمجي موثق. |
| `SearchTests.test_alpha_normalization_and_original_immutable` | `method` | `Lines 16–22` | `def test_alpha_normalization_and_original_immutable(self):` | رمز برمجي موثق. |
| `SearchTests.test_multimetric_score_and_empty_edges` | `method` | `Lines 23–26` | `def test_multimetric_score_and_empty_edges(self):` | رمز برمجي موثق. |
| `SearchTests.test_native_pixel_worker` | `method` | `Lines 27–32` | `def test_native_pixel_worker(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SearchTests` — `Lines 9–32`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `32` (`Lines 9–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–32`):**
```python
class SearchTests(unittest.TestCase):
    def test_exact_owner_mapping_and_budget(self):
        pilots=pilot_configs();self.assertEqual(pilots[0],OWNER)
        self.assertEqual(OWNER['layer_difference'],0);self.assertEqual(OWNER['simplify'],1.5)
        self.assertEqual(len(pilots),13);self.assertEqual(len(refined_configs(OWNER)),4)
        self.assertEqual({p['clustering'] for p in pilots},{'color-cluster','watershed','bw'})
        self.assertEqual({p['hierarchical'] for p in pilots},{'cutout','stacked'})
    def test_alpha_normalization_and_original_immutable(self):
        with tempfile.TemporaryDirectory() as folder:
            src=Path(folder)/'source.png';out=Path(folder)/'normalized.png'
            a=np.array([[[200,0,0,0],[0,0,0,255],[255,0,0,128]]],dtype=np.uint8);Image.fromarray(a,'RGBA').save(src);original=src.read_bytes()
            info=prepare_input(src,out);actual=np.array(Image.open(out))
            np.testing.assert_array_equal(actual[0],[[255,255,255],[0,0,0],[255,127,127]])
            self.assertEqual(src.read_bytes(),original);self.assertEqual(info['alpha_extrema'],[0,255])
    def test_multimetric_score_and_empty_edges(self):
        m={'ssim':1.,'psnr_db':None,'identical':True,'edge_f1_1_5px':None,'delta_e76_mean':0.,'highpass_rmse_sigma1':0.}
        self.assertAlmostEqual(fidelity_score(m),1.)
        for k,v in [('ssim',.5),('delta_e76_mean',10),('highpass_rmse_sigma1',10),('edge_f1_1_5px',.5)]:self.assertLess(fidelity_score(m|{k:v}),1.)
    def test_native_pixel_worker(self):
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);a=np.zeros((16,16,3),dtype=np.uint8);a[:8]=[255,0,0];a[8:]=[0,120,255];source=folder/'s.png';Image.fromarray(a).save(source)
            r=run_trial(source,folder/'trial',OWNER|{'mode':'pixel','simplify':None})
            self.assertEqual(r['status'],'ok',r);self.assertTrue(r['structure']['raster_free']);self.assertGreater(r['metrics']['ssim'],.95)
            self.assertEqual(r['vtracer_version'],'1.0.0a4')
```

### `SearchTests.test_exact_owner_mapping_and_budget` — `Lines 10–15`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `15` (`Lines 10–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–15`):**
```python
    def test_exact_owner_mapping_and_budget(self):
        pilots=pilot_configs();self.assertEqual(pilots[0],OWNER)
        self.assertEqual(OWNER['layer_difference'],0);self.assertEqual(OWNER['simplify'],1.5)
        self.assertEqual(len(pilots),13);self.assertEqual(len(refined_configs(OWNER)),4)
        self.assertEqual({p['clustering'] for p in pilots},{'color-cluster','watershed','bw'})
        self.assertEqual({p['hierarchical'] for p in pilots},{'cutout','stacked'})
```

### `SearchTests.test_alpha_normalization_and_original_immutable` — `Lines 16–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `22` (`Lines 16–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–22`):**
```python
    def test_alpha_normalization_and_original_immutable(self):
        with tempfile.TemporaryDirectory() as folder:
            src=Path(folder)/'source.png';out=Path(folder)/'normalized.png'
            a=np.array([[[200,0,0,0],[0,0,0,255],[255,0,0,128]]],dtype=np.uint8);Image.fromarray(a,'RGBA').save(src);original=src.read_bytes()
            info=prepare_input(src,out);actual=np.array(Image.open(out))
            np.testing.assert_array_equal(actual[0],[[255,255,255],[0,0,0],[255,127,127]])
            self.assertEqual(src.read_bytes(),original);self.assertEqual(info['alpha_extrema'],[0,255])
```

### `SearchTests.test_multimetric_score_and_empty_edges` — `Lines 23–26`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `26` (`Lines 23–26`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–26`):**
```python
    def test_multimetric_score_and_empty_edges(self):
        m={'ssim':1.,'psnr_db':None,'identical':True,'edge_f1_1_5px':None,'delta_e76_mean':0.,'highpass_rmse_sigma1':0.}
        self.assertAlmostEqual(fidelity_score(m),1.)
        for k,v in [('ssim',.5),('delta_e76_mean',10),('highpass_rmse_sigma1',10),('edge_f1_1_5px',.5)]:self.assertLess(fidelity_score(m|{k:v}),1.)
```

### `SearchTests.test_native_pixel_worker` — `Lines 27–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `32` (`Lines 27–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–32`):**
```python
    def test_native_pixel_worker(self):
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);a=np.zeros((16,16,3),dtype=np.uint8);a[:8]=[255,0,0];a[8:]=[0,120,255];source=folder/'s.png';Image.fromarray(a).save(source)
            r=run_trial(source,folder/'trial',OWNER|{'mode':'pixel','simplify':None})
            self.assertEqual(r['status'],'ok',r);self.assertTrue(r['structure']['raster_free']);self.assertGreater(r['metrics']['ssim'],.95)
            self.assertEqual(r['vtracer_version'],'1.0.0a4')
```
