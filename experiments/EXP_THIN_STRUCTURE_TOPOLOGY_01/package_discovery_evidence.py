# START CHANGE AGD-THIN-PACKAGE-EVIDENCE | 2026-10-29T11:43:50Z | CREATED | Author: root
from pathlib import Path
import sys,json,datetime,hashlib
import numpy as np
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent
sys.path.insert(0,str(r));sys.dont_write_bytecode=True
from study import CASES,destination,dump
rows=json.loads((r/'reports/SUMMARY.json').read_text(encoding='utf-8'))
decision={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'executed':False,'policy_unchanged':True,'fine_features':'A accepted zero bridges; B accepted zero repairs. Both independent prerequisites fail.','A01_shield':'B accepted zero repairs. A changes are outside dedicated crown ROI and do not demonstrate missing crown recovery.','conclusion':'Do not execute combined condition under frozen same-case gate; no parameters or thresholds retuned.'}
dump(r/'reports/COMBINED_DECISION.json',decision)
compact=[]
for case in CASES:
 out=destination(case)
 a=json.loads((out/'A_audit.json').read_text(encoding='utf-8'))
 im=Image.open(out/'working.png').convert('RGB');draw=ImageDraw.Draw(im)
 for bridge in a['bridges']:
  path=[(x,y) for y,x in bridge['path']];draw.line(path,fill='#ff0033',width=2)
  for p in [bridge['endpoint_a'],bridge['endpoint_b']]:
   x,y=p;draw.ellipse((x-3,y-3,x+3,y+3),outline='#00aaff',width=1)
 im.save(out/'A_bridge_locations.png')
 # Coordinate arrays are not images: remove misleading automatic array visualization
 # from dashboard enumeration without deleting preserved worker evidence.
 for m in [x for x in rows if x['case']==case]:
  full=json.loads((out/(m['condition']+'_metrics.json')).read_text(encoding='utf-8'))
  compact.append({k:full.get(k) for k in ['case','condition','microgeometry','visible_microgeometry','shield_components','arabic_source_proxy','render_wall_seconds','coverage']})
dump(r/'reports/DETAIL_DIAGNOSTICS.json',compact)
for item in compact:
 print(json.dumps(item,ensure_ascii=True))

# END CHANGE AGD-THIN-PACKAGE-EVIDENCE | 2026-10-29T11:43:50Z | CREATED | Author: root
