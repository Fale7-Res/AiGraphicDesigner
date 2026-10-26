# START CHANGE VTRACER-COMMON-METRICS | 2026-10-24T14:57:03Z | EDITED | Author: vtracer_baselines
"""Rerender exact historical SVGs; do not regenerate or modify historical engines."""
# START CHANGE VTRACER-BASELINES | 2026-10-24T09:56:09Z | CREATED | Author: vtracer_baselines
from pathlib import Path
import argparse,hashlib,json,resource,shutil,subprocess,sys,time
from PIL import Image
from evaluate import load_rgb,render_svg,compare,svg_structure
from search import extra_metrics
ROOT=Path(__file__).resolve().parents[1]

def measure(svg,source,out):
    """Fresh-process baseline native render with exact dimensions and color audit."""
    out.mkdir(parents=True,exist_ok=True)
    with Image.open(source) as im:
        metadata={'mode':im.mode,'dimensions':list(im.size),'icc_present':bool(im.info.get('icc_profile')),'alpha_present':'A' in im.getbands(),'info_keys':list(im.info)}
    if metadata['icc_present'] or metadata['alpha_present']:raise ValueError('This historical benchmark requires explicit new normalization review for ICC/alpha inputs')
    ref=load_rgb(source);h,w=ref.shape[:2];wall=time.perf_counter();cpu=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    timing=render_svg(svg,out/'render.png',w,h)
    with Image.open(out/'render.png') as im:im.verify()
    with Image.open(out/'render.png') as im:im.load()
    pred=load_rgb(out/'render.png');metrics=compare(ref,pred)
    metrics.update(extra_metrics(ref,pred))
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result={'source_name':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),'input_metadata':metadata,'metrics':metrics,'structure':svg_structure(svg),'render':timing,'resources':{'wall_seconds':time.perf_counter()-wall,'parent_cpu_seconds':time.process_time()-cpu,'renderer_child_cpu_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'parent_peak_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,'child_peak_mib':after.ru_maxrss/1024,'scope':'Fresh worker process per SVG. Child peak includes Inkscape export and version subprocess, not simultaneous tree peak; historical generation excluded.'},'scope':'Fresh render of exact historical SVG; not an engine reproduction; untagged RGB assumed sRGB, white compositing, no resize.'}
    (out/'metrics.json').write_text(json.dumps(result,indent=2));return result

def candidates():
    """Map frozen baseline copies to corresponding benchmark images."""
    for source in sorted((ROOT/'inputs').glob('*.png')):
        for label in ['original','repair']:
            svg=ROOT/'baselines'/label/(source.stem+'_v04.svg')
            if not svg.exists():raise FileNotFoundError(svg)
            yield source,label,svg
        recent=ROOT/'baselines/recent'/source.stem
        if recent.exists():
            for svg in sorted(recent.glob('*.svg')):yield source,svg.stem,svg

def run(out):
    """Run native historical rendering serially and preserve every result."""
    rows=[]
    for source,label,svg in candidates():
        target=out/source.stem/label
        subprocess.run([sys.executable,__file__,'--worker','--svg',str(svg),'--source',str(source),'--output',str(target)],check=True)
        row=json.loads((target/'metrics.json').read_text());row['label']=label;row['case']=source.stem;rows.append(row);(out/'summary.json').write_text(json.dumps(rows,indent=2));print(source.stem,label,round(row['metrics']['ssim'],6),flush=True)
    return rows

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=ROOT/'results_baselines');parser.add_argument('--worker',action='store_true');parser.add_argument('--svg',type=Path);parser.add_argument('--source',type=Path);a=parser.parse_args()
    if a.worker:measure(a.svg,a.source,a.output)
    else:run(a.output)
# END CHANGE VTRACER-BASELINES | 2026-10-24T09:56:09Z | CREATED | Author: vtracer_baselines

# END CHANGE VTRACER-COMMON-METRICS | 2026-10-24T14:57:03Z | EDITED | Author: vtracer_baselines
