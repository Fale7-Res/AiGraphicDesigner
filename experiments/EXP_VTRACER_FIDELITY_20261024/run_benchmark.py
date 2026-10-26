# START CHANGE VTRACER-BENCHMARK | 2026-10-24T09:56:44Z | CREATED | Author: parent
"""Development selection, frozen holdout evaluation, then separate per-image tuning."""
from pathlib import Path
import sys,json,hashlib,datetime,subprocess,argparse
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from search import search

def run_benchmark(destination=ROOT):
    destination=Path(destination).resolve();destination.mkdir(parents=True,exist_ok=True)
    protocol=json.loads((ROOT/'protocol.json').read_text());images=sorted((ROOT/'inputs').glob('*.png'))
    for p in images:
        if p.stem[:3] in protocol['development']:
            out=destination/'results'/p.stem
            if not (out/'ranking.json').exists():search(p,out)
    common={}
    for p in images:
        if p.stem[:3] not in protocol['development']:continue
        r=json.loads((destination/'results'/p.stem/'ranking.json').read_text())
        for v in r['ranked']:
            if v['phase']!='pilot':continue
            key=json.dumps(v['config'],sort_keys=True)
            common.setdefault(key,[]).append(v['score'])
    eligible=[(sum(scores)/4,key,scores) for key,scores in common.items() if len(scores)==4]
    if not eligible:raise RuntimeError('No successful common pilot across development')
    score,key,scores=max(eligible);config=json.loads(key)
    frozen=destination/'frozen_common.json'
    if frozen.exists():
        previous=json.loads(frozen.read_text());assert previous['config']==config
    else:
        frozen.write_text(json.dumps({'config':config,'development_mean_score':score,'development_scores':scores,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'config_sha256':hashlib.sha256(key.encode()).hexdigest(),'selection':'Only13shared pilots evaluated on4development images; holdout not used'},indent=2))
    for p in images:
        if p.stem[:3] not in protocol['holdout']:continue
        out=destination/'holdout_common'/p.stem
        if not (out/'ranking.json').exists():search(p,out,configs=[config],refine=False)
    # All eight common-preset evaluations complete BEFORE per-image holdout tuning.
    marker=destination/'holdout_evaluation_completed.json'
    if not marker.exists():marker.write_text(json.dumps({'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_sha256':hashlib.sha256(frozen.read_bytes()).hexdigest()}))
    for p in images:
        if p.stem[:3] not in protocol['holdout']:continue
        out=destination/'results'/p.stem
        if not (out/'ranking.json').exists():search(p,out)

if __name__=='__main__':
    cli=argparse.ArgumentParser();cli.add_argument('--output-directory',type=Path,default=ROOT);args=cli.parse_args();run_benchmark(args.output_directory)

# END CHANGE VTRACER-BENCHMARK | 2026-10-24T09:56:44Z | CREATED | Author: parent
