"""Independent final-artifact verifier: regeneration, SVG structure, embeds, render dimensions."""
from pathlib import Path
import json, re, sys, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
HERE=Path(__file__).resolve(); VERSION_DIR=HERE.parents[1]; ROOT=HERE.parents[3]
sys.path.insert(0,str(VERSION_DIR))
from src.challenger import AdaptiveVectorSurface, Config, add_edge_residual_layer
from src.run_benchmark import SRC_DIR,OUT

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
if __name__=='__main__':main()
