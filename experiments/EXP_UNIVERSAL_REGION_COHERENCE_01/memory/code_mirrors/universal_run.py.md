# مرآة الكود التفصيلية: `universal_run.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `universal_run.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `universal_run.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `80` (`Lines 1–80`)
- **بصمة الملف (`SHA-256`):** `ba74fe4a89a0600fa9c06d76aa4ecae37bc2351dd1c31bc19c34646a537e8ba5`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-RUN | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `output_folder` | `function` | `Lines 23–24` | `def output_folder(case):` | رمز برمجي موثق. |
| `selection_rank` | `function` | `Lines 26–44` | `def selection_rank(traces,rgb):` | Fixed score, all source features only; no length term or image identifiers. |
| `new_classical` | `function` | `Lines 46–59` | `def new_classical(rgb):` | رمز برمجي موثق. |
| `run_universal_case` | `function` | `Lines 61–78` | `def run_universal_case(case):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `output_folder` — `Lines 23–24`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `24` (`Lines 23–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–24`):**
```python
def output_folder(case):
 return (W/'universal_geometry/local_only'/case if case=='fine_features' else E/'results'/case)
```

### `selection_rank` — `Lines 26–44`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `44` (`Lines 26–44`)
- **الوظيفة:** Fixed score, all source features only; no length term or image identifiers.
- **الكود الفعلي (`Lines 26–44`):**
```python
def selection_rank(traces,rgb):
 """Fixed score, all source features only; no length term or image identifiers."""
 lab=cv2.cvtColor(rgb,cv2.COLOR_RGB2LAB).astype(float)/255.;h,w=rgb.shape[:2];fields=[]
 for sigma in [.6,1.2]:
  smooth=ndimage.gaussian_filter(lab,(sigma,sigma,0));gx=ndimage.sobel(smooth,axis=1)/8;gy=ndimage.sobel(smooth,axis=0)/8;fields.append(np.sqrt((gx*gx+gy*gy).sum(axis=2)))
 thresholds=[max(float(np.quantile(g,.65)),1e-6) for g in fields];near=[ndimage.distance_transform_edt(~(g>=t))<=1 for g,t in zip(fields,thresholds)]
 scale=max(float(np.quantile(fields[0],.9)),1e-6);ends=collections.Counter()
 for t in traces:
  p=np.asarray(t['source_points_xy']);ends[tuple(p[0])]+=1;ends[tuple(p[-1])]+=1
 rows=[]
 for t in traces:
  p=np.asarray(t['source_points_xy']);ix=np.clip(p[:,0].astype(int),0,w-1);iy=np.clip(p[:,1].astype(int),0,h-1)
  persistent=float(np.mean(near[0][iy,ix]&near[1][iy,ix]));contrast=float(np.mean(np.clip(fields[0][iy,ix]/scale,0,1)))
  closed=bool(np.array_equal(p[0],p[-1]));junction=sum(ends[tuple(q)]>=3 for q in [p[0],p[-1]])/2
  simple=cv2.approxPolyDP(p.astype('float32'),.35,False).reshape(-1,2);v=np.diff(simple,axis=0);angles=np.unwrap(np.arctan2(v[:,1],v[:,0]));turn=float(np.median(abs(np.diff(angles)))) if len(angles)>1 else 0.;coherence=float(np.exp(-turn/np.pi))
  score=.35*persistent+.25*contrast+.15*closed+.15*junction+.10*coherence
  rows.append(dict(trace_id=t['trace_id'],score=score,persistence=persistent,contrast=contrast,closed=closed,junction=junction,coherence=coherence,length_px=t['length_px'],eligible=t['length_px']>=6))
 rank={r['trace_id']:r['score'] for r in rows};ordered=sorted(traces,key=lambda t:(-rank[t['trace_id']],t['trace_id']))
 return ordered,rows
