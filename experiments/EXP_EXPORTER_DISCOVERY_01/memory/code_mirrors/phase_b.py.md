# مرآة الكود التفصيلية: `phase_b.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `phase_b.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `phase_b.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `55` (`Lines 1–55`)
- **بصمة الملف (`SHA-256`):** `5e5e196f42ceda8c0e888f380941e363f67f2b62684e1b27f8f8caff1466299b`
- **الوصف التفصيلي:** # START CHANGE AGD-EXPORT-PHASE-B | 2026-10-29T22:12:25Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `destination` | `function` | `Lines 17–17` | `def destination(case):return (WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case` | رمز برمجي موثق. |
| `render_size` | `function` | `Lines 19–20` | `def render_size(svg,png,width,height,scale=1):` | رمز برمجي موثق. |
| `execute` | `function` | `Lines 22–51` | `def execute(case):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `destination` — `Lines 17–17`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `17` (`Lines 17–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–17`):**
```python
def destination(case):return (WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case
```

### `render_size` — `Lines 19–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `20` (`Lines 19–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–20`):**
```python
def render_size(svg,png,width,height,scale=1):
    started=time.perf_counter();subprocess.run([str(RESVG),'--width',str(width*scale),'--height',str(height*scale),str(svg),str(png)],check=True,capture_output=True,timeout=60);return time.perf_counter()-started
```

### `execute` — `Lines 22–51`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `51` (`Lines 22–51`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–51`):**
```python
def execute(case):
    inputs=json.loads((ROOT/'BASELINE_PINS.json').read_text(encoding='utf-8'))
    for item in [*inputs['cases'][case].values(),*inputs['dependencies'].values()]:assert digest(item['path'])==item['sha256']
    for name,value in json.loads((ROOT/'FREEZE.json').read_text())['files'].items():assert digest(ROOT/name)==value
    out=destination(case);out.mkdir(parents=True,exist_ok=False);start=time.monotonic();cpu=time.process_time()
    for name in ['O.json','R.json','B.json','A.json','labels.npy','A_labels.npy','working.png']:shutil.copy2(inputs['cases'][case][name]['path'],out/name)
    graphs={n:json.loads((out/(n+'.json')).read_text(encoding='utf-8')) for n in ['O','R','B','A']}
    assert graphs['O']['chains']==graphs['R']['chains']
    for name,g in graphs.items():
        for kind,raw,regions in [('curves',False,False),('regions',False,True),('raw_regions',True,True)]:
            p=out/(name+'_'+kind+'.svg');p.write_text(svg_graph(g,raw=raw,regions=regions),encoding='utf-8')
            for scale in ([1,8] if regions else [1]):render_size(p,out/(name+'_'+kind+f'_{scale}x.png'),g['width'],g['height'],scale)
    checks=[]
    for kind,scale in [('raw_regions',1),('raw_regions',8),('regions',8)]:
        a=np.asarray(Image.open(out/('O_'+kind+f'_{scale}x.png')).convert('RGBA'));b=np.asarray(Image.open(out/('R_'+kind+f'_{scale}x.png')).convert('RGBA'));checks.append({'kind':kind,'scale':scale,'differing_rgba_pixels':int(np.sum(np.any(a!=b,axis=-1))),'equal':bool(np.array_equal(a,b))})
    impact=[]
    for name,g in graphs.items():
        p=out/(name+'_legacy_regions.svg');p.write_text(legacy_svg_graph(g,regions=True),encoding='utf-8');render_size(p,p.with_suffix('.png'),g['width'],g['height'],8)
        c=out/(name+'_corrected8_regions.svg');c.write_text(svg_graph(g,regions=True,precision=8),encoding='utf-8');render_size(c,c.with_suffix('.png'),g['width'],g['height'],8)
        old=np.asarray(Image.open(p.with_suffix('.png')).convert('RGBA'));p8=np.asarray(Image.open(c.with_suffix('.png')).convert('RGBA'));p17=np.asarray(Image.open(out/(name+'_regions_8x.png')).convert('RGBA'))
        impact.append({'condition':name,'closure_semantics_only_changed_pixels_8x':int(np.sum(np.any(old!=p8,axis=-1))),'precision_only_changed_pixels_8x':int(np.sum(np.any(p8!=p17,axis=-1))),'legacy_vs_corrected17_changed_pixels_8x':int(np.sum(np.any(old!=p17,axis=-1)))})
    passed=all(x['equal'] for x in checks);dump(out/'MATCHED_CONTROLS.json',{'checks':checks,'passed':passed,'corrected_serializer':'17digit explicit chainclosure; originalsource unchanged','geometry_parameters_changed':False});dump(out/'SERIALIZATION_IMPACT.json',impact)
    if passed:
        if case=='K01_linear_corner_hole':
            shutil.copy2(inputs['cases'][case]['RB.json']['path'],out/'RB.json');guard={'status':'REUSED_PREVIOUS_CONTROL_NO_REFIT','source_sha256':digest(out/'RB.json')}
        else:
            rb,guard=initialize_safe(graphs['R']);dump(out/'RB.json',rb)
        dump(out/'RB_audit.json',guard)
    else:dump(out/'RB_SKIPPED.json',{'reason':'Corrected serialization equivalence fails; no guard bypass or parameter change'})
    dump(out/'PHASE_B_RESOURCES.json',{'wall_seconds':time.monotonic()-start,'process_cpu_seconds':time.process_time()-cpu,'case':case,'gate_passed':passed,'labels_sha256':digest(out/'labels.npy')})
```
