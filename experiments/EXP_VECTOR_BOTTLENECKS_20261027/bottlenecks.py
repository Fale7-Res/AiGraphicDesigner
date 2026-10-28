"""Isolated oracle/coverage/granularity research; no production architecture changes."""
# START CHANGE AGD-BOTTLENECKS-01 | 2026-10-28T03:34:28Z | EDITED | Author: root
from pathlib import Path
import argparse,collections,copy,csv,hashlib,html,json,os,shutil,sys,tempfile,time
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image,ImageDraw
from scipy.ndimage import binary_dilation
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'EXP_GEOMETRY_APPEARANCE_ABLATION_01'
BASE=ROOT.parent/'EXP_CODEX_WINDOWS_FIDELITY_20261027'
sys.path.insert(0,str(OLD))
import run_experiment as inherited
import fit_appearance as appearance
SVG=inherited.SVG;ET.register_namespace('',SVG)

def paths_for_case(case):
    """Check frozen saved sources without modifying any historical experiment."""
    for key in ['source','reference','geometry','ground_truth_svg','previous_result']:
        if key in case and inherited.digest(case[key])!=case[key+'_sha256']:raise ValueError('Frozen hash drift '+case['id']+' '+key)
    return OLD/'results'/case['id']

def visible_geometry(svg,source,folder):
    """Native pixel-center visibility area of RGB micro-paths; masks excluded explicitly."""
    root=ET.parse(svg).getroot();entries=appearance._paths(root);tiny=[];small=[]
    for path,matrix in entries:
        pen=BoundsPen(None);parse_path(path.get('d',''),pen)
        if pen.bounds:
            x0,y0,x1,y1=pen.bounds;w=x1-x0;h=y1-y0
            tiny.append(w<=1.0001 and h<=1.0001);small.append(w<=2.0001 and h<=2.0001)
        else:tiny.append(False);small.append(False)
    diagnostic=copy.deepcopy(root);codes=(np.arange(1,len(entries)+1,dtype=np.int64)*104729)%(2**24)
    for (p,_),code in zip(appearance._paths(diagnostic),codes):
        p.set('fill',f'#{int(code):06x}');p.set('shape-rendering','crispEdges');p.set('stroke','none')
    diagnostic.set('shape-rendering','crispEdges');folder.mkdir(parents=True,exist_ok=True)
    file=folder/'region_ids.svg';ET.ElementTree(diagnostic).write(file,encoding='utf-8',xml_declaration=True)
    with Image.open(source) as image:size=image.size
    inherited.render_svg(file,folder/'region_ids.png',*size)
    image=np.asarray(Image.open(folder/'region_ids.png').convert('RGBA'));rgb=image[:,:,:3].astype(np.int64)
    actual=(rgb[:,:,0]<<16)|(rgb[:,:,1]<<8)|rgb[:,:,2];order=np.argsort(codes);sorted_codes=codes[order]
    position=np.searchsorted(sorted_codes,actual);safe=np.minimum(position,len(codes)-1)
    valid=(position<len(codes))&(sorted_codes[safe]==actual)&(image[:,:,3]==255)
    labels=np.full(actual.shape,-1,dtype=int);labels[valid]=order[safe[valid]]
    weights=np.asarray(Image.open(source).convert('RGBA'))[:,:,3]/255.;known=valid&(weights>0)
    total=float(weights.sum());den=float(weights[known].sum());one=np.zeros_like(known);two=np.zeros_like(known)
    one[known]=np.asarray(tiny)[labels[known]];two[known]=np.asarray(small)[labels[known]]
    areas=np.bincount(labels[known],weights=weights[known],minlength=len(entries))
    boundaries=np.zeros_like(valid)
    boundaries[:,1:]|=labels[:,1:]!=labels[:,:-1];boundaries[1:,:]|=labels[1:,:]!=labels[:-1,:]
    band=binary_dilation(boundaries,iterations=1)
    Image.fromarray(np.uint8(band)*255).save(folder/'boundary_band.png')
    report={'rgb_path_count':len(entries),'paths_bbox_le1':sum(tiny),'paths_bbox_le2':sum(small),
       'visible_alpha_weighted_area_tiny1_fraction':float(weights[one].sum()/den) if den else None,
       'visible_alpha_weighted_area_tiny2_fraction':float(weights[two].sum()/den) if den else None,
       'assigned_visible_alpha_fraction':den/total if total else None,'zero_visible_sample_rgb_paths':int((areas==0).sum()),
       'method':'Native pixel-center unique-ID crispEdges SVG diagnostic; alpha-weighted visible ownership. RGB geometry only, no alpha-mask runs. Not exact continuous vector area or high-resolution contour truth.',
       'visible_sample_area_by_rgb_path':areas.tolist()}
    inherited.save_json(folder/'visible_geometry.json',report);return report,band

