# START CHANGE VTRACER-RESUME-GUARD | 2026-10-25T04:45:18Z | EDITED | Author: parent
# START CHANGE VTRACER-EXTENSION | 2026-10-24T23:42:30Z | CREATED | Author: vtracer_engine
"""Post-hoc bounded clustering probes after negative fixed-geometry color refit."""
from pathlib import Path
import argparse,json
from datetime import datetime,timezone
from search import OWNER,run_trial
ROOT=Path(__file__).resolve().parents[1]
DEVELOPMENT=['A01_shield','A03_burger_layers','A05_orange_juice_transparency','A10_restaurant_logo']
BASE=OWNER|{'mode':'pixel','simplify':None}
PROBES=[BASE|{'hierarchical':'cutout'},BASE|{'layer_difference':1},BASE|{'hierarchical':'cutout','layer_difference':1}]

def development():
    """Three fixed mechanistic probes per development case; freeze one if it helps."""
    root=ROOT/'extension';root.mkdir(exist_ok=True)
    if (root/'freeze.json').exists():
        frozen=json.loads((root/'freeze.json').read_text())
        if frozen['winner_config'] not in PROBES:raise ValueError('Frozen configuration differs from declared probes')
        return frozen
    plan={'created_utc':datetime.now(timezone.utc).isoformat(),'development':DEVELOPMENT,'configs':PROBES,'reason':'Visible-color refit negligible; probe diagonal clustering switch at layer_difference0 vs1 and previously untested pixel cutout. Post-hoc diagnostic, no claim of exhaustive optimum.','selection':'Choose highest mean composite score among3probes, compare to pixelstacked0. Require mean score improvement>0.0001 before extending to holdout.'}
    if not (root/'plan.json').exists():(root/'plan.json').write_text(json.dumps(plan,indent=2))
    results={}
    for case in DEVELOPMENT:
        source=ROOT/'results'/case/'normalized.png';results[case]=[]
        for index,config in enumerate(PROBES):
            out=root/case/f'probe_{index}'
            result=json.loads((out/'result.json').read_text()) if (out/'result.json').exists() else run_trial(source,out,config)
            if result.get('status')!='ok':raise RuntimeError(f'Failed development probe: {out}')
            results[case].append(result);print(case,index,result.get('score'),flush=True)
    means=[sum(results[case][i].get('score',0) for case in DEVELOPMENT)/len(DEVELOPMENT) for i in range(3)]
    base=sum(json.loads((ROOT/'results'/case/'trial_07/result.json').read_text())['score'] for case in DEVELOPMENT)/len(DEVELOPMENT)
    winner=max(range(3),key=lambda i:means[i]);freeze={'frozen_utc':datetime.now(timezone.utc).isoformat(),'development_mean_scores':means,'base_pixel_stacked_mean':base,'winner_index':winner,'winner_config':PROBES[winner],'mean_gain':means[winner]-base,'advance_to_holdout':means[winner]-base>.0001,'development_results':results}
    (root/'freeze.json').write_text(json.dumps(freeze,indent=2));print({k:v for k,v in freeze.items() if k!='development_results'},flush=True)

def holdout():
    """Apply one previously frozen extra configuration to other eight images."""
    root=ROOT/'extension';freeze=json.loads((root/'freeze.json').read_text())
    if not freeze['advance_to_holdout']:raise ValueError('Development gate failed; no holdout expansion')
    cases=[ROOT/'results'/p.stem for p in sorted((ROOT/'inputs').glob('*.png')) if p.stem not in DEVELOPMENT]
    if len(cases)!=8 or any(not (c/'normalized.png').exists() for c in cases):raise ValueError('Need exactly eight complete holdout inputs')
    for case in cases:
        if not case.is_dir() or case.name in DEVELOPMENT:continue
        if not (case/'normalized.png').exists():continue
        out=root/case.name/'frozen'
        if (out/'result.json').exists():
            if json.loads((out/'result.json').read_text()).get('status')!='ok':raise RuntimeError(f'Existing failed holdout: {out}')
            continue
        r=run_trial(case/'normalized.png',out,freeze['winner_config'])
        if r.get('status')!='ok':raise RuntimeError(f'Failed holdout: {out}')
        print(case.name,r.get('score'),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['development','holdout']);args=p.parse_args();development() if args.phase=='development' else holdout()

# END CHANGE VTRACER-EXTENSION | 2026-10-24T23:42:30Z | CREATED | Author: vtracer_engine

# END CHANGE VTRACER-RESUME-GUARD | 2026-10-25T04:45:18Z | EDITED | Author: parent
