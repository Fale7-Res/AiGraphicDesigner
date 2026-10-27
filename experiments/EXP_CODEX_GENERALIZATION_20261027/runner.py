"""Frozen-baseline search and explicit alpha-aware candidate selection research."""
# START CHANGE AGD-GEN-ENGINE | 2026-10-27T11:07:02Z | CREATED | Author: root
from pathlib import Path
import argparse, hashlib, json, os, shutil, sys, time
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'EXP_CODEX_WINDOWS_FIDELITY_20261027'
sys.path.insert(0,str(BASE))
from optimizer import optimize
from alpha_optimizer import prepare_transparent_input,apply_vector_alpha,evaluate_alpha
from windows_search import compare,load_rgb,extra_metrics,fidelity_score,svg_structure

def read_suite(path):
    """Load frozen case list and reject hash drift before invoking any search."""
    payload=json.loads(Path(path).read_text(encoding='utf-8'))
    cases=payload if isinstance(payload,list) else payload.get('cases',payload.get('inputs'))
    if not cases:raise ValueError('Manifest requires cases or inputs')
    return cases

def rgb_diagnostics(reference,predicted):
    """Inherited metrics plus independent worst spatial-tile residual diagnostics."""
    m=compare(reference,predicted)|extra_metrics(reference,predicted)
    error=(reference.astype(float)-predicted.astype(float))**2
    tiles=[float(np.sqrt(error[y:y+32,x:x+32].mean())) for y in range(0,len(error),32) for x in range(0,error.shape[1],32)]
    m.update(worst_32px_tile_rmse=max(tiles),median_32px_tile_rmse=float(np.median(tiles)))
    return m

def run_generalization_case(case,manifest_hash,max_candidates=24,max_seconds=240):
    """One inherited search per unseen image; new alpha selection reuses its candidates."""
    case_id=case['id'];file=case['file'];source=ROOT/'inputs'/file
    if not source.is_file():source=ROOT/file
    actual=hashlib.sha256(source.read_bytes()).hexdigest()
    if case.get('sha256') and actual!=case['sha256']:raise ValueError('Frozen input hash differs')
    out=ROOT/'results'/case_id
    if (out/'case_result.json').exists():
        result=json.loads((out/'case_result.json').read_text());assert result['source_sha256']==actual
        print('REUSE completed current-cycle case',case_id,flush=True);return result
    if out.exists() and any(out.iterdir()):raise FileExistsError('Partial case preserved; choose a new experiment or investigate')
    out.mkdir(parents=True,exist_ok=True);started=time.perf_counter()
    with Image.open(source) as im:has_alpha=im.convert('RGBA').getchannel('A').getextrema()!=(255,255)
    prep=prepare_transparent_input(source,out/'prepared')
    ranking=optimize(out/'prepared/unassociated_rgb.png',out/'baseline_search',max_candidates,max_seconds,'reject')
    if not ranking['ranked']:
        failure={'id':case_id,'status':'failed','ranking':ranking,'source_sha256':actual}
        (out/'case_result.json').write_text(json.dumps(failure,indent=2));return failure
    best=ranking['ranked'][0];evaluated=[];cache={}
    for row in ranking['ranked']:
        trial=row['trial'];rgb_svg=out/'baseline_search'/trial/'output.svg'
        if has_alpha:
            digest=hashlib.sha256(rgb_svg.read_bytes()).hexdigest()
            if digest in cache:
                assessment=dict(cache[digest]);assessment.update(trial=trial,cache_reused_from=cache[digest]['trial'])
            else:
                target=out/'alpha_candidates'/trial;target.mkdir(parents=True)
                mask=apply_vector_alpha(rgb_svg,out/'prepared/source_alpha.png',target/'output.svg')
                assessment=evaluate_alpha(out/'prepared/reference_srgb_rgba.png',target/'output.svg',target)
                assessment['trial']=trial;assessment['svg_relative']=str((target/'output.svg').relative_to(out));assessment['png_relative']=str((target/'render_rgba.png').relative_to(out))
                assessment['vector_alpha']=mask
                cache[digest]=assessment
            scores=[fidelity_score(m) for m in assessment['background_metrics'].values()]
            assessment.update(robust_score=min(scores),mean_score=float(np.mean(scores)),inherited_rgb_score=row['score'])
        else:
            pred=load_rgb(out/'baseline_search'/trial/'render.png');ref=load_rgb(out/'prepared/unassociated_rgb.png')
            metrics=rgb_diagnostics(ref,pred)
            assessment={'trial':trial,'metrics':metrics,'robust_score':row['score'],'mean_score':row['score'],
                        'svg_relative':str(rgb_svg.relative_to(out)),'png_relative':str((out/'baseline_search'/trial/'render.png').relative_to(out)),'inherited_rgb_score':row['score']}
        evaluated.append(assessment)
    inherited=next(x for x in evaluated if x['trial']==best['trial'])
    selected=sorted(evaluated,key=lambda r:(-r['robust_score'],-r['mean_score'],-r['inherited_rgb_score'],r['trial']))[0]
    # Opaque images deliberately retain frozen baseline until a separate measured hypothesis is enabled.
    if not has_alpha:selected=inherited
    for label,row in [('inherited',inherited),('new',selected)]:
        shutil.copyfile(out/row['svg_relative'],out/f'{label}.svg');shutil.copyfile(out/row['png_relative'],out/f'{label}.png')
    result={'id':case_id,'status':'ok','source_sha256':actual,'dataset_manifest_sha256':manifest_hash,'has_alpha':has_alpha,
            'normalization':prep,'baseline_commit':'b398de3d95539a77ee4ea1cafea2e1ecc7f2efdf','baseline_candidates':ranking['evaluated_candidates'],
            'failed_candidates':len(ranking['failed']),'baseline_stop':ranking['stop_reason'],'baseline_search_wall_seconds':ranking['search_wall_seconds'],
            'families_evaluated':ranking['families_evaluated'],'selection_policy':'maximize minimum inherited fidelity score over white/black/bluegray, mean then RGB score tie-break; no complexity penalty',
            'inherited':inherited,'new':selected,'alpha_candidate_assessments':evaluated if has_alpha else [],
            'rgb_metric_leaders':{k:max(ranking['ranked'],key=lambda r:r['metrics'][k] if r['metrics'][k] is not None else float('-inf'))['trial'] for k in ['ssim','psnr_db','edge_f1_1_5px']},
            'maximum_sampled_worker_tree_mib':max(r['performance']['worker_tree_resources']['sampled_tree_peak_mib'] for r in ranking['ranked']),
            'total_wall_seconds':time.perf_counter()-started,'architecture':'NOT_APPROVED'}
    (out/'case_result.json').write_text(json.dumps(result,indent=2,allow_nan=False),encoding='utf-8')
    print('COMPLETE',case_id,'alpha',has_alpha,'candidates',result['baseline_candidates'],'selected',inherited['trial'],'->',selected['trial'],'wall',round(result['total_wall_seconds'],1),flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--manifest',type=Path,default=ROOT/'inputs/manifest.json');p.add_argument('--case');p.add_argument('--max-candidates',type=int,default=24);p.add_argument('--max-seconds',type=float,default=240);a=p.parse_args()
    manifest_hash=hashlib.sha256(a.manifest.read_bytes()).hexdigest();cases=read_suite(a.manifest)
    for c in cases:
        if a.case and c['id']!=a.case:continue
        print('START',c['id'],flush=True);run_generalization_case(c,manifest_hash,a.max_candidates,a.max_seconds)
# END CHANGE AGD-GEN-ENGINE | 2026-10-27T11:07:02Z | CREATED | Author: root