```

### `new_classical` — `Lines 46–59`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `46` إلى السطر `59` (`Lines 46–59`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 46–59`):**
```python
def new_classical(rgb):
 arrays,meta=extract(rgb);support=arrays['persistent_edges'];sk=skeletonize(support);raw,_=_trace(sk)
 traces=[]
 for tid,p in enumerate(raw):traces.append(dict(trace_id=tid,length_px=float(np.linalg.norm(np.diff(p,axis=0),axis=1).sum()),source_points_xy=p.tolist(),reason='not_fitted'))
 traces.sort(key=lambda t:(-t['length_px'],t['trace_id']));accepted=[];start=time.monotonic();eligible=0
 for t in traces:
  if t['length_px']<6:t['reason']='short_chain';continue
  eligible+=1
  if eligible>128:t['reason']='proposal_budget';continue
  if time.monotonic()-start>120:t['reason']='case_wall_budget';continue
  cc,meta=fit(np.asarray(t['source_points_xy']));t['stable_fit']=meta
  if cc is None:t['reason']=meta['reason']
  else:t['reason']='accepted';accepted.append(dict(trace_id=t['trace_id'],curves=cc.tolist(),length_px=t['length_px']))
 return dict(traces=traces,accepted=accepted),support,sk
```

### `run_universal_case` — `Lines 61–78`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `61` إلى السطر `78` (`Lines 61–78`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 61–78`):**
```python
def run_universal_case(case):
 protocol=json.loads((E/'protocol.json').read_text());config=protocol['cases'][case];out=output_folder(case);out.mkdir(parents=True,exist_ok=False);start=time.monotonic()
 source=Path(config['source']);assert hashlib.sha256(source.read_bytes()).hexdigest()==protocol['pins'][str(source)]['sha256'];rgb=np.asarray(Image.open(source).convert('RGB'));shutil.copy2(source,out/'source.png')
 h,w=rgb.shape[:2]
 if config['cached']:
  base=Path(config['baseline']);pbase=Path(config['partitioned']);frozen=json.loads((base/'construction.json').read_text());p=json.loads((pbase/'P.json').read_text());disc=np.load(base/'discovery.npz');support=disc['support'];sk=disc['skeleton']
  shutil.copy2(base/'stable.svg',out/'O.svg');shutil.copy2(pbase/'P.svg',out/'P.svg')
 else:
  frozen,support,sk=new_classical(rgb);p=construct_condition(frozen,'P',time.monotonic()+120)
  for tag,items in [('O',frozen['accepted']),('P',p['accepted'])]:(out/(tag+'.svg')).write_text(svg_graph(chain_graph(items,w,h)))
 (out/'frozen_traces.json').write_text(json.dumps(frozen));(out/'P.json').write_text(json.dumps(p));(out/'O.json').write_text(json.dumps(dict(accepted=frozen['accepted'])))
 Image.fromarray((support*255).astype('uint8')).save(out/'evidence.png');np.savez_compressed(out/'evidence.npz',support=support,skeleton=sk)
 selected,score=selection_rank(frozen['traces'],rgb);sinput=dict(frozen,traces=selected);s=construct_condition(sinput,'P',time.monotonic()+120);s['condition']='S';s['selection_scores']=score
 (out/'S.json').write_text(json.dumps(s));(out/'S.svg').write_text(svg_graph(chain_graph(s['accepted'],w,h)))
 graph,audit=integrate(p['accepted'],w,h,rgb);(out/'R_graph.json').write_text(json.dumps(graph));(out/'R_audit.json').write_text(json.dumps(audit));(out/'R.svg').write_text(svg_graph(graph,regions=True));(out/'R_strokes.svg').write_text(svg_graph(graph));(out/'R.json').write_text(json.dumps(dict(accepted=p['accepted'])))
 c,caudit=refine(p['accepted'],frozen['traces']);(out/'C_audit.json').write_text(json.dumps(caudit));(out/'C.json').write_text(json.dumps(dict(accepted=c)));(out/'C.svg').write_text(svg_graph(chain_graph(c,w,h)))
 (out/'WORKER.json').write_text(json.dumps(dict(wall_seconds=time.monotonic()-start,source_sha256=hashlib.sha256((out/'source.png').read_bytes()).hexdigest(),cached=config['cached'],holdout=config['split'],geometry='NOT_ACCEPTED')))
 print(case,'completed',len(p['accepted']),len(s['accepted']),audit['bounded_atomic_faces'],caudit['accepted_changes'],time.monotonic()-start,flush=True)
```
