# مرآة الكود التفصيلية: `run_matrix.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_matrix.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_matrix.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `68` (`Lines 1–68`)
- **بصمة الملف (`SHA-256`):** `f748284a0c49d94b14f409cca7358e969ede20b84ff69637164e0363cc0b0ffa`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-RUN-MATRIX | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `verify_resume_inputs` | `function` | `Lines 16–28` | `def verify_resume_inputs():` | رمز برمجي موثق. |
| `launch` | `function` | `Lines 30–35` | `def launch(command,name):` | رمز برمجي موثق. |
| `vt_segment` | `function` | `Lines 37–47` | `def vt_segment(case):` | رمز برمجي موثق. |
| `vt_fit` | `function` | `Lines 49–59` | `def vt_fit(case,seg):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `verify_resume_inputs` — `Lines 16–28`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `28` (`Lines 16–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–28`):**
```python
def verify_resume_inputs():
    inputs=json.loads((ROOT/'inputs/manifest.json').read_text())
    for case,item in inputs.items():
        if digest(item['source'])!=item['source_sha256'] or digest(item['working'])!=item['working_sha256']:
            raise RuntimeError('Frozen source/working input changed: '+case)
    existing=[case_dir(c)/(s+'_F_'+f+'.json') for c in CASES for s in ['S_A','S_V'] for f in ['A','V']]
    existing=[p for p in existing if p.exists()]
    if existing:
        manifest=ROOT/'reports/CANDIDATE_MANIFEST.json'
        if not manifest.exists():raise RuntimeError('Existing candidates need explicit artifact validation; refusing existence-only resume')
        expected=json.loads(manifest.read_text())['files']
        for path in existing:
            if expected.get(str(path))!=digest(path):raise RuntimeError('Existing candidate hash differs: '+str(path))
```

### `launch` — `Lines 30–35`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `35` (`Lines 30–35`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–35`):**
```python
def launch(command,name):
    record=mon.monitor([str(x) for x in command],logs/(name+'.log'),timeout=600,memory_mib=4096)
    dump(logs/(name+'.json'),record)
    print(name,json.dumps(record),flush=True)
    if record['returncode'] or record['termination_reason']:raise RuntimeError(name+' failed; preserve output and stop portion')
    return record
```

### `vt_segment` — `Lines 37–47`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `37` إلى السطر `47` (`Lines 37–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 37–47`):**
```python
def vt_segment(case):
    out=case_dir(case);target=out/'S_V.npy'
    if target.exists():return
    rgba=np.asarray(Image.open(out/'working.png').convert('RGBA'));h,w=rgba.shape[:2]
    request=WORK/'complete_geometry_isolation'/('segment_'+case+'.json');request.parent.mkdir(parents=True,exist_ok=True)
    dump(request,{'width':w,'height':h,'rgba':rgba.ravel().tolist(),'detail':192,'min_area':0})
    response=out/'S_V_response.json';launch([native,'segment',request,response],case+'_segment_V')
    obj=json.loads(response.read_text());labels=np.asarray(obj.pop('labels'),dtype=np.uint32).reshape(h,w)
    assert labels.min()>=1
    np.save(target,labels);obj['labels_sha256']=digest(target);dump(out/'S_V_meta.json',obj)
    response.unlink() # transient duplicate label serialization; canonical NPY preserved
```

### `vt_fit` — `Lines 49–59`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `59` (`Lines 49–59`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–59`):**
```python
def vt_fit(case,seg):
    out=case_dir(case);target=out/(seg+'_F_V.json')
    if target.exists():return
    labels=np.load(out/(seg+'.npy'),allow_pickle=False);h,w=labels.shape
    request=WORK/'complete_geometry_isolation'/('fit_'+case+'_'+seg+'.json')
    dump(request,{'width':w,'height':h,'labels':labels.ravel().tolist()})
    launch([native,'fit',request,target],case+'_'+seg+'_fit_V')
    obj=json.loads(target.read_text());echo=np.asarray(obj.pop('labels'),dtype=np.uint32).reshape(h,w)
    assert np.array_equal(echo,labels),'Initializer changed labels'
    assert obj['graph_matches_exact_labels']
    obj['labels_sha256']=digest(out/(seg+'.npy'));dump(target,obj)
```
