"""Separate rasterizer coverage seams from geometry holes; reversible stroke diagnostic."""
# START CHANGE AGD-COVERAGE-01 | 2026-10-27T20:38:55Z | EDITED | Author: package_generalization
from pathlib import Path
import argparse,copy,importlib.util,json,os,sys,time,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image,ImageDraw
from scipy.ndimage import distance_transform_edt,binary_erosion
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path

REPO=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
ROOT=Path(os.environ.get('AGD_COVERAGE_ROOT',REPO/'experiments/EXP_VECTOR_BOTTLENECKS_20261027'))
OLD=REPO/'experiments/EXP_GEOMETRY_APPEARANCE_ABLATION_01'
sys.path.insert(0,str(OLD))
import run_experiment as inherited
SVG=inherited.SVG
os.environ.setdefault('AGD_RENDERER','resvg')
os.environ.setdefault('AGD_RENDERER_EXE',str(Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\resvg\resvg.exe')))

def rgb_paths(root):
    """Exclude all geometry inside defs, masks and clipping constructions."""
    result=[]
    def visit(node,excluded=False):
        excluded=excluded or node.tag.rsplit('}',1)[-1] in ('defs','mask','clipPath','pattern')
        if node.tag.rsplit('}',1)[-1]=='path' and not excluded:result.append(node)
        for child in node:visit(child,excluded)
    visit(root);return result

def correct_coverage(input_svg,output_svg,width=.25):
    """Add narrow matching-paint strokes without altering d, order, topology or masks.

    This is an explicitly overlapping coverage correction, not a geometry/topology
    repair. Stroke extends the exterior by width/2 and may harm fine details.
    """
    if not 0<width<=.5:raise ValueError('Bounded diagnostic stroke width must be (0,.5] source pixels')
    root=ET.parse(input_svg).getroot();changed=0
    for path in rgb_paths(root):
        fill=path.get('fill')
        if fill is None or fill=='none':continue
        if path.get('stroke') not in (None,'none'):raise ValueError('Preserve input existing strokes; unsupported here')
        path.set('stroke',fill);path.set('stroke-width',str(width));path.set('stroke-linejoin','round')
        path.set('stroke-linecap','round');path.set('paint-order','stroke fill');changed+=1
    output_svg=Path(output_svg);output_svg.parent.mkdir(parents=True,exist_ok=True)
    ET.ElementTree(root).write(output_svg,encoding='utf-8',xml_declaration=True)
    return {'changed_rgb_paths':changed,'width_source_px':width,'exterior_max_nominal_offset_px':width/2,
       'method':'matching-fill narrow stroke, round joins, stroke-before-fill; overlap correction only, not topology repair'}

def write_svg(path,root):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    ET.ElementTree(root).write(path,encoding='utf-8',xml_declaration=True)

def render_alpha(svg,png,scale=1):
    root=ET.parse(svg).getroot();w=int(float(root.get('width').removesuffix('px')));h=int(float(root.get('height').removesuffix('px')))
    performance=inherited.render_svg(Path(svg),Path(png),w*scale,h*scale)
    return np.asarray(Image.open(png).convert('RGBA'))[:,:,3],performance

def coverage_versions(svg,folder):
    """Paint each region white; compound fill is a winding diagnostic, NOT Boolean union.

    Nonzero compound may cancel oppositely wound overlapping paths. Hole winding
    and fill-rule assumptions are disclosed; only analytic known-union controls
    establish ground-truth union. Real-image compound results remain conditional.
    """
    root=ET.parse(svg).getroot();paths=rgb_paths(root)
    # Preserve RGB parent transforms; remove masks to isolate color-region support.
    for node in root.iter():
        node.attrib.pop('mask',None)
    for p in paths:
        p.set('fill','white');p.attrib.pop('fill-opacity',None);p.attrib.pop('opacity',None)
    separate=folder/'white_separate.svg';write_svg(separate,root)
    crisp=copy.deepcopy(root)
    for p in rgb_paths(crisp):p.set('shape-rendering','crispEdges')
    write_svg(folder/'white_crisp.svg',crisp)
    # Flatten translate-only VTracer geometry to one global nonzero compound.
    pen=SVGPathPen(None);unsupported=[];rules=[]
    import re
    for p in paths:
        rules.append(p.get('fill-rule','nonzero'));transform=p.get('transform','')
        match=re.fullmatch(r'\s*translate\(\s*([-\d.eE]+)[ ,]+([-\d.eE]+)\s*\)\s*',transform)
        if transform and not match:unsupported.append(transform);continue
        dx,dy=map(float,match.groups()) if match else (0,0)
        parse_path(p.get('d',''),TransformPen(pen,(1,0,0,1,dx,dy)))
    for group in root.iter(f'{{{SVG}}}g'):
        if group.get('transform'):unsupported.append('ancestor '+group.get('transform'))
    compound=ET.Element(f'{{{SVG}}}svg',{k:v for k,v in root.attrib.items() if k in ('width','height','viewBox')})
    ET.SubElement(compound,f'{{{SVG}}}path',{'d':pen.getCommands(),'fill':'white','fill-rule':'nonzero'})
    write_svg(folder/'white_compound_nonzero.svg',compound)
    return {'rgb_paths':len(paths),'unsupported_transforms':unsupported,'fill_rules':dict((r,rules.count(r)) for r in set(rules)),
      'compound_is_boolean_union':False,'compound_limits':'diagnostic only: nonzero winding can cancel overlapping opposite orientations; evenodd per-region holes not converted; no geometry-gap proof from this comparison alone'}

def alpha_summary(separate,reference,scale=1):
    """Measure coverage loss in reference-opaque interiors and exterior changes."""
    interior=reference==255;support=reference>=128
    deficit=np.maximum(reference.astype(float)-separate.astype(float),0)
    extra=np.maximum(separate.astype(float)-reference.astype(float),0)
    missing=interior&(separate<255);locations=np.argwhere(missing)
    dist=distance_transform_edt(missing)/scale
    return {'opaque_reference_pixels':int(interior.sum()),'interior_alpha_deficit_pixels':int(missing.sum()),
      'interior_fully_uncovered_pixels':int((interior&(separate==0)).sum()),
      'coverage_deficit_source_pixel_equivalents':float(deficit.sum()/255/scale**2),
      'coverage_excess_source_pixel_equivalents':float(extra.sum()/255/scale**2),
      'threshold128_support_lost_samples':int((support&(separate<128)).sum()),
      'threshold128_support_gained_samples':int((~support&(separate>=128)).sum()),
      'maximum_missing_run_radius_source_px':float(dist.max()),
      'first_deficit_locations_xy_source_px':[[float(x/scale),float(y/scale)] for y,x in locations[:32]]}

def save_alpha_heat(alpha,reference,path):
    deficit=np.maximum(reference.astype(float)-alpha.astype(float),0)
    excess=np.maximum(alpha.astype(float)-reference.astype(float),0)
    heat=np.zeros((*alpha.shape,3),dtype=np.uint8);heat[:,:,0]=np.minimum(deficit*4,255);heat[:,:,2]=np.minimum(excess*4,255)
    Image.fromarray(heat).save(path)

def run_exact_controls():
    """Two exact known partitions, plus a real-gap negative and exterior-stroke control."""
    folder=ROOT/'results/coverage/controls'
    if folder.exists() and any(folder.iterdir()):raise FileExistsError('Preserve completed/partial controls; regenerate using fresh AGD_COVERAGE_ROOT')
    folder.mkdir(parents=True,exist_ok=True);results={}
    # Both partitions cover the exact same 112x112 square; reverse shared boundaries.
    fixtures={
      'diagonal': ['M8 8H120V120Z','M8 8L120 120H8Z'],
      'curved': ['M8 8H64C110 40 18 88 64 120H8Z','M64 8H120V120H64C18 88 110 40 64 8Z'],
      'genuine_gap': ['M8 8H63.5V120H8Z','M64.5 8H120V120H64.5Z']}
    for name,paths in fixtures.items():
        out=folder/name;out.mkdir(exist_ok=True)
        root=ET.Element(f'{{{SVG}}}svg',{'width':'128','height':'128','viewBox':'0 0 128 128'})
        for i,d in enumerate(paths):ET.SubElement(root,f'{{{SVG}}}path',{'d':d,'fill':('#d94325','#2478ca')[i]})
        write_svg(out/'region_ids.svg',root);coverage_versions(out/'region_ids.svg',out)
        union=ET.Element(f'{{{SVG}}}svg',dict(root.attrib));ET.SubElement(union,f'{{{SVG}}}path',{'fill':'white','d':'M8 8H120V120H8Z'})
        write_svg(out/'known_union.svg',union)
        correct_coverage(out/'white_separate.svg',out/'white_stroke025.svg')
        correct_coverage(out/'region_ids.svg',out/'region_ids_stroke025.svg')
        values={};times={}
        for scale in (1,4,16):
            reference,perf=render_alpha(out/'known_union.svg',out/f'known_union_{scale}x.png',scale);times[f'union_{scale}']=perf
            for label,file in [('separate','white_separate'),('compound','white_compound_nonzero'),('crisp','white_crisp'),('stroke025','white_stroke025')]:
                alpha,perf=render_alpha(out/f'{file}.svg',out/f'{file}_{scale}x.png',scale)
                values[f'{label}_{scale}x']=alpha_summary(alpha,reference,scale);times[f'{label}_{scale}x']=perf
                save_alpha_heat(alpha,reference,out/f'{file}_alpha_error_{scale}x.png')
            inherited.render_svg(out/'region_ids.svg',out/f'region_ids_{scale}x.png',128*scale,128*scale)
            inherited.render_svg(out/'region_ids_stroke025.svg',out/f'region_ids_stroke025_{scale}x.png',128*scale,128*scale)
        results[name]={'coverage':values,'render_performance':times,'known_geometry_gap':name=='genuine_gap',
          'interpretation':'Exact shared boundaries for diagonal/curved; genuine_gap deliberately leaves 1 source-pixel strip. Stroke can conceal coverage deficits but changes exterior; it does not establish topology repair.'}
    # Single curved silhouette isolates damage from applying strokes to exterior edges.
    out=folder/'exterior';out.mkdir(exist_ok=True)
    circle=ET.Element(f'{{{SVG}}}svg',{'width':'128','height':'128','viewBox':'0 0 128 128'})
    ET.SubElement(circle,f'{{{SVG}}}path',{'fill':'white','d':'M104 64C104 86.0914 86.0914 104 64 104C41.9086 104 24 86.0914 24 64C24 41.9086 41.9086 24 64 24C86.0914 24 104 41.9086 104 64Z'})
    write_svg(out/'original.svg',circle);correct_coverage(out/'original.svg',out/'stroke025.svg')
    values={}
    for scale in (1,4,16):
        a,_=render_alpha(out/'original.svg',out/f'original_{scale}x.png',scale);b,_=render_alpha(out/'stroke025.svg',out/f'stroke025_{scale}x.png',scale)
        values[f'{scale}x']=alpha_summary(b,a,scale)
    results['exterior']={'coverage':values,'interpretation':'Unmodified single silhouette ground truth: stroke expansion is an unwanted appearance/silhouette change, not a shared-edge correction.'}
    inherited.save_json(folder/'results.json',results);build_coverage_index();return results

def sampled_region_coverage(svg,folder,scale=4,max_regions=128):
    """Independent per-region thresholded alpha occupancy; samples, not analytic topology.

    Uses exact source paths, each rendered separately. At shared boundaries AA >=128
    can classify both sides; observed overlap is NOT automatically geometric overlap.
    """
    root=ET.parse(svg).getroot();paths=rgb_paths(root)
    if len(paths)>max_regions:return {'status':'SKIPPED_BOUNDED_REGION_LIMIT','regions':len(paths),'limit':max_regions}
    counts=None
    for i,path in enumerate(paths):
        isolated=ET.Element(f'{{{SVG}}}svg',{k:v for k,v in root.attrib.items() if k in ('width','height','viewBox')})
        item=copy.deepcopy(path);item.set('fill','white');item.attrib.pop('fill-opacity',None);item.attrib.pop('opacity',None);isolated.append(item)
        target=folder/f'region_{i:03d}.svg';write_svg(target,isolated)
        alpha,_=render_alpha(target,target.with_suffix('.png'),scale)
        if counts is None:counts=np.zeros(alpha.shape,dtype=np.uint16)
        counts+=alpha>=128
    Image.fromarray(np.minimum(counts,255).astype('uint8')).save(folder/'region_count_4x.png')
    return {'status':'SAMPLED','regions':len(paths),'scale':scale,'samples_zero':int((counts==0).sum()),
      'samples_one':int((counts==1).sum()),'samples_multiple':int((counts>1).sum()),'maximum_occupancy':int(counts.max()),
      'limits':'AA threshold128 samples, not exact point-in-curve or analytic intersections; viewport exterior counts included; may report AA boundary ties as overlap'}

def run_real_cases():
    results={}
    for case in ['A01_shield','G01_coffee','G05_chelsea_nativecrop','G06_arabic','G08_dice_alpha']:
        old=OLD/'results'/case;source=old/'D/rgb_unmasked.svg'
        if not source.exists():source=old/'D/output.svg'
        out=ROOT/'results/coverage'/case
        if out.exists() and any(out.iterdir()):raise FileExistsError('Preserve completed/partial coverage case; regenerate using fresh AGD_COVERAGE_ROOT')
        out.mkdir(parents=True,exist_ok=True)
        audit=coverage_versions(source,out);alphas={};performance={};values={}
        for scale in (1,4):
            compound,perf=render_alpha(out/'white_compound_nonzero.svg',out/f'white_compound_{scale}x.png',scale);performance[f'compound_{scale}x']=perf
            for name in ('white_separate','white_crisp'):
                alpha,perf=render_alpha(out/f'{name}.svg',out/f'{name}_{scale}x.png',scale);performance[f'{name}_{scale}x']=perf
                values[f'{name}_vs_compound_{scale}x']=alpha_summary(alpha,compound,scale);save_alpha_heat(alpha,compound,out/f'{name}_deficit_{scale}x.png')
        correction=correct_coverage(old/'D/output.svg',out/'corrected.svg')
        corrected=inherited.evaluate_condition(old/'source.png',out/'corrected.svg',out/'corrected')
        previous=json.loads((old/'result.json').read_text())['conditions']['D']
        unmasked=correct_coverage(source,out/'corrected_unmasked.svg')
        original_alpha=np.asarray(Image.open(old/'source.png').convert('RGBA'))[:,:,3]
        unmasked_alpha,perf=render_alpha(out/'corrected_unmasked.svg',out/'corrected_unmasked.png');performance['corrected_unmasked']=perf
        separate_alpha=np.asarray(Image.open(out/'white_separate_1x.png').convert('RGBA'))[:,:,3]
        nontransparent=original_alpha==255
        corrected['metrics_delta_vs_D']={bg:{key:corrected['metrics'][bg][key]-previous['metrics'][bg][key] for key in ('ssim','mse','worst_32px_tile_rmse')} for bg in ('white','black','bluegray')}
        result={'case':case,'source_svg':str(source),'source_sha256':inherited.digest(source),'white_geometry_audit':audit,
          'coverage_vs_compound':values,'unmasked_alpha_original_opaque_samples':int(nontransparent.sum()),
          'unmasked_alpha_deficit_on_original_opaque_samples':int((nontransparent&(separate_alpha<255)).sum()),
          'per_region_4x':sampled_region_coverage(out/'white_separate.svg',out/'regions4x'),
          'correction':correction,'corrected_evaluation':corrected,'render_performance':performance,
          'interpretation':'Compound diagnostic is not a Boolean union. Separately rendered white regions show actual source-over AA coverage; analytic controls establish that exact shared geometry can still produce AA seams. Stroke correction overlaps regions and can change exterior; does not certify topology.'}
        inherited.save_json(out/'results.json',result);results[case]=result
        print('COVERAGE',case,audit['rgb_paths'],result['coverage_vs_compound']['white_separate_vs_compound_1x']['interior_alpha_deficit_pixels'],corrected['metrics_delta_vs_D']['white'],flush=True)
    finalize_real_visuals(results)
    inherited.save_json(ROOT/'results/coverage/real_results.json',results);build_coverage_index();return results

def finalize_real_visuals(results):
    """Export actual region IDs and 4x vector renders, retaining expansion negatives."""
    summary={}
    for name,row in results.items():
        out=ROOT/'results/coverage'/name;old=OLD/'results'/name
        root=ET.parse(out/'white_separate.svg').getroot()
        for i,p in enumerate(rgb_paths(root)):
            p.set('fill',f'#{(i*79+43)%256:02x}{(i*113+97)%256:02x}{(i*157+193)%256:02x}')
        write_svg(out/'region_ids.svg',root);render_alpha(out/'region_ids.svg',out/'region_ids_4x.png',4)
        a,perf=render_alpha(old/'D/output.svg',out/'original_D_4x.png',4)
        b,perf2=render_alpha(out/'corrected.svg',out/'corrected_4x.png',4)
        row['correction_vs_original_D_alpha_4x']=alpha_summary(b,a,4)
        row['render_performance']['original_D_4x']=perf;row['render_performance']['corrected_4x']=perf2
        save_alpha_heat(b,a,out/'stroke_alpha_change_4x.png')
        ims=[Image.open(old/'source.png').convert('RGBA'),Image.open(old/'D/render.png').convert('RGBA'),Image.open(out/'corrected/render.png').convert('RGBA')]
        w,h=ims[0].size;board=Image.new('RGB',(3*max(w,250),h+50),'white');draw=ImageDraw.Draw(board)
        for i,(label,im) in enumerate(zip(('Prepared source','Original D128','Matching-paint .25px stroke'),ims)):
            draw.text((i*max(w,250)+5,8),label,fill='black');board.paste(Image.alpha_composite(Image.new('RGBA',im.size,'white'),im).convert('RGB'),(i*max(w,250),35))
        board.save(out/'correction_comparison.png');inherited.save_json(out/'results.json',row)
        previous=json.loads((old/'result.json').read_text())['conditions']['D']
        summary[name]={'paths':row['white_geometry_audit']['rgb_paths'],
           'native_white_alpha_deficit_pixels_vs_compound':row['coverage_vs_compound']['white_separate_vs_compound_1x']['interior_alpha_deficit_pixels'],
           'per_region_4x':row['per_region_4x'],'correction_white':row['corrected_evaluation']['metrics_delta_vs_D']['white'],
           'corrected_alpha_mae':row['corrected_evaluation']['alpha_mae'],'original_alpha_mae':previous['alpha_mae'],
           'corrected_vs_original_D_alpha_4x':row['correction_vs_original_D_alpha_4x']}
    inherited.save_json(ROOT/'results/coverage/summary.json',summary)

def build_coverage_index():
    """Small self-contained overview; preserve real failures as prominently as gains."""
    base=ROOT/'results/coverage';parts=['<!doctype html><meta charset="utf-8"><title>Coverage diagnostics</title><style>body{font:16px system-ui;margin:24px}img{max-width:100%}section{border-top:1px solid #777;padding:16px}a{margin-right:14px}</style><h1>Coverage diagnostics — architecture NOT_APPROVED</h1><p>Exact shared-boundary controls distinguish source-over antialiasing from true holes. Compound fill is NOT general Boolean union. Matching-paint .25px strokes create overlap and can change exterior/detail; they are not topology repair. Real cases here use previous D128. Parent D192 correction is a separate comparison.</p>']
    for name in ('diagonal','curved','genuine_gap','exterior'):
        folder=base/'controls'/name
        if not folder.exists():continue
        parts.append(f'<section><h2>Control: {name}</h2><a href="controls/results.json">Metrics</a>')
        for image in sorted(folder.glob('*4x.png'))+sorted(folder.glob('*16x.png')):
            if 'alpha_error' in image.name:continue
            relative=image.relative_to(base).as_posix();parts.append(f'<details><summary>{image.name}</summary><a href="{relative}">Full PNG</a><img loading="lazy" src="{relative}"></details>')
        parts.append('</section>')
    for path in sorted(base.glob('*/results.json')):
        row=json.loads(path.read_text())
        if 'case' not in row:continue
        name=row['case'];delta=row['corrected_evaluation']['metrics_delta_vs_D']['white']
        parts.append(f'<section><h2>{name}</h2><p>White SSIM delta {delta["ssim"]:+.9f}; MSE delta {delta["mse"]:+.6f}; worst-tile RMSE delta {delta["worst_32px_tile_rmse"]:+.6f}.</p><a href="{name}/results.json">Metrics</a><a href="{name}/corrected.svg">Actual corrected SVG</a><img loading="lazy" src="{name}/correction_comparison.png">')
        for image in ('region_ids_4x.png','white_separate_deficit_4x.png','white_crisp_deficit_4x.png','original_D_4x.png','corrected_4x.png','stroke_alpha_change_4x.png'):
            parts.append(f'<details><summary>{image}</summary><a href="{name}/{image}">Full PNG</a><img loading="lazy" src="{name}/{image}"></details>')
        parts.append('</section>')
    (base/'index.html').write_text(''.join(parts),encoding='utf-8')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--controls',action='store_true');parser.add_argument('--real',action='store_true');args=parser.parse_args()
    if args.controls:
        data=run_exact_controls();print(json.dumps({k:{s:v for s,v in r['coverage'].items() if s.endswith('1x')} for k,r in data.items()},indent=2))
    if args.real:run_real_cases()
# END CHANGE AGD-COVERAGE-01 | 2026-10-27T20:38:55Z | EDITED | Author: package_generalization
