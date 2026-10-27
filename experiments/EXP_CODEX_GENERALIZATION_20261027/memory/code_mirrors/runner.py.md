# مرآة الكود التفصيلية: `runner.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `runner.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `runner.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `93` (`Lines 1–93`)
- **بصمة الملف (`SHA-256`):** `dd9001c3111fc7b0390f6058e3b500a6fc8f98789c5b0b28983c709a70e0a1d0`
- **الوصف التفصيلي:** """Frozen-baseline search and explicit alpha-aware candidate selection research."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `read_suite` | `function` | `Lines 14–19` | `def read_suite(path):` | Load frozen case list and reject hash drift before invoking any search. |
| `rgb_diagnostics` | `function` | `Lines 21–27` | `def rgb_diagnostics(reference,predicted):` | Inherited metrics plus independent worst spatial-tile residual diagnostics. |
| `run_generalization_case` | `function` | `Lines 29–85` | `def run_generalization_case(case,manifest_hash,max_candidates=24,max_seconds=240):` | One inherited search per unseen image; new alpha selection reuses its candidates. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `read_suite` — `Lines 14–19`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `19` (`Lines 14–19`)
- **الوظيفة:** Load frozen case list and reject hash drift before invoking any search.
- **الكود الفعلي (`Lines 14–19`):**
```python
def read_suite(path):
    """Load frozen case list and reject hash drift before invoking any search."""
    payload=json.loads(Path(path).read_text(encoding='utf-8'))
    cases=payload if isinstance(payload,list) else payload.get('cases',payload.get('inputs'))
    if not cases:raise ValueError('Manifest requires cases or inputs')
    return cases
```

### `rgb_diagnostics` — `Lines 21–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `27` (`Lines 21–27`)
- **الوظيفة:** Inherited metrics plus independent worst spatial-tile residual diagnostics.
- **الكود الفعلي (`Lines 21–27`):**
```python
def rgb_diagnostics(reference,predicted):
    """Inherited metrics plus independent worst spatial-tile residual diagnostics."""
    m=compare(reference,predicted)|extra_metrics(reference,predicted)
    error=(reference.astype(float)-predicted.astype(float))**2
    tiles=[float(np.sqrt(error[y:y+32,x:x+32].mean())) for y in range(0,len(error),32) for x in range(0,error.shape[1],32)]
    m.update(worst_32px_tile_rmse=max(tiles),median_32px_tile_rmse=float(np.median(tiles)))
    return m
```

### `run_generalization_case` — `Lines 29–85`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `85` (`Lines 29–85`)
- **الوظيفة:** One inherited search per unseen image; new alpha selection reuses its candidates.
- **الكود الفعلي (`Lines 29–85`):**
```python
def run_generalization_case(case,manifest_hash,max_candidates=24,max_seconds=240):
    """One inherited search per unseen image; new alpha selection reuses its candidates."""
    case_id=case['id'];file=case['file'];source=ROOT/'inputs'/file
    if not source.is_file():source=ROOT/file
    actual=hashlib.sha256(source.read_bytes()).hexdigest()
    if case.get('sha256') and actual!=case['sha256']:raise ValueError('Frozen input hash differs')
    out=ROOT/'results'/case_id
    if (out/'case_result.json').exists():
        result=json.loads((out/'case_result.json').read_text());assert result['source_sha256']==actual
        print('REUSE completed current-cycle case',case_id,flush=True);return result
    if out.exists() and any(out.iterdir()):raise FileExistsError('Partial case preserved; choose a new experiment or investigate')
    out.mkdir(parents=True,exist_ok=True);started=time.perf_counter()
    with Image.open(source) as im:has_alpha=im.convert('RGBA').getchannel('A').getextrema()!=(255,255)
    prep=prepare_transparent_input(source,out/'prepared')
    ranking=optimize(out/'prepared/unassociated_rgb.png',out/'baseline_search',max_candidates,max_seconds,'reject')
    if not ranking['ranked']:
        failure={'id':case_id,'status':'failed','ranking':ranking,'source_sha256':actual}
        (out/'case_result.json').write_text(json.dumps(failure,indent=2));return failure
    best=ranking['ranked'][0];evaluated=[];cache={}
    for row in ranking['ranked']:
        trial=row['trial'];rgb_svg=out/'baseline_search'/trial/'output.svg'
        if has_alpha:
            digest=hashlib.sha256(rgb_svg.read_bytes()).hexdigest()
            if digest in cache:
                assessment=dict(cache[digest]);assessment.update(trial=trial,cache_reused_from=cache[digest]['trial'])
            else:
                target=out/'alpha_candidates'/trial;target.mkdir(parents=True)
                mask=apply_vector_alpha(rgb_svg,out/'prepared/source_alpha.png',target/'output.svg')
                assessment=evaluate_alpha(out/'prepared/reference_srgb_rgba.png',target/'output.svg',target)
                assessment['trial']=trial;assessment['svg_relative']=str((target/'output.svg').relative_to(out));assessment['png_relative']=str((target/'render_rgba.png').relative_to(out))
                assessment['vector_alpha']=mask
                cache[digest]=assessment
            scores=[fidelity_score(m) for m in assessment['background_metrics'].values()]
            assessment.update(robust_score=min(scores),mean_score=float(np.mean(scores)),inherited_rgb_score=row['score'])
        else:
            pred=load_rgb(out/'baseline_search'/trial/'render.png');ref=load_rgb(out/'prepared/unassociated_rgb.png')
            metrics=rgb_diagnostics(ref,pred)
            assessment={'trial':trial,'metrics':metrics,'robust_score':row['score'],'mean_score':row['score'],
                        'svg_relative':str(rgb_svg.relative_to(out)),'png_relative':str((out/'baseline_search'/trial/'render.png').relative_to(out)),'inherited_rgb_score':row['score']}
        evaluated.append(assessment)
    inherited=next(x for x in evaluated if x['trial']==best['trial'])
    selected=sorted(evaluated,key=lambda r:(-r['robust_score'],-r['mean_score'],-r['inherited_rgb_score'],r['trial']))[0]
    # Opaque images deliberately retain frozen baseline until a separate measured hypothesis is enabled.
    if not has_alpha:selected=inherited
    for label,row in [('inherited',inherited),('new',selected)]:
        shutil.copyfile(out/row['svg_relative'],out/f'{label}.svg');shutil.copyfile(out/row['png_relative'],out/f'{label}.png')
    result={'id':case_id,'status':'ok','source_sha256':actual,'dataset_manifest_sha256':manifest_hash,'has_alpha':has_alpha,
            'normalization':prep,'baseline_commit':'b398de3d95539a77ee4ea1cafea2e1ecc7f2efdf','baseline_candidates':ranking['evaluated_candidates'],
            'failed_candidates':len(ranking['failed']),'baseline_stop':ranking['stop_reason'],'baseline_search_wall_seconds':ranking['search_wall_seconds'],
            'families_evaluated':ranking['families_evaluated'],'selection_policy':'maximize minimum inherited fidelity score over white/black/bluegray, mean then RGB score tie-break; no complexity penalty',
            'inherited':inherited,'new':selected,'alpha_candidate_assessments':evaluated if has_alpha else [],
            'rgb_metric_leaders':{k:max(ranking['ranked'],key=lambda r:r['metrics'][k] if r['metrics'][k] is not None else float('-inf'))['trial'] for k in ['ssim','psnr_db','edge_f1_1_5px']},
            'maximum_sampled_worker_tree_mib':max(r['performance']['worker_tree_resources']['sampled_tree_peak_mib'] for r in ranking['ranked']),
            'total_wall_seconds':time.perf_counter()-started,'architecture':'NOT_APPROVED'}
    (out/'case_result.json').write_text(json.dumps(result,indent=2,allow_nan=False),encoding='utf-8')
    print('COMPLETE',case_id,'alpha',has_alpha,'candidates',result['baseline_candidates'],'selected',inherited['trial'],'->',selected['trial'],'wall',round(result['total_wall_seconds'],1),flush=True)
    return result
```
