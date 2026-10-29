# مرآة الكود التفصيلية: `run_case.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_case.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_case.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `49` (`Lines 1–49`)
- **بصمة الملف (`SHA-256`):** `463e9dc9e4fb3fb9e199ea883e61b9597519b38b40e2d6fd4d18c96ab0564a69`
- **الوصف التفصيلي:** # START CHANGE AGD-RAWFACE-RUN-CASE | 2026-10-29T12:20:15Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `destination` | `function` | `Lines 19–20` | `def destination(case):` | رمز برمجي موثق. |
| `execute` | `function` | `Lines 22–45` | `def execute(case):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `destination` — `Lines 19–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `20` (`Lines 19–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–20`):**
```python
def destination(case):
    return (WORK/'raw_face_junction/external_results' if case=='fine_features' else ROOT/'results')/case
```

### `execute` — `Lines 22–45`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `45` (`Lines 22–45`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–45`):**
```python
def execute(case):
    pins=json.loads((ROOT/'BASELINE_PINS.json').read_text(encoding='utf-8'))['cases'][case]
    for item in pins.values():assert digest(item['path'])==item['sha256']
    for name,value in json.loads((ROOT/'FREEZE.json').read_text(encoding='utf-8'))['files'].items():assert digest(ROOT/name)==value
    out=destination(case);out.mkdir(parents=True,exist_ok=False)
    started=time.monotonic();cpu=time.process_time()
    for old,new in [('baseline.json','O.json'),('baseline_labels.npy','labels.npy'),('working.png','working.png'),('B.json','B.json')]:shutil.copy2(pins[old]['path'],out/new)
    original=json.loads((out/'O.json').read_text(encoding='utf-8'));candidate,audit=decompose(original);dump(out/'R.json',candidate);dump(out/'R_audit.json',audit)
    checks=[]
    for name,g in [('O',original),('R',candidate)]:
        for raw in [True,False]:
            stem=name+('_raw_regions' if raw else '_fitted_regions');svg=out/(stem+'.svg');svg.write_text(svg_graph(g,raw=raw,regions=True),encoding='utf-8')
            for scale in ([1,8] if raw else [8]):
                png=out/(stem+f'_{scale}x.png')
                subprocess.run([str(RESVG),'--width',str(g['width']*scale),'--height',str(g['height']*scale),str(svg),str(png)],check=True,capture_output=True,timeout=60)
    for raw,scale in [(True,1),(True,8),(False,8)]:
        stem='_raw_regions' if raw else '_fitted_regions';a=np.asarray(Image.open(out/('O'+stem+f'_{scale}x.png')).convert('RGBA'));b=np.asarray(Image.open(out/('R'+stem+f'_{scale}x.png')).convert('RGBA'))
        checks.append({'raw':raw,'scale':scale,'different_rgba_pixels':int(np.sum(np.any(a!=b,axis=-1))),'equal':bool(np.array_equal(a,b))})
    gate=all(x['equal'] for x in checks) and not audit['rejections']
    dump(out/'MATCHED_CONTROLS.json',{'checks':checks,'RB_permitted':gate,'labels_sha256':digest(out/'labels.npy'),'no_parameter_tuning':True})
    if gate:
        corrected,guard=initialize_safe(candidate);dump(out/'RB.json',corrected);dump(out/'RB_audit.json',guard)
    else:dump(out/'RB_SKIPPED.json',{'reason':'Frozen representation equivalence gate failed; no guard bypass or altered segmentation'})
    dump(out/'CONSTRUCTION_RESOURCES.json',{'wall_seconds':time.monotonic()-started,'process_cpu_seconds':time.process_time()-cpu,'case':case,'RB_executed':gate,'labels_sha256':digest(out/'labels.npy')})
```
