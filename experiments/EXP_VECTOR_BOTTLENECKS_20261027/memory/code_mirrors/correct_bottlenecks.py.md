# مرآة الكود التفصيلية: `correct_bottlenecks.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `correct_bottlenecks.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `correct_bottlenecks.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `46` (`Lines 1–46`)
- **بصمة الملف (`SHA-256`):** `dcb872ad162a476d08ff077ff3375a5f74208ee52f563cb90f9c17bc2554a642`
- **الوصف التفصيلي:** """Paired coverage intervention at uniform detail192; every result retained."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `corrected_case` | `function` | `Lines 12–40` | `def corrected_case(case):` | رمز برمجي موثق. |
| `corrected_case.signature` | `nested_function` | `Lines 25–28` | `def signature(root):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `corrected_case` — `Lines 12–40`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `40` (`Lines 12–40`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–40`):**
```python
def corrected_case(case):
    source=ROOT/'results/granularity'/case['id'];baseline=source/'192/D/output.svg'
    out=ROOT/'results/corrections'/case['id'];out.mkdir(parents=True,exist_ok=True)
    if (out/'result.json').exists():
        saved=json.loads((out/'result.json').read_text())
        assert b.inherited.digest(out/'output.svg')==saved['sha256']
        assert b.inherited.digest(baseline)==saved['baseline_svg_sha256']
        return
    if any(out.iterdir()):raise FileExistsError('Preserve partial correction evidence')
    start=time.perf_counter();change=correct_coverage(baseline,out/'output.svg',.25)
    row=b.inherited.evaluate_condition(source/'source.png',out/'output.svg',out)
    old=json.loads((source/'result.json').read_text())['levels']['192']['conditions']['D']
    original=ET.parse(baseline).getroot();modified=ET.parse(out/'output.svg').getroot()
    def signature(root):
        for node in root.iter():
            for key in ['stroke','stroke-width','stroke-linejoin','stroke-linecap','paint-order']:node.attrib.pop(key,None)
        return ET.tostring(root,encoding='utf-8')
    assert signature(original)==signature(modified)
    original_alpha=np.asarray(Image.open(source/'192/D/render.png').convert('RGBA'))[:,:,3]
    new_alpha=np.asarray(Image.open(out/'render.png').convert('RGBA'))[:,:,3]
    target=np.asarray(Image.open(source/'source.png').convert('RGBA'))[:,:,3]
    row.update(baseline_detail=192,baseline_svg_sha256=b.inherited.digest(baseline),baseline_metrics=old['metrics'],
       correction=change,delta={bg:{key:row['metrics'][bg][key]-old['metrics'][bg][key] for key in ['ssim','mse','worst_32px_tile_rmse']} for bg in ['white','black','bluegray']},
       alpha_support={'baseline_alpha_mae':float(np.abs(target.astype(float)-original_alpha).mean()),'new_alpha_mae':row['alpha_mae'],
       'new_support_pixels_source_alpha_zero':int(((target==0)&(new_alpha>0)).sum()),'baseline_support_pixels_source_alpha_zero':int(((target==0)&(original_alpha>0)).sum()),
       'alpha_increase_pixels':int((new_alpha>original_alpha).sum()),'alpha_decrease_pixels':int((new_alpha<original_alpha).sum())},
       wall_seconds=time.perf_counter()-start,interpretation='Same path d/order/fills/masks, explicitly overlapping narrowstrokes. Coverage can improve while contours/colors worsen. Not topology repair or accepted default.',architecture='NOT_APPROVED')
    b.inherited.save_json(out/'result.json',row)
    print('CORRECTION',case['id'],row['delta']['white'],'alpha',row['alpha_support'],flush=True)
```

### `corrected_case.signature` — `Lines 25–28`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `28` (`Lines 25–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–28`):**
```python
    def signature(root):
        for node in root.iter():
            for key in ['stroke','stroke-width','stroke-linejoin','stroke-linecap','paint-order']:node.attrib.pop(key,None)
        return ET.tostring(root,encoding='utf-8')
```
