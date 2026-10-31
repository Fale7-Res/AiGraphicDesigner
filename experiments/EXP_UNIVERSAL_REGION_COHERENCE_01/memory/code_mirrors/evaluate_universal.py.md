# مرآة الكود التفصيلية: `evaluate_universal.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `evaluate_universal.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `evaluate_universal.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `75` (`Lines 1–75`)
- **بصمة الملف (`SHA-256`):** `a2786fa8996e6c9eaf48b638b29eeeccec6e2448dd8323c878a499c94d03e2ce`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-EVALUATE | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `evaluate_universal_case` | `function` | `Lines 14–59` | `def evaluate_universal_case(case):` | رمز برمجي موثق. |
| `evaluate_all_universal` | `function` | `Lines 61–73` | `def evaluate_all_universal():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `evaluate_universal_case` — `Lines 14–59`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `59` (`Lines 14–59`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–59`):**
```python
def evaluate_universal_case(case):
 out=output_folder(case)
 if all((out/(c+'_metrics.json')).exists() for c in ['O','P','S','R','C']) and (out/'comparison.png').exists():return [json.loads((out/(c+'_metrics.json')).read_text()) for c in ['O','P','S','R','C']]
 source=out/'source.png';rgb,target,holes,tag=references(case,source);h,w=rgb.shape[:2];frozen=json.loads((out/'frozen_traces.json').read_text());raws={t['trace_id']:t for t in frozen['traces']};allpts=xy(np.load(out/'evidence.npz')['skeleton']);data={c:json.loads((out/(c+'.json')).read_text()) for c in ['O','P','S','R','C']}
 guide=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text()) if case=='A01_shield' else None
 r=json.loads((out/'R_audit.json').read_text());rows=[]
 for c,d in data.items():
  items=d['accepted'];lines,points=samples_from_items(items)
  selectedids={t['trace_id'] for t in d.get('traces',[]) if t.get('selection')=='selected'} if c in ['P','S'] else {t['trace_id'] for t in data['P'].get('traces',[]) if t.get('selection')=='selected'}
  if c=='O':selectedids={t['trace_id'] for t in frozen['traces'] if t['reason'] not in ['short_chain','proposal_budget']}
  selectedpts=np.concatenate([np.asarray(raws[i]['source_points_xy']) for i in selectedids]) if selectedids else np.empty((0,2))
  quality=[curve_quality(i['curves']) for i in items];m=dict(case=case,condition=c,paths=len(items),cubics=sum(len(i['curves']) for i in items),closed_curves=sum(bool(np.array_equal(np.asarray(i['curves'])[0,0],np.asarray(i['curves'])[-1,-1])) for i in items),reference=tag,source_edge_agreement_proxy=support_stats(allpts,points,1.25),selected_source_edge_agreement_proxy=support_stats(allpts,selectedpts,1.25),loss=d.get('summary'),topology=topology_diagnostics(items,raws),micro=micro_diagnostics(items),quality=quality,render_seconds={},filled_atomic_faces=r['bounded_atomic_faces'] if c=='R' else 0,semantic_ownership='NOT_ESTABLISHED',geometry='NOT_ACCEPTED')
  if target is not None:
   m['boundary_1_25px']={k:support_stats(target,p,1.25) for k,p in [('raw',allpts),('selected',selectedpts),('fitted',points)]}
   m['hole_boundary_support_NOT_ownership']=[support_stats(q,points,1.25) for q in holes]
  if guide:
   m['critical_guides']=[]
   for g in guide['components']+guide['appearance_only']:
    q=np.concatenate([sample_segments(np.asarray(p,float),.25) for p in g['polylines']]);m['critical_guides'].append(dict(id=g['id'],required=g.get('structural_boundary_required',False),uncertainty_px=g['uncertainty_px'],selected=support_stats(q,selectedpts,g['uncertainty_px']),fitted=support_stats(q,points,g['uncertainty_px'])))
  root=ET.parse(out/(c+'.svg')).getroot();assert not any(x.tag.rsplit('}',1)[-1]=='image' for x in root.iter());assert not any('href' in k for x in root.iter() for k in x.attrib)
  m['svg_bytes']=(out/(c+'.svg')).stat().st_size
  for scale in [1,4]:m['render_seconds'][str(scale)]=render(out/(c+'.svg'),out/(c+f'_{scale}x.png'),w,h,scale)
  # ROI is evaluator-only presentation, never passed to algorithms.
  roi=[115,70,145,100] if case=='A01_shield' else [w//4,h//4,min(128,w//2),min(96,h//2)]
  root.set('viewBox',' '.join(map(str,roi)));root.set('width',str(roi[2]));root.set('height',str(roi[3]));(out/(c+'_detail.svg')).write_text(ET.tostring(root,encoding='unicode'))
  for scale in [1,4,16]:m['render_seconds']['detail'+str(scale)]=render(out/(c+'_detail.svg'),out/(c+f'_detail_{scale}x.png'),roi[2],roi[3],scale)
  overlay=Image.fromarray(rgb.copy());paint=Image.open(out/(c+'_1x.png')).convert('RGBA');overlay=overlay.convert('RGBA');overlay.alpha_composite(paint);overlay.convert('RGB').save(out/(c+'_source_overlay.png'))
  alpha=np.asarray(paint)[...,3];m['rendered_coverage_fraction']=float((alpha>0).mean());m['coverage_limit']='Stroke or diagnostic atomic-face footprint, not reconstruction silhouette correctness. Atomic nested faces include material islands and potential voids.'
  if c=='R':m['integration']=r
  if c=='C':m['coherence']=json.loads((out/'C_audit.json').read_text())
  if c in ['P','S']:
   lossview=Image.fromarray(rgb.copy());draw=ImageDraw.Draw(lossview);ledger=[]
   for t in d['traces']:
    raw=raws[t['trace_id']]['source_points_xy']
    for part in t['ledger']:
     draw.line([tuple(q) for q in raw[part['lo']:part['hi']+1]],fill=(0,180,0) if part['status']=='accepted' else (230,30,90),width=1)
     ledger.append(dict(trace_id=t['trace_id'],lo=part['lo'],hi=part['hi'],length_px=part['length_px'],status=part['status'],reason=part['reason']))
   lossview.save(out/(c+'_loss_overlay.png'))
   if ledger:
    with (out/(c+'_ledger.csv')).open('w',newline='') as stream:writer=csv.DictWriter(stream,fieldnames=list(ledger[0]));writer.writeheader();writer.writerows(ledger)
  (out/(c+'_metrics.json')).write_text(json.dumps(m,indent=2));rows.append(m)
  print(case,c,'evaluated',flush=True)
 sheet=Image.new('RGB',(6*300,290),'white');draw=ImageDraw.Draw(sheet)
 for i,c in enumerate(['source','O','P','S','R','C']):
  im=Image.open(out/('source.png' if c=='source' else c+'_1x.png')).convert('RGBA');white=Image.new('RGBA',im.size,'white');white.alpha_composite(im);sheet.paste(ImageOps.contain(white.convert('RGB'),(284,250)),(i*300+8,32));draw.text((i*300+8,8),c+' | geometry only' if c!='source' else 'Source',fill='black')
 sheet.save(out/'comparison.png');return rows
```

