# مرآة الكود التفصيلية: `src/baselines.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/baselines.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/baselines.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `53` (`Lines 1–53`)
- **بصمة الملف (`SHA-256`):** `7791464d37e5840658daabfffa8075c56a5413b44fa6e658e378129cecd47e28`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `measure` | `function` | `Lines 11–25` | `def measure(svg,source,out):` | Fresh-process baseline native render with exact dimensions and color audit. |
| `candidates` | `function` | `Lines 27–36` | `def candidates():` | Map frozen baseline copies to corresponding benchmark images. |
| `run` | `function` | `Lines 38–45` | `def run(out):` | Run native historical rendering serially and preserve every result. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `measure` — `Lines 11–25`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `25` (`Lines 11–25`)
- **الوظيفة:** Fresh-process baseline native render with exact dimensions and color audit.
- **الكود الفعلي (`Lines 11–25`):**
```python
def measure(svg,source,out):
    """Fresh-process baseline native render with exact dimensions and color audit."""
    out.mkdir(parents=True,exist_ok=True)
    with Image.open(source) as im:
        metadata={'mode':im.mode,'dimensions':list(im.size),'icc_present':bool(im.info.get('icc_profile')),'alpha_present':'A' in im.getbands(),'info_keys':list(im.info)}
    if metadata['icc_present'] or metadata['alpha_present']:raise ValueError('This historical benchmark requires explicit new normalization review for ICC/alpha inputs')
    ref=load_rgb(source);h,w=ref.shape[:2];wall=time.perf_counter();cpu=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    timing=render_svg(svg,out/'render.png',w,h)
    with Image.open(out/'render.png') as im:im.verify()
    with Image.open(out/'render.png') as im:im.load()
    pred=load_rgb(out/'render.png');metrics=compare(ref,pred)
    metrics.update(extra_metrics(ref,pred))
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result={'source_name':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),'input_metadata':metadata,'metrics':metrics,'structure':svg_structure(svg),'render':timing,'resources':{'wall_seconds':time.perf_counter()-wall,'parent_cpu_seconds':time.process_time()-cpu,'renderer_child_cpu_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'parent_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,'child_peak_mib':after.ru_maxrss/1024,'scope':'Fresh worker process per SVG. Child peak includes Inkscape export and version subprocess, not simultaneous tree peak; historical generation excluded.'},'scope':'Fresh render of exact historical SVG; not an engine reproduction; untagged RGB assumed sRGB, white compositing, no resize.'}
    (out/'metrics.json').write_text(json.dumps(result,indent=2));return result
```

### `candidates` — `Lines 27–36`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `36` (`Lines 27–36`)
- **الوظيفة:** Map frozen baseline copies to corresponding benchmark images.
- **الكود الفعلي (`Lines 27–36`):**
```python
def candidates():
    """Map frozen baseline copies to corresponding benchmark images."""
    for source in sorted((ROOT/'inputs').glob('*.png')):
        for label in ['original','repair']:
            svg=ROOT/'baselines'/label/(source.stem+'_v04.svg')
            if not svg.exists():raise FileNotFoundError(svg)
            yield source,label,svg
        recent=ROOT/'baselines/recent'/source.stem
        if recent.exists():
            for svg in sorted(recent.glob('*.svg')):yield source,svg.stem,svg
```

### `run` — `Lines 38–45`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `38` إلى السطر `45` (`Lines 38–45`)
- **الوظيفة:** Run native historical rendering serially and preserve every result.
- **الكود الفعلي (`Lines 38–45`):**
```python
def run(out):
    """Run native historical rendering serially and preserve every result."""
    rows=[]
    for source,label,svg in candidates():
        target=out/source.stem/label
        subprocess.run([sys.executable,__file__,'--worker','--svg',str(svg),'--source',str(source),'--output',str(target)],check=True)
        row=json.loads((target/'metrics.json').read_text());row['label']=label;row['case']=source.stem;rows.append(row);(out/'summary.json').write_text(json.dumps(rows,indent=2));print(source.stem,label,round(row['metrics']['ssim'],6),flush=True)
    return rows
```
