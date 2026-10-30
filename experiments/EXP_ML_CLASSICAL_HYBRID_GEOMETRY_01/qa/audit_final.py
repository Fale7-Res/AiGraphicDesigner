# START CHANGE AGD-ML-QA-FINAL | 2026-10-30T08:20:00Z | CREATED | Author: ml_geometry_qa
"""Read-only packaging, links, AST identity and holdout evidence checks."""
from pathlib import Path
import ast,json,hashlib
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
from PIL import Image
import numpy as np
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01';W=Path.cwd()/'work';Q=W/'ml_geometry/qa'
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ['href','src'] and v:self.links.append(v)
checks={'links':[],'source_AST':[],'holdouts':[],'images':0,'errors':[]}
for page in [E/'review.html',Path.cwd()/'outputs/ml_geometry_review/review.html']:
    p=Links();p.feed(page.read_text(encoding='utf8'));missing=[]
    for href in p.links:
        url=urlsplit(href)
        if url.scheme or href.startswith('#'):continue
        target=(page.parent/unquote(url.path)).resolve()
        if not target.exists():missing.append(href)
    checks['links'].append({'page':str(page),'references':len(p.links),'missing':missing})
    if missing:checks['errors'].append('Missing links '+str(page))
for name in ['infer_dexined.py','construct_geometry.py','evaluate_results.py','build_review.py','run_inference.py','run_construction.py','acquire_model.py']:
    a=E/name;b=W/'ml_geometry'/name
    same=ast.dump(ast.parse(a.read_text(encoding='utf8')))==ast.dump(ast.parse(b.read_text(encoding='utf8')))
    checks['source_AST'].append({'name':name,'AST_identical':same})
    if not same:checks['errors'].append('Execution/snapshot differs '+name)
a=E/'stable_fit.py';b=W/'ml_geometry/fitting_control/stable_fit.py'
assert ast.dump(ast.parse(a.read_text()))==ast.dump(ast.parse(b.read_text()))
for row in json.loads((E/'reports/HOLDOUT_FREEZE.json').read_text())['cases']:
    case=row['case'];p=E/'inputs'/case/'working.png';assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
    item={'case':case,'source_hash':True,'arms':[]}
    for arm in ['Classical','ML','Hybrid']:
        folder=E/'results'/case/arm;metrics=json.loads((folder/'metrics.json').read_text());construct=json.loads((folder/'construction.json').read_text())
        assert metrics['vector']['paths']==len(construct['accepted'])
        assert metrics['vector']['cubics']==sum(len(x['curves']) for x in construct['accepted'])
        for z in [1,4,16]:
            image=Image.open(folder/f'detail_{z}x.png');image.verify()
        item['arms'].append({'arm':arm,'paths':metrics['vector']['paths'],'cubics':metrics['vector']['cubics'],'pair_crossings':len(metrics['topology']['mutual_crossing_or_overlap_pairs'])})
    checks['holdouts'].append(item)
for p in E.rglob('*.png'):
    image=Image.open(p);image.verify();checks['images']+=1
unknown=[str(p.relative_to(E)) for p in E.rglob('*') if p.is_file() and ('fine_features' in p.parts or p.suffix in ['.onnx','.pt','.safetensors'])]
checks['unknown_rights_or_weights_paths']=unknown
if unknown:checks['errors'].append('Forbidden asset present')
(Q/'FINAL_ARTIFACT_AUDIT.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2));assert not checks['errors']
# END CHANGE AGD-ML-QA-FINAL | 2026-10-30T08:20:00Z | CREATED | Author: ml_geometry_qa
