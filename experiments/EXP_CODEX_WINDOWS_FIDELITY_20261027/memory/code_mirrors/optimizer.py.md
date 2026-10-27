# مرآة الكود التفصيلية: `optimizer.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `optimizer.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `optimizer.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `103` (`Lines 1–103`)
- **بصمة الملف (`SHA-256`):** `094956a42000f93b1954c4de4619c1d2717e34d9ec9d26844bdecfea2ea03baf`
- **الوصف التفصيلي:** """Historical adaptive optimizer derived copy with native Windows trial adapter.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `canonical` | `function` | `Lines 16–29` | `def canonical(c):` | رمز برمجي موثق. |
| `pilots` | `function` | `Lines 31–42` | `def pilots():` | رمز برمجي موثق. |
| `neighborhood` | `function` | `Lines 44–51` | `def neighborhood(c):` | رمز برمجي موثق. |
| `optimize` | `function` | `Lines 53–98` | `def optimize(source,output,max_candidates=24,max_seconds=720,alpha_policy='reject'):` | رمز برمجي موثق. |
| `optimize.budget` | `nested_function` | `Lines 66–66` | `def budget():return len(rows)>=max_candidates or time.monotonic()-start>=max_seconds` | رمز برمجي موثق. |
| `optimize.trial` | `nested_function` | `Lines 67–72` | `def trial(c,phase):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `canonical` — `Lines 16–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `29` (`Lines 16–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–29`):**
```python
def canonical(c):
    c=dict(c); f=c['clustering']
    if f!='color-cluster':
        c.pop('color_precision',None)
        if not (f=='bw' and c['hierarchical']=='cutout'):c.pop('layer_difference',None)
    if f!='watershed':c.pop('watershed_detail',None)
    if f!='bw':
        for k in ('binary_threshold','adaptive','adaptive_window','adaptive_t'):c.pop(k,None)
    elif c.get('adaptive',False):c.pop('binary_threshold',None)
    else:
        for k in ('adaptive_window','adaptive_t'):c.pop(k,None)
    if c['mode']!='spline':
        for k in ('simplify','corner_threshold','length_threshold','max_iterations','splice_threshold'):c.pop(k,None)
    return c
```

### `pilots` — `Lines 31–42`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `42` (`Lines 31–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–42`):**
```python
def pilots():
    changes=[{}, {'mode':'pixel','layer_difference':1}, {'mode':'pixel','layer_difference':0},
      {'mode':'pixel','layer_difference':1,'hierarchical':'cutout'},
      {'mode':'polygon','path_precision':3}, {'path_precision':3,'simplify':None},
      {'clustering':'watershed','mode':'pixel','watershed_detail':512,'hierarchical':'cutout','path_precision':3},
      {'clustering':'watershed','mode':'pixel','watershed_detail':256},
      {'clustering':'watershed','mode':'spline','watershed_detail':128,'hierarchical':'cutout','path_precision':3,'simplify':None},
      {'clustering':'watershed','mode':'polygon','watershed_detail':256,'hierarchical':'cutout','path_precision':3},
      {'clustering':'bw','mode':'pixel','binary_threshold':128},
      {'clustering':'bw','mode':'spline','hierarchical':'cutout','binary_threshold':128,'path_precision':3,'simplify':None},
      {'clustering':'bw','mode':'pixel','adaptive':True,'adaptive_window':0,'adaptive_t':15}]
    return [canonical(OWNER|d) for d in changes]
```

### `neighborhood` — `Lines 44–51`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `51` (`Lines 44–51`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–51`):**
```python
def neighborhood(c):
    f=c['clustering']
    if f=='watershed':changes=[{'watershed_detail':min(2048,c.get('watershed_detail',128)*2)},{'watershed_detail':max(1,c.get('watershed_detail',128)//2)}]
    elif f=='color-cluster':changes=[{'layer_difference':x} for x in (1,2,8,0)]+[{'color_precision':x} for x in (7,6)]
    else:changes=([{'adaptive_t':x} for x in (5,25)]+[{'adaptive_window':x} for x in (15,31)]) if c.get('adaptive') else [{'binary_threshold':x} for x in (96,160,192)]
    changes += [{'hierarchical':'cutout' if c['hierarchical']=='stacked' else 'stacked'}]+[{'filter_speckle':x} for x in (1,2)]+[{'path_precision':x} for x in (5,1)]+[{'optimize':0}]
    if c['mode']=='spline':changes += [{'simplify':x} for x in (None,.25,.75)]+[{'length_threshold':2.},{'corner_threshold':45},{'splice_threshold':30},{'max_iterations':20}]
    return [canonical(c|d) for d in changes]
```

### `optimize` — `Lines 53–98`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `53` إلى السطر `98` (`Lines 53–98`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 53–98`):**
```python
def optimize(source,output,max_candidates=24,max_seconds=720,alpha_policy='reject'):
    source=Path(source);out=Path(output)
    if out.exists() and any(out.iterdir()):raise FileExistsError('Output must be empty')
    if max_candidates<13 or max_seconds<=0:raise ValueError('Require >=13 candidates and positive time budget')
    if version('vtracer')!='1.0.0a4':raise RuntimeError('Pinned parameter surface requires vtracer 1.0.0a4')
    with Image.open(source) as im:
        if getattr(im,'n_frames',1)!=1 or min(im.size)<7:raise ValueError('Requires single frame, width and height >=7')
        if alpha_policy not in ('reject','white'):raise ValueError('Unknown alpha policy')
        if im.convert('RGBA').getchannel('A').getextrema()!=(255,255) and alpha_policy=='reject':raise ValueError('Transparency unsupported; explicitly choose white compositing')
    out.mkdir(parents=True,exist_ok=True);start=time.monotonic();rows=[];events=[];seen=set()
    norm=prepare_input(source,out/'normalized.png');norm['requested_alpha_policy']=alpha_policy
    (out/'normalization.json').write_text(json.dumps(norm,indent=2))
    (out/'plan.json').write_text(json.dumps({'pilots':pilots(),'max_candidates':max_candidates,'max_seconds':max_seconds,'stagnation_rounds':2,'minimum_improvement':1e-5,'budget':'dispatch deadline; current worker may add180seconds'},indent=2))
    def budget():return len(rows)>=max_candidates or time.monotonic()-start>=max_seconds
    def trial(c,phase):
        key=json.dumps(canonical(c),sort_keys=True)
        if key in seen:
            events.append({'status':'rejected','reason':'duplicate_effective_config','config':c});return False
        seen.add(key);name=f'trial_{len(rows):02d}';r=run_trial(out/'normalized.png',out/name,canonical(c));r.update(trial=name,phase=phase);rows.append(r)
        (out/'progress.json').write_text(json.dumps(rows,indent=2));return True
    for c in pilots():
        if budget():break
        trial(c,'pilot')
    stale=0;stop='budget'
    while not budget():
        good=sorted((r for r in rows if r['status']=='ok'),key=lambda r:-r['score'])
        if not good:stop='all_failed';break
        if good[0]['score']>=1-1e-12:stop='perfect_numeric_score';break
        previous=good[0]['score'];leaders={}
        for r in good:leaders.setdefault(r['config']['clustering'],r)
        attempted=False
        for r in leaders.values():
            if budget():break
            for c in neighborhood(r['config']):
                if trial(c,'adaptive'):attempted=True;break
        if not attempted:stop='neighborhood_exhausted';break
        current=max(r.get('score',0) for r in rows)
        stale=stale+1 if current-previous<1e-5 else 0
        if stale>=2:stop='stagnation';break
    ranked=sorted((r for r in rows if r['status']=='ok'),key=lambda r:(-r['score'],r['trial']))
    result={'ranked':ranked,'failed':[r for r in rows if r['status']!='ok'],'events':events,'stop_reason':stop,'search_wall_seconds':time.monotonic()-start,'evaluated_candidates':len(rows),'families_evaluated':sorted({r['config']['clustering'] for r in rows})}
    (out/'ranking.json').write_text(json.dumps(result,indent=2));(out/'search_events.json').write_text(json.dumps(events,indent=2))
    if ranked:
        for a,b in [('output.svg','best.svg'),('render.png','best.png')]:shutil.copyfile(out/ranked[0]['trial']/a,out/b)
        (out/'best_config.json').write_text(json.dumps(ranked[0]['config'],indent=2))
    return result
```

### `optimize.budget` — `Lines 66–66`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `66` إلى السطر `66` (`Lines 66–66`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 66–66`):**
```python
    def budget():return len(rows)>=max_candidates or time.monotonic()-start>=max_seconds
```

### `optimize.trial` — `Lines 67–72`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `67` إلى السطر `72` (`Lines 67–72`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 67–72`):**
```python
    def trial(c,phase):
        key=json.dumps(canonical(c),sort_keys=True)
        if key in seen:
            events.append({'status':'rejected','reason':'duplicate_effective_config','config':c});return False
        seen.add(key);name=f'trial_{len(rows):02d}';r=run_trial(out/'normalized.png',out/name,canonical(c));r.update(trial=name,phase=phase);rows.append(r)
        (out/'progress.json').write_text(json.dumps(rows,indent=2));return True
```