### `evaluate_all_universal` — `Lines 61–73`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `61` إلى السطر `73` (`Lines 61–73`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 61–73`):**
```python
def evaluate_all_universal():
 protocol=json.loads((E/'protocol.json').read_text());rows=[]
 for case in protocol['cases']:
  if not (output_folder(case)/'WORKER.json').exists():continue
  rows+=evaluate_universal_case(case);(E/'reports/METRICS.json').write_text(json.dumps(rows,indent=2))
 # Independently justified S+R prerequisite; skipped if either control regresses.
 checks=[]
 for case in ['K01_linear_corner_hole','fine_features']:
  d={r['condition']:r for r in rows if r['case']==case}
  if not d:checks.append(dict(case=case,passed=False,reason='missing_case'));continue
  checks.append(dict(case=case,passed=d['S']['boundary_1_25px']['fitted']['recall']>=d['P']['boundary_1_25px']['fitted']['recall']-.01 and d['R']['filled_atomic_faces']>0 and not d['R']['topology']['new_cross_or_overlap_pairs_vs_same_raw_pair'],S_recall=d['S']['boundary_1_25px']['fitted']['recall'],P_recall=d['P']['boundary_1_25px']['fitted']['recall'],faces=d['R']['filled_atomic_faces']))
 (E/'reports/COMBINATION_GATE.json').write_text(json.dumps(dict(checks=checks,execute=all(c['passed'] for c in checks),decision='Run only if both independent control prerequisites pass; no tuning.'),indent=2))
 return rows
```
