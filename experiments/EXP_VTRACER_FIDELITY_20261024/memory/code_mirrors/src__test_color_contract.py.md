# مرآة الكود التفصيلية: `src/test_color_contract.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/test_color_contract.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/test_color_contract.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `58` (`Lines 1–58`)
- **بصمة الملف (`SHA-256`):** `d42703bf1f8618d27247ed4eb8b19a571e433b2470cbd35db2506ecf81549880`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `audit_color_contract` | `function` | `Lines 12–38` | `def audit_color_contract(destination):` | Compare raw alpha and explicit white composition through native SVG rendering. |
| `ColorContractTests` | `class` | `Lines 40–50` | `class ColorContractTests(unittest.TestCase):` | رمز برمجي موثق. |
| `ColorContractTests.test_explicit_white_contract_and_raw_alpha_diagnostic` | `method` | `Lines 41–50` | `def test_explicit_white_contract_and_raw_alpha_diagnostic(self):` | Opaque canonical fixtures retain colors; raw partial alpha is not silently approved. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `audit_color_contract` — `Lines 12–38`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `38` (`Lines 12–38`)
- **الوظيفة:** Compare raw alpha and explicit white composition through native SVG rendering.
- **الكود الفعلي (`Lines 12–38`):**
```python
def audit_color_contract(destination):
    """Compare raw alpha and explicit white composition through native SVG rendering."""
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    fixtures={}
    a=np.zeros((16,16,4),np.uint8);a[:]=[255,0,0,128];fixtures['partial_red']=a
    a=a.copy();a[:,:,3]=np.arange(16,dtype=np.uint8)[None,:]*17;fixtures['alpha_ramp']=a
    a=a.copy();a[:,:,3]=0;fixtures['fully_transparent']=a
    a=np.zeros((16,16,4),np.uint8);a[:8,:8]=[255,0,0,255];a[:8,8:]=[0,255,0,255];a[8:,:8]=[0,0,255,255];a[8:,8:]=[128,128,128,255];fixtures['srgb_patches']=a
    records=[]
    for name,rgba in fixtures.items():
        source=destination/(name+'.png');Image.fromarray(rgba).save(source)
        white=load_rgb(source);prepared=destination/(name+'_white.png');Image.fromarray(white).save(prepared)
        for clustering in ['color-cluster','watershed']:
            for route,input_path in [('raw',source),('white',prepared)]:
                stem=name+'_'+clustering+'_'+route;svg=destination/(stem+'.svg');png=destination/(stem+'.png')
                config={'clustering':clustering,'filter_speckle':0,'color_precision':8,'layer_difference':0,'mode':'pixel','path_precision':3,'watershed_detail':512}
                code='import vtracer,json,sys;vtracer.Config(**json.loads(sys.argv[3])).convert_file(sys.argv[1],sys.argv[2])'
                proc=subprocess.run([sys.executable,'-c',code,str(input_path),str(svg),json.dumps(config)],capture_output=True,text=True,timeout=30)
                row={'fixture':name,'clustering':clustering,'route':route,'config':config,'returncode':proc.returncode,'stderr':proc.stderr}
                if proc.returncode==0:
                    render_svg(svg,png,16,16)
                    with Image.open(png) as im:im.verify()
                    pred=load_rgb(png);row['white_composited_metrics']=compare(white,pred)
                    with Image.open(png) as im:row['rendered_alpha_range']=[int(np.array(im.convert('RGBA'))[:,:,3].min()),int(np.array(im.convert('RGBA'))[:,:,3].max())]
                records.append(row)
    report={'contract':'RGB sRGB numeric values; explicit white composition before tracing. Raw arbitrary alpha is diagnostic only, not supported contract. No ICC conversion tested here.','records':records}
    (destination/'audit.json').write_text(json.dumps(report,indent=2));return report
```

### `ColorContractTests` — `Lines 40–50`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `40` إلى السطر `50` (`Lines 40–50`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 40–50`):**
```python
class ColorContractTests(unittest.TestCase):
    def test_explicit_white_contract_and_raw_alpha_diagnostic(self):
        """Opaque canonical fixtures retain colors; raw partial alpha is not silently approved."""
        with tempfile.TemporaryDirectory() as temporary:
            report=audit_color_contract(temporary)
        for row in report['records']:
            if row['route']=='white':
                self.assertEqual(row['returncode'],0,row)
                self.assertLessEqual(row['white_composited_metrics']['rmse'],1,row)
        raw=[r for r in report['records'] if r['fixture']=='partial_red' and r['route']=='raw']
        self.assertTrue(any(r['returncode'] or r['white_composited_metrics']['rmse']>10 for r in raw))
```

### `ColorContractTests.test_explicit_white_contract_and_raw_alpha_diagnostic` — `Lines 41–50`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `50` (`Lines 41–50`)
- **الوظيفة:** Opaque canonical fixtures retain colors; raw partial alpha is not silently approved.
- **الكود الفعلي (`Lines 41–50`):**
```python
    def test_explicit_white_contract_and_raw_alpha_diagnostic(self):
        """Opaque canonical fixtures retain colors; raw partial alpha is not silently approved."""
        with tempfile.TemporaryDirectory() as temporary:
            report=audit_color_contract(temporary)
        for row in report['records']:
            if row['route']=='white':
                self.assertEqual(row['returncode'],0,row)
                self.assertLessEqual(row['white_composited_metrics']['rmse'],1,row)
        raw=[r for r in report['records'] if r['fixture']=='partial_red' and r['route']=='raw']
        self.assertTrue(any(r['returncode'] or r['white_composited_metrics']['rmse']>10 for r in raw))
```
