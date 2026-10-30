# START CHANGE AGD-EXPORT-QA-VERIFY-FROZEN | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
import hashlib,json
from pathlib import Path
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_EXPORTER_DISCOVERY_01')
checks=[]
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from phase_b import digest
freeze=json.loads((ROOT/'FREEZE.json').read_text(encoding='utf-8'))
for rel,sha in freeze['files'].items():checks.append({'path':str(ROOT/rel),'expected':sha,'actual':digest(ROOT/rel)})
def visit(obj):
    if isinstance(obj,dict):
        if 'path' in obj and 'sha256' in obj:checks.append({'path':obj['path'],'expected':obj['sha256'],'actual':digest(obj['path'])})
        else:
            for value in obj.values():visit(value)
    elif isinstance(obj,list):
        for value in obj:visit(value)
visit(json.loads((ROOT/'BASELINE_PINS.json').read_text(encoding='utf-8')))
visit(json.loads((ROOT/'references/INHERITED_REFERENCE_PINS.json').read_text(encoding='utf-8')))
result={'checked':len(checks),'failures':[x for x in checks if x['expected']!=x['actual']],'checks':checks}
(Path(__file__).parent/'frozen_integrity.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
assert not result['failures'],result['failures']
print('PASS',len(checks),'frozen policy, source/candidate, dependency and reference hashes')

# END CHANGE AGD-EXPORT-QA-VERIFY-FROZEN | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
