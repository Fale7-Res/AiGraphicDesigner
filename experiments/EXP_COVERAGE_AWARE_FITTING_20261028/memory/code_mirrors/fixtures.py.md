# مرآة الكود التفصيلية: `fixtures.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `fixtures.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `fixtures.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `96` (`Lines 1–96`)
- **بصمة الملف (`SHA-256`):** `f07b982436bb8573b25f0f99aea195ca72a6ac1eee6521b80377dfca063b41d9`
- **الوصف التفصيلي:** """Freeze two small known-vector coverage controls; render only their source truth."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `fixture_specs` | `function` | `Lines 14–51` | `def fixture_specs():` | Ground truth uses <=7 paint paths, no bitmap/grid, <=4 equally spaced stops. |
| `freeze_fixtures` | `function` | `Lines 53–91` | `def freeze_fixtures():` | Write all fixture inputs before fitting; refuse nonempty generation targets. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `fixture_specs` — `Lines 14–51`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `51` (`Lines 14–51`)
- **الوظيفة:** Ground truth uses <=7 paint paths, no bitmap/grid, <=4 equally spaced stops.
- **الكود الفعلي (`Lines 14–51`):**
```python
def fixture_specs():
    """Ground truth uses <=7 paint paths, no bitmap/grid, <=4 equally spaced stops."""
    opaque='''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="128" viewBox="0 0 160 128"><defs>
<linearGradient id="warm" gradientUnits="userSpaceOnUse" x1="8" y1="0" x2="80" y2="0"><stop offset="0" stop-color="#3d0714"/><stop offset="0.333333333333" stop-color="#a32918"/><stop offset="0.666666666667" stop-color="#f4a021"/><stop offset="1" stop-color="#fff0a0"/></linearGradient>
<linearGradient id="cool" gradientUnits="userSpaceOnUse" x1="80" y1="8" x2="152" y2="120"><stop offset="0" stop-color="#073f77"/><stop offset="0.5" stop-color="#257bc0"/><stop offset="1" stop-color="#b7f1ef"/></linearGradient>
<radialGradient id="highlight" gradientUnits="userSpaceOnUse" cx="143" cy="28" r="15"><stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#f5ec80"/><stop offset="1" stop-color="#ba6e14"/></radialGradient></defs>
<path id="background" fill="#111b31" d="M0 0H160V128H0Z"/>
<path id="warm_region" fill="url(#warm)" d="M8 8H80C116 32 44 96 80 120H8Z"/>
<path id="cool_region" fill="url(#cool)" d="M80 8H152V120H80C44 96 116 32 80 8Z"/>
<path id="thin_diagonal" fill="#00ff83" d="M29.7 12.3L129.7 112.3L130.3 111.7L30.3 11.7Z"/>
<path id="hole_ring" fill="#fee625" fill-rule="evenodd" d="M118 67C135 67 141 78 141 91C141 107 128 114 117 108C103 101 101 79 118 67Z M119 79C110 84 113 98 120 99C129 100 133 88 128 82C125 79 122 78 119 79Z"/>
<path id="sharp_junction" fill="#aa21ff" d="M16 93L52 72L47 112L36 98Z"/>
<path id="edge_highlight" fill="url(#highlight)" d="M137 14C150 12 152 27 150 43C142 44 133 39 133 28C133 21 135 16 137 14Z"/></svg>'''
    rgba='''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="128" viewBox="0 0 160 128"><defs>
<linearGradient id="alpha" gradientUnits="userSpaceOnUse" x1="8" y1="0" x2="152" y2="0"><stop offset="0" stop-color="white" stop-opacity="1"/><stop offset="0.333333333333" stop-color="white" stop-opacity="0.82"/><stop offset="0.666666666667" stop-color="white" stop-opacity="0.37"/><stop offset="1" stop-color="white" stop-opacity="0.08"/></linearGradient>
<mask id="soft_mask" maskUnits="userSpaceOnUse" maskContentUnits="userSpaceOnUse" x="0" y="0" width="160" height="128" style="mask-type:alpha"><path fill="url(#alpha)" d="M0 0H160V128H0Z"/></mask>
<linearGradient id="base" gradientUnits="userSpaceOnUse" x1="8" y1="8" x2="152" y2="120"><stop offset="0" stop-color="#171c65"/><stop offset="0.5" stop-color="#5059bc"/><stop offset="1" stop-color="#ded6ef"/></linearGradient>
<linearGradient id="cyan" gradientUnits="userSpaceOnUse" x1="19" y1="0" x2="112" y2="0"><stop offset="0" stop-color="#00405a"/><stop offset="0.333333333333" stop-color="#04aac2"/><stop offset="0.666666666667" stop-color="#a7fff0"/><stop offset="1" stop-color="#f5ffca"/></linearGradient>
<radialGradient id="rose" gradientUnits="userSpaceOnUse" cx="105" cy="54" r="53"><stop offset="0" stop-color="#fff0a0"/><stop offset="0.5" stop-color="#ef3d79"/><stop offset="1" stop-color="#5e183e"/></radialGradient>
<radialGradient id="gleam" gradientUnits="userSpaceOnUse" cx="139" cy="28" r="14"><stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#eaf7e8"/><stop offset="1" stop-color="#91c1da"/></radialGradient></defs>
<g mask="url(#soft_mask)">
<path id="base_shape" fill="url(#base)" opacity="0.91" d="M22 10C67 1 124 8 146 26C161 49 153 104 128 118C89 126 30 119 13 97C4 66 6 24 22 10Z"/>
<path id="cyan_overlap" fill="url(#cyan)" opacity="0.72" d="M20 30C59 9 94 21 112 61C118 90 79 109 42 104C17 92 10 55 20 30Z"/>
<path id="rose_overlap_hole" fill="url(#rose)" opacity="0.64" fill-rule="evenodd" d="M81 21C126 7 153 33 148 73C138 111 99 116 74 90C58 68 58 37 81 21Z M101 57C94 57 91 74 99 79C108 84 115 66 110 61C108 58 104 57 101 57Z"/>
<path id="thin_ribbon" fill="#ffd926" opacity="0.86" d="M24 93.2L133 37.2L133.3 37.8L24.3 93.8Z"/>
<path id="edge_gleam" fill="url(#gleam)" opacity="0.83" d="M135 16C147 16 151 28 148 40C142 43 132 36 131 28C131 23 132 18 135 16Z"/>
</g></svg>'''
    return [
      {'id':'F01_thin_shared_junction_hole','svg':opaque,'dimensions':[160,128],
       'paint_paths':7,'opaque':True,'shared_boundary':'warm/cool: C116 32 44 96 80 120 and exact reversed C44 96 116 32 80 8',
       'thin_regions':[{'id':'thin_diagonal','nominal_perpendicular_width_px':0.848528137423857,'center_line':[[30,12],[130,112]],'critical_box':[74,56,16,16]}],
       'critical_features':{'junction_box':[30,82,24,24],'hole_box':[108,73,30,32],'edge_highlight_box':[130,12,24,34]},
       'overlap_policy':'ring, triangle, ribbon and highlight intentionally source-over base partition; no geometry gap between base warm/cool'},
      {'id':'F02_soft_alpha_overlap_highlight','svg':rgba,'dimensions':[160,128],
       'paint_paths':5,'opaque':False,'alpha':'one common vector linear-gradient alpha mask; 4 equal stops, no raster alpha runs',
       'thin_regions':[{'id':'thin_ribbon','nominal_perpendicular_width_px':0.670820393249937,'center_line':[[24.15,93.5],[133.15,37.5]],'critical_box':[70,60,20,20]}],
       'critical_features':{'overlap_box':[72,36,40,48],'hole_box':[90,54,28,30],'edge_highlight_box':[128,13,26,30],'soft_alpha_box':[112,8,40,112]},
       'overlap_policy':'fixed path opacities plus common mask; source-over mixtures must be modeled; restoring opacity after a hard-ownership fit does not solve inverse compositing'}]
```

### `freeze_fixtures` — `Lines 53–91`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `53` إلى السطر `91` (`Lines 53–91`)
- **الوظيفة:** Write all fixture inputs before fitting; refuse nonempty generation targets.
- **الكود الفعلي (`Lines 53–91`):**
```python
def freeze_fixtures():
    """Write all fixture inputs before fitting; refuse nonempty generation targets."""
    directory=ROOT/'inputs/analytic'
    if directory.exists() and any(directory.iterdir()):raise FileExistsError('Preserve frozen fixtures; use fresh AGD_FIXTURES_ROOT to regenerate')
    directory.mkdir(parents=True,exist_ok=True);cases=[]
    for spec in fixture_specs():
        name=spec['id'];folder=directory/name;folder.mkdir()
        truth=folder/'truth.svg';truth.write_text(spec['svg'],encoding='utf-8')
        root=ET.parse(truth).getroot();initial=copy.deepcopy(root)
        # Mask paths remain unchanged; only visible paint paths receive dummy fills.
        truth_models=[]
        for path in root.iter(f'{{{SVG}}}path'):
            if not path.get('id'):continue
            truth_models.append({'id':path.get('id'),'fill':path.get('fill'),'opacity':float(path.get('opacity','1')),'fill_rule':path.get('fill-rule','nonzero'),'d':path.get('d')})
        for path in initial.iter(f'{{{SVG}}}path'):
            if path.get('id'):path.set('fill','#808080')
        ET.ElementTree(initial).write(folder/'initial.svg',encoding='utf-8',xml_declaration=True)
        gradients=[]
        for node in root.iter():
            kind=node.tag.rsplit('}',1)[-1]
            if kind not in ('linearGradient','radialGradient'):continue
            gradients.append({'kind':kind,'attributes':dict(node.attrib),'stops':[dict(child.attrib) for child in node]})
        timing=render_svg(truth,folder/'source.png',*spec['dimensions'])
        record={k:v for k,v in spec.items() if k!='svg'}
        record.update(source_png=(folder/'source.png').relative_to(ROOT).as_posix(),truth_svg=truth.relative_to(ROOT).as_posix(),initial_svg=(folder/'initial.svg').relative_to(ROOT).as_posix(),
          truth_regions=truth_models,truth_gradients=gradients,render=timing,license='CC0-1.0',author='AiGraphicDesigner research / package_generalization',
          provenance='Deterministic authored analytic vector control; no remote/generated image source; not real-image generalization evidence')
        record['files']={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in folder.iterdir() if p.is_file()}
        cases.append(record)
    old=REPO/'experiments/EXP_GEOMETRY_APPEARANCE_ABLATION_01'
    references=[{'id':name,'truth_svg':str(old/'inputs'/f'{name}.svg'),'source_png':str(old/'inputs'/f'{name}.png'),
      'truth_sha256':hashlib.sha256((old/'inputs'/f'{name}.svg').read_bytes()).hexdigest(),
      'source_sha256':hashlib.sha256((old/'inputs'/f'{name}.png').read_bytes()).hexdigest(),
      'policy':'Existing analytic reference only; no new tracing/rendering performed'} for name in ('K01_linear_corner_hole','K02_radial_shared_curves')]
    manifest={'status':'FROZEN_BEFORE_FITTING','cases':cases,'existing_control_references':references,'architecture':'NOT_APPROVED',
      'representation':'2 new compact known-vector controls, same true fixed geometry for all conditions; no hidden pixels',
      'baseline_adapter_requirement':'Old fitter rejects masks, opacity and gradient dummy fallbacks. Remove mask/opacity only from its RGB fitting input; preserve/restore exact original masks and opacity on ALL final conditions. This adapter is not overlap-aware fitting.'}
    (directory/'manifest.json').write_text(json.dumps(manifest,indent=2,allow_nan=False),encoding='utf-8')
    return manifest
```
