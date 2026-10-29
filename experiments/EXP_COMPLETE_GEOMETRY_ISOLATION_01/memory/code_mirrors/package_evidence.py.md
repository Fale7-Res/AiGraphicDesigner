# مرآة الكود التفصيلية: `package_evidence.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `package_evidence.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `package_evidence.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `96` (`Lines 1–96`)
- **بصمة الملف (`SHA-256`):** `534a72437ae008b2821248fdb3d785d7586fcece3456a0eef2bf2d979cb30f31`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-PACKAGE-EVIDENCE | 2026-10-29T07:02:00Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `pixel_path` | `function` | `Lines 11–15` | `def pixel_path(case):` | رمز برمجي موثق. |
| `img` | `function` | `Lines 17–19` | `def img(path,label,svg=None):` | رمز برمجي موثق. |
| `main` | `function` | `Lines 21–92` | `def main():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `pixel_path` — `Lines 11–15`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `15` (`Lines 11–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–15`):**
```python
def pixel_path(case):
    p=REPO/'experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity'/case/'A/output.svg'
    if p.exists():return p
    p=REPO/'experiments/EXP_GEOMETRY_APPEARANCE_ABLATION_01/results'/case/'A/output.svg'
    return p if p.exists() else None
```

### `img` — `Lines 17–19`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `19` (`Lines 17–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–19`):**
```python
def img(path,label,svg=None):
    link=svg or path
    return f'<figure><a href="{html.escape(link)}"><img loading="lazy" src="{html.escape(path)}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'
