# مرآة الكود التفصيلية: `validate_local.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `validate_local.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `validate_local.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `75` (`Lines 1–75`)
- **بصمة الملف (`SHA-256`):** `c4216a54a60c4180400910205922630712c026635a939f324a07e4ba451b3cc8`
- **الوصف التفصيلي:** """Independent saved-metric and real-output checks for the local handoff."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `audit_saved_metrics` | `function` | `Lines 12–26` | `def audit_saved_metrics():` | Recompute twelve selected saved renders; this is not retracing twelve images. |
| `audit_local_case` | `function` | `Lines 28–69` | `def audit_local_case(name,repeat=False):` | Check every candidate and winner, recompute metrics, optionally retrace winner. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `audit_saved_metrics` — `Lines 12–26`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `26` (`Lines 12–26`)
- **الوظيفة:** Recompute twelve selected saved renders; this is not retracing twelve images.
- **الكود الفعلي (`Lines 12–26`):**
```python
def audit_saved_metrics():
    """Recompute twelve selected saved renders; this is not retracing twelve images."""
    inherited=ROOT.parent/'EXP_ADAPTIVE_VTRACER_20261027'
    rows=[]
    for folder in sorted((inherited/'results').glob('A*')):
        ranking=json.loads((folder/'ranking.json').read_text())
        best=ranking['ranked'][0]
        ref=load_rgb(folder/'normalized.png');pred=load_rgb(folder/'best.png')
        metrics=compare(ref,pred)|extra_metrics(ref,pred)
        differences={k:abs(v-best['metrics'][k]) for k,v in metrics.items() if isinstance(v,(int,float)) and best['metrics'].get(k) is not None}
        rows.append({'case':folder.name,'metrics':metrics,'maximum_numeric_difference':max(differences.values()),'selected_svg_copy_matches':(folder/'best.svg').read_bytes()==(folder/best['trial']/'output.svg').read_bytes()})
    assert len(rows)==12 and all(r['maximum_numeric_difference']<1e-10 and r['selected_svg_copy_matches'] for r in rows)
    report={'scope':'Independent metric recomputation from saved historical renders, not tracing or rerendering all twelve','cases':rows,'mean_ssim':float(np.mean([r['metrics']['ssim'] for r in rows])),'mean_psnr_db':float(np.mean([r['metrics']['psnr_db'] for r in rows]))}
    (ROOT/'reports/saved12_metric_recomputation.json').write_text(json.dumps(report,indent=2))
    print('Saved12',report['mean_ssim'],report['mean_psnr_db'],flush=True)
```

### `audit_local_case` — `Lines 28–69`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `28` إلى السطر `69` (`Lines 28–69`)
- **الوظيفة:** Check every candidate and winner, recompute metrics, optionally retrace winner.
- **الكود الفعلي (`Lines 28–69`):**
```python
def audit_local_case(name,repeat=False):
    """Check every candidate and winner, recompute metrics, optionally retrace winner."""
    folder=ROOT/'results'/name;ranking=json.loads((folder/'ranking.json').read_text())
    good=ranking['ranked'];assert good,ranking
    assert good==sorted(good,key=lambda r:(-r['score'],r['trial']))
    audits=[]
    for row in good:
        svg=folder/row['trial']/'output.svg';render=folder/row['trial']/'render.png'
        root=ET.fromstring(svg.read_bytes());tags={e.tag.split('}')[-1] for e in root.iter()}
        assert tags<={'svg','path'},tags
        structure=svg_structure(svg)
        assert structure['raster_free'] and structure['external_href_count']==0
        metrics=compare(load_rgb(folder/'normalized.png'),load_rgb(render))|extra_metrics(load_rgb(folder/'normalized.png'),load_rgb(render))
        assert metrics==row['metrics'] and fidelity_score(metrics)==row['score']
        assert Image.open(render).size==Image.open(folder/'normalized.png').size
        audits.append({'trial':row['trial'],'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),'tags':sorted(tags)})
    best=good[0];assert (folder/'best.svg').read_bytes()==(folder/best['trial']/'output.svg').read_bytes()
    result={'case':name,'candidate_count':ranking['evaluated_candidates'],'successful':len(good),'failed':len(ranking['failed']),'stop_reason':ranking['stop_reason'],'winner':best,'all_candidate_checks':audits,'maximum_sampled_worker_tree_mib':max(r['performance']['worker_tree_resources']['sampled_tree_peak_mib'] for r in good),'search_wall_seconds':ranking['search_wall_seconds']}
    inherited=ROOT.parent/'EXP_ADAPTIVE_VTRACER_20261027/results'/name
    if inherited.exists():
        old=json.loads((inherited/'ranking.json').read_text())['ranked'][0]
        result['historical_comparison']={'same_selected_config':best['config']==old['config'],'same_svg_bytes':(folder/'best.svg').read_bytes()==(inherited/'best.svg').read_bytes(),'historical_metrics':old['metrics'],'renderer_change':'local resvg vs historical Inkscape'}
    if repeat:
        replay_folder=ROOT/'reproduction'/name
        if replay_folder.exists() and any(replay_folder.iterdir()):
            raise FileExistsError('Replay destination is nonempty; preserve prior evidence')
        rerun=run_trial(folder/'normalized.png',replay_folder,best['config'])
        result['repeat']=rerun
        assert rerun['status']=='ok'
        result['repeat_svg_equal']=(ROOT/'reproduction'/name/'output.svg').read_bytes()==(folder/'best.svg').read_bytes()
        result['repeat_png_equal']=(ROOT/'reproduction'/name/'render.png').read_bytes()==(folder/'best.png').read_bytes()
        result['repeat_metrics_equal']=rerun['metrics']==best['metrics']
        assert result['repeat_svg_equal'] and result['repeat_png_equal'] and result['repeat_metrics_equal']
    ref=Image.open(folder/'normalized.png').convert('RGB');pred=Image.open(folder/'best.png').convert('RGB');w,h=ref.size
    sheet=Image.new('RGB',(3*w,h+26),'white');draw=ImageDraw.Draw(sheet)
    err=np.abs(np.array(ref).astype(float)-np.array(pred).astype(float)).mean(2)
    heat=np.stack([np.clip(err*8,0,255),np.zeros_like(err),np.zeros_like(err)],axis=2).astype('uint8')
    for i,(label,im) in enumerate([('Original',ref),('Actual SVG render',pred),('Mean absolute error x8',Image.fromarray(heat))]):
        draw.text((i*w+4,5),label,fill='black');sheet.paste(im,(i*w,26))
    sheet.save(folder/'local_comparison.png')
    (ROOT/'reports'/f'{name}_validation.json').write_text(json.dumps(result,indent=2))
    print(name,best['metrics']['ssim'],best['metrics']['psnr_db'],len(good),result['maximum_sampled_worker_tree_mib'],flush=True)
```
