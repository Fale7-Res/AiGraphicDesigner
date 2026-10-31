# مرآة الكود التفصيلية: `build_review.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `build_review.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `build_review.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `49` (`Lines 1–49`)
- **بصمة الملف (`SHA-256`):** `2c486a51dc49492a33e451f81fd33a54cf8e4d0d41e32ac88ad502c82d205c93`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-REVIEW | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `make_geometry_review` | `function` | `Lines 9–47` | `def make_geometry_review():` | رمز برمجي موثق. |
| `make_geometry_review.dashboard` | `nested_function` | `Lines 18–46` | `def dashboard(owner):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `make_geometry_review` — `Lines 9–47`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `47` (`Lines 9–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–47`):**
```python
def make_geometry_review():
 protocol=json.loads((E/'protocol.json').read_text());rows=json.loads((E/'reports/METRICS.json').read_text());lookup={(m['case'],m['condition']):m for m in rows};local=Path.cwd()/'outputs/universal_geometry_review';local.mkdir(exist_ok=True)
 for case in protocol['cases']:
  out=output_folder(case);rgb=Image.open(out/'source.png').convert('RGB');p=json.loads((out/'P.json').read_text());audit=json.loads((out/'R_audit.json').read_text());drawing=rgb.copy();draw=ImageDraw.Draw(drawing)
  for i,item in enumerate(p['accepted']):
   lines,_=samples_from_items([item]);draw.line([tuple(q) for q in lines[0]],fill=(0,170,40) if audit['rows'][i]['integrated'] else (230,20,140),width=1)
  drawing.save(out/'R_rejection_overlay.png')
  faceareas=[f['area_px2'] for f in audit['faces']];audit['microfaces']=dict(count_le4px2=sum(a<=4 for a in faceareas),count_le16px2=sum(a<=16 for a in faceareas),visible_atomic_area_fraction_le4px2=sum(a for a in faceareas if a<=4)/max(sum(faceareas),1e-9),limits='Numerical .005px flattened disjoint atomic region area; not semantic objects. Strokes use length-weighted proxy separately.')
  graph=json.loads((out/'R_graph.json').read_text());audit['shared_interfaces']=sum(len(c['adjacent_face_labels'])==2 for c in graph['chains']);audit['overassigned_interfaces']=sum(len(c['adjacent_face_labels'])>2 for c in graph['chains']);audit['unintegrated_reasons']=dict(collections.Counter(reason for row in audit['unintegrated'] for reason in row['reasons']));(out/'R_diagnostics.json').write_text(json.dumps(audit,indent=2))
 def dashboard(owner):
  page=['<!doctype html><meta charset="utf-8"><title>Universal geometry evidence</title><style>body{font:16px system-ui;background:#eef1f4;color:#17212b;margin:24px}section{background:white;margin:20px 0;padding:20px;border-radius:12px} .grid{display:grid;grid-template-columns:repeat(3,minmax(240px,1fr));gap:12px} img{max-width:100%;background:white;border:1px solid #ccd} figure{margin:0}figcaption{font-weight:650;padding:6px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:7px;border:1px solid #bbc} .bad{background:#ffe1df;padding:14px}.note{background:#fff1cb;padding:14px}a{color:#0756a5}details{margin:12px 0} .zoom{max-height:650px;overflow:auto}.zoom img{max-width:none}</style>', '<h1>Universal geometry: selection, regions and coherence</h1><p><b>Geometry NOT_ACCEPTED · Architecture NOT_APPROVED</b></p><p class="bad">S is not a universal improvement. Crown guide coverage increases while Burger/photo support drops. R can form some atomic faces, but cannot establish complete region ownership. C makes modest bounded changes; staircases remain. Diagnostic ID fills are not final appearance.</p><p>O = historical stable; P = partitioned control; S = new source score with unchanged P; R = P exact-endpoint atomic faces; SR = S through same R after frozen control gates; C = conservative P refit. Blank R is an integration failure, not a blank source. Unintegrated strokes are preserved.</p>']
  page.append('<nav>'+ ' · '.join(f'<a href="#{html.escape(c)}">{html.escape(c)}</a>' for c in protocol['cases'])+'</nav>')
  for case,config in protocol['cases'].items():
   out=output_folder(case);base=out.as_uri()+'/' if owner else str(out.relative_to(E)).replace('\\','/')+'/' if case!='fine_features' else None
   page.append(f'<section id="{case}"><h2>{case} — {config["split"]}</h2>')
   if base is None:page.append('<p>Fine Features source and all derivative geometry/images are owner-local pending Arena rights. Metrics are in the public report. Open the owner-local dashboard for visual evidence.</p></section>');continue
   page.append('<div class="grid">')
   panels=[('Source raster (not high-resolution vector truth)','source.png'),('Frozen classical source evidence','evidence.png'),('P control','P_1x.png'),('S: changed selection only','S_1x.png'),('R: atomic ID regions; blank = no faces','R_1x.png'),('R rejected/unintegrated magenta; integrated green','R_rejection_overlay.png'),('C: same P input, bounded refit','C_1x.png'),('SR: conditional combined atomic regions','SR_1x.png'),('Original stable O','O_1x.png')]
   for label,file in panels:page.append(f'<figure><a href="{base+file}"><img loading="lazy" src="{base+file}"></a><figcaption>{label}</figcaption></figure>')
   page.append('</div><p>Actual SVGs: '+ ' · '.join(f'<a href="{base+c}.svg">{c}</a>' for c in ['O','P','S','R','SR','C'])+f' · <a href="{base}R_strokes.svg">R all preserved strokes</a> · <a href="{base}P_ledger.csv">P loss ledger</a> · <a href="{base}S_ledger.csv">S loss ledger</a> · <a href="{base}R_diagnostics.json">region rejection audit</a></p>')
   page.append('<table><tr><th>Condition</th><th>Paths / cubics</th><th>Boundary recall</th><th>Source-proxy recall</th><th>Tiny cubic length fraction</th><th>Atomic faces</th></tr>')
   for c in ['O','P','S','R','SR','C']:
    m=lookup.get((case,c))
    if not m:continue
    truth=m.get('boundary_1_25px',{}).get('fitted',{}).get('recall');scope=' all preserved strokes' if c in ['R','SR'] else '';page.append(f'<tr><td>{c+scope}</td><td>{m["paths"]} / {m["cubics"]}</td><td>{truth if truth is not None else "No independent truth"}</td><td>{m["source_edge_agreement_proxy"]["recall"]:.4f}</td><td>{m["micro"]["tiny_cubic_length_weighted_fraction"]:.4f}</td><td>{m["filled_atomic_faces"]}</td></tr>')
   page.append('</table><p><b>Actually integrated face-boundary source support:</b> '+ ' · '.join(c+': '+f'{lookup[(case,c)]["integrated_only"]["source_proxy"]["recall"]:.4f}' for c in ['R','SR'])+'</p>')
   page.append('<p class="note">Source agreement does not establish precision against meaningful structure. Lighting and texture may be retained. Arabic uses threshold proxies; Shield guides carry 1.2–2px uncertainty. Atomic containment is not semantic hole ownership.</p>')
   if case=='A01_shield':
    page.append('<h3>Entire crown: tips, valleys, ornament, band</h3><table><tr><th>Critical guide (uncertain)</th><th>P recall</th><th>S recall</th><th>C recall</th></tr>')
    for i,g in enumerate(lookup[(case,'P')]['critical_guides']):page.append('<tr><td>'+g['id']+'</td>'+''.join(f'<td>{lookup[(case,c)]["critical_guides"][i]["fitted"]["recall"]:.3f}</td>' for c in ['P','S','C'])+'</tr>')
    page.append('</table><p class="bad">Crown completeness fails. Higher approximate guide proximity is not proof that the crown, band and metallic structure have been faithfully reconstructed.</p>')
   for zoom in [1,4,16]:
    page.append(f'<details><summary>True SVG-rendered detail at {zoom}×'+(' — dedicated crown ROI' if case=='A01_shield' else '')+'</summary><div class="grid">')
    for c in ['O','P','S','R','SR','C']:page.append(f'<figure><figcaption>{c}</figcaption><div class="zoom"><img loading="lazy" src="{base+c}_detail_{zoom}x.png"></div><a href="{base+c}_detail.svg">Actual detail SVG</a></figure>')
    page.append('</div></details>')
   page.append('<details><summary>Full image actual 4× renders</summary><div class="grid">'+''.join(f'<figure><figcaption>{c}</figcaption><a href="{base+c}_4x.png"><img loading="lazy" src="{base+c}_4x.png"></a></figure>' for c in ['P','S','R','C'])+'</div></details></section>')
  page.append('<p>Research report, protocol, full metrics and QA remain beside this dashboard. No model inference or final appearance reconstruction was performed.</p>')
  return ''.join(page)
 (E/'review.html').write_text(dashboard(False),encoding='utf-8');(local/'review.html').write_text(dashboard(True),encoding='utf-8');print(local/'review.html')
