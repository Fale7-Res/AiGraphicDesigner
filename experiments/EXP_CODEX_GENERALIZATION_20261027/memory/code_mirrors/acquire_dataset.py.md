# مرآة الكود التفصيلية: `acquire_dataset.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `acquire_dataset.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `acquire_dataset.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `95` (`Lines 1–95`)
- **بصمة الملف (`SHA-256`):** `1e00b90d63140ee6a633560a5f13a4b8dc4e33971613e8df6ff29d047d81f144`
- **الوصف التفصيلي:** # START CHANGE AGD-GENERALIZATION-DATA | 2026-10-27T11:09:10Z | CREATED | Author: codex-dataset-agent; Parent: AGD-GENERALIZATION-20261027

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `fetch` | `function` | `Lines 29–32` | `def fetch(url):` | رمز برمجي موثق. |
| `digest` | `function` | `Lines 34–35` | `def digest(data):` | رمز برمجي موثق. |
| `alpha_info` | `function` | `Lines 37–40` | `def alpha_info(image):` | رمز برمجي موثق. |
| `main` | `function` | `Lines 42–91` | `def main():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `fetch` — `Lines 29–32`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `32` (`Lines 29–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–32`):**
```python
def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent':'AiGraphicDesignerResearch/1.0 (licensed raster benchmarking)'})
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read(), response.url
```

### `digest` — `Lines 34–35`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `35` (`Lines 34–35`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–35`):**
```python
def digest(data):
    return hashlib.sha256(data).hexdigest()
```

### `alpha_info` — `Lines 37–40`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `37` إلى السطر `40` (`Lines 37–40`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 37–40`):**
```python
def alpha_info(image):
    alpha = image.convert('RGBA').getchannel('A')
    histogram = alpha.histogram()
    return {'unique_values':sum(v>0 for v in histogram),'transparent_pixels':histogram[0], 'partial_pixels':sum(histogram[1:255]), 'opaque_pixels':histogram[255]}
```

### `main` — `Lines 42–91`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `91` (`Lines 42–91`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–91`):**
```python
def main():
    INPUTS.mkdir(exist_ok=True)
    (DATASET/'originals').mkdir(parents=True, exist_ok=True)
    (DATASET/'sources').mkdir(exist_ok=True)
    cases=[]
    for cid, filename, domains, author, license_name, url, source, mode in SPECS:
        stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        sourcefile = DATASET/'sources'/('scikit-image-data.html' if source==DOC else cid+'.html')
        if not sourcefile.exists():
            try:
                sourcefile.write_bytes(fetch(source)[0])
            except Exception as exc:
                print('LICENSE SNAPSHOT FAILURE', cid, str(exc), flush=True)
                raise
        if url is None:
            markup=sourcefile.read_text(encoding='utf-8')
            match=re.search(r'<a[^>]+href="([^"]+)"[^>]*>Original file</a>', markup)
            if not match:
                match=re.search(r'class="fullMedia".*?href="([^"]+)"',markup,re.S)
            if not match:
                raise RuntimeError('Cannot find original raster URL for '+cid)
            url=html.unescape(match.group(1))
            if url.startswith('//'): url='https:'+url
        original=DATASET/'originals'/filename
        if not original.exists():
            raw,resolved=fetch(url)
            original.write_bytes(raw)
        else:
            raw=original.read_bytes(); resolved=url
        image=Image.open(io.BytesIO(raw)); image.load()
        native_dimensions=list(image.size); native_alpha=alpha_info(image)
        image=image.convert('RGBA' if native_alpha['transparent_pixels']+native_alpha['partial_pixels'] else 'RGB')
        transforms=[]
        if mode=='center_crop':
            w,h=image.size; edge=min(256,w,h)
            box=((w-edge)//2,(h-edge)//2,(w+edge)//2,(h+edge)//2)
            image=image.crop(box); transforms.append({'operation':'prespecified_center_crop','box':list(box),'resampling':'none'})
        elif max(image.size)>320:
            old=image.size; scale=320/max(old)
            size=(round(old[0]*scale),round(old[1]*scale))
            image=image.resize(size,Image.Resampling.LANCZOS)
            transforms.append({'operation':'aspect_preserving_resize','from':list(old),'to':list(size),'resampling':'Pillow LANCZOS; premultiplied RGBA internally'})
        out=INPUTS/(cid+'.png'); image.save(out)
        cases.append({'id':cid,'file':out.name,'domains':domains,'source_url':source,'download_url':url,'resolved_download_url':resolved,'license':license_name,'license_url':{'CC0':'https://creativecommons.org/publicdomain/zero/1.0/','CC-BY-SA-3.0':'https://creativecommons.org/licenses/by-sa/3.0/'}.get(license_name,source),'author':author,'accessed_at_utc':stamp,'original_file':str(original.relative_to(ROOT)).replace('\\','/'),'original_dimensions':native_dimensions,'dimensions':list(image.size),'transforms':transforms,'sha256':digest(out.read_bytes()),'original_sha256':digest(raw),'original_bytes':len(raw),'native_alpha':native_alpha,'normalized_alpha':alpha_info(image),'license_snapshot':str(sourcefile.relative_to(ROOT)).replace('\\','/'),'split':'unseen_by_this_engine_before_this_cycle','linked_source_case':'G02_chelsea' if mode=='center_crop' else None})
        (INPUTS/'manifest.json').write_text(json.dumps({'cases':cases,'status':'ACQUIRING','max_edge':320},indent=2),encoding='utf-8')
        print('READY',cid,list(image.size),native_alpha,flush=True)
    manifest={'cases':cases,'status':'FROZEN_BEFORE_BENCHMARK','frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selection_policy':'Prespecified cross-domain sources, no score-based filtering; G05 is a correlated center-crop diagnostic, not an independent source. Dice is a published 3D-rendered asset, not a photograph. No new SVG rasterizations. Historical astronaut, brick, A01-A12 and synthetic fixtures excluded.','max_edge':320,'independent_source_images':7,'modifications_license':'Normalized rasters and vector reconstructions inherit original applicable license; attribution retained in this manifest. Logos used for technical comparison, no affiliation implied.'}
    frozen=json.dumps(manifest,indent=2).encode()
    (INPUTS/'manifest.json').write_bytes(frozen)
    (DATASET/'freeze.json').write_text(json.dumps({'manifest_sha256':digest(frozen),'frozen_at_utc':manifest['frozen_at_utc'],'case_count':len(cases)},indent=2))
```
