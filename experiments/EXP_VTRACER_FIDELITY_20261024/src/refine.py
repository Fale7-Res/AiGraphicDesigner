# START CHANGE VTRACER-REFINE | 2026-10-24T14:57:17Z | CREATED | Author: vtracer_engine
"""Fixed pixel geometry: isolate edge rasterization and visible-color estimation."""
from pathlib import Path
import argparse,copy,json,resource,tempfile,time,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
from evaluate import load_rgb,render_svg,compare,svg_structure
from search import extra_metrics,fidelity_score
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)

def inspect_pixel_document(root,config):
    """Restrict ownership refit to supported opaque solid path-only pixel output."""
    if config.get('mode')!='pixel':raise ValueError('Only pixel mode is supported by exact visible-ownership refit')
    paths=list(root)
    if not paths or len(paths)>=2**24-1:raise ValueError('Invalid path count')
    for path in paths:
        if path.tag!=f'{{{NS}}}path' or set(path.attrib)-{'d','fill','fill-rule'}:raise ValueError('Requires simple opaque path-only document')
        if not path.get('fill','').startswith('#') or len(path.get('fill'))!=7:raise ValueError('Requires solid hexadecimal RGB fills')
        if any(c in path.get('d','') for c in 'CcSsQqTtAa'):raise ValueError('Pixel ownership cannot include curves')
    return paths

def ownership_render(root,source_shape,directory):
    """Cross-check two bijective RGB IDs; reject ambiguous/antialiased ownership."""
    h,w=source_shape[:2];n=len(list(root));mod=2**24;prime=104729;inv=pow(prime,-1,mod);maps=[]
    for encoding in [1,prime]:
        trial=copy.deepcopy(root);trial.set('shape-rendering','crispEdges')
        for i,path in enumerate(trial):path.set('fill',f'#{((i+1)*encoding)%mod:06x}')
        with tempfile.TemporaryDirectory() as temp:
            svg=Path(temp)/'ownership.svg';png=Path(temp)/'ownership.png';ET.ElementTree(trial).write(svg,encoding='utf-8',xml_declaration=True);render_svg(svg,png,w,h)
            with Image.open(png) as im:rgba=np.array(im.convert('RGBA'))
        rgb=rgba[:,:,:3].astype(np.int64);encoded=rgb[:,:,0]*65536+rgb[:,:,1]*256+rgb[:,:,2]
        ids=encoded if encoding==1 else encoded*inv%mod
        valid=(rgba[:,:,3]==255)&(ids>=1)&(ids<=n)
        maps.append((ids,valid))
    agreement=maps[0][1]&maps[1][1]&(maps[0][0]==maps[1][0])
    if not agreement.all():raise ValueError(f'Ambiguous or uncovered ownership at {int((~agreement).sum())} pixels')
    np.savez_compressed(directory/'visible_ownership.npz',path_ids=maps[0][0].astype(np.uint32))
    return maps[0][0],{'cross_encoding_agreement_pixels':int(agreement.sum()),'ambiguous_pixels':0,'path_count':n,'id_encoding_multiplier':prime}

def refine(source,base_svg,config,output):
    """Evaluate original, crispEdges control, and visible-support mean color refit."""
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    if (output/'results.json').exists():raise FileExistsError('Use new output directory')
    wall=time.perf_counter();cpu=time.process_time();rgb=load_rgb(source);h,w=rgb.shape[:2]
    root=ET.parse(base_svg).getroot();paths=inspect_pixel_document(root,config);ids,audit=ownership_render(root,rgb.shape,output)
    counts=np.bincount(ids.ravel(),minlength=len(paths)+1);means=np.zeros((len(paths)+1,3))
    for channel in range(3):means[:,channel]=np.bincount(ids.ravel(),weights=rgb[:,:,channel].ravel(),minlength=len(paths)+1)/np.maximum(counts,1)
    results={'config':config,'ownership_audit':audit,'conditions':{},'no_geometry_changes':True,'note':'Source-resolution visible-support least squares on existing shapes; no new geometry. Pixel-grid complexity is inherited and not disguised.'}
    for label in ['original','crisp_control','visible_color_refit']:
        candidate=copy.deepcopy(root)
        if label!='original':candidate.set('shape-rendering','crispEdges')
        if label=='visible_color_refit':
            for i,path in enumerate(candidate):
                if counts[i+1]:path.set('fill','#'+''.join(f'{int(v):02x}' for v in np.rint(means[i+1])))
        svg=output/f'{label}.svg';png=output/f'{label}.png';ET.ElementTree(candidate).write(svg,encoding='utf-8',xml_declaration=True);timing=render_svg(svg,png,w,h)
        with Image.open(png) as im:im.verify()
        pred=load_rgb(png);metrics=compare(rgb,pred)|extra_metrics(rgb,pred);structure=svg_structure(svg)
        results['conditions'][label]={'metrics':metrics,'score':fidelity_score(metrics),'structure':structure,'render':timing}
    results['resources']={'wall_seconds':time.perf_counter()-wall,'parent_cpu_seconds':time.process_time()-cpu,'parent_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,'child_peak_mib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1024}
    results['ownership_audit']['visible_paths']=int(np.sum(counts[1:]>0));results['ownership_audit']['fully_occluded_paths']=int(np.sum(counts[1:]==0))
    (output/'results.json').write_text(json.dumps(results,indent=2));print({k:round(v['metrics']['ssim'],6) for k,v in results['conditions'].items()},flush=True);return results

if __name__=='__main__':
    cli=argparse.ArgumentParser();cli.add_argument('--source',type=Path,required=True);cli.add_argument('--svg',type=Path,required=True);cli.add_argument('--config',type=Path,required=True);cli.add_argument('--output',type=Path,required=True);args=cli.parse_args();refine(args.source,args.svg,json.loads(args.config.read_text()),args.output)

# END CHANGE VTRACER-REFINE | 2026-10-24T14:57:17Z | CREATED | Author: vtracer_engine