def spatial_error_partition(source,render,band):
    """Disjoint spatial error accounting; expressly not causal/additive bottleneck attribution."""
    a=Image.open(source).convert('RGBA');b=Image.open(render).convert('RGBA');back=Image.new('RGBA',a.size,'white')
    x=np.asarray(Image.alpha_composite(back,a).convert('RGB')).astype(float)
    y=np.asarray(Image.alpha_composite(back,b).convert('RGB')).astype(float);sq=((x-y)**2).mean(axis=2)
    return {'boundary_band_pixel_fraction':float(band.mean()),'boundary_band_mse':float(sq[band].mean()) if band.any() else None,
       'interior_mse':float(sq[~band].mean()) if (~band).any() else None,'overall_mse':float(sq.mean()),
       'note':'Boundary band follows reconstructed regions, not object truth. Spatial means can be weighted to overall MSE but are not percentages attributable to causes.'}

def evaluate_and_record(source,svg,folder,band=None):
    row=inherited.evaluate_condition(source,svg,folder)
    if band is not None:row['spatial_error_partition']=spatial_error_partition(source,folder/'render.png',band)
    inherited.save_json(folder/'evaluation.json',row);return row

def run_granularity(case):
    saved=paths_for_case(case);out=ROOT/'results/granularity'/case['id'];out.mkdir(parents=True,exist_ok=True)
    result_path=out/'result.json'
    if result_path.exists():
        result=json.loads(result_path.read_text())
        for level,row in result['levels'].items():
            for name,data in row['conditions'].items():assert inherited.digest(out/level/name/'output.svg')==data['sha256']
        print('REUSE complete',case['id'],flush=True);return
    if (out/'source.png').exists():raise FileExistsError('Partial run preserved; inspect it before resuming')
    shutil.copyfile(case['source'],out/'source.png');Image.open(out/'source.png').convert('RGB').save(out/'rgb.png')
    summary={'id':case['id'],'source_sha256':inherited.digest(out/'source.png'),'levels':{},'architecture':'NOT_APPROVED'}
    old_result=json.loads((saved/'result.json').read_text());summary['reference']=old_result['conditions']['A']
    (out/'A').mkdir();shutil.copyfile(saved/'A/output.svg',out/'A/output.svg');shutil.copyfile(saved/'A/render.png',out/'A/render.png');shutil.copyfile(saved/'A/white.png',out/'A/white.png')
    for detail in [128,192,256]:
        level=out/str(detail);level.mkdir();started=time.perf_counter()
        for name in 'BCD':(level/name).mkdir()
        if detail==128:
            for name in 'BCD':
                for file in ['output.svg','render.png','white.png','black.png','bluegray.png']:
                    shutil.copyfile(saved/name/file,level/name/file)
            for file in ['fitting.json']:
                shutil.copyfile(saved/file,level/file)
            raw=saved/'B/rgb_unmasked.svg' if (saved/'B/rgb_unmasked.svg').exists() else saved/'B/output.svg'
            conditions=copy.deepcopy(old_result['conditions']);conditions.pop('A');reused=True
        else:
            config=inherited.pilots()[8]|{'watershed_detail':detail}
            trace=inherited.run_trial(out/'rgb.png',level/'trace',config)
            if trace['status']!='ok':raise RuntimeError(trace)
            raw=level/'trace/output.svg';shutil.copyfile(raw,level/'B/output.svg')
            appearance.fit_svg(out/'source.png',raw,level/'C/output.svg',level/'D/output.svg',level/'fitting.json',deadline_seconds=180)
            alpha=Image.open(out/'source.png').convert('RGBA').getchannel('A')
            if alpha.getextrema()!=(255,255):
                alpha.save(out/'source_alpha.png')
                for name in 'BCD':
                    shutil.move(str(level/name/'output.svg'),str(level/name/'rgb_unmasked.svg'))
                    inherited.apply_vector_alpha(level/name/'rgb_unmasked.svg',out/'source_alpha.png',level/name/'output.svg')
            conditions={name:evaluate_and_record(out/'source.png',level/name/'output.svg',level/name) for name in 'BCD'};reused=False
        visible,band=visible_geometry(raw,out/'source.png',level/'geometry')
        for name,row in conditions.items():row['spatial_error_partition']=spatial_error_partition(out/'source.png',level/name/'render.png',band)
        # Identical paths, transforms, masks; compare against source as well as between fits.
        from test_artifacts import geometry_tree
        trees=[geometry_tree(ET.parse(level/name/'output.svg').getroot()) for name in 'BCD']
        assert trees[0]==trees[1]==trees[2]
        if case['known_vector']:
            shutil.copyfile(out/'source.png',level/'source.png')
            inherited.known_control_geometry(case,level)
        summary['levels'][str(detail)]={'conditions':conditions,'visible_geometry':visible,'reused_saved_fit':reused,'current_wall_seconds':time.perf_counter()-started}
        print('LEVEL',case['id'],detail,'paths',conditions['D']['geometry']['rgb_paths'],'SSIM',conditions['D']['metrics']['white']['ssim'],'visiblemicro2',visible['visible_alpha_weighted_area_tiny2_fraction'],flush=True)
    # Contextual historical spline: different segmentation/hierarchy, not a controlled granularity condition.
    historical=(BASE/'results/A01_shield') if case['id']=='A01_shield' else ROOT.parent/'EXP_CODEX_GENERALIZATION_20261027/results'/case['id']/'baseline_search'
    if os.environ.get('AGD_INCLUDE_HISTORICAL_CONTEXT')=='1' and (historical/'ranking.json').exists():
        ranked=json.loads((historical/'ranking.json').read_text())['ranked'];splines=[x for x in ranked if x['config'].get('mode')=='spline']
        if splines:
            best=max(splines,key=lambda x:x['metrics']['ssim']);folder=out/'historical_spline';folder.mkdir();raw=historical/best['trial']/'output.svg';target=folder/'output.svg'
            alpha=Image.open(out/'source.png').convert('RGBA').getchannel('A')
            if alpha.getextrema()!=(255,255):alpha.save(out/'source_alpha.png');inherited.apply_vector_alpha(raw,out/'source_alpha.png',target)
            else:shutil.copyfile(raw,target)
            summary['historical_context']={'source':str(raw),'source_sha256':inherited.digest(raw),'config':best['config'],'evaluation':evaluate_and_record(out/'source.png',target,folder),'limits':'Selected from previously saved spline candidates by stored SSIM; different segmentation/hierarchy, inherited appearance, not a controlled detail comparison.'}
    inherited.save_json(result_path,summary)

