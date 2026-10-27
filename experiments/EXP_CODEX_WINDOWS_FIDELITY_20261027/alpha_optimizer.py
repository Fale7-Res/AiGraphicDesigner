"""EXPERIMENTAL: preserve source alpha using only genuine SVG vector mask paths.

Trace unassociated sRGB, then attach exact per-pixel source alpha as horizontal
equal-alpha runs. This favors fidelity over geometry size or semantic editing.
The initial candidate winner is selected on opaque RGB; multi-background and
alpha diagnostics are post-selection evidence, not a claim of alpha-aware search.
"""
# START CHANGE AGD-CODEX-ALPHA-PROBE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension
import argparse
import hashlib
import io
import json
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
import numpy as np
from PIL import Image, ImageCms
from optimizer import optimize
from windows_search import compare, extra_metrics, fidelity_score, render_svg, svg_structure
SVG='http://www.w3.org/2000/svg'
ET.register_namespace('',SVG)
# END CHANGE AGD-CODEX-ALPHA-PROBE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension

# START CHANGE AGD-CODEX-ALPHA-NORMALIZE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension
def prepare_transparent_input(source: Path,folder: Path,max_pixels: int=1048576) -> dict:
    """Retain unassociated RGB and alpha; convert declared ICC to sRGB once."""
    source=Path(source);folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    with Image.open(source) as image:
        if getattr(image,'n_frames',1)!=1 or min(image.size)<7:
            raise ValueError('Single frame with width/height >=7 required')
        if image.width*image.height>max_pixels:
            raise ValueError('Experimental vector alpha mask pixel budget exceeded')
        image.load();alpha=image.convert('RGBA').getchannel('A');rgb=image.convert('RGB')
        profile=image.info.get('icc_profile')
        if profile:
            rgb=ImageCms.profileToProfile(rgb,ImageCms.ImageCmsProfile(io.BytesIO(profile)),
                                         ImageCms.createProfile('sRGB'),outputMode='RGB')
        rgba=rgb.convert('RGBA');rgba.putalpha(alpha)
        rgb.save(folder/'unassociated_rgb.png');alpha.save(folder/'source_alpha.png')
        rgba.save(folder/'reference_srgb_rgba.png')
        report={'source':str(source.resolve()),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                'dimensions':list(image.size),'alpha_extrema':list(alpha.getextrema()),
                'color_policy':'embedded profile transformed to sRGB' if profile else 'untagged RGB assumed sRGB',
                'alpha_policy':'preserve original 8-bit alpha as SVG vector mask; no white compositing',
                'pixel_budget':max_pixels,'status':'EXPERIMENTAL_REQUIRES_RENDER_VALIDATION'}
    (folder/'normalization.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return report
# END CHANGE AGD-CODEX-ALPHA-NORMALIZE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension

# START CHANGE AGD-CODEX-ALPHA-MASK | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension
def apply_vector_alpha(rgb_svg: Path,alpha_png: Path,destination: Path) -> dict:
    """Attach alpha run paths at native integer pixel coordinates; no raster tags."""
    alpha=np.asarray(Image.open(alpha_png).convert('L'));height,width=alpha.shape
    structure=svg_structure(rgb_svg)
    if not structure['raster_free'] or structure['external_href_count'] or structure['script_count']:
        raise ValueError('Input RGB SVG must be self-contained, raster-free, and script-free')
    root=ET.parse(rgb_svg).getroot()
    if root.tag!=f'{{{SVG}}}svg': raise ValueError('Expected SVG namespace root')
    viewbox=root.get('viewBox')
    if viewbox and [float(v) for v in viewbox.replace(',',' ').split()]!=[0.,0.,float(width),float(height)]:
        raise ValueError('Mask requires native source viewBox coordinates')
    for key,expected in (('width',width),('height',height)):
        raw=root.get(key,'').removesuffix('px')
        if not raw or float(raw)!=expected: raise ValueError('SVG/source alpha dimensions differ')
    mask_id='agd_source_alpha_mask'
    if any(element.get('id')==mask_id for element in root.iter()): raise ValueError('Alpha mask id collision')
    runs=defaultdict(list);count=0;start=time.perf_counter()
    for y,row in enumerate(alpha):
        changes=np.flatnonzero(row[1:]!=row[:-1])+1
        boundaries=np.concatenate(([0],changes,[width]))
        for x,end in zip(boundaries[:-1],boundaries[1:]):
            level=int(row[x])
            if not level: continue
            runs[level].append(f'M{int(x)} {y}H{int(end)}V{y+1}H{int(x)}Z');count+=1
    # Preserve original definitions and paint order inside a single masked group.
    original=list(root)
    for element in original: root.remove(element)
    definitions=ET.SubElement(root,f'{{{SVG}}}defs')
    mask=ET.SubElement(definitions,f'{{{SVG}}}mask',{'id':mask_id,'maskUnits':'userSpaceOnUse',
         'maskContentUnits':'userSpaceOnUse','x':'0','y':'0','width':str(width),'height':str(height),
         'style':'mask-type:alpha'})
    for level,paths in sorted(runs.items()):
        ET.SubElement(mask,f'{{{SVG}}}path',{'fill':'white','fill-opacity':format(level/255.,'.10f'),
                      'shape-rendering':'crispEdges','d':' '.join(paths)})
    group=ET.SubElement(root,f'{{{SVG}}}g',{'mask':f'url(#{mask_id})','data-representation':'fidelity-rgb-with-source-alpha'})
    for element in original: group.append(element)
    root.set('viewBox',f'0 0 {width} {height}')
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    ET.ElementTree(root).write(destination,encoding='utf-8',xml_declaration=True)
    return {'alpha_run_count':count,'alpha_level_paths':len(runs),'alpha_geometry_wall_seconds':time.perf_counter()-start,
            'representation':'source-derived equal-alpha horizontal vector runs; no semantic/clean-geometry claim',
            'structure':svg_structure(destination)}
# END CHANGE AGD-CODEX-ALPHA-MASK | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension

# START CHANGE AGD-CODEX-ALPHA-EVALUATE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension
def evaluate_alpha(reference_rgba: Path,svg: Path,folder: Path) -> dict:
    """Measure native alpha and visible fidelity on white, black, and blue-gray."""
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    with Image.open(reference_rgba) as source: reference=source.convert('RGBA')
    timing=render_svg(svg,folder/'render_rgba.png',*reference.size)
    with Image.open(folder/'render_rgba.png') as image: rendered=image.convert('RGBA')
    ref=np.asarray(reference);pred=np.asarray(rendered)
    delta=np.abs(ref[:,:,3].astype(float)-pred[:,:,3].astype(float));metrics={}
    for name,color in (('white',(255,255,255,255)),('black',(0,0,0,255)),('bluegray',(40,80,120,255))):
        background=Image.new('RGBA',reference.size,color)
        a=np.asarray(Image.alpha_composite(background,reference).convert('RGB'))
        b=np.asarray(Image.alpha_composite(background,rendered).convert('RGB'))
        Image.fromarray(a).save(folder/f'reference_{name}.png')
        Image.fromarray(b).save(folder/f'render_{name}.png')
        metrics[name]=compare(a,b)|extra_metrics(a,b)
    report={'status':'EXPERIMENTAL_MEASURED_NOT_OWNER_ACCEPTED','alpha_mae_0_255':float(delta.mean()),
            'alpha_max_error_0_255':float(delta.max()),'alpha_exact_fraction':float(np.mean(delta==0)),
            'background_metrics':metrics,'mean_background_fidelity_score':float(np.mean([fidelity_score(m) for m in metrics.values()])),
            'render':timing,'structure':svg_structure(svg),
            'limits':'Native-resolution 8-bit alpha; no scale-invariance, semantic geometry, or independent application interoperability claim.'}
    (folder/'alpha_evaluation.json').write_text(json.dumps(report,indent=2,allow_nan=False),encoding='utf-8')
    return report
# END CHANGE AGD-CODEX-ALPHA-EVALUATE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension

# START CHANGE AGD-CODEX-ALPHA-PIPELINE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension
def optimize_alpha(source: Path,output: Path,max_candidates: int=13,max_seconds: float=720.) -> dict:
    """Run inherited opaque RGB search, then experimentally preserve source alpha."""
    output=Path(output)
    if output.exists() and any(output.iterdir()): raise FileExistsError('Output must be empty')
    output.mkdir(parents=True,exist_ok=True)
    normalization=prepare_transparent_input(source,output/'input')
    ranking=optimize(output/'input'/'unassociated_rgb.png',output/'rgb_search',max_candidates,max_seconds,'reject')
    report={'normalization':normalization,'status':'EXPERIMENTAL_UNVALIDATED',
            'selection_policy':'Inherited opaque unassociated-RGB score; alpha/background metrics evaluated only after selection.',
            'rgb_search_candidates':ranking['evaluated_candidates']}
    if ranking['ranked']:
        report['mask']=apply_vector_alpha(output/'rgb_search'/'best.svg',output/'input'/'source_alpha.png',output/'best_alpha.svg')
        report['evaluation']=evaluate_alpha(output/'input'/'reference_srgb_rgba.png',output/'best_alpha.svg',output/'evaluation')
        report['status']='EXPERIMENTAL_MEASURED_NOT_OWNER_ACCEPTED'
    (output/'alpha_result.json').write_text(json.dumps(report,indent=2,allow_nan=False),encoding='utf-8')
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--input',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path);parser.add_argument('--max-candidates',type=int,default=13)
    parser.add_argument('--max-seconds',type=float,default=720.);args=parser.parse_args()
    print(json.dumps(optimize_alpha(args.input,args.output,args.max_candidates,args.max_seconds),indent=2))
# END CHANGE AGD-CODEX-ALPHA-PIPELINE | 2026-10-27T10:26:04Z | CREATED | Author: windows_extension
