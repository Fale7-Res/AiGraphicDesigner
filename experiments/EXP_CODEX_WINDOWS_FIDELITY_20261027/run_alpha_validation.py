"""Bounded sequential native alpha comparison, gated on completed baseline search."""
# START CHANGE AGD-CODEX-ALPHA-LOCAL-RUN | 2026-10-27T10:29:26Z | CREATED | Author: windows_extension
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def run_alpha_comparison(renderer_exe: Path,baseline_ranking: Path) -> dict:
    """Compare explicit-white inherited policy to vector-mask alpha experiment."""
    ranking=json.loads(Path(baseline_ranking).read_text(encoding='utf-8'))
    if not ranking.get('ranked') or ranking.get('evaluated_candidates',0)<13:
        raise RuntimeError('A completed successful inherited baseline search is required first')
    if not Path(renderer_exe).is_file(): raise FileNotFoundError(renderer_exe)
    os.environ['AGD_RENDERER']='resvg';os.environ['AGD_RENDERER_EXE']=str(Path(renderer_exe).resolve())
    from optimizer import optimize
    from alpha_optimizer import optimize_alpha, evaluate_alpha
    source=ROOT/'inputs'/'N02_local_soft_alpha.png'
    white=ROOT/'results'/'N02_white_baseline';alpha=ROOT/'results'/'N02_alpha_preserve'
    print('N02: inherited explicit-white search, 13 candidates',flush=True)
    white_rank=optimize(source,white,13,720.,'white')
    if not white_rank['ranked']: raise RuntimeError('White baseline produced no successful candidate')
    print('N02: unassociated RGB search + vector alpha, 13 candidates',flush=True)
    alpha_report=optimize_alpha(source,alpha,13,720.)
    if 'evaluation' not in alpha_report: raise RuntimeError('Alpha prototype produced no successful candidate')
    white_eval=evaluate_alpha(alpha/'input'/'reference_srgb_rgba.png',white/'best.svg',white/'alpha_evaluation')
    improved=alpha_report['evaluation']
    report={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'source':str(source),
            'completed_baseline_ranking':str(Path(baseline_ranking).resolve()),
            'protocol':'Sequential 13 candidates each; explicit inherited white baseline versus unassociated RGB + vector mask. Post-selection alpha and three-background metrics; resvg differs from historical Inkscape.',
            'white_baseline':white_eval,'alpha_preserve':improved,
            'alpha_mae_reduction':white_eval['alpha_mae_0_255']-improved['alpha_mae_0_255'],
            'mean_background_score_increase':improved['mean_background_fidelity_score']-white_eval['mean_background_fidelity_score'],
            'white_candidates':white_rank['evaluated_candidates'],'alpha_candidates':alpha_report['rgb_search_candidates'],
            'architecture_status':'NOT_APPROVED','owner_acceptance':'NOT_REQUESTED_BY_SCRIPT'}
    (ROOT/'reports'/'alpha_comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False),encoding='utf-8')
    print(json.dumps({key:report[key] for key in ('alpha_mae_reduction','mean_background_score_increase','white_candidates','alpha_candidates')},indent=2),flush=True)
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--renderer-exe',required=True,type=Path)
    parser.add_argument('--baseline-ranking',type=Path,default=ROOT/'results'/'A03_burger_layers'/'ranking.json')
    args=parser.parse_args();run_alpha_comparison(args.renderer_exe,args.baseline_ranking)
# END CHANGE AGD-CODEX-ALPHA-LOCAL-RUN | 2026-10-27T10:29:26Z | CREATED | Author: windows_extension
