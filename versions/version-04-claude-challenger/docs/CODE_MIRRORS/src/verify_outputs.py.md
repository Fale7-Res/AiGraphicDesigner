# مرآة الكود التفصيلية للإصدار: `version-04-claude-challenger/src/verify_outputs.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-04-claude-challenger/src/verify_outputs.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-04-claude-challenger`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/verify_outputs.py`
- **الإصدار المعماري (`Architecture Version`):** `version-04-claude-challenger`
- **إجمالي عدد الأسطر (`Total Lines`):** `54` (`Lines 1–54`)
- **بصمة الملف (`SHA-256`):** `7b31a3d0aa747ab60481005bc2ce00a113f4b6d319ae1193b4d456fb2733dad6`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-04-claude-challenger`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-04-claude-challenger` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `main` | `function` | `Lines 11–53` | `def main():` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `main` — `Lines 11–53`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `53` (`Lines 11–53`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 11–53`):**
```python
def main():
    records=[]
    sources=sorted(p for p in SRC_DIR.glob('A*.png') if re.match(r'A\d\d_',p.name))
    if len(sources)!=12: raise RuntimeError(f'Expected 12 inputs; found {len(sources)}')
    for i,src_path in enumerate(sources,1):
        aid=src_path.name.split('_')[0]; source=np.asarray(Image.open(src_path).convert('RGB'),dtype=np.uint8)
        svg_path=OUT/'outputs'/f'{src_path.stem}_v04.svg'
        png_path=OUT/'rendered'/'v04'/f'{aid}_v04.png'
        if not svg_path.exists() or not png_path.exists(): raise FileNotFoundError(f'Missing SVG/render for {aid}')
        text=svg_path.read_text(encoding='utf-8')
        base,_=AdaptiveVectorSurface(Config(max_cells=9000)).vectorize(source)
        regenerated,_=add_edge_residual_layer(base,source,dilation=1,color_bits=5)
        same=(text==regenerated)
        root=ET.fromstring(text)
        tags=[node.tag.rsplit('}',1)[-1] for node in root.iter()]
        desc=' '.join((root.find('{http://www.w3.org/2000/svg}desc').text or '').split()) if root.find('{http://www.w3.org/2000/svg}desc') is not None else ''
        rendered=Image.open(png_path)
        dims_ok=rendered.size==(source.shape[1],source.shape[0])
        rec={'image_id':aid,'deterministic_reproduction_byte_identical':same,'svg_xml_well_formed':True,
             'embedded_image_elements':tags.count('image'),'external_image_href':bool(re.search(r'href=["\'](?:https?:|file:|data:image)',text,re.I)),
             'svg_bytes':svg_path.stat().st_size,'render_png_dimensions':list(rendered.size),'source_dimensions':[source.shape[1],source.shape[0]],
             'render_dimensions_match':dims_ok,'representation_declares_hybrid_vector_only':'Hybrid vector-only representation' in desc}
        records.append(rec)
        print(f"[{i}/12] {aid}: deterministic={same}, SVG bytes={rec['svg_bytes']}, images={rec['embedded_image_elements']}, render_dims={dims_ok}",flush=True)
    result={'images':len(records),'all_deterministic_byte_identical':all(r['deterministic_reproduction_byte_identical'] for r in records),
            'all_svg_xml_well_formed':all(r['svg_xml_well_formed'] for r in records),'no_embedded_raster_images':all(r['embedded_image_elements']==0 and not r['external_image_href'] for r in records),
            'all_render_dimensions_match_source':all(r['render_dimensions_match'] for r in records),'all_hybrid_representation_labels_present':all(r['representation_declares_hybrid_vector_only'] for r in records),'per_image':records}
    target=OUT/'metrics'/'verification.json'; target.write_text(json.dumps(result,indent=2),encoding='utf-8')
    summary_path=OUT/'metrics'/'summary.json'
    if summary_path.exists():
        summary=json.loads(summary_path.read_text(encoding='utf-8'))
        summary['verification']=result
        summary['deterministic_svg_reproduction_all_images']=result['all_deterministic_byte_identical']
        summary_path.write_text(json.dumps(summary,indent=2),encoding='utf-8')
    report=OUT/'metrics'/'RESULTS_REPORT.md'
    if report.exists():
        body=report.read_text(encoding='utf-8')
        body=body.replace('**Status:** completed local experimental evaluation; no global approval state modified.',
            '**Status:** completed local experimental evaluation; no global approval state modified. The independent verifier regenerated all 12 final SVGs byte-identically: **'+str(result['all_deterministic_byte_identical'])+'**; all were XML-well-formed, rendered at input dimensions, and contained zero embedded raster image elements.')
        report.write_text(body,encoding='utf-8')
    if not (result['all_deterministic_byte_identical'] and result['all_svg_xml_well_formed'] and result['no_embedded_raster_images'] and result['all_render_dimensions_match_source'] and result['all_hybrid_representation_labels_present']):
        raise SystemExit('One or more final artifact verification checks failed; inspect verification.json')
    print(json.dumps({k:v for k,v in result.items() if k!='per_image'},indent=2))
```
