# START CHANGE AGD-TOOL-SESSIONS | 2026-10-31T11:55:00Z | CREATED | Author: root
"""Matched offline controllers; mock is explicitly not pretrained inference."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import sys,json,time,copy,hashlib,shutil
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');W=Path.cwd()/'work';E=R/'experiments/EXP_AI_GUIDED_GEOMETRY_01';U=R/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01';L=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'
sys.path[:0]=[str(E),str(U),str(L),str(W/'geometry-deps')]
import numpy as np
from PIL import Image
from geometry_engine import GeometryToolEngine,geometry_digest
from universal_run import new_classical,construct_condition
from construct_geometry import chain_graph
from svg_exporter import svg_graph
from monitor import supervise

def run_controller(engine,kind):
 """Fixed policy before benchmark. Every action uses the same dispatch contract."""
 rois=[[0,0,1,1],[0,0,1,1]] if kind=='B' else [[0,0,1,.5],[0,.5,1,1]]
 for roi in rois:
  engine.dispatch('inspect_region',{'roi':roi});found=engine.dispatch('get_candidates',{'roi':roi,'limit':16});ids=[x['trace_id'] for x in found['candidates'] if x['eligible']][:2]
  if ids:
   staged=engine.dispatch('stage_candidates',{'trace_ids':ids})
   engine.dispatch('commit_change' if staged.get('added_paths',0) else 'rollback_change',{})
  else:
   engine.dispatch('validate_geometry',{});engine.dispatch('validate_geometry',{})
  engine.dispatch('render_geometry',{'scale':1})
 engine.dispatch('validate_geometry',{});engine.dispatch('render_geometry',{'scale':4})
 return engine.export_state()

def session_worker(case):
 protocol=json.loads((E/'protocol.json').read_text());cfg=protocol['cases'][case];out=E/'results'/case;out.mkdir(exist_ok=False);rgb=np.asarray(Image.open(cfg['source']).convert('RGB'));h,w=rgb.shape[:2];shutil.copy2(cfg['source'],out/'source.png');start=time.monotonic()
 if cfg.get('baseline'):
  frozen=json.loads(Path(cfg['traces']).read_text());p=json.loads(Path(cfg['baseline']).read_text());shutil.copy2(cfg['baseline_svg'],out/'A.svg')
 else:
  frozen,_,_=new_classical(rgb);p=construct_condition(frozen,'P',time.monotonic()+120);(out/'A.svg').write_text(svg_graph(chain_graph(p['accepted'],w,h)),encoding='utf-8')
 (out/'frozen_traces.json').write_text(json.dumps(frozen),encoding='utf-8');(out/'A.json').write_text(json.dumps(dict(accepted=p['accepted'])),encoding='utf-8')
 for kind in ['B','M']:
  eng=GeometryToolEngine(rgb,frozen['traces'],p['accepted'],out/kind,R,W);result=run_controller(eng,kind);result.update(controller='deterministic_fullframe' if kind=='B' else 'MOCK_FIXED_PLAN_NOT_AI',decision_hash=eng.replay_decision_hash(),tool_events=eng.events,api_requests=0,actual_api_cost_usd=0,AI_performance='NOT_TESTED');(out/(kind+'.json')).write_text(json.dumps(result),encoding='utf-8')
  last=next(ev['result'] for ev in reversed(eng.events) if ev['tool']=='render_geometry' and ev['status']=='ok');shutil.copy2(out/kind/last['svg'],out/(kind+'.svg'))
  if kind=='M':
   replay=GeometryToolEngine(rgb,frozen['traces'],p['accepted'],out/'replay_M',R,W)
   for event in eng.events:replay.dispatch(event['tool'],event['arguments'])
   assert replay.state_hash()==eng.state_hash();assert replay.replay_decision_hash()==eng.replay_decision_hash();(out/'REPLAY.json').write_text(json.dumps(dict(passed=True,geometry_hash=result['state_hash'],decision_hash=result['decision_hash'],events=len(eng.events),runtime_hashes_expected_to_differ=True)))
 (out/'C_STATUS.json').write_text(json.dumps(dict(AI_performance='NOT_TESTED',live_requests=0,reason='Account free-tier/quota/no-charge state unverified. No pasted credential used.')))
 (out/'WORKER.json').write_text(json.dumps(dict(wall_seconds=time.monotonic()-start,case=case,conditions=['A','B','M'],C='NOT_TESTED')));print(case,'completed',flush=True)

def launch_sessions():
 protocol=json.loads((E/'protocol.json').read_text());results=[]
 for file,pin in protocol['pins'].items():assert hashlib.sha256(Path(file).read_bytes()).hexdigest()==pin['sha256'],file
 for case in protocol['cases']:
  result=supervise([sys.executable,Path(__file__),case],E/'reports'/(case+'.log'));results.append(dict(case=case,**result));(E/'reports/RESOURCES.json').write_text(json.dumps(results,indent=2));print(case,result['status'],result['wall_seconds'],result['sampled_tree_RSS_peak_mib'],flush=True)
if __name__=='__main__':
 if len(sys.argv)>1:session_worker(sys.argv[1])
 else:launch_sessions()
# END CHANGE AGD-TOOL-SESSIONS | 2026-10-31T11:55:00Z | CREATED | Author: root
