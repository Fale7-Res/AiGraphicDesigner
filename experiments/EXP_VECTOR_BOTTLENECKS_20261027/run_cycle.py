# START CHANGE AGD-BOTTLENECK-RUNNER | 2026-10-28T03:34:28Z | EDITED | Author: root
"""Reproduce bounded workers or verify/reuse complete evidence; no destructive reset."""
from pathlib import Path
import argparse,json,sys,os,hashlib
from safe_monitor import monitor
ROOT=Path(__file__).resolve().parent

def verify_inventory(path):
    record=json.loads(Path(path).read_text(encoding='utf-8'))
    if not record.get('files'):raise ValueError('Missing artifact inventory')
    for relative,row in record['files'].items():
        file=(ROOT/relative).resolve()
        if not file.is_relative_to(ROOT.resolve()):raise ValueError('Inventory path outside experiment')
        assert file.is_file() and hashlib.sha256(file.read_bytes()).hexdigest()==row['sha256'],relative

def artifact_inventory(target):
    target=Path(target);files={}
    for file in target.rglob('*'):
        if file.is_file() and file.name not in ['FILE_INVENTORY.json','index.html']:
            files[file.relative_to(ROOT).as_posix()]={'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
    (target/'FILE_INVENTORY.json').write_text(json.dumps({'files':files},indent=2))

def run_bounded(name,args,timeout):
    result=monitor([sys.executable,*map(str,args)],ROOT/'reports'/f'{name}.log',timeout,4096)
    (ROOT/'reports'/f'{name}_resources.json').write_text(json.dumps(result,indent=2))
    if result['returncode'] or result['termination_reason']:raise RuntimeError(result)
    print(name,result,flush=True)

def oracle_dashboard():
    rows=[]
    for folder in sorted((ROOT/'results/oracle').glob('K*')):
        rows.append(f'<h2>{folder.name}</h2><p>Exact geometry is privileged diagnostic data; not a deployable reconstruction.</p>')
        for name in ['comparison.png','center_4x.png','center_16x.png']:rows.append(f'<div style="overflow:auto"><img src="{folder.name}/{name}"></div>')
        rows.append('<p>'+' | '.join(f'<a href="{folder.name}/{name}.svg">{name}</a>' for name in ['oracle_truth','oracle_C','oracle_D'])+'</p>')
    (ROOT/'results/oracle/index.html').write_text('<!doctype html><meta charset="utf-8"><title>Geometry oracle</title><h1>Geometry oracle — NOT_APPROVED architecture</h1>'+''.join(rows),encoding='utf-8')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--phase',choices=['granularity','oracle','coverage','corrections','dashboard','tests'],required=True);a=p.parse_args()
    ROOT.joinpath('reports').mkdir(exist_ok=True);os.environ['PYTHONDONTWRITEBYTECODE']='1'
    if not os.environ.get('AGD_RENDERER_EXE'):raise ValueError('Set AGD_RENDERER_EXE to verified resvg0.49.0')
    os.environ['AGD_RENDERER']='resvg'
    if a.phase=='granularity':
        # Per-case bounds and complete saved-artifact checks live in this driver.
        import subprocess
        raise SystemExit(subprocess.run([sys.executable,str(ROOT/'bottlenecks.py')]).returncode)
    if a.phase=='oracle':
        target=ROOT/'results/oracle'
        if (target/'summary.json').exists():
            expected={'K01_linear_corner_hole','K02_radial_shared_curves'}
            assert {p.name for p in target.glob('K*') if p.is_dir()}==expected
            verify_inventory(target/'FILE_INVENTORY.json')
            for folder in [target/name for name in sorted(expected)]:
                data=json.loads((folder/'result.json').read_text())
                for name,row in data['conditions'].items():assert hashlib.sha256((folder/f'{name}.svg').read_bytes()).hexdigest()==row['sha256']
            print('REUSE complete oracle')
        else:
            run_bounded('oracle_worker',[ROOT/'oracle.py','--repository',ROOT.parent.parent,'--output',target],300)
            artifact_inventory(target)
        oracle_dashboard()
    if a.phase=='coverage':
        os.environ['AGD_COVERAGE_ROOT']=str(ROOT)
        if (ROOT/'results/coverage/summary.json').exists():
            summary=json.loads((ROOT/'results/coverage/summary.json').read_text())
            assert set(summary)=={'A01_shield','G01_coffee','G05_chelsea_nativecrop','G06_arabic','G08_dice_alpha'}
            assert (ROOT/'results/coverage/controls/results.json').is_file()
            verify_inventory(ROOT/'results/coverage/FILE_INVENTORY.json')
            print('REUSE hash-verified complete coverage')
        else:
            run_bounded('coverage_controls_worker',[ROOT/'coverage.py','--controls'],300)
            run_bounded('coverage_real_worker',[ROOT/'coverage.py','--real'],600)
            artifact_inventory(ROOT/'results/coverage')
    if a.phase=='corrections':
        cases=json.loads((ROOT/'inputs/manifest.json').read_text())['cases']
        for case in cases:
            if (ROOT/'results/corrections'/case['id']/'result.json').exists():
                from correct_bottlenecks import corrected_case
                corrected_case(case);print('REUSE correction',case['id']);continue
            run_bounded(case['id']+'_correction',[ROOT/'correct_bottlenecks.py','--case',case['id']],180)
    if a.phase=='dashboard':
        from bottlenecks import comparisons
        comparisons();oracle_dashboard()
    if a.phase=='tests':
        for name in ['test_oracle.py','test_coverage.py','test_bottlenecks.py']:run_bounded(name,[ROOT/name],180)

# END CHANGE AGD-BOTTLENECK-RUNNER | 2026-10-28T03:34:28Z | EDITED | Author: root
