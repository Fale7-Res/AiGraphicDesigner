# مرآة الكود التفصيلية: `windows_search.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `windows_search.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `windows_search.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `178` (`Lines 1–178`)
- **بصمة الملف (`SHA-256`):** `136e8697431d66dc762ec445753b163267bb82e92b004f2d6e6edb3c4d730c71`
- **الوصف التفصيلي:** """Native Windows trials; explicit derived helpers, unchanged historical evaluator."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `prepare_input` | `function` | `Lines 21–34` | `def prepare_input(source,destination):` | Historical derived copy: ICC to sRGB and explicitly composite on white. |
| `extra_metrics` | `function` | `Lines 36–41` | `def extra_metrics(source,pred):` | Historical derived copy: unchanged color and high-frequency diagnostics. |
| `fidelity_score` | `function` | `Lines 43–50` | `def fidelity_score(metrics):` | Historical derived copy: fixed multi-metric score, no complexity penalty. |
| `terminate_tree` | `function` | `Lines 54–63` | `def terminate_tree(process: psutil.Process, known: dict) -> None:` | Kill root and known descendants; wait for termination. |
| `supervise` | `function` | `Lines 65–108` | `def supervise(command: list[str], log: Path, timeout: float=180., memory_limit_mib: float=4096.) -> dict:` | Sample simultaneous tree RSS incl renderer. Peaks/CPU are sampling bounds. |
| `render_svg` | `function` | `Lines 112–132` | `def render_svg(path: Path,png: Path,width: int,height: int) -> dict:` | Explicit renderer selection; never silently fall back from Inkscape. |
| `run_trial` | `function` | `Lines 136–155` | `def run_trial(source: Path,folder: Path,config: dict) -> dict:` | Run isolated native worker; retain failed configs, logs, and measurements. |
| `worker` | `function` | `Lines 157–172` | `def worker(source: Path,folder: Path) -> None:` | Generate real SVG; historical validation and metrics, native renderer. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `prepare_input` — `Lines 21–34`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `34` (`Lines 21–34`)
- **الوظيفة:** Historical derived copy: ICC to sRGB and explicitly composite on white.
- **الكود الفعلي (`Lines 21–34`):**
```python
def prepare_input(source,destination):
    """Historical derived copy: ICC to sRGB and explicitly composite on white."""
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

### `extra_metrics` — `Lines 36–41`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `41` (`Lines 36–41`)
- **الوظيفة:** Historical derived copy: unchanged color and high-frequency diagnostics.
- **الكود الفعلي (`Lines 36–41`):**
```python
def extra_metrics(source,pred):
    """Historical derived copy: unchanged color and high-frequency diagnostics."""
    de=np.linalg.norm(rgb2lab(source/255.)-rgb2lab(pred/255.),axis=2)
    residual=source.astype(float)-pred.astype(float);high=residual-gaussian_filter(residual,(1.,1.,0))
    return {'delta_e76_mean':float(de.mean()),'delta_e76_p95':float(np.percentile(de,95)),
            'highpass_rmse_sigma1':float(np.sqrt(np.mean(high**2)))}
```

### `fidelity_score` — `Lines 43–50`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `43` إلى السطر `50` (`Lines 43–50`)
- **الوظيفة:** Historical derived copy: fixed multi-metric score, no complexity penalty.
- **الكود الفعلي (`Lines 43–50`):**
```python
def fidelity_score(metrics):
    """Historical derived copy: fixed multi-metric score, no complexity penalty."""
    psnr=60. if metrics.get('identical') else (metrics.get('psnr_db') or 0.)
    edge=metrics.get('edge_f1_1_5px')
    edge=metrics['ssim'] if edge is None else edge
    return float(.40*metrics['ssim']+.15*min(psnr/60.,1.)+.20*edge+
                 .15*math.exp(-metrics['delta_e76_mean']/12.)+
                 .10*math.exp(-metrics['highpass_rmse_sigma1']/20.))
```

### `terminate_tree` — `Lines 54–63`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `54` إلى السطر `63` (`Lines 54–63`)
- **الوظيفة:** Kill root and known descendants; wait for termination.
- **الكود الفعلي (`Lines 54–63`):**
```python
def terminate_tree(process: psutil.Process, known: dict) -> None:
    """Kill root and known descendants; wait for termination."""
    try:
        for child in process.children(recursive=True): known[child.pid]=child
    except psutil.Error: pass
    targets=list(known.values())+[process]
    for target in targets:
        try: target.kill()
        except psutil.Error: pass
    psutil.wait_procs(targets,timeout=10)
```

### `supervise` — `Lines 65–108`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `108` (`Lines 65–108`)
- **الوظيفة:** Sample simultaneous tree RSS incl renderer. Peaks/CPU are sampling bounds.
- **الكود الفعلي (`Lines 65–108`):**
```python
def supervise(command: list[str], log: Path, timeout: float=180., memory_limit_mib: float=4096.) -> dict:
    """Sample simultaneous tree RSS incl renderer. Peaks/CPU are sampling bounds.

    Per-process Windows peak working sets are recorded separately, never summed.
    The RSS limit is sampled/soft, not an OS reservation. Short-lived children or
    memory peaks between samples can be absent; observed CPU is a lower bound.
    The 10ms sleep is a requested polling delay; enumeration adds overhead.
    """
    start=time.perf_counter();known={};cpu={};peaks={};maximum=0;samples=0;reason=None
    with Path(log).open('w',encoding='utf-8') as stream:
        popen=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,
                               creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        process=psutil.Process(popen.pid)
        try:
            while True:
                try: members=[process]+process.children(recursive=True)
                except psutil.Error: members=list(known.values())
                rss=0
                for member in members:
                    known[member.pid]=member
                    try:
                        mem=member.memory_info();rss+=mem.rss
                        timing=member.cpu_times();cpu[member.pid]=max(cpu.get(member.pid,0),timing.user+timing.system)
                        if hasattr(mem,'peak_wset'): peaks[member.pid]=max(peaks.get(member.pid,0),mem.peak_wset)
                    except psutil.Error: pass
                maximum=max(maximum,rss);samples+=1
                if popen.poll() is not None: break
                if time.perf_counter()-start>timeout: reason='timeout';break
                if rss>memory_limit_mib*1024**2: reason='sampled_memory_limit';break
                time.sleep(.01)
            if reason: terminate_tree(process,known)
            returncode=popen.wait(timeout=10)
        finally:
            for pid,member in known.items():
                if pid!=process.pid:
                    try:
                        if member.is_running(): member.kill()
                    except psutil.Error: pass
            if popen.poll() is None: terminate_tree(process,known)
    return {'returncode':returncode,'termination_reason':reason,'wall_seconds':time.perf_counter()-start,
            'sampled_tree_peak_mib':maximum/1024**2,'observed_process_cpu_seconds':sum(cpu.values()),
            'memory_samples':samples,'observed_pids':sorted(known),
            'windows_peak_wset_mib_by_pid':{str(k):v/1024**2 for k,v in peaks.items()},
            'memory_note':'10ms polling delay plus sampling overhead; simultaneous process-tree RSS including renderer may miss short peaks; separate Windows per-process peak_wset; 4096 MiB soft sampled limit'}
```

### `render_svg` — `Lines 112–132`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `112` إلى السطر `132` (`Lines 112–132`)
- **الوظيفة:** Explicit renderer selection; never silently fall back from Inkscape.
- **الكود الفعلي (`Lines 112–132`):**
```python
def render_svg(path: Path,png: Path,width: int,height: int) -> dict:
    """Explicit renderer selection; never silently fall back from Inkscape."""
    kind=os.environ.get('AGD_RENDERER','inkscape');executable=os.environ.get('AGD_RENDERER_EXE','inkscape')
    if kind=='inkscape':
        command=[executable,str(Path(path).resolve()),'--export-area-page','--export-type=png',
                 f'--export-filename={Path(png).resolve()}',f'--export-width={width}',f'--export-height={height}']
    elif kind=='resvg':
        command=[executable,'--width',str(width),'--height',str(height),str(Path(path).resolve()),str(Path(png).resolve())]
    else: raise ValueError('AGD_RENDERER must explicitly be inkscape or resvg')
    stats=supervise(command,Path(png).with_suffix('.renderer.log'),120.)
    if stats['returncode'] or stats['termination_reason']: raise RuntimeError(f'Renderer failed: {stats}')
    with Image.open(png) as im:
        if im.size!=(width,height): raise ValueError('Renderer dimensions differ from source')
        im.verify()
    identified=subprocess.run([executable,'--version'],capture_output=True,text=True,timeout=15,
                              creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    return {'render_seconds':stats['wall_seconds'],'renderer_kind':kind,
            'renderer':(identified.stdout+identified.stderr).strip(),'renderer_command':command,
            'renderer_executable':str(Path(executable).resolve()) if Path(executable).exists() else executable,
            'renderer_resources':stats,'renderer_comparability':
            'historical renderer family' if kind=='inkscape' else 'different renderer: historical Inkscape scores not directly equivalent'}
```

### `run_trial` — `Lines 136–155`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `136` إلى السطر `155` (`Lines 136–155`)
- **الوظيفة:** Run isolated native worker; retain failed configs, logs, and measurements.
- **الكود الفعلي (`Lines 136–155`):**
```python
def run_trial(source: Path,folder: Path,config: dict) -> dict:
    """Run isolated native worker; retain failed configs, logs, and measurements."""
    # START CHANGE AGD-CODEX-WIN-EVIDENCE-GUARD | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
    folder=Path(folder)
    if folder.exists() and any(folder.iterdir()):
        raise FileExistsError('Trial folder must be empty; previous evidence is immutable')
    folder.mkdir(parents=True,exist_ok=True)
    # END CHANGE AGD-CODEX-WIN-EVIDENCE-GUARD | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
    (folder/'config.json').write_text(json.dumps(config,indent=2),encoding='utf-8')
    start=time.perf_counter();stats=None
    try:
        stats=supervise([sys.executable,str(Path(__file__).resolve()),'--worker','--input',
                         str(Path(source).resolve()),'--output',str(folder.resolve())],folder/'process.log')
        if stats['returncode'] or stats['termination_reason']: raise RuntimeError(f'worker failed: {stats}')
        result=json.loads((folder/'result.json').read_text(encoding='utf-8'))
    except Exception as error: result={'status':'failed','error':str(error),'config':config}
    result['isolated_process_wall_seconds']=time.perf_counter()-start
    result.setdefault('performance',{})['worker_tree_resources']=stats
    (folder/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False),encoding='utf-8')
    return result
```

### `worker` — `Lines 157–172`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `157` إلى السطر `172` (`Lines 157–172`)
- **الوظيفة:** Generate real SVG; historical validation and metrics, native renderer.
- **الكود الفعلي (`Lines 157–172`):**
```python
def worker(source: Path,folder: Path) -> None:
    """Generate real SVG; historical validation and metrics, native renderer."""
    import vtracer
    folder=Path(folder);config=json.loads((folder/'config.json').read_text(encoding='utf-8'))
    rgb=load_rgb(source);h,w=rgb.shape[:2];svg=folder/'output.svg'
    start=time.perf_counter();cpu=time.process_time()
    vtracer.Config(**config).convert_file(str(source),str(svg))
    trace={'trace_wall_seconds':time.perf_counter()-start,'trace_cpu_seconds':time.process_time()-cpu}
    structure=svg_structure(svg)
    if not structure['raster_free'] or structure['external_href_count'] or structure['script_count']:
        raise ValueError('Not a self-contained raster-free SVG')
    timing=render_svg(svg,folder/'render.png',w,h)
    pred=load_rgb(folder/'render.png');metrics=compare(rgb,pred)|extra_metrics(rgb,pred)
    result={'status':'ok','vtracer_version':version('vtracer'),'config':config,'metrics':metrics,
            'score':fidelity_score(metrics),'structure':structure,'performance':trace|timing}
    (folder/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False),encoding='utf-8')
```
