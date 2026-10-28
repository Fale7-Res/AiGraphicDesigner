# مرآة الكود التفصيلية: `research.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `research.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `research.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `162` (`Lines 1–162`)
- **بصمة الملف (`SHA-256`):** `696db616fa22f94eb194f72ede6dcb1a0b385cb2e79fcda783080fad00bd8ae3`
- **الوصف التفصيلي:** """Bounded fixed-geometry coverage experiment. Historical evidence is read-only."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `save` | `function` | `Lines 17–19` | `def save(path,data):` | رمز برمجي موثق. |
| `sha` | `function` | `Lines 20–20` | `def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()` | رمز برمجي موثق. |
| `prepare` | `function` | `Lines 21–44` | `def prepare():` | رمز برمجي موثق. |
| `transplant` | `function` | `Lines 45–56` | `def transplant(template,fitted,target):` | رمز برمجي موثق. |
| `old_fit` | `function` | `Lines 57–57` | `def old_fit():return new._historical()` | رمز برمجي موثق. |
| `fixture_baseline` | `function` | `Lines 58–80` | `def fixture_baseline(c,out):` | رمز برمجي موثق. |
| `evaluate_extra` | `function` | `Lines 81–105` | `def evaluate_extra(source,png,maps,reference):` | رمز برمجي موثق. |
| `evaluate_extra.mean` | `nested_function` | `Lines 95–95` | `def mean(mask):return float(err[mask].mean()) if mask.any() else None` | رمز برمجي موثق. |
| `run` | `function` | `Lines 106–148` | `def run(c):` | رمز برمجي موثق. |
| `main` | `function` | `Lines 149–160` | `def main():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `save` — `Lines 17–19`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `19` (`Lines 17–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–19`):**
```python
def save(path,data):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(data,indent=2,allow_nan=False),encoding='utf-8')
```

### `sha` — `Lines 20–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `20` (`Lines 20–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–20`):**
```python
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
```

### `prepare` — `Lines 21–44`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `44` (`Lines 21–44`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–44`):**
```python
def prepare():
    cases=[]
    for name in ['A01_shield','G01_coffee','G05_chelsea_nativecrop','G06_arabic','G08_dice_alpha']:
        p=PRIOR/'results/granularity'/name
        cases.append(dict(id=name,kind='real',source=str(p/'source.png'),flat=str(p/'192/C/output.svg'),gradient=str(p/'192/D/output.svg'),pixel=str(p/'A/output.svg'),saved_result=str(p/'result.json')))
    for name in ['K01_linear_corner_hole','K02_radial_shared_curves']:
        p=PRIOR/'results/oracle'/name
        cases.append(dict(id=name,kind='existing_oracle',source=str(p/'source.png'),flat=str(p/'oracle_C.svg'),gradient=str(p/'oracle_D.svg'),truth=str(p/'oracle_truth.svg'),pixel=str(ABL/'results'/name/'A/output.svg'),saved_result=str(p/'result.json')))
    fixtures=json.loads((ROOT/'inputs/analytic/manifest.json').read_text())
    for f in fixtures['cases']:
        cases.append(dict(id=f['id'],kind='new_oracle',source=str(ROOT/f['source_png']),initial=str(ROOT/f['initial_svg']),truth=str(ROOT/f['truth_svg']),fixture=f))
    for c in cases:c['hashes']={k:sha(c[k]) for k in ['source','flat','gradient','pixel','truth','initial','saved_result'] if k in c}
    path=ROOT/'inputs/manifest.json'
    data={'baseline_git':'ed6072b15d3f9fca4774856ffcf31909d1785fd7','architecture':'NOT_APPROVED','cases':cases,
      'protocol':{'geometry':'Fixed saved D192 unstroked geometry for five real cases; exact known geometry for four controls. No tracing/searches or geometry changes.',
      'conditions':['Aflat existing interior flat','Agrad existing interior adaptive','B coverage flat','C coverage adaptive same family <=4 equal stops'],
      'objective':'Equal mean MSE on white, black and bluegray. Float effective target Ps+(Ar-As)*meanBg. No extra alpha weighting.',
      'split':'(x+3y)%5 train012 selection3 test4; test is withheld from this fitting update only. Historical geometry and seeds already saw source. Periodic interpolation, not independent generalization.',
      'budget':'20 flat sweeps; 2 gradient passes; inherited 100 evaluations per region; 300 seconds fit; 900 seconds/4096MiB worker; coverage arrays <=200MiB; 15 seconds per diagnostic probe.',
      'acceptance':'Support requires held-out and actual-render gains without geometry/alpha changes; report cross-category failures, individual backgrounds, reference gap, not just training loss. No numeric improvement promise.',
      'limitations':'Fixed alpha-run masks remain for real transparent cases. New analytic baselines temporarily remove mask/opacity for old RGB fitter, then restore exact original scene; this adapter is explicitly overlap-unaware.'}}
    if path.exists():assert json.loads(path.read_text())==data
    else:save(path,data)
    return data
```

### `transplant` — `Lines 45–56`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `45` إلى السطر `56` (`Lines 45–56`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 45–56`):**
```python
def transplant(template,fitted,target):
    root=copy.deepcopy(template);fitroot=ET.parse(fitted).getroot();entries=old_fit()._paths(root);paint=old_fit()._paths(fitroot)
    assert len(entries)==len(paint)
    refs=set()
    for (p,_),(q,_) in zip(entries,paint):
        p.set('fill',q.get('fill'))
        if q.get('fill','').startswith('url(#'):refs.add(q.get('fill')[5:-1])
    defs=root.find(f'{{{SVG}}}defs')
    if refs and defs is None:defs=ET.SubElement(root,f'{{{SVG}}}defs')
    for node in fitroot.iter():
        if node.get('id') in refs:defs.append(copy.deepcopy(node))
    ET.ElementTree(root).write(target,encoding='utf-8',xml_declaration=True)
```

### `old_fit` — `Lines 57–57`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `57` (`Lines 57–57`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–57`):**
```python
def old_fit():return new._historical()
```

### `fixture_baseline` — `Lines 58–80`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `80` (`Lines 58–80`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 58–80`):**
```python
def fixture_baseline(c,out):
    template=ET.parse(c['initial']).getroot()
    dependencies=set()
    import re
    for mask in template.iter(f'{{{SVG}}}mask'):
        dependencies.update(re.findall(r'url\(#([^)]*)\)',ET.tostring(mask,encoding='unicode')))
    for parent in template.iter():
        for child in list(parent):
            if child.tag.rsplit('}',1)[-1] in ('linearGradient','radialGradient') and child.get('id') not in dependencies:parent.remove(child)
    temp=copy.deepcopy(template)
    for parent in temp.iter():
        for child in list(parent):
            if child.tag.rsplit('}',1)[-1]=='mask':parent.remove(child)
    for node in temp.iter():
        node.attrib.pop('mask',None);node.attrib.pop('opacity',None)
    # Remove unused RGB truth gradients; mask dependency remains only in full template.
    for parent in temp.iter():
        for child in list(parent):
            if child.tag.rsplit('}',1)[-1] in ('linearGradient','radialGradient'):parent.remove(child)
    ET.ElementTree(temp).write(out/'interior_rgb_input.svg',encoding='utf-8',xml_declaration=True)
    fit_svg(out/'source.png',out/'interior_rgb_input.svg',out/'interior_flat_raw.svg',out/'interior_grad_raw.svg',out/'interior_fitting.json',deadline_seconds=120)
    for label,raw in [('Aflat','interior_flat_raw.svg'),('Agrad','interior_grad_raw.svg')]:
        transplant(template,out/raw,out/label/'output.svg')
```

### `evaluate_extra` — `Lines 81–105`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `81` إلى السطر `105` (`Lines 81–105`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 81–105`):**
```python
def evaluate_extra(source,png,maps,reference):
    a=np.asarray(Image.open(source).convert('RGBA'),dtype=float);b=np.asarray(Image.open(png).convert('RGBA'),dtype=float)
    h,w=a.shape[:2];aa=a[:,:,3]/255;ba=b[:,:,3]/255
    ap=a[:,:,:3]*aa[:,:,None];bp=b[:,:,:3]*ba[:,:,None]
    W=maps['weights'];total=maps['total'].reshape(h,w);dominant=W.max(axis=0).reshape(h,w)
    # Effective-mixture boundary, not a claim of geometric ground truth.
    boundary=(total>1e-7)&((dominant<total-.002)|(total<.998))
    interior=(total>.998)&(dominant>=total-.002)
    yy,xx=np.indices((h,w));part=(xx+3*yy)%5;test=part==4
    sq=[];bgrows={}
    for name,color in [('white',(255,255,255)),('black',(0,0,0)),('bluegray',(40,80,120))]:
        bg=np.array(color);e=((bp+(1-ba[:,:,None])*bg)-(ap+(1-aa[:,:,None])*bg))**2
        sq.append(e.mean(axis=2));bgrows[name]=float(e.mean())
    err=np.mean(sq,axis=0)
    def mean(mask):return float(err[mask].mean()) if mask.any() else None
    supports=[]
    for i,weight in enumerate(W):
        wt=weight.reshape(h,w)**2*test;den=wt.sum()
        supports.append({'region':i,'heldout_effective_mixture_mse':float((wt*err).sum()/den) if den>1e-12 else None,'heldout_weight_energy':float(den),'support_pixels':int((weight>1e-8).sum())})
    r=np.asarray(Image.open(reference).convert('RGBA')) if reference else None
    return {'float_three_background_mse':float(err.mean()),'float_per_background_mse':bgrows,'heldout_float_three_background_mse':mean(test),
      'boundary_float_three_background_mse':mean(boundary),'interior_float_three_background_mse':mean(interior),'boundary_pixels':int(boundary.sum()),'interior_pixels':int(interior.sum()),
      'alpha_mse':float(((a[:,:,3]-b[:,:,3])**2).mean()),'alpha_nonzero_difference_pixels':int((a[:,:,3]!=b[:,:,3]).sum()),
      'fixed_baseline_alpha_max_change_bytes':int(np.abs(b[:,:,3]-(r[:,:,3] if r is not None else b[:,:,3])).max()),
      'regions':supports,'boundary_definition':'Effective contribution mixed or total alpha<.998; includes translucent interiors. Not independent physical boundary truth. Region scores are weighted final mixed-pixel residuals, not uniquely attributable paint errors.'},err,boundary
```

### `evaluate_extra.mean` — `Lines 95–95`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `95` إلى السطر `95` (`Lines 95–95`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 95–95`):**
```python
    def mean(mask):return float(err[mask].mean()) if mask.any() else None
```

### `run` — `Lines 106–148`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `106` إلى السطر `148` (`Lines 106–148`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 106–148`):**
```python
def run(c):
    out=ROOT/'results'/c['id']
    for k,v in c['hashes'].items():assert sha(c[k])==v,(c['id'],k)
    if (out/'result.json').exists():
        r=json.loads((out/'result.json').read_text())
        assert sha(out/'source.png')==c['hashes']['source']
        assert sha(out/'coverage/maps.npz')==r['map_metadata']['maps_npz_sha256']
        for k,v in r['conditions'].items():
            assert sha(out/k/'output.svg')==v['sha256']
            for png in ['render.png','white.png','black.png','bluegray.png']:Image.open(out/k/png).verify()
        print('REUSE',c['id'],flush=True);return
    if out.exists() and any(out.iterdir()):raise FileExistsError('Preserve partial evidence; inspect before retry: '+str(out))
    started=time.monotonic();out.mkdir(parents=True);shutil.copyfile(c['source'],out/'source.png')
    for k in ['Aflat','Agrad','B','C','pixel','truth']:(out/k).mkdir()
    if c['kind']=='new_oracle':fixture_baseline(c,out)
    else:
        for k,s in [('Aflat','flat'),('Agrad','gradient')]:shutil.copyfile(c[s],out/k/'output.svg')
    for k in ['pixel','truth']:
        if k in c:shutil.copyfile(c[k],out/k/'output.svg')
    meta=new.build_maps(out/'Aflat/output.svg',out/'coverage')
    new.fit_case(out/'source.png',out/'Aflat/output.svg',out/'Agrad/output.svg',out/'coverage',out/'B/output.svg',out/'C/output.svg',out/'fitting.json',max_seconds=300)
    with np.load(out/'coverage/maps.npz') as archive:maps={key:archive[key] for key in archive.files}
    rows={}
    for k in ['Aflat','Agrad','B','C','pixel','truth']:
        svg=out/k/'output.svg'
        if not svg.exists():continue
        # Render baselines once here for common evaluation and alpha invariants; no tracing or fitting rerun on seven saved cases.
        row=old.evaluate_condition(out/'source.png',svg,out/k)
        extra,err,band=evaluate_extra(out/'source.png',out/k/'render.png',maps,out/'Aflat/render.png')
        row.update(extra);rows[k]=row
        Image.fromarray(np.uint8(np.clip(np.sqrt(err)*6,0,255))).save(out/k/'error.png')
        if k=='C':Image.fromarray(np.uint8(band)*255).save(out/'coverage/boundary_band.png')
    signatures={new._shape_signature(ET.parse(out/k/'output.svg').getroot()) for k in ['Aflat','Agrad','B','C']}
    assert len(signatures)==1,'Geometry/mask drift'
    oracle=[]
    if c['kind']=='new_oracle':
        truth=c['fixture']['truth_regions']
        for k in ['Aflat','B']:
            colors=new._models(ET.parse(out/k/'output.svg').getroot(),old_fit())
            for i,t in enumerate(truth):
                if not t['fill'].startswith('url('):oracle.append({'condition':k,'region':t['id'],'flat_color_rmse_bytes':float(np.sqrt(np.mean((new._color(t['fill'])-colors[i]['colors'][0])**2)))})
    save(out/'result.json',{'id':c['id'],'kind':c['kind'],'conditions':rows,'fixed_scene_signature':next(iter(signatures)),'map_metadata':meta,'oracle_flat_color_errors':oracle,'wall_seconds':time.monotonic()-started,'architecture':'NOT_APPROVED'})
    print('COMPLETE',c['id'],{k:round(v['metrics']['white']['ssim'],6) for k,v in rows.items()},flush=True)
```

### `main` — `Lines 149–160`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `149` إلى السطر `160` (`Lines 149–160`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 149–160`):**
```python
def main():
    p=argparse.ArgumentParser();p.add_argument('--prepare',action='store_true');p.add_argument('--case');args=p.parse_args()
    if args.prepare:prepare();return
    manifest=json.loads((ROOT/'inputs/manifest.json').read_text())
    if args.case:run(next(c for c in manifest['cases'] if c['id']==args.case));return
    (ROOT/'reports').mkdir(exist_ok=True)
    for c in sorted(manifest['cases'],key=lambda c:c['kind']!='new_oracle'):
        if (ROOT/'results'/c['id']/'result.json').exists():run(c);continue
        stats=monitor([sys.executable,str(Path(__file__).resolve()),'--case',c['id']],ROOT/'reports'/f'{c["id"]}.log',900,4096)
        save(ROOT/'reports'/f'{c["id"]}_resources.json',stats)
        print(c['id'],stats,flush=True)
        if stats['returncode'] or stats['termination_reason']:raise SystemExit('Failed case preserved: '+c['id'])
```
