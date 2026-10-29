# مرآة الكود التفصيلية: `isolation.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `isolation.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `isolation.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `109` (`Lines 1–109`)
- **بصمة الملف (`SHA-256`):** `8ddecea692545fc440fc527d685dbe5bdbaf9e1cfb93c43472b089aee216b3c1`
- **الوصف التفصيلي:** """Research-only fixed-label isolation harness. Never reads evaluator annotations.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `digest` | `function` | `Lines 27–28` | `def digest(path):` | رمز برمجي موثق. |
| `dump` | `function` | `Lines 30–32` | `def dump(path, obj):` | رمز برمجي موثق. |
| `case_dir` | `function` | `Lines 34–36` | `def case_dir(case):` | رمز برمجي موثق. |
| `prepare` | `function` | `Lines 38–51` | `def prepare():` | رمز برمجي موثق. |
| `arena_modules` | `function` | `Lines 53–66` | `def arena_modules():` | رمز برمجي موثق. |
| `arena_modules.denied` | `nested_function` | `Lines 58–58` | `def denied(*a,**k): raise RuntimeError('Appearance/rendering forbidden in external geometry worker')` | رمز برمجي موثق. |
| `worker` | `function` | `Lines 68–91` | `def worker(case,stage,segmentation):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `digest` — `Lines 27–28`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `28` (`Lines 27–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–28`):**
```python
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
```

### `dump` — `Lines 30–32`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `32` (`Lines 30–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–32`):**
```python
def dump(path, obj):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,allow_nan=False),encoding='utf-8')
```

### `case_dir` — `Lines 34–36`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `36` (`Lines 34–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–36`):**
```python
def case_dir(case):
    # Unknown-rights independent fixture and derived artwork are local-only.
    return (LOCAL/'external_results' if case=='fine_features' else ROOT/'results')/case
```

### `prepare` — `Lines 38–51`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `38` إلى السطر `51` (`Lines 38–51`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 38–51`):**
```python
def prepare():
    manifest={}
    for case,src in CASES.items():
        out=case_dir(case); out.mkdir(parents=True,exist_ok=True)
        rgba=Image.open(src).convert('RGBA')
        bg=Image.new('RGBA',rgba.size,'white'); bg.alpha_composite(rgba)
        working=out/'working.png'; bg.convert('RGB').save(working)
        manifest[case]={'source':str(src),'source_sha256':digest(src),'working':str(working),
          'working_sha256':digest(working),'size':list(rgba.size),
          'source_alpha_min':int(np.asarray(rgba)[...,3].min()),
          'pixels_unchanged':bool(np.array_equal(np.asarray(rgba)[...,:3],np.asarray(bg)[...,:3])),
          'rights':'external owner ZIP, not redistributed' if case=='fine_features' else 'existing repository input'}
    dump(ROOT/'inputs/manifest.json',manifest)
    return manifest
```

### `arena_modules` — `Lines 53–66`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `53` إلى السطر `66` (`Lines 53–66`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 53–66`):**
```python
def arena_modules():
    sys.path.insert(0,str(WORK/'geometry-deps'))
    # Legacy imports CairoSVG at module load. This geometry-only wrapper denies
    # that renderer explicitly; none of the called graph/fit functions need it.
    stub=types.ModuleType('cairosvg')
    def denied(*a,**k): raise RuntimeError('Appearance/rendering forbidden in external geometry worker')
    stub.svg2png=denied; sys.modules['cairosvg']=stub
    package='agd_external_arena'
    spec=importlib.util.spec_from_file_location(package,EXTERNAL/'src/__init__.py',submodule_search_locations=[str(EXTERNAL/'src')])
    module=importlib.util.module_from_spec(spec);sys.modules[package]=module;spec.loader.exec_module(module)
    from importlib import import_module
    mods=[import_module(package+'.'+name) for name in ['segment','graph','fit']]
    hashes={str(p.relative_to(EXTERNAL)):digest(p) for p in list((EXTERNAL/'src').glob('*.py'))+[EXTERNAL/'historical/legacy_penvector.py']}
    return (*mods,hashes)
```

### `arena_modules.denied` — `Lines 58–58`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `58` (`Lines 58–58`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 58–58`):**
```python
    def denied(*a,**k): raise RuntimeError('Appearance/rendering forbidden in external geometry worker')
```

### `worker` — `Lines 68–91`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `68` إلى السطر `91` (`Lines 68–91`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 68–91`):**
```python
def worker(case,stage,segmentation):
    out=case_dir(case); image=out/'working.png'
    if stage=='segment':
        sm,gm,fm,hashes=arena_modules()
        if case in ('A01_shield','fine_features'):
            saved=EXTERNAL/('outputs/shield' if case=='A01_shield' else 'outputs/fine_features')/'labels.npy'
            original=EXTERNAL/('inputs/shield.png' if case=='A01_shield' else 'inputs/synthetic/fine_features.png')
            if not np.array_equal(np.asarray(Image.open(original).convert('RGB')),np.asarray(Image.open(image))):
                raise ValueError('Saved labels do not match common working pixels')
            labels=np.load(saved,allow_pickle=False); meta={'saved_labels':str(saved),'sha256':digest(saved)}
        else:
            _,labels,_,_,meta=sm.segment_image(image,method='felzenszwalb',scale=400,min_area=12,max_regions=1500)
        if labels.ndim!=2 or labels.min()<1: raise ValueError('Inside labels must be positive; zero reserved for exterior')
        np.save(out/'S_A.npy',labels.astype(np.uint32))
        dump(out/'S_A_meta.json',{'segmentation':meta,'external_source_hashes':hashes})
    elif stage=='arena_fit':
        sm,gm,fm,hashes=arena_modules(); labels=np.load(out/(segmentation+'.npy'),allow_pickle=False)
        graph=gm.construct(labels); raw=gm.serialize(graph,labels.shape[1],labels.shape[0])
        dump(out/(segmentation+'_raw_arena.json'),raw)
        stats=fm.initialize(graph,labels.shape[1],labels.shape[0],tolerance=.8,smooth=1.)
        fitted=gm.serialize(graph,labels.shape[1],labels.shape[0])
        fitted['stats']=stats;fitted['labels_sha256']=digest(out/(segmentation+'.npy'))
        dump(out/(segmentation+'_F_A.json'),fitted)
    else: raise ValueError(stage)
```