def comparisons():
    """Every granularity and worst residual shown; no favorable case filtering."""
    cards=[];rows=[]
    for file in sorted((ROOT/'results/granularity').glob('*/result.json')):
        result=json.loads(file.read_text());folder=file.parent;source=Image.open(folder/'source.png').convert('RGBA');w,h=source.size
        white=Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')
        variants=[('source',white,None),('A pixel',Image.open(folder/'A/white.png').convert('RGB'),folder/'A/output.svg')]
        variants.append(('old D128',Image.open(folder/'128/D/white.png').convert('RGB'),folder/'128/D/output.svg'))
        if 'evaluation' in result.get('historical_context',{}):variants.append(('historical spline',Image.open(folder/'historical_spline/white.png').convert('RGB'),folder/'historical_spline/output.svg'))
        for detail in ['192','256']:variants.append(('D'+detail,Image.open(folder/detail/'D/white.png').convert('RGB'),folder/detail/'D/output.svg'))
        for detail,row in result['levels'].items():
            for condition,v in row['conditions'].items():rows.append({'case':result['id'],'detail':detail,'condition':condition,'ssim':v['metrics']['white']['ssim'],'psnr_db':v['metrics']['white']['psnr_db'],'mse':v['metrics']['white']['mse'],'worst_tile_rmse':v['metrics']['white']['worst_32px_tile_rmse'],'paths':v['geometry']['rgb_paths'],'cubics':v['geometry']['cubic_segments'],'micro2_visible_fraction':row['visible_geometry']['visible_alpha_weighted_area_tiny2_fraction'],'alpha_mae':v['alpha_mae']})
        # Add explicit corrected candidate only when this independent intervention is available.
        correction=ROOT/'results/corrections'/result['id']
        if (correction/'result.json').exists():variants.append(('D192 stroke.25',Image.open(correction/'white.png').convert('RGB'),correction/'output.svg'))
        canvas=Image.new('RGB',(w*len(variants),h+28),'#20262f');draw=ImageDraw.Draw(canvas)
        error=Image.new('RGB',(w*(len(variants)-1),h+28),'#20262f');ed=ImageDraw.Draw(error)
        for i,(name,im,svg) in enumerate(variants):
            draw.text((i*w+3,5),name,fill='white');canvas.paste(im,(i*w,28))
            if i:
                heat=np.uint8(np.clip(np.abs(np.asarray(white).astype(float)-np.asarray(im).astype(float))*6,0,255));error.paste(Image.fromarray(heat),((i-1)*w,28));ed.text(((i-1)*w+3,5),name+' error x6',fill='white')
        canvas.save(folder/'comparison.png');error.save(folder/'errors.png')
        sq=((np.asarray(white).astype(float)-np.asarray(variants[-1][1]).astype(float))**2).mean(axis=2)
        _,x,y=max((float(sq[y:y+24,x:x+24].mean()),x,y) for y in range(0,h-23,24) for x in range(0,w-23,24))
        zooms=[]
        for scale in [4,16]:
            sheet=Image.new('RGB',(24*scale*len(variants),24*scale+24),'#20262f');sd=ImageDraw.Draw(sheet)
            for i,(name,im,svg) in enumerate(variants):
                if svg:
                    with tempfile.TemporaryDirectory() as tmp:
                        target=Path(tmp)/'zoom.svg';perf=inherited.crop_svg(svg,target,(x,y,24,24),scale);image=Image.open(target.with_suffix('.png')).convert('RGBA');image=Image.alpha_composite(Image.new('RGBA',image.size,'white'),image).convert('RGB')
                    zooms.append({'label':name,'scale':scale,'box':[x,y,24,24],'render':perf})
                else:image=white.crop((x,y,x+24,y+24)).resize((24*scale,24*scale),Image.Resampling.NEAREST)
                sheet.paste(image,(i*24*scale,24));sd.text((i*24*scale+2,4),name,fill='white')
            sheet.save(folder/f'worst_{scale}x.png')
        inherited.save_json(folder/'zoom_measurements.json',zooms)
        relative=folder.relative_to(ROOT).as_posix();cards.append(f'<section id="{result["id"]}"><h2>{result["id"]}</h2><p>All fixed granularities shown. Historical spline is contextual, with different clustering/hierarchy and inherited appearance. The final column is a reversible D192 stroke correction when present; it changes coverage and overlaps, not the fitted region geometry.</p>')
        for name in ['comparison.png','errors.png','worst_4x.png','worst_16x.png']:cards.append(f'<figure><img loading="lazy" src="{relative}/{name}"></figure>')
        cards.append('<p>'+' | '.join(f'<a href="{svg.relative_to(ROOT).as_posix()}">{name} SVG</a>' for name,im,svg in variants if svg)+f' | <a href="{relative}/result.json">full metrics</a></p></section>')
    oracle='<p><a href="results/oracle/index.html">Geometry oracle comparisons</a> | <a href="results/coverage/index.html">Coverage diagnostics</a></p><p><strong>Important negative controls:</strong> <a href="#K02_radial_shared_curves">radial control</a> worsens from SSIM0.9135 at128 to0.7645 at256; <a href="#G06_arabic">Arabic</a> D192 stroke raises SSIM slightly while worsening MSE. Neither higher detail nor global strokes are accepted solutions.</p>'
    (ROOT/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Vector reconstruction bottlenecks</title><style>body{font:16px system-ui;background:#17202a;color:#eee;margin:24px}a{color:#8df}section{border-top:2px solid #678;margin:40px 0}figure{overflow:auto;margin:12px 0}img{max-width:none}</style><h1>Vector bottlenecks — bounded research</h1><p>Architecture NOT_APPROVED. Native scores and visual quality are separate from geometric validity. Source crops are nearest-neighbor displays, not high-resolution contour ground truth. All input cases and failed corrections are retained.</p>'+oracle+''.join(cards),encoding='utf-8')
    inherited.save_json(ROOT/'reports/granularity_metrics.json',rows)
    with (ROOT/'reports/granularity_metrics.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--case');parser.add_argument('--dashboard',action='store_true');a=parser.parse_args()
    manifest=json.loads((ROOT/'inputs/manifest.json').read_text())
    if a.case:run_granularity(next(c for c in manifest['cases'] if c['id']==a.case))
    elif a.dashboard:comparisons()
    else:
        from safe_monitor import monitor
        failures=[]
        for c in manifest['cases']:
            if (ROOT/'results/granularity'/c['id']/'result.json').exists():run_granularity(c);continue
            stats=monitor([sys.executable,str(Path(__file__).resolve()),'--case',c['id']],ROOT/'reports'/f'{c["id"]}.log',900,4096)
            inherited.save_json(ROOT/'reports'/f'{c["id"]}_resources.json',stats)
            print(c['id'],'exit',stats['returncode'],'seconds',round(stats['wall_seconds'],1),'MiB',round(stats['sampled_tree_peak_mib'],1),flush=True)
            if stats['returncode'] or stats['termination_reason']:failures.append(c['id'])
        if failures:raise SystemExit('Failedcasespreserved '+','.join(failures))
# END CHANGE AGD-BOTTLENECKS-01 | 2026-10-28T03:34:28Z | EDITED | Author: root
