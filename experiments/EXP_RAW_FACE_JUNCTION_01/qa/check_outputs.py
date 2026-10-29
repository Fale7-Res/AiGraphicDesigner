# START CHANGE AGD-RAWFACE-QA-CHECK-OUTPUTS | 2026-10-29T12:39:51Z | CREATED | Author: raw_face_qa
import json,sys,hashlib,collections
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np
sys.path[:0]=[str(Path('work/geometry-deps').resolve()),r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_COMPLETE_GEOMETRY_ISOLATION_01']
from shapely.geometry import Polygon
import geometry_eval as e
from PIL import Image
p=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_RAW_FACE_JUNCTION_01')
summary={}
def occurrence(g):return {f:collections.Counter((r['chain'],r['forward']) for w in rings for r in w) for f,rings in g['faces'].items()}
for case in ['fine_features','G06_arabic','A01_shield','K01_linear_corner_hole']:
 root=Path('work/raw_face_junction/external_results')/case if case=='fine_features' else p/'results'/case
 gs={name:json.loads((root/f'{name}.json').read_text(encoding='utf-8')) for name in ['O','R','B']}
 a,b=gs['O'],gs['R'];assert a['chains']==b['chains'];assert occurrence(a)==occurrence(b)
 assert {k:v for k,v in a.items() if k!='faces'}=={k:v for k,v in b.items() if k!='faces'}
 rows={}
 for name,g in gs.items():
  raw={c['id']:e.chain_points(c,True) for c in g['chains']};bad=0;count=0;area=collections.defaultdict(float)
  for f,rings in g['faces'].items():
   for w in rings:
    coords,gap=e.ring_points(w,raw);ar=e.signed_area(coords);area[f]+=ar
    if int(f)!=0:count+=1;bad+=not (Polygon(coords).is_valid and abs(ar)>1e-6 and gap<=.001)
  rows[name]={'raw_invalid':bad,'raw_rings':count,'per_face_signed_area':dict(area)}
 assert all(abs(rows['O']['per_face_signed_area'][k]-rows['R']['per_face_signed_area'][k])<=1e-9 for k in rows['O']['per_face_signed_area'])
 audit=json.loads((root/'R_audit.json').read_text(encoding='utf-8'))
 assert all(abs(m['raw_area_before']-sum(q['raw_signed_area'] for q in m['parts']))<=1e-9 for m in audit['mapping'])
 control=json.loads((root/'MATCHED_CONTROLS.json').read_text(encoding='utf-8'))
 assert (root/'RB.json').exists()==control['RB_permitted']
 if control['RB_permitted']:
  rb=json.loads((root/'RB.json').read_text(encoding='utf-8'));assert rb==gs['B']
 summary[case]={'raw_statistics':{n:{k:v for k,v in d.items() if k!='per_face_signed_area'} for n,d in rows.items()},'split_count':audit['splits'],'chain_and_metadata_equality':True,'directed_occurrences':True,'per_label_signed_area':True,'per_walk_signed_area':True,'RB_permitted':control['RB_permitted'],'RB_equals_old_B':control['RB_permitted']}
Path('work/raw_face_qa/output_integrity.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))

# END CHANGE AGD-RAWFACE-QA-CHECK-OUTPUTS | 2026-10-29T12:39:51Z | CREATED | Author: raw_face_qa
