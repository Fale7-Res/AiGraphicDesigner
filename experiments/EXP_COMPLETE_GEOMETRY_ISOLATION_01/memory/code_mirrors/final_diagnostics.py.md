# مرآة الكود التفصيلية: `final_diagnostics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `final_diagnostics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `final_diagnostics.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `80` (`Lines 1–80`)
- **بصمة الملف (`SHA-256`):** `948e0274fc3051cbe9f734fd253ae8be0a74fa2f9b3cd8112fba4475d1498dcc`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-FINAL-DIAGNOSTICS | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `coverage_geometry` | `function` | `Lines 14–29` | `def coverage_geometry(g):` | رمز برمجي موثق. |
| `visible_micro` | `function` | `Lines 31–50` | `def visible_micro(g,m,out,name):` | رمز برمجي موثق. |
| `failure_example` | `function` | `Lines 52–66` | `def failure_example():` | رمز برمجي موثق. |
| `failure_example.make` | `nested_function` | `Lines 56–61` | `def make(source,raw,color):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `coverage_geometry` — `Lines 14–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `29` (`Lines 14–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–29`):**
```python
def coverage_geometry(g):
    chains={c['id']:chain_points(c) for c in g['chains']};faces=[];bad=[]
    for label,loops in g['faces'].items():
        face=None
        for refs in loops:
            p,gap=ring_points(refs,chains)
            if len(p)<4:bad.append(int(label));face=None;break
            poly=Polygon(p)
            if gap>.001 or not poly.is_valid:bad.append(int(label));face=None;break
            face=poly if face is None else face.symmetric_difference(poly)
        if face is not None and not face.is_empty:faces.append(face)
    if bad:return {'status':'NOT_ESTABLISHED_INVALID_RINGS','invalid_face_labels':sorted(set(bad)),'note':'No make_valid or hidden polygon repair is applied'}
    union=unary_union(faces);domain=box(0,0,g['width'],g['height'])
    return {'status':'NUMERICAL_FLATTENED_DIAGNOSTIC','uncovered_domain_area_px2':float(domain.difference(union).area),
     'outside_domain_area_px2':float(union.difference(domain).area),'overlap_area_multiplicity_px2':float(sum(f.area for f in faces)-union.area),
     'note':'<=.01px curve flattening, double predicates. Not exact analytic certification; alpha compositing separate.'}
```

### `visible_micro` — `Lines 31–50`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `50` (`Lines 31–50`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–50`):**
```python
def visible_micro(g,m,out,name):
    svg=out/(name+'_visible_ids.svg');svg.write_text(svg_graph(g,regions=True),encoding='utf-8')
    png=svg.with_suffix('.png');scale=4
    subprocess.run([str(RESVG),'--width',str(g['width']*scale),'--height',str(g['height']*scale),str(svg),str(png)],check=True,capture_output=True,timeout=60)
    rgba=np.asarray(Image.open(png).convert('RGBA'));encoded=(rgba[...,0].astype(np.uint32)<<16)|(rgba[...,1].astype(np.uint32)<<8)|rgba[...,2]
    # Injective odd-multiplier24bit palette. Count only fully opaque exact
    # region colors. AA/color mixtures remain explicitly unclassified.
    vals,cnt=np.unique(encoded[rgba[...,3]==255],return_counts=True);counts=dict(zip(map(int,vals),map(int,cnt)))
    assigned=0;bylabel={}
    for label in g['faces']:
        color=label_rgb(int(label));code=color[0]*65536+color[1]*256+color[2]
        n=counts.get(code,0);assigned+=n;bylabel[int(label)]=n
    total=encoded.size;unassigned=total-assigned
    scales={}
    for s in [1,2,4]:
        n=sum(bylabel[r['label']] for r in m['microgeometry']['regions'] if max(r['span_px'])<=s and r['lattice_fraction']>=.8)
        scales[str(s)]={'visible_area_lower_fraction':n/total,'conservative_upper_fraction':(n+unassigned)/total}
    return {'scale':4,'fully_opaque_exact_color_assigned_fraction':assigned/total,'unclassified_AA_alpha_fraction':unassigned/total,
     'scales_px':scales,'alarm_2px_lower_bound_ge10percent':scales['2']['visible_area_lower_fraction']>=.1,
     'note':'Actual SVG4xvisible-area diagnostic. AA mixtures unclassified; extremely rare blended colors coinciding with palette not analytically excluded. No blanket fineROI exemptions, no proof of professional geometry.'}
```

### `failure_example` — `Lines 52–66`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `52` إلى السطر `66` (`Lines 52–66`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 52–66`):**
```python
def failure_example():
    out=ROOT/'results/A01_shield';g=json.loads((out/'S_A_F_A_common_faces.json').read_text())
    v=json.loads((out/'S_A_F_V_common_faces.json').read_text());refs=g['faces']['10'];ids={r['chain'] for loop in refs for r in loop}
    chains=[c for c in g['chains'] if c['id'] in ids];allp=np.concatenate([np.asarray(c['pixel_crack_vertices']) for c in chains]);lo=allp.min(axis=0)-.3;hi=allp.max(axis=0)+.3
    def make(source,raw,color):
        obj={**source,'chains':[c for c in source['chains'] if c['id'] in ids]}
        import xml.etree.ElementTree as ET
        tree=ET.fromstring(svg_graph(obj,raw=raw));tree.set('viewBox',f'{lo[0]} {lo[1]} {hi[0]-lo[0]} {hi[1]-lo[1]}');tree.set('width','512');tree.set('height','512')
        for node in tree:node.set('stroke',color);node.set('stroke-width','.02')
        return ET.tostring(tree,encoding='unicode')
    for label,source,raw,color in [('raw',g,True,'#777777'),('Arena',g,False,'#0044bb'),('VTracer',v,False,'#c0392b')]:
        p=out/('face10_'+label+'.svg');p.write_text(make(source,raw,color));subprocess.run([str(RESVG),str(p),str(p.with_suffix('.png'))],check=True,capture_output=True)
    dump(out/'face10_evidence.json',{'face':10,'chain_ids':sorted(ids),'raw_chains':[c for c in g['chains'] if c['id'] in ids],
      'VTracer_common_chains':[c for c in v['chains'] if c['id'] in ids],
      'interpretation':'Existing1px raw enclosed cell. Both tested initializers collapse it. This is fitting-introduced loss, not proof the cell is desirable final artwork; no cell inserted as corrective geometry.'})
```

### `failure_example.make` — `Lines 56–61`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `56` إلى السطر `61` (`Lines 56–61`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 56–61`):**
```python
    def make(source,raw,color):
        obj={**source,'chains':[c for c in source['chains'] if c['id'] in ids]}
        import xml.etree.ElementTree as ET
        tree=ET.fromstring(svg_graph(obj,raw=raw));tree.set('viewBox',f'{lo[0]} {lo[1]} {hi[0]-lo[0]} {hi[1]-lo[1]}');tree.set('width','512');tree.set('height','512')
        for node in tree:node.set('stroke',color);node.set('stroke-width','.02')
        return ET.tostring(tree,encoding='unicode')
```
