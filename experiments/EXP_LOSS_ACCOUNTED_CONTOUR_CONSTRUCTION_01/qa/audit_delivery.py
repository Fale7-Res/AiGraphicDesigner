# START CHANGE AGD-CONTOUR-QA-DELIVERY | 2026-10-30T08:58:04Z | CREATED | Author: contour_qa
"""Read-only frozen source, topology-control, delivery and resource audit."""
import ast,hashlib,json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlparse
W=Path(__file__).resolve().parents[2];sys.path.insert(0,str(W/'geometry-deps'))
import numpy as np
from PIL import Image
from shapely.geometry import Polygon
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'
protocol=json.loads((E/'protocol.json').read_text());matches=[];coverage=[];nesting=[]
t=np.linspace(0,1,129);B=np.stack([(1-t)**3,3*(1-t)**2*t,3*(1-t)*t*t,t**3],1)
for case,config in protocol['cases'].items():
 for arm in protocol['arms']:
  base=(W/'contour_construction/local_only'/case if case=='fine_features' else E/'results'/case)/arm
  source=Path(config['base'])/arm
  assert (base/'O.svg').read_bytes()==(source/'stable.svg').read_bytes();matches.append([case,arm])
  old=json.loads((source/'construction.json').read_text());traces={x['trace_id']:x for x in old['traces']}
  sk=np.load(source/'discovery.npz')['skeleton'];points={tuple(v) for trace in old['traces'] for v in trace['source_points_xy']}
  omitted=[(float(x)+.5,float(y)+.5) for y,x in np.argwhere(sk) if (float(x)+.5,float(y)+.5) not in points]
  isolated=[]
  for x,y in omitted:
   yi,xi=int(y-.5),int(x-.5);window=sk[max(0,yi-1):yi+2,max(0,xi-1):xi+2]
   isolated.append(int(window.sum())==1)
  assert all(isolated),(case,arm,omitted)
  coverage.append({'case':case,'arm':arm,'skeleton_vertices_absent_from_source_traces':len(omitted),'all_omitted_vertices_isolated':all(isolated)})
  if case.startswith('K01'):
   rawpolys={i:Polygon(trace['source_points_xy']) for i,trace in traces.items()}
   for condition in ['P','Q']:
    data=json.loads((base/(condition+'.json')).read_text());fitted={}
    for chain in data['accepted']:
     if not chain['closed']:continue
     q=np.einsum('tk,nkd->ntd',B,np.array(chain['curves'])).reshape(-1,2);fitted[chain['trace_id']]=Polygon(q)
    relationships=[]
    for i in rawpolys:
     for j in rawpolys:
      if i==j:continue
      if i not in fitted or j not in fitted:continue
      raw,fittedrelation=rawpolys[i].contains(rawpolys[j]),fitted[i].contains(fitted[j])
      assert raw==fittedrelation
      relationships.append({'outer_trace':i,'inner_trace':j,'raw_contains':raw,'fitted_contains':fittedrelation})
    nesting.append({'arm':arm,'condition':condition,'raw_valid':all(x.is_valid for x in rawpolys.values()),'closed_fitted':len(fitted),'fitted_valid':all(x.is_valid for x in fitted.values()),'relationships':relationships,'claim_limit':'Closed contour containment only; no filled region or hole ownership inferred.'})
resources=json.loads((E/'reports/CONSTRUCTION_RESOURCES.json').read_text());assert len(resources)==18
assert all(x['status']=='COMPLETED' and x['exit_code']==0 and x['sample_count']>0 and len(x['observed_pid_peak_bytes'])>=2 for x in resources)
assert all(x['sampled_tree_RSS_peak_mib']<768 and x['wall_seconds']<300 for x in resources)
astmatches=[]
for source,target in [(W/'contour_construction/run_case.py',E/'run_case.py'),(W/'contour_construction/monitor.py',E/'monitor.py'),(W/'contour_construction/implementation/partition_fit.py',E/'partition_fit.py')]:
 assert ast.dump(ast.parse(source.read_text()))==ast.dump(ast.parse(target.read_text()));astmatches.append(target.name)
pngs=[]
for path in E.rglob('*.png'):
 with Image.open(path) as im:im.verify()
 pngs.append(str(path.relative_to(E)))
out={'saved_O_identical_count':len(matches),'stage0_skeleton_coverage':coverage,'known_control_nesting':nesting,'resource_workers':len(resources),'resource_max_sampled_tree_RSS_mib':max(x['sampled_tree_RSS_peak_mib'] for x in resources),'resource_total_wall_seconds':sum(x['wall_seconds'] for x in resources),'packaged_execution_AST_matches':astmatches,'PNG_decode_count':len(pngs)}
(Path(__file__).parent/'DELIVERY_AUDIT.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ['stage0_skeleton_coverage','known_control_nesting']},indent=2))
# END CHANGE AGD-CONTOUR-QA-DELIVERY | 2026-10-30T08:58:04Z | CREATED | Author: contour_qa
