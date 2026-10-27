"""Per-input bounded VTracer search using the immutable historical evaluator."""
# START CHANGE ADAPTIVE-RECOVERY | 2026-10-27T03:08:56Z | CREATED | Author: restore_execute
import argparse, json, shutil, sys, time
from pathlib import Path
from importlib.metadata import version
from PIL import Image
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'/'src'))
from search import OWNER, prepare_input, run_trial

def canonical(c):
    c=dict(c); f=c['clustering']
    if f!='color-cluster':
        c.pop('color_precision',None)
        if not (f=='bw' and c['hierarchical']=='cutout'):c.pop('layer_difference',None)
    if f!='watershed':c.pop('watershed_detail',None)
    if f!='bw':
        for k in ('binary_threshold','adaptive','adaptive_window','adaptive_t'):c.pop(k,None)
    elif c.get('adaptive',False):c.pop('binary_threshold',None)
    else:
        for k in ('adaptive_window','adaptive_t'):c.pop(k,None)
    if c['mode']!='spline':
        for k in ('simplify','corner_threshold','length_threshold','max_iterations','splice_threshold'):c.pop(k,None)
    return c

def pilots():
    changes=[{}, {'mode':'pixel','layer_difference':1}, {'mode':'pixel','layer_difference':0},
      {'mode':'pixel','layer_difference':1,'hierarchical':'cutout'},
      {'mode':'polygon','path_precision':3}, {'path_precision':3,'simplify':None},
      {'clustering':'watershed','mode':'pixel','watershed_detail':512,'hierarchical':'cutout','path_precision':3},
      {'clustering':'watershed','mode':'pixel','watershed_detail':256},
      {'clustering':'watershed','mode':'spline','watershed_detail':128,'hierarchical':'cutout','path_precision':3,'simplify':None},
      {'clustering':'watershed','mode':'polygon','watershed_detail':256,'hierarchical':'cutout','path_precision':3},
      {'clustering':'bw','mode':'pixel','binary_threshold':128},
      {'clustering':'bw','mode':'spline','hierarchical':'cutout','binary_threshold':128,'path_precision':3,'simplify':None},
      {'clustering':'bw','mode':'pixel','adaptive':True,'adaptive_window':0,'adaptive_t':15}]
    return [canonical(OWNER|d) for d in changes]

def neighborhood(c):
    f=c['clustering']
    if f=='watershed':changes=[{'watershed_detail':min(2048,c.get('watershed_detail',128)*2)},{'watershed_detail':max(1,c.get('watershed_detail',128)//2)}]
    elif f=='color-cluster':changes=[{'layer_difference':x} for x in (1,2,8,0)]+[{'color_precision':x} for x in (7,6)]
    else:changes=([{'adaptive_t':x} for x in (5,25)]+[{'adaptive_window':x} for x in (15,31)]) if c.get('adaptive') else [{'binary_threshold':x} for x in (96,160,192)]
    changes += [{'hierarchical':'cutout' if c['hierarchical']=='stacked' else 'stacked'}]+[{'filter_speckle':x} for x in (1,2)]+[{'path_precision':x} for x in (5,1)]+[{'optimize':0}]
    if c['mode']=='spline':changes += [{'simplify':x} for x in (None,.25,.75)]+[{'length_threshold':2.},{'corner_threshold':45},{'splice_threshold':30},{'max_iterations':20}]
    return [canonical(c|d) for d in changes]

def optimize(source,output,max_candidates=24,max_seconds=720,alpha_policy='reject'):
    source=Path(source);out=Path(output)
    if out.exists() and any(out.iterdir()):raise FileExistsError('Output must be empty')
    if max_candidates<13 or max_seconds<=0:raise ValueError('Require >=13 candidates and positive time budget')
    if version('vtracer')!='1.0.0a4':raise RuntimeError('Pinned parameter surface requires vtracer 1.0.0a4')
    with Image.open(source) as im:
        if getattr(im,'n_frames',1)!=1 or min(im.size)<7:raise ValueError('Requires single frame, width and height >=7')
        if alpha_policy not in ('reject','white'):raise ValueError('Unknown alpha policy')
        if im.convert('RGBA').getchannel('A').getextrema()!=(255,255) and alpha_policy=='reject':raise ValueError('Transparency unsupported; explicitly choose white compositing')
    out.mkdir(parents=True,exist_ok=True);start=time.monotonic();rows=[];events=[];seen=set()
    norm=prepare_input(source,out/'normalized.png');norm['requested_alpha_policy']=alpha_policy
    (out/'normalization.json').write_text(json.dumps(norm,indent=2))
    (out/'plan.json').write_text(json.dumps({'pilots':pilots(),'max_candidates':max_candidates,'max_seconds':max_seconds,'stagnation_rounds':2,'minimum_improvement':1e-5,'budget':'dispatch deadline; current worker may add180seconds'},indent=2))
    def budget():return len(rows)>=max_candidates or time.monotonic()-start>=max_seconds
    def trial(c,phase):
        key=json.dumps(canonical(c),sort_keys=True)
        if key in seen:
            events.append({'status':'rejected','reason':'duplicate_effective_config','config':c});return False
        seen.add(key);name=f'trial_{len(rows):02d}';r=run_trial(out/'normalized.png',out/name,canonical(c));r.update(trial=name,phase=phase);rows.append(r)
        (out/'progress.json').write_text(json.dumps(rows,indent=2));return True
    for c in pilots():
        if budget():break
        trial(c,'pilot')
    stale=0;stop='budget'
    while not budget():
        good=sorted((r for r in rows if r['status']=='ok'),key=lambda r:-r['score'])
        if not good:stop='all_failed';break
        if good[0]['score']>=1-1e-12:stop='perfect_numeric_score';break
        previous=good[0]['score'];leaders={}
        for r in good:leaders.setdefault(r['config']['clustering'],r)
        attempted=False
        for r in leaders.values():
            if budget():break
            for c in neighborhood(r['config']):
                if trial(c,'adaptive'):attempted=True;break
        if not attempted:stop='neighborhood_exhausted';break
        current=max(r.get('score',0) for r in rows)
        stale=stale+1 if current-previous<1e-5 else 0
        if stale>=2:stop='stagnation';break
    ranked=sorted((r for r in rows if r['status']=='ok'),key=lambda r:(-r['score'],r['trial']))
    result={'ranked':ranked,'failed':[r for r in rows if r['status']!='ok'],'events':events,'stop_reason':stop,'search_wall_seconds':time.monotonic()-start,'evaluated_candidates':len(rows),'families_evaluated':sorted({r['config']['clustering'] for r in rows})}
    (out/'ranking.json').write_text(json.dumps(result,indent=2));(out/'search_events.json').write_text(json.dumps(events,indent=2))
    if ranked:
        for a,b in [('output.svg','best.svg'),('render.png','best.png')]:shutil.copyfile(out/ranked[0]['trial']/a,out/b)
        (out/'best_config.json').write_text(json.dumps(ranked[0]['config'],indent=2))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--max-candidates',type=int,default=24);p.add_argument('--max-seconds',type=float,default=720);p.add_argument('--alpha-policy',choices=['reject','white'],default='reject');a=p.parse_args()
    r=optimize(a.input,a.output,a.max_candidates,a.max_seconds,a.alpha_policy);print(json.dumps({'stop':r['stop_reason'],'tested':r['evaluated_candidates'],'best':r['ranked'][0]['metrics'] if r['ranked'] else None}))
# END CHANGE ADAPTIVE-RECOVERY | 2026-10-27T03:08:56Z | CREATED | Author: restore_execute