```

### `make_geometry_review.dashboard` — `Lines 18–46`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `46` (`Lines 18–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–46`):**
```python
 def dashboard(owner):
  page=['<!doctype html><meta charset="utf-8"><title>Universal geometry evidence</title><style>body{font:16px system-ui;background:#eef1f4;color:#17212b;margin:24px}section{background:white;margin:20px 0;padding:20px;border-radius:12px} .grid{display:grid;grid-template-columns:repeat(3,minmax(240px,1fr));gap:12px} img{max-width:100%;background:white;border:1px solid #ccd} figure{margin:0}figcaption{font-weight:650;padding:6px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:7px;border:1px solid #bbc} .bad{background:#ffe1df;padding:14px}.note{background:#fff1cb;padding:14px}a{color:#0756a5}details{margin:12px 0} .zoom{max-height:650px;overflow:auto}.zoom img{max-width:none}</style>', '<h1>Universal geometry: selection, regions and coherence</h1><p><b>Geometry NOT_ACCEPTED · Architecture NOT_APPROVED</b></p><p class="bad">S is not a universal improvement. Crown guide coverage increases while Burger/photo support drops. R can form some atomic faces, but cannot establish complete region ownership. C makes modest bounded changes; staircases remain. Diagnostic ID fills are not final appearance.</p><p>O = historical stable; P = partitioned control; S = new source score with unchanged P; R = P exact-endpoint atomic faces; SR = S through same R after frozen control gates; C = conservative P refit. Blank R is an integration failure, not a blank source. Unintegrated strokes are preserved.</p>']
  page.append('<nav>'+ ' · '.join(f'<a href="#{html.escape(c)}">{html.escape(c)}</a>' for c in protocol['cases'])+'</nav>')
  for case,config in protocol['cases'].items():
   out=output_folder(case);base=out.as_uri()+'/' if owner else str(out.relative_to(E)).replace('\\','/')+'/' if case!='fine_features' else None
   page.append(f'<section id="{case}"><h2>{case} — {config["split"]}</h2>')
   if base is None:page.append('<p>Fine Features source and all derivative geometry/images are owner-local pending Arena rights. Metrics are in the public report. Open the owner-local dashboard for visual evidence.</p></section>');continue
   page.append('<div class="grid">')
   panels=[('Source raster (not high-resolution vector truth)','source.png'),('Frozen classical source evidence','evidence.png'),('P control','P_1x.png'),('S: changed selection only','S_1x.png'),('R: atomic ID regions; blank = no faces','R_1x.png'),('R rejected/unintegrated magenta; integrated green','R_rejection_overlay.png'),('C: same P input, bounded refit','C_1x.png'),('SR: conditional combined atomic regions','SR_1x.png'),('Original stable O','O_1x.png')]
   for label,file in panels:page.append(f'<figure><a href="{base+file}"><img loading="lazy" src="{base+file}"></a><figcaption>{label}</figcaption></figure>')
   page.append('</div><p>Actual SVGs: '+ ' · '.join(f'<a href="{base+c}.svg">{c}</a>' for c in ['O','P','S','R','SR','C'])+f' · <a href="{base}R_strokes.svg">R all preserved strokes</a> · <a href="{base}P_ledger.csv">P loss ledger</a> · <a href="{base}S_ledger.csv">S loss ledger</a> · <a href="{base}R_diagnostics.json">region rejection audit</a></p>')
   page.append('<table><tr><th>Condition</th><th>Paths / cubics</th><th>Boundary recall</th><th>Source-proxy recall</th><th>Tiny cubic length fraction</th><th>Atomic faces</th></tr>')
   for c in ['O','P','S','R','SR','C']:
    m=lookup.get((case,c))
    if not m:continue
    truth=m.get('boundary_1_25px',{}).get('fitted',{}).get('recall');scope=' all preserved strokes' if c in ['R','SR'] else '';page.append(f'<tr><td>{c+scope}</td><td>{m["paths"]} / {m["cubics"]}</td><td>{truth if truth is not None else "No independent truth"}</td><td>{m["source_edge_agreement_proxy"]["recall"]:.4f}</td><td>{m["micro"]["tiny_cubic_length_weighted_fraction"]:.4f}</td><td>{m["filled_atomic_faces"]}</td></tr>')
   page.append('</table><p><b>Actually integrated face-boundary source support:</b> '+ ' · '.join(c+': '+f'{lookup[(case,c)]["integrated_only"]["source_proxy"]["recall"]:.4f}' for c in ['R','SR'])+'</p>')
   page.append('<p class="note">Source agreement does not establish precision against meaningful structure. Lighting and texture may be retained. Arabic uses threshold proxies; Shield guides carry 1.2–2px uncertainty. Atomic containment is not semantic hole ownership.</p>')
   if case=='A01_shield':
    page.append('<h3>Entire crown: tips, valleys, ornament, band</h3><table><tr><th>Critical guide (uncertain)</th><th>P recall</th><th>S recall</th><th>C recall</th></tr>')
    for i,g in enumerate(lookup[(case,'P')]['critical_guides']):page.append('<tr><td>'+g['id']+'</td>'+''.join(f'<td>{lookup[(case,c)]["critical_guides"][i]["fitted"]["recall"]:.3f}</td>' for c in ['P','S','C'])+'</tr>')
    page.append('</table><p class="bad">Crown completeness fails. Higher approximate guide proximity is not proof that the crown, band and metallic structure have been faithfully reconstructed.</p>')
   for zoom in [1,4,16]:
    page.append(f'<details><summary>True SVG-rendered detail at {zoom}×'+(' — dedicated crown ROI' if case=='A01_shield' else '')+'</summary><div class="grid">')
    for c in ['O','P','S','R','SR','C']:page.append(f'<figure><figcaption>{c}</figcaption><div class="zoom"><img loading="lazy" src="{base+c}_detail_{zoom}x.png"></div><a href="{base+c}_detail.svg">Actual detail SVG</a></figure>')
    page.append('</div></details>')
   page.append('<details><summary>Full image actual 4× renders</summary><div class="grid">'+''.join(f'<figure><figcaption>{c}</figcaption><a href="{base+c}_4x.png"><img loading="lazy" src="{base+c}_4x.png"></a></figure>' for c in ['P','S','R','C'])+'</div></details></section>')
  page.append('<p>Research report, protocol, full metrics and QA remain beside this dashboard. No model inference or final appearance reconstruction was performed.</p>')
  return ''.join(page)
```
