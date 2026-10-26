# START CHANGE DELIVERY-REPRODUCE | 2026-10-25T15:01:53Z | CREATED | Author: parent
"""Prepare fresh source/data copy; optionally replay completed research stages."""
from pathlib import Path
import argparse,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
def prepare(destination):
    destination=destination.resolve()
    if destination.exists():raise FileExistsError('Destination must not exist')
    if len(list((ROOT/'inputs').glob('*.png')))!=12:raise ValueError('Expected twelve inputs')
    destination.mkdir(parents=True)
    for name in ['src','inputs','baselines','annotations']:shutil.copytree(ROOT/name,destination/name,ignore=shutil.ignore_patterns('__pycache__','.*'))
    for name in ['run_benchmark.py','summarize.py','requirements.txt','protocol.json']:shutil.copy2(ROOT/name,destination/name)
    (destination/'reports').mkdir()
    return destination
def execute(destination):
    def run(*args):subprocess.run([sys.executable,*args],cwd=destination,check=True)
    run('-m','unittest','discover','-s','src','-p','test*.py');run('run_benchmark.py');run('src/baselines.py')
    for case in ['A01_shield','A03_burger_layers','A05_orange_juice_transparency','A10_restaurant_logo']:
        run('src/refine.py','--source',f'inputs/{case}.png','--svg',f'results/{case}/trial_07/output.svg','--config',f'results/{case}/trial_07/config.json','--output',f'refinement/{case}')
    run('src/extension.py','development');run('src/extension.py','holdout');run('summarize.py');run('src/render_check.py');run('src/test_color_contract.py','--output','reports/color_contract')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path,required=True);parser.add_argument('--run',action='store_true');args=parser.parse_args();target=prepare(args.destination);print('Prepared',target)
    if args.run:execute(target)
# END CHANGE DELIVERY-REPRODUCE | 2026-10-25T15:01:53Z | CREATED | Author: parent
