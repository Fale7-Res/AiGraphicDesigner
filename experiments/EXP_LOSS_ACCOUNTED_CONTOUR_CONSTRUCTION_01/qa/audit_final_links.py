# START CHANGE AGD-CONTOUR-QA-FINAL-LINKS | 2026-10-30T15:17:03Z | CREATED | Author: contour_qa
"""Read-only final dashboard and separately frozen CAP512 evidence audit."""
import hashlib,json,subprocess
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlparse
from xml.etree import ElementTree as ET
W=Path(__file__).resolve().parents[2];E=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01')
freeze=json.loads((E/'reports/CAP512_DIAGNOSTIC_FREEZE.json').read_text())
assert hashlib.sha256((W/'contour_construction/cap_control.py').read_bytes()).hexdigest()==freeze['source_code_sha256']
cap=[]
for arm in freeze['arms']:
 folder=E/'results/K01_linear_corner_hole'/arm
 data=json.loads((folder/'CAP512.json').read_text());assert len(data['records'])==3
 assert data['not_main_condition'] and data['accepted']==[]
 assert all(x['new_status']=='deviation_budget' and x['meta']['numerical_upper_envelope_px']>.6 for x in data['records'])
 root=ET.parse(folder/'CAP512.svg').getroot();assert len(root)==0
 subprocess.run([str(W/'resvg/resvg.exe'),str(folder/'CAP512.svg'),str(Path(__file__).parent/(arm+'_CAP512.png'))],check=True,capture_output=True)
 cap.append({'arm':arm,'source_trace_ids':[x['trace_id'] for x in data['records']],'accepted':0,'deviation_rejected':3,'wall_seconds':data['wall_seconds']})
class Links(HTMLParser):
 def __init__(self):super().__init__();self.items=[]
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('src','href') and value:self.items.append(value)
checks=[]
protocol=json.loads((E/'protocol.json').read_text());metric_checks=0
for case,config in protocol['cases'].items():
 for arm in protocol['arms']:
  base=(W/'contour_construction/local_only'/case if case=='fine_features' else E/'results'/case)/arm
  old=json.loads((Path(config['base'])/arm/'metrics.json').read_text())
  current=json.loads((base/'O_metrics.json').read_text())
  if 'boundary_1_25px' in old:
   for stage in ['raw_all','fitted']:assert old['boundary_1_25px'][stage]==current['boundary_1_25px'][stage]
  if 'critical_guides' in old:
   for a,b in zip(old['critical_guides'],current['critical_guides']):assert a['id']==b['id'] and a['fitted']==b['fitted'] and a['raw']==b['raw']
  metric_checks+=1
for path in [E/'review.html',W.parent/'outputs/contour_construction_review/review.html']:
 parser=Links();parser.feed(path.read_text(encoding='utf-8'));broken=[];local=0
 for value in parser.items:
  if value.startswith(('#','http:','https:','data:','javascript:')):continue
  parsed=urlparse(value);link=unquote(parsed.path)
  if parsed.scheme=='file':
   if link.startswith('/') and len(link)>2 and link[2]==':':link=link[1:]
   target=Path(link)
  else:target=path.parent/link
  local+=1
  if not target.exists():broken.append({'href':value,'resolved':str(target)})
 checks.append({'path':str(path),'local_links':local,'broken':broken})
 assert not broken,checks[-1]
out={'saved_O_metric_case_arm_matches':metric_checks,'CAP512_code_pin_matches':True,'CAP512_frozen_utc':freeze['utc'],'CAP512_results':cap,'CAP512_interpretation':'Raising whole-trace cubic cap64to512 alone still rejects all9K01traces at unchanged .6deviation/8rounds. Does not prove generic partition superiority or optimized periodic fit necessity.','dashboards':checks}
(Path(__file__).parent/'FINAL_LINKS_CAP_AUDIT.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
# END CHANGE AGD-CONTOUR-QA-FINAL-LINKS | 2026-10-30T15:17:03Z | CREATED | Author: contour_qa
