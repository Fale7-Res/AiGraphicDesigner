# مرآة الكود التفصيلية: `test_research.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_research.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_research.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `21` (`Lines 1–21`)
- **بصمة الملف (`SHA-256`):** `cac93455186609a7314591ea53b7543d06bdb12f87517e04c1d56d960edc34e5`
- **الوصف التفصيلي:** """Independent formula and scientific-contract tests; no dataset fitting."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `ResearchTests` | `class` | `Lines 6–19` | `class ResearchTests(unittest.TestCase):` | رمز برمجي موثق. |
| `ResearchTests.test_balanced_background_objective` | `method` | `Lines 7–13` | `def test_balanced_background_objective(self):` | رمز برمجي موثق. |
| `ResearchTests.test_manifest_capacity_and_no_search` | `method` | `Lines 14–19` | `def test_manifest_capacity_and_no_search(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `ResearchTests` — `Lines 6–19`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `19` (`Lines 6–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–19`):**
```python
class ResearchTests(unittest.TestCase):
    def test_balanced_background_objective(self):
        rng=np.random.default_rng(42);p=rng.random((30,3))*255;s=rng.random((30,3))*255
        ar=rng.random((30,1));ass=rng.random((30,1));bg=np.array([[255,255,255],[0,0,0],[40,80,120]])
        actual=np.mean([np.mean((p-s+(ass-ar)*b)**2) for b in bg])
        target=s+(ar-ass)*bg.mean(axis=0)
        constant=np.mean([(ass-ar)**2*(b-bg.mean(axis=0))**2 for b in bg])
        self.assertAlmostEqual(actual,float(np.mean((p-target)**2)+constant),places=9)
    def test_manifest_capacity_and_no_search(self):
        import json
        m=json.loads((r.ROOT/'inputs/manifest.json').read_text())
        self.assertEqual(len(m['cases']),9);self.assertEqual(m['architecture'],'NOT_APPROVED')
        self.assertEqual(sum(c['kind']=='real' for c in m['cases']),5)
        self.assertIn('No tracing/searches',m['protocol']['geometry'])
```

### `ResearchTests.test_balanced_background_objective` — `Lines 7–13`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `13` (`Lines 7–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–13`):**
```python
    def test_balanced_background_objective(self):
        rng=np.random.default_rng(42);p=rng.random((30,3))*255;s=rng.random((30,3))*255
        ar=rng.random((30,1));ass=rng.random((30,1));bg=np.array([[255,255,255],[0,0,0],[40,80,120]])
        actual=np.mean([np.mean((p-s+(ass-ar)*b)**2) for b in bg])
        target=s+(ar-ass)*bg.mean(axis=0)
        constant=np.mean([(ass-ar)**2*(b-bg.mean(axis=0))**2 for b in bg])
        self.assertAlmostEqual(actual,float(np.mean((p-target)**2)+constant),places=9)
```

### `ResearchTests.test_manifest_capacity_and_no_search` — `Lines 14–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `19` (`Lines 14–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–19`):**
```python
    def test_manifest_capacity_and_no_search(self):
        import json
        m=json.loads((r.ROOT/'inputs/manifest.json').read_text())
        self.assertEqual(len(m['cases']),9);self.assertEqual(m['architecture'],'NOT_APPROVED')
        self.assertEqual(sum(c['kind']=='real' for c in m['cases']),5)
        self.assertIn('No tracing/searches',m['protocol']['geometry'])
```
