# مرآة الكود التفصيلية: `src/search.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/search.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/search.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `127` (`Lines 1–127`)
- **بصمة الملف (`SHA-256`):** `0f1d1d33561e7f1fc6d885be329b97edc6c165a5b51e88f361417577e625b4ca`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `prepare_input` | `function` | `Lines 16–29` | `def prepare_input(source,destination):` | Normalize declared ICC to sRGB and explicitly composite alpha on white. |
| `extra_metrics` | `function` | `Lines 31–36` | `def extra_metrics(source,pred):` | Color and high-frequency diagnostics, complementing SSIM/PSNR/edge metrics. |
| `fidelity_score` | `function` | `Lines 38–46` | `def fidelity_score(metrics):` | Fixed multi-metric score, no geometry/size/runtime penalty; not perceptual truth. |
| `pilot_configs` | `function` | `Lines 48–60` | `def pilot_configs():` | Diverse, fixed thirteen pilots, including the owner's exact mapped settings. |
| `refined_configs` | `function` | `Lines 62–66` | `def refined_configs(best):` | Four local one-coordinate probes around pilot winner; no unbounded search. |
| `run_trial` | `function` | `Lines 68–80` | `def run_trial(source,folder,config):` | Run one isolated worker; preserve even failed parameter sets and logs. |
| `worker` | `function` | `Lines 82–96` | `def worker(source,folder):` | Trace, validate raster exclusion, native-render, evaluate in a fresh process. |
| `search` | `function` | `Lines 98–121` | `def search(source,output,configs=None,refine=True):` | Execute thirteen fixed pilots and at most four adaptive probes, retaining all. |
| `search.evaluate` | `nested_function` | `Lines 104–110` | `def evaluate(config,phase):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `prepare_input` — `Lines 16–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `29` (`Lines 16–29`)
- **الوظيفة:** Normalize declared ICC to sRGB and explicitly composite alpha on white.
- **الكود الفعلي (`Lines 16–29`):**
```python
def prepare_input(source,destination):
    """Normalize declared ICC to sRGB and explicitly composite alpha on white."""
    source=Path(source);destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    with Image.open(source) as im:
        im.load();info={'original_mode':im.mode,'original_dimensions':list(im.size),'icc_present':bool(im.info.get('icc_profile')),'original_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'alpha_policy':'composite onto opaque sRGB white; transparent SVG fidelity is not tested'}
        alpha=im.convert('RGBA').getchannel('A');rgb=im.convert('RGB')
        if im.info.get('icc_profile'):
            profile=ImageCms.ImageCmsProfile(io.BytesIO(im.info['icc_profile']))
            rgb=ImageCms.profileToProfile(rgb,profile,ImageCms.createProfile('sRGB'),outputMode='RGB')
            info['color_policy']='embedded profile transformed to sRGB with Pillow LittleCMS'
        else:info['color_policy']='untagged RGB assumed sRGB; no inferred gamma conversion'
        info['alpha_extrema']=list(alpha.getextrema());rgba=rgb.convert('RGBA');rgba.putalpha(alpha)
        normalized=Image.alpha_composite(Image.new('RGBA',im.size,'white'),rgba).convert('RGB');normalized.save(destination)
    return info
```

### `extra_metrics` — `Lines 31–36`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `36` (`Lines 31–36`)
- **الوظيفة:** Color and high-frequency diagnostics, complementing SSIM/PSNR/edge metrics.
- **الكود الفعلي (`Lines 31–36`):**
```python
def extra_metrics(source,pred):
    """Color and high-frequency diagnostics, complementing SSIM/PSNR/edge metrics."""
    de=np.linalg.norm(rgb2lab(source/255.)-rgb2lab(pred/255.),axis=2)
    residual=source.astype(float)-pred.astype(float);high=residual-gaussian_filter(residual,(1.,1.,0))
    return {'delta_e76_mean':float(de.mean()),'delta_e76_p95':float(np.percentile(de,95)),
            'highpass_rmse_sigma1':float(np.sqrt(np.mean(high**2)))}
```

