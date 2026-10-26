"""Bounded VTracer configuration search with native SVG fidelity evaluation."""
# START CHANGE VTRACER-SEARCH | 2026-10-24T09:56:03Z | CREATED | Author: vtracer_engine
from pathlib import Path
import argparse,hashlib,io,json,math,os,resource,shutil,subprocess,sys,time
import numpy as np
from PIL import Image,ImageCms
from scipy.ndimage import gaussian_filter
from skimage.color import rgb2lab
from evaluate import compare,load_rgb,render_svg,svg_structure

OWNER={'clustering':'color-cluster','color_precision':8,'layer_difference':0,
       'hierarchical':'stacked','filter_speckle':0,'mode':'spline','simplify':1.5,
       'path_precision':0,'optimize':1,'corner_threshold':60,'length_threshold':4.,
       'max_iterations':10,'splice_threshold':45}

def prepare_input(source,destination):
    """Normalize declared ICC to sRGB and explicitly composite alpha on white."""
    source=Path(source);destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    with Image.open(source) as im:
        im.load();info={'original_mode':im.mode,'original_dimensions':list(im.size),'icc_present':bool(im.info.get('icc_profile')),'original_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'alpha_policy':'composite onto opaque sRGB white; transparent SVG fidelity is not tested'}
        alpha=im.convert('RGBA').getchannel('A');rgb=im.convert('RGB')
        if im.info.get('icc_profile'):
            profile=ImageCms.ImageCmsProfile(io.BytesIO(im.info['icc_profile']))
            rgb=ImageCms.profileToProfile(rgb,profile,ImageCms.createProfile('sRGB'),outputMode='RGB')
            info['color_policy']='embedded profile transformed to sRGB with Pillow LittleCMS'
        else:info['color_policy']='untagged RGB assumed sRGB; no inferred gamma conversion'
        info['alpha_extrema']=list(alpha.getextrema());rgba=rgb.convert('RGBA');rgba.putalpha(alpha)
        normalized=Image.alpha_composite(Image.new('RGBA',im.size,'white'),rgba).convert('RGB');normalized.save(destination)
    return info

def extra_metrics(source,pred):
    """Color and high-frequency diagnostics, complementing SSIM/PSNR/edge metrics."""
    de=np.linalg.norm(rgb2lab(source/255.)-rgb2lab(pred/255.),axis=2)
    residual=source.astype(float)-pred.astype(float);high=residual-gaussian_filter(residual,(1.,1.,0))
    return {'delta_e76_mean':float(de.mean()),'delta_e76_p95':float(np.percentile(de,95)),
            'highpass_rmse_sigma1':float(np.sqrt(np.mean(high**2)))}

def fidelity_score(metrics):
    """Fixed multi-metric score, no geometry/size/runtime penalty; not perceptual truth."""
    psnr=60. if metrics.get('identical') else (metrics.get('psnr_db') or 0.)
    edge=metrics.get('edge_f1_1_5px')
    # Empty edge maps: do not invent agreement; reallocate this term to SSIM.
    edge=metrics['ssim'] if edge is None else edge
    return float(.40*metrics['ssim']+.15*min(psnr/60.,1.)+.20*edge+
                 .15*math.exp(-metrics['delta_e76_mean']/12.)+
                 .10*math.exp(-metrics['highpass_rmse_sigma1']/20.))

def pilot_configs():
    """Diverse, fixed thirteen pilots, including the owner's exact mapped settings."""
    changes=[{}, {'path_precision':3}, {'path_precision':3,'simplify':None},
      {'path_precision':3,'simplify':.5},
      {'hierarchical':'cutout','path_precision':3,'simplify':None},
      {'hierarchical':'cutout'}, {'mode':'polygon','path_precision':3,'simplify':None},
      {'mode':'pixel','path_precision':0,'simplify':None},
      {'color_precision':6,'layer_difference':16,'path_precision':3,'simplify':None},
      {'layer_difference':8,'path_precision':3,'simplify':None},
      {'clustering':'watershed','hierarchical':'cutout','watershed_detail':128,'path_precision':3,'simplify':None},
      {'clustering':'watershed','hierarchical':'cutout','watershed_detail':256,'path_precision':3,'simplify':None},
      {'clustering':'bw','hierarchical':'stacked','path_precision':3,'simplify':None}]
    return [OWNER|change for change in changes]

def refined_configs(best):
    """Four local one-coordinate probes around pilot winner; no unbounded search."""
    return [best|{'path_precision':p} for p in [1,5]]+[
            best|{'simplify':.25 if best['simplify']!=.25 else .75},
            best|{'optimize':0}]

def run_trial(source,folder,config):
    """Run one isolated worker; preserve even failed parameter sets and logs."""
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    (folder/'config.json').write_text(json.dumps(config,indent=2));start=time.perf_counter()
    try:
        proc=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker','--input',str(Path(source).resolve()),'--output',str(folder.resolve())],capture_output=True,text=True,timeout=180)
        (folder/'process.log').write_text(proc.stdout+'\n'+proc.stderr)
        if proc.returncode:raise RuntimeError('worker exit '+str(proc.returncode))
        result=json.loads((folder/'result.json').read_text())
    except Exception as error:
        result={'status':'failed','error':str(error),'config':config}
    result['isolated_process_wall_seconds']=time.perf_counter()-start
    (folder/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False));return result

