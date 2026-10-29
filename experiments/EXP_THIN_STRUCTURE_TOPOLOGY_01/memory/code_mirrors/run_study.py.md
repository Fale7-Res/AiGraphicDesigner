# مرآة الكود التفصيلية: `run_study.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_study.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_study.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `52` (`Lines 1–52`)
- **بصمة الملف (`SHA-256`):** `98755e25a654d6304584df5da2220bb95763a9520235dd256e10cc56179ca101`
- **الوصف التفصيلي:** # START CHANGE AGD-THIN-RUN-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `execute` | `function` | `Lines 8–47` | `def execute(case,condition):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `execute` — `Lines 8–47`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `47` (`Lines 8–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–47`):**
```python
def execute(case,condition):
    policy=json.loads((ROOT/'protocol.json').read_text(encoding='utf-8'))
    if policy['status']!='FROZEN_BEFORE_CANDIDATES':raise RuntimeError('Protocol not frozen')
    pins=json.loads((ROOT/'BASELINE_PINS.json').read_text(encoding='utf-8'))['cases'][case]
    for item in pins.values():
        if digest(item['path'])!=item['sha256']:raise RuntimeError('Inherited baseline changed')
    out=destination(case);out.mkdir(parents=True,exist_ok=True)
    target=out/(condition+'.json')
    if target.exists():raise RuntimeError('Refusing candidate overwrite: '+str(target))
    rgb,labels,g=load_baseline(case);Image.fromarray(rgb).save(out/'working.png')
    start=time.monotonic();cpu=time.process_time();audit={}
    if condition=='baseline':
        shutil.copy2(pins['S_A_F_A_common_faces.json']['path'],target)
    elif condition=='A':
        from track_a import discover,DEFAULT_CONFIG
        cfg={k:policy['track_a'].get(k,v) for k,v in DEFAULT_CONFIG.items()}
        cfg['radius_floor_px']=policy['track_a']['radius_floor'];cfg['max_endpoint_pairs']=policy['track_a']['max_pair_proposals']
        labels,audit,evidence=discover(rgb,labels,config=cfg)
        if labels.shape!=rgb.shape[:2] or labels.min()<1:raise ValueError('Invalid source-discovery label contract')
        for name,array in evidence.items():
            array=np.asarray(array)
            if array.ndim==2:
                lo=float(np.nanmin(array));hi=float(np.nanmax(array));image=np.nan_to_num((array-lo)/max(hi-lo,1e-9)*255).astype(np.uint8)
                Image.fromarray(image).save(out/('A_evidence_'+name+'.png'))
        np.savez_compressed(out/'A_evidence.npz',**evidence)
        g=initialize_labels(labels);dump(target,g)
    elif condition=='B':
        from track_b import initialize_safe,FROZEN_CONFIG
        cfg={k:policy['track_b'][k] for k in FROZEN_CONFIG}
        g,audit=initialize_safe(g,config=cfg);dump(target,g)
    elif condition=='AB':
        from track_b import initialize_safe,FROZEN_CONFIG
        labels=np.load(out/'A_labels.npy',allow_pickle=False);g=json.loads((out/'A.json').read_text(encoding='utf-8'))
        cfg={k:policy['track_b'][k] for k in FROZEN_CONFIG}
        g,audit=initialize_safe(g,config=cfg);dump(target,g)
    else:raise ValueError(condition)
    np.save(out/(condition+'_labels.npy'),labels)
    audit['case']=case;audit['condition']=condition;audit['wall_seconds']=time.monotonic()-start;audit['process_cpu_seconds']=time.process_time()-cpu
    audit['candidate_sha256']=digest(target);audit['labels_sha256']=digest(out/(condition+'_labels.npy'));dump(out/(condition+'_audit.json'),audit)
    print(json.dumps({k:audit[k] for k in ['case','condition','wall_seconds','process_cpu_seconds','candidate_sha256']}),flush=True)
```