```

### `main` — `Lines 21–92`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `92` (`Lines 21–92`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–92`):**
```python
def main():
    summary=json.loads((ROOT/'reports/common_face_summary.json').read_text())
    rows={ (x['case'],x['condition']):x for x in summary}
    body=['<h1>Complete geometry isolation</h1><p class="warning">Research result: NOT_ACCEPTED / NOT_ESTABLISHED. Architecture NOT_APPROVED. Both segmentation and initialization contribute. No candidate is a complete high-fidelity reconstruction.</p>',
     '<p>Same-label comparisons use identical cracks and evaluator-only common face references. All 24 candidates remain visible. Colors below are arbitrary region IDs, not reconstructed appearance. Shield annotations have1.2â€“2px uncertainty and cannot certify the fixed1px gate. Known masks are sampled8Ã— from independent vectors. Click images for actual SVGs.</p>',
     '<p><a href="REPORT.md">Technical report</a> Â· <a href="reports/common_face_summary.json">All metrics</a> Â· <a href="reports/graph_integrity_unique_ids.json">Exact raw-label checks</a> Â· <a href="protocol.json">Frozen protocol</a></p>',
     '<nav>'+ ' Â· '.join(f'<a href="#{c}">{c}</a>' for c in CASES)+'</nav>',
     '<h2>Failures first</h2><table><tr><th>Case</th><th>Condition</th><th>Collapsed rings</th><th>Invalid common rings</th><th>Known IoU</th><th>Status</th></tr>']
    for row in summary:
        known=row.get('known_geometry',{});iou=f'{known["foreground_iou"]:.4f}' if known else 'no exactGT'
        body.append(f'<tr><td>{row["case"]}</td><td>{row["condition"]}</td><td>{row["raw_nonzero_fit_degenerate_rings"]}</td><td>{row["invalid_fit_rings"]}</td><td>{iou}</td><td>{row["geometry_acceptance"]}</td></tr>')
    body.append('</table>')
    external_manifest=[]
    for case in CASES:
        out=case_dir(case);rel=out.as_uri() if case=='fine_features' else 'results/'+case
        body.append(f'<section id="{case}"><h2>{case}</h2>')
        if case=='fine_features':body.append('<p>External fixture rights unresolved. Evidence remains local; public Git manifest preserves hashes and retrieval requirements.</p>')
        pixel=pixel_path(case)
        if pixel:
            shutil.copy2(pixel,out/'pixel_reference.svg')
            subprocess.run([str(RESVG),str(out/'pixel_reference.svg'),str(out/'pixel_reference.png')],check=True,capture_output=True,timeout=60)
            dump(out/'pixel_reference_provenance.json',{'source':str(pixel),'sha256':digest(pixel),'purpose':'Saved strongest pixel-equivalent context, no new search or appearance fit'})
        body.append('<div class="grid">'+img(rel+'/working.png','Frozen working raster')+(img(rel+'/pixel_reference.png','Saved high-fidelity pixel SVG reference',rel+'/pixel_reference.svg') if pixel else '<p>No saved adaptive pixelSVG for external analytic fixture; source vector used only as independent evaluator.</p>')+'</div>')
        for seg in ['S_A','S_V']:
            body.append(f'<h3>{seg} â€” frozen partition</h3><div class="grid">')
            body.append(img(rel+'/'+seg+'_labels.png','Segmentation labels, arbitrary colors'))
            body.append(img(rel+'/'+seg+'_F_A_raw.png','Raw unit-crack graph',rel+'/'+seg+'_F_A_raw.svg'))
            for f in ['F_A','F_V']:
                name=seg+'_'+f;m=rows[(case,name)]
                # Re-export final curve evidence with correct native Z closure.
                from geometry_eval import svg_graph
                g=json.loads((out/(name+'.json')).read_text());p=out/(name+'_curves.svg');p.write_text(svg_graph(g),encoding='utf-8')
                subprocess.run([str(RESVG),str(p),str(p.with_suffix('.png'))],check=True,capture_output=True,timeout=60)
                body.append(img(rel+'/'+name+'_curves.png',f'{name}: {m["raw_nonzero_fit_degenerate_rings"]} collapsed rings',rel+'/'+name+'_curves.svg'))
            body.append('</div>')
        body.append('<h3>True SVG detail renders â€”1Ã— /4Ã— /16Ã—</h3><p>Source crop is raster guidance, not high-resolution vector truth. Geometry images are rendered from actual SVG viewports.</p>')
        x,y,w,h=ZOOMS[case];im=Image.open(out/'working.png');im.crop((x,y,min(im.width,x+w),min(im.height,y+h))).save(out/'source_detail.png')
        body.append(img(rel+'/source_detail.png','Native raster detail guide'))
        import xml.etree.ElementTree as ET
        for scale in [1,4,16]:
            body.append(f'<details {"open" if scale==4 else ""}><summary>{scale}Ã— actual SVG viewport</summary><div class="grid four">')
            for seg in ['S_A','S_V']:
                for f in ['F_A','F_V']:
                    name=seg+'_'+f;tree=ET.fromstring((out/(name+'_curves.svg')).read_text());tree.set('viewBox',f'{x} {y} {w} {h}');tree.set('width',str(w*scale));tree.set('height',str(h*scale))
                    p=out/(name+f'_detail_{scale}x.svg');p.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8')
                    subprocess.run([str(RESVG),str(p),str(p.with_suffix('.png'))],check=True,capture_output=True,timeout=60)
                    body.append(img(rel+'/'+p.with_suffix('.png').name,name,rel+'/'+p.name))
            body.append('</div></details>')
        if case in ['fine_features','K01_linear_corner_hole']:
            body.append('<h3>Independent known-vector mask errors</h3><p>Red=truth, green=candidate; yellow=agreement. Shape correspondence uses fixed source-only majority labeling. Topology counts use4-connectivity at8Ã—.</p><div class="grid four">')
            for seg in ['S_A','S_V']:
                for f in ['F_A','F_V']:
                    name=seg+'_'+f;body.append(img(rel+'/'+name+'_known_error.png',name+' known-mask error',rel+'/'+name+'_foreground.svg'))
            body.append('</div>')
        body.append('<h3>Source / raw / fitted boundary diagnostics</h3><p>Red=raw cracks, cyan=fitted curves over the native source. Separate amplified maps compare raw/fitted render alpha, not final RGB fidelity or geometric ground truth.</p><div class="grid four">')
        for seg in ['S_A','S_V']:
            for f in ['F_A','F_V']:
                name=seg+'_'+f
                body.append(img(rel+'/'+name+'_source_overlay.png',name+' source overlay',rel+'/'+name+'_raw_fit_overlay.svg'))
                body.append(img(rel+'/'+name+'_render_difference_x4.png',name+' render-alpha difference ×4'))
        body.append('</div>')
        if case=='A01_shield':
            body.append('<h3>Concrete fitting collapse: raw face10</h3><p>The raw1px cell becomes a diagonal/zero-area shape. This demonstrates fitting damage; it does not make that cell desirable final artwork.</p><div class="grid">')
            for label in ['raw','Arena','VTracer']:body.append(img(rel+'/face10_'+label+'.png',label,rel+'/face10_'+label+'.svg'))
            body.append('</div><p><a href="references/shield_complete_boundary_reference.json">All13critical-component diagnostics and annotation roles</a></p>')
        body.append('</section>')
        if case=='fine_features':
            external_manifest=[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(out.rglob('*')) if p.is_file()]
    dump(ROOT/'external/LOCAL_EVIDENCE_MANIFEST.json',{'rights':'Unresolved external fixture license; derived artwork remains local, no silent omission. Reproduction requires original owner ZIP e0549964698d696694f671a8343fcc020a3ec6bb30dc273b92d1a6fb4e330fd9','files':external_manifest})
    css='body{font:16px system-ui;margin:24px;background:#eee;color:#152132}h1,h2{color:#102b46}.warning{background:#fff0c1;padding:18px}section{border-top:3px solid #8392a1;margin-top:36px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}.four{grid-template-columns:repeat(4,minmax(200px,1fr));overflow:auto}figure{margin:0;background:white;padding:8px;border:1px solid #ccd}img{max-width:100%;height:auto;background:white}figcaption{font-size:14px;margin:8px}td,th{padding:5px;border:1px solid #bbc;font-size:12px}table{border-collapse:collapse;background:white}summary{cursor:pointer;padding:14px}a{color:#075a9e}'
    (ROOT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Geometry isolation review</title><style>'+css+'</style>'+''.join(body)+'</html>',encoding='utf-8')
    print('dashboard generated; external files',len(external_manifest))
```
