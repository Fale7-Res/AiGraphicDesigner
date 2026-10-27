# مرآة الكود التفصيلية: `verify_alpha_geometry.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `verify_alpha_geometry.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `verify_alpha_geometry.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `46` (`Lines 1–46`)
- **بصمة الملف (`SHA-256`):** `fe376979057878cb38ebfa8c1861d26f6d78379f58de1670a1e57366d45cec45`
- **الوصف التفصيلي:** """Independent reconstruction checks for vector alpha run geometry, no renderer claim."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `verify_alpha_runs` | `function` | `Lines 13–43` | `def verify_alpha_runs() -> dict:` | Reconstruct all 256 alpha levels and boundary cases from serialized paths. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `verify_alpha_runs` — `Lines 13–43`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `43` (`Lines 13–43`)
- **الوظيفة:** Reconstruct all 256 alpha levels and boundary cases from serialized paths.
- **الكود الفعلي (`Lines 13–43`):**
```python
def verify_alpha_runs() -> dict:
    """Reconstruct all 256 alpha levels and boundary cases from serialized paths."""
    matrices={'all_levels':np.arange(256,dtype='uint8').reshape(16,16),
              'all_transparent':np.zeros((16,16),dtype='uint8'),
              'all_opaque':np.full((16,16),255,dtype='uint8'),
              'checker':np.indices((16,16)).sum(axis=0).astype('uint8')%2*255}
    results={}
    with tempfile.TemporaryDirectory() as directory:
        folder=Path(directory)
        source=folder/'rgb.svg'
        source.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><rect width="16" height="16" fill="red"/></svg>',encoding='utf-8')
        for name,expected in matrices.items():
            Image.fromarray(expected).save(folder/'alpha.png')
            stats=apply_vector_alpha(source,folder/'alpha.png',folder/'output.svg')
            reconstructed=np.zeros_like(expected)
            root=ET.parse(folder/'output.svg').getroot()
            mask=next(e for e in root.iter() if e.tag.endswith('}mask'))
            for path in mask:
                alpha=int(round(float(path.get('fill-opacity'))*255))
                for match in re.finditer(r'M(\d+) (\d+)H(\d+)V(\d+)H(\d+)Z',path.get('d')):
                    x,y,end,next_y,back=map(int,match.groups())
                    if back!=x or next_y!=y+1: raise AssertionError('Malformed horizontal run')
                    reconstructed[y:next_y,x:end]=alpha
            equal=np.array_equal(expected,reconstructed)
            results[name]={'exact_array_reconstruction':equal,'raster_free':stats['structure']['raster_free'],
                           'alpha_run_count':stats['alpha_run_count']}
            if not equal or not stats['structure']['raster_free']: raise AssertionError(results)
    report={'passed':True,'cases':results,'scope':'serialized vector geometry only; actual renderer alpha correctness requires separate evaluate_alpha run'}
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports'/'alpha_geometry_tests.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return report
```