### `fidelity_score` — `Lines 38–46`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `38` إلى السطر `46` (`Lines 38–46`)
- **الوظيفة:** Fixed multi-metric score, no geometry/size/runtime penalty; not perceptual truth.
- **الكود الفعلي (`Lines 38–46`):**
```python
def fidelity_score(metrics):
    """Fixed multi-metric score, no geometry/size/runtime penalty; not perceptual truth."""
    psnr=60. if metrics.get('identical') else (metrics.get('psnr_db') or 0.)
    edge=metrics.get('edge_f1_1_5px')
    # Empty edge maps: do not invent agreement; reallocate this term to SSIM.
    edge=metrics['ssim'] if edge is None else edge
    return float(.40*metrics['ssim']+.15*min(psnr/60.,1.)+.20*edge+
                 .15*math.exp(-metrics['delta_e76_mean']/12.)+
                 .10*math.exp(-metrics['highpass_rmse_sigma1']/20.))
```

### `pilot_configs` — `Lines 48–60`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `60` (`Lines 48–60`)
- **الوظيفة:** Diverse, fixed thirteen pilots, including the owner's exact mapped settings.
- **الكود الفعلي (`Lines 48–60`):**
```python
def pilot_configs():
    """Diverse, fixed thirteen pilots, including the owner's exact mapped settings."""
    changes=[{}, {'path_precision':3}, {'path_precision':3,'simplify':None},
      {'path_precision':3,'simplify':.5},
      {'hierarchical':'cutout','path_precision':3,'simplify':None},
      {'hierarchical':'cutout'}, {'mode':'polygon','path_precision':3,'simplify':None},
      {'mode':'pixel','path_precision':0,'simplify':None},
      {'color_precision':6,'layer_difference':16,'path_precision':3,'simplify':None},
      {'layer_difference':8,'path_precision':3,'simplify':None},
      {'clustering':'watershed','hierarchical':'cutout','watershed_detail':128,'path_precision':3,'simplify':None},
      {'clustering':'watershed','hierarchical':'cutout','watershed_detail':256,'path_precision':3,'simplify':None},
      {'clustering':'bw','hierarchical':'stacked','path_precision':3,'simplify':None}]
    return [OWNER|change for change in changes]
```

### `refined_configs` — `Lines 62–66`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `62` إلى السطر `66` (`Lines 62–66`)
- **الوظيفة:** Four local one-coordinate probes around pilot winner; no unbounded search.
- **الكود الفعلي (`Lines 62–66`):**
```python
def refined_configs(best):
    """Four local one-coordinate probes around pilot winner; no unbounded search."""
    return [best|{'path_precision':p} for p in [1,5]]+[
            best|{'simplify':.25 if best['simplify']!=.25 else .75},
            best|{'optimize':0}]
```

### `run_trial` — `Lines 68–80`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `68` إلى السطر `80` (`Lines 68–80`)
- **الوظيفة:** Run one isolated worker; preserve even failed parameter sets and logs.
- **الكود الفعلي (`Lines 68–80`):**
```python
def run_trial(source,folder,config):
    """Run one isolated worker; preserve even failed parameter sets and logs."""
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    (folder/'config.json').write_text(json.dumps(config,indent=2));start=time.perf_counter()
    try:
        proc=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker','--input',str(Path(source).resolve()),'--output',str(folder.resolve())],capture_output=True,text=True,timeout=180)
        (folder/'process.log').write_text(proc.stdout+'\n'+proc.stderr)
        if proc.returncode:raise RuntimeError('worker exit '+str(proc.returncode))
        result=json.loads((folder/'result.json').read_text())
    except Exception as error:
        result={'status':'failed','error':str(error),'config':config}
    result['isolated_process_wall_seconds']=time.perf_counter()-start
    (folder/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False));return result
```