def worker(source,folder):
    """Trace, validate raster exclusion, native-render, evaluate in a fresh process."""
    import vtracer
    from importlib.metadata import version
    folder=Path(folder);config=json.loads((folder/'config.json').read_text());rgb=load_rgb(source);h,w=rgb.shape[:2]
    start=time.perf_counter();cpu=time.process_time();svg=folder/'output.svg'
    vtracer.Config(**config).convert_file(str(source),str(svg))
    trace={'trace_wall_seconds':time.perf_counter()-start,'trace_cpu_seconds':time.process_time()-cpu,'trace_process_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024}
    structure=svg_structure(svg)
    if not structure['raster_free'] or structure['external_href_count'] or structure['script_count']:raise ValueError('Not a self-contained raster-free SVG')
    timing=render_svg(svg,folder/'render.png',w,h)
    with Image.open(folder/'render.png') as image:image.verify()
    pred=load_rgb(folder/'render.png');metrics=compare(rgb,pred)|extra_metrics(rgb,pred)
    result={'status':'ok','vtracer_version':version('vtracer'),'config':config,'metrics':metrics,'score':fidelity_score(metrics),'structure':structure,'performance':trace|timing|{'worker_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,'renderer_child_peak_mib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1024,'memory_note':'separate Linux process high-water marks, not simultaneous process-tree RSS'}}
    (folder/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False))

def search(source,output,configs=None,refine=True):
    """Execute thirteen fixed pilots and at most four adaptive probes, retaining all."""
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    if (output/'ranking.json').exists():raise FileExistsError('Use a new output directory; prior evidence is immutable')
    normalized=output/'normalized.png';normalization=prepare_input(source,normalized)
    (output/'normalization.json').write_text(json.dumps(normalization,indent=2));results=[];seen=set()
    def evaluate(config,phase):
        key=json.dumps(config,sort_keys=True)
        if key in seen:return
        seen.add(key);name=f'trial_{len(results):02d}';result=run_trial(normalized,output/name,config)
        result['trial']=name;result['phase']=phase;results.append(result)
        (output/'progress.json').write_text(json.dumps(results,indent=2))
        print(name,result['status'],round(result.get('score',0),6),flush=True)
    for config in (pilot_configs() if configs is None else configs):evaluate(config,'pilot' if configs is None else 'frozen')
    successful=[r for r in results if r['status']=='ok']
    if refine and configs is None and successful:
        winner=max(successful,key=lambda r:r['score'])
        for config in refined_configs(winner['config']):evaluate(config,'local')
    ranked=sorted([r for r in results if r['status']=='ok'],key=lambda r:(-r['score'],r['trial']))
    record={'normalization':normalization,'selection':'score=.40SSIM+.15min(PSNR/60,1)+.20edgeF1+.15exp(-meanDeltaE76/12)+.10exp(-highpassRMSE/20); no complexity penalty. Visual review remains required.','ranked':ranked,'failed':[r for r in results if r['status']!='ok']}
    (output/'ranking.json').write_text(json.dumps(record,indent=2))
    if ranked:
        best=ranked[0];shutil.copyfile(output/best['trial']/'output.svg',output/'best.svg');shutil.copyfile(output/best['trial']/'render.png',output/'best.png');(output/'best_config.json').write_text(json.dumps(best['config'],indent=2))
    return record

if __name__=='__main__':
    cli=argparse.ArgumentParser();cli.add_argument('--input',required=True,type=Path);cli.add_argument('--output',required=True,type=Path);cli.add_argument('--configs',type=Path);cli.add_argument('--no-refine',action='store_true');cli.add_argument('--worker',action='store_true');args=cli.parse_args()
    if args.worker:worker(args.input,args.output)
    else:search(args.input,args.output,json.loads(args.configs.read_text()) if args.configs else None,not args.no_refine)
# END CHANGE VTRACER-SEARCH | 2026-10-24T09:56:03Z | CREATED | Author: vtracer_engine
