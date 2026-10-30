# START CHANGE AGD-ML-QA-TEST | 2026-10-30T08:20:00Z | CREATED | Author: ml_geometry_qa
"""Run packaged tests with explicit isolated dependency path, no package installs."""
from pathlib import Path
import os,subprocess,sys,json
W=Path.cwd()/'work';E=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01')
env=os.environ.copy();env['PYTHONPATH']=str(W/'geometry-deps')
r=subprocess.run([sys.executable,str(E/'test_stable_fit.py'),'-v'],env=env,capture_output=True,text=True,timeout=30)
(W/'ml_geometry/qa/SNAPSHOT_TESTS.json').write_text(json.dumps({'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'explicit_dependency_path':env['PYTHONPATH']},indent=2));print(r.stdout,r.stderr);assert r.returncode==0
# END CHANGE AGD-ML-QA-TEST | 2026-10-30T08:20:00Z | CREATED | Author: ml_geometry_qa
