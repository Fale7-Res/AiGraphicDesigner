# مرآة الكود التفصيلية: `src/test_icc.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/test_icc.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/test_icc.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `18` (`Lines 1–18`)
- **بصمة الملف (`SHA-256`):** `1709d3bbd2b5c3ed92af3ff64296aaca988c38d42d9ae848c57e0fd35dc42143`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `ICCSmoke` | `class` | `Lines 8–15` | `class ICCSmoke(unittest.TestCase):` | رمز برمجي موثق. |
| `ICCSmoke.test_declared_srgb_matches_untagged_assumption` | `method` | `Lines 9–15` | `def test_declared_srgb_matches_untagged_assumption(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `ICCSmoke` — `Lines 8–15`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `15` (`Lines 8–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–15`):**
```python
class ICCSmoke(unittest.TestCase):
    def test_declared_srgb_matches_untagged_assumption(self):
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);rng=np.random.default_rng(91);a=rng.integers(0,256,(32,32,3),dtype=np.uint8)
            p=folder/'tagged.png';q=folder/'normalized.png'
            profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
            Image.fromarray(a).save(p,icc_profile=profile);info=prepare_input(p,q)
            self.assertTrue(info['icc_present']);np.testing.assert_array_equal(a,np.array(Image.open(q)))
```

### `ICCSmoke.test_declared_srgb_matches_untagged_assumption` — `Lines 9–15`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `15` (`Lines 9–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–15`):**
```python
    def test_declared_srgb_matches_untagged_assumption(self):
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);rng=np.random.default_rng(91);a=rng.integers(0,256,(32,32,3),dtype=np.uint8)
            p=folder/'tagged.png';q=folder/'normalized.png'
            profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
            Image.fromarray(a).save(p,icc_profile=profile);info=prepare_input(p,q)
            self.assertTrue(info['icc_present']);np.testing.assert_array_equal(a,np.array(Image.open(q)))
```
