# مرآة الكود التفصيلية: `benchmark.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `benchmark.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `benchmark.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `48` (`Lines 1–48`)
- **بصمة الملف (`SHA-256`):** `3be6b982bdfdd1f815b940848c548493adaf221aff1aee7d47760e0859e4bec1`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `fixtures` | `function` | `Lines 12–27` | `def fixtures():` | رمز برمجي موثق. |
| `execute` | `function` | `Lines 29–33` | `def execute(item):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `fixtures` — `Lines 12–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `27` (`Lines 12–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–27`):**
```python
def fixtures():
    p=ROOT/'unseen';p.mkdir(exist_ok=True);manifest=[]
    y,x=np.mgrid[:192,:256];shade=np.exp(-((x-130)**2/2600+(y-120)**2/350))
    rgb=np.stack([230-70*shade+x/30,225-65*shade+y/40,215-55*shade],2).clip(0,255).astype('uint8')
    images={'U01_smooth_shadow':Image.fromarray(rgb),'U02_fine_monochrome':Image.new('RGB',(256,192),'white')}
    d=ImageDraw.Draw(images['U02_fine_monochrome'])
    for k in range(15):d.line([(10,8+k*11),(240,12+k*11)],fill='black',width=1+k%3)
    rng=np.random.default_rng(26026);images['U03_color_texture']=Image.fromarray(rng.integers(0,256,(192,256,3),dtype='uint8'))
    alpha=Image.fromarray(rgb).convert('RGBA');alpha.putalpha(Image.fromarray((x/255*255).astype('uint8')));images['U04_partial_alpha']=alpha
    images['U05_astronaut']=Image.fromarray(data.astronaut());images['U06_brick']=Image.fromarray(data.brick())
    for name,im in images.items():
        f=p/(name+'.png')
        if not f.exists():im.save(f)
        manifest.append({'id':name,'file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'size':im.size,'alpha_policy':'white' if name=='U04_partial_alpha' else 'reject','split':'new_real' if name in ('U05_astronaut','U06_brick') else 'new_synthetic'})
    (p/'manifest.json').write_text(json.dumps({'inputs':manifest,'real_source':'scikit-image0.26 bundled data; https://scikit-image.org/docs/stable/api/skimage.data.html; astronaut NASA publicdomain, brick CC0Textures CC0; native dimensions unchanged'},indent=2))
    return manifest
```

### `execute` — `Lines 29–33`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `33` (`Lines 29–33`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–33`):**
```python
def execute(item):
    source,split,alpha=item;out=ROOT/'results'/source.stem
    if (out/'ranking.json').exists():return {'id':source.stem,'status':'reused_completed'}
    r=optimize(source,out,24,720,alpha)
    return {'id':source.stem,'split':split,'tested':r['evaluated_candidates'],'stop':r['stop_reason'],'status':'ok' if r['ranked'] else 'failed','metrics':r['ranked'][0]['metrics'] if r['ranked'] else None}
```