### `worker` — `Lines 82–96`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `82` إلى السطر `96` (`Lines 82–96`)
- **الوظيفة:** Trace, validate raster exclusion, native-render, evaluate in a fresh process.
- **الكود الفعلي (`Lines 82–96`):**
```python
def worker(source,folder):
    """Trace, validate raster exclusion, native-render, evaluate in a fresh process."""
    import vtracer
    from importlib.metadata import version
    folder=Path(folder);config=json.loads((folder/'config.json').read_text());rgb=load_rgb(source);h,w=rgb.shape[:2]
    start=time.perf_counter();cpu=time.process_time();svg=folder/'output.svg'
    vtracer.Config(**config).convert_file(str(source),str(svg))
    trace={'trace_wall_seconds':time.perf_counter()-start,'trace_cpu_seconds':time.process_time()-cpu,'trace_process_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024}
    structure=svg_structure(svg)
    if not structure['raster_free'] or structure['external_href_count'] or structure['script_count']:raise ValueError('Not a self-contained raster-free SVG')
    timing=render_svg(svg,folder/'render.png',w,h)
    with Image.open(folder/'render.png') as image:image.verify()
    pred=load_rgb(folder/'render.png');metrics=compare(rgb,pred)|extra_metrics(rgb,pred)
    result={'status':'ok','vtracer_version':version('vtracer'),'config':config,'metrics':metrics,'score':fidelity_score(metrics),'structure':structure,'performance':trace|timing|{'worker_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,'renderer_child_peak_mib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1024,'memory_note':'separate Linux process high-water marks, not simultaneous process-tree RSS'}}
    (folder/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False))
```

### `search` — `Lines 98–121`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `98` إلى السطر `121` (`Lines 98–121`)
- **الوظيفة:** Execute thirteen fixed pilots and at most four adaptive probes, retaining all.
- **الكود الفعلي (`Lines 98–121`):**
```python
def search(source,output,configs=None,refine=True):
    """Execute thirteen fixed pilots and at most four adaptive probes, retaining all."""
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    if (output/'ranking.json').exists():raise FileExistsError('Use a new output directory; prior evidence is immutable')
    normalized=output/'normalized.png';normalization=prepare_input(source,normalized)
    (output/'normalization.json').write_text(json.dumps(normalization,indent=2));results=[];seen=set()
    def evaluate(config,phase):
        key=json.dumps(config,sort_keys=True)
        if key in seen:return
        seen.add(key);name=f'trial_{len(results):02d}';result=run_trial(normalized,output/name,config)
        result['trial']=name;result['phase']=phase;results.append(result)
        (output/'progress.json').write_text(json.dumps(results,indent=2))
        print(name,result['status'],round(result.get('score',0),6),flush=True)
    for config in (pilot_configs() if configs is None else configs):evaluate(config,'pilot' if configs is None else 'frozen')
    successful=[r for r in results if r['status']=='ok']
    if refine and configs is None and successful:
        winner=max(successful,key=lambda r:r['score'])
        for config in refined_configs(winner['config']):evaluate(config,'local')
    ranked=sorted([r for r in results if r['status']=='ok'],key=lambda r:(-r['score'],r['trial']))
    record={'normalization':normalization,'selection':'score=.40SSIM+.15min(PSNR/60,1)+.20edgeF1+.15exp(-meanDeltaE76/12)+.10exp(-highpassRMSE/20); no complexity penalty. Visual review remains required.','ranked':ranked,'failed':[r for r in results if r['status']!='ok']}
    (output/'ranking.json').write_text(json.dumps(record,indent=2))
    if ranked:
        best=ranked[0];shutil.copyfile(output/best['trial']/'output.svg',output/'best.svg');shutil.copyfile(output/best['trial']/'render.png',output/'best.png');(output/'best_config.json').write_text(json.dumps(best['config'],indent=2))
    return record
```

### `search.evaluate` — `Lines 104–110`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `104` إلى السطر `110` (`Lines 104–110`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 104–110`):**
```python
    def evaluate(config,phase):
        key=json.dumps(config,sort_keys=True)
        if key in seen:return
        seen.add(key);name=f'trial_{len(results):02d}';result=run_trial(normalized,output/name,config)
        result['trial']=name;result['phase']=phase;results.append(result)
        (output/'progress.json').write_text(json.dumps(results,indent=2))
        print(name,result['status'],round(result.get('score',0),6),flush=True)
```
