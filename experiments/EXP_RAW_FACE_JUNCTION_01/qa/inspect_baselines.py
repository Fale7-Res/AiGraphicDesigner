# START CHANGE AGD-RAWFACE-QA-INSPECT-BASELINES | 2026-10-29T12:39:51Z | CREATED | Author: raw_face_qa
"""Read-only inherited face-walk audit, no construction or fitting."""
import sys,json,collections
from pathlib import Path
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path('work/geometry-deps').resolve()))
sys.path.insert(0,r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_COMPLETE_GEOMETRY_ISOLATION_01')
from shapely.geometry import Polygon
from shapely.validation import explain_validity
import geometry_eval as e
root=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_THIN_STRUCTURE_TOPOLOGY_01\results')
output={}
for case in ['A01_shield','G06_arabic','K01_linear_corner_hole','fine_features']:
 source=root/case/'baseline.json' if case!='fine_features' else Path('work/thin_structure_topology/external_results/fine_features/baseline.json')
 g=json.loads(source.read_text(encoding='utf-8'));chains={c['id']:c for c in g['chains']};raw={key:e.chain_points(c,True) for key,c in chains.items()};rows=[]
 for label,loops in g['faces'].items():
  if int(label)==0:continue
  for index,refs in enumerate(loops):
   p,gap=e.ring_points(refs,raw);poly=Polygon(p) if len(p)>=3 else Polygon()
   vertices=[tuple(raw[r['chain']][0 if r['forward'] else -1]) for r in refs]
   repeat=[{'vertex':list(k),'count':n} for k,n in collections.Counter(vertices).items() if n>1]
   allpoints=[tuple(x) for x in p[:-1]]
   internal_repeat=[list(k) for k,n in collections.Counter(allpoints).items() if n>1 and k not in set(vertices)]
   if not poly.is_valid or repeat or internal_repeat:
    rows.append({'face':label,'ring':index,'valid':poly.is_valid,'reason':explain_validity(poly),'area':e.signed_area(p),'endpoint_repeats':repeat,'internal_repeat_points':internal_repeat,'refs':len(refs),'gap':gap})
 output[case]={'chains':len(chains),'invalid':sum(not r['valid'] for r in rows),'endpoint_repeated_walks':sum(bool(r['endpoint_repeats']) for r in rows),'internal_repeated_walks':sum(bool(r['internal_repeat_points']) for r in rows),'rows':rows}
Path('work/raw_face_qa/baseline_face_audit.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
print(json.dumps({k:{x:v for x,v in a.items() if x!='rows'} for k,a in output.items()},indent=2))

# END CHANGE AGD-RAWFACE-QA-INSPECT-BASELINES | 2026-10-29T12:39:51Z | CREATED | Author: raw_face_qa
