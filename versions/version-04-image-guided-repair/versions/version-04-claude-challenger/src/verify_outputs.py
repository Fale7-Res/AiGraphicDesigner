"""Verify final outputs against deterministic regeneration and renderer outputs."""
from pathlib import Path
import json, re, sys, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
HERE=Path(__file__).resolve();V4=HERE.parents[1];ROOT=HERE.parents[3]
sys.path.insert(0,str(V4))
from src.challenger import Challenger,Config,estimate_target_regions
from src.run_benchmark import SRC,OUT

def main():
    inputs=sorted(p for p in SRC.glob('A*.png') if re.match(r'A\d\d_',p.name))
    results=[]
    for ix,src in enumerate(inputs,1):
        aid=src.stem.split('_')[0];rgb=np.asarray(Image.open(src).convert('RGB'),dtype=np.uint8)
        target,_=estimate_target_regions(rgb)
        svg,meta=Challenger(Config(target_regions=target,compactness=9.0)).vectorize(rgb)
        svg_path=OUT/'outputs'/f'{src.stem}_v04.svg';render_path=OUT/'rendered/v04'/f'{aid}_v04.png'
        saved=svg_path.read_text(encoding='utf-8')
        root=ET.fromstring(saved);tags=[e.tag.rsplit('}',1)[-1] for e in root.iter()]
        render=Image.open(render_path)
        row={'image_id':aid,'target_regions':target,'byte_identical_regeneration':saved==svg,
             'xml_well_formed':True,'embedded_image_elements':tags.count('image'),
             'external_image_href':bool(re.search(r'href=["\'](?:https?:|file:|data:image)',saved,re.I)),
             'linear_gradients':tags.count('linearGradient'),'radial_gradients':tags.count('radialGradient'),
             'clip_paths':tags.count('clipPath'),'svg_bytes':svg_path.stat().st_size,
             'render_dimensions_match':render.size==(rgb.shape[1],rgb.shape[0]),
             'source_dimensions':[rgb.shape[1],rgb.shape[0]],'render_dimensions':list(render.size)}
        results.append(row)
        print(f'[{ix}/12] {aid}: byte-identical={row["byte_identical_regeneration"]}, raster elements={row["embedded_image_elements"]}, dimensions={row["render_dimensions_match"]}',flush=True)
    result={'count':len(results),'all_byte_identical':len(results)==12 and all(x['byte_identical_regeneration'] for x in results),
            'all_xml_well_formed':all(x['xml_well_formed'] for x in results),
            'no_embedded_or_external_raster':all(x['embedded_image_elements']==0 and not x['external_image_href'] for x in results),
            'all_render_dimensions_match':all(x['render_dimensions_match'] for x in results),
            'every_image_has_smooth_silhouette_clip':all(x['clip_paths']>=2 for x in results),
            'per_image':results}
    p=OUT/'metrics'/'verification.json';p.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='per_image'},indent=2))
    if not all(result[k] for k in ['all_byte_identical','all_xml_well_formed','no_embedded_or_external_raster','all_render_dimensions_match','every_image_has_smooth_silhouette_clip']): raise SystemExit('Verification failed')
if __name__=='__main__':main()
