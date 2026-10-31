# START CHANGE AGD-AGENTIC-QA-FREEZE | 2026-10-31T15:12:48Z | EDITED | Author: agentic_qa
"""Read-only independent byte-pin and pre-execution check."""
from pathlib import Path
import hashlib
import json
from datetime import datetime,timezone

EXPERIMENT = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01')
protocol = json.loads((EXPERIMENT/'protocol.json').read_text())
errors = []
for name,pin in protocol['pins'].items():
    path = Path(name)
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin['sha256'] or path.stat().st_size != pin['bytes']:
        errors.append(name)
summary = dict(pins=len(protocol['pins']), errors=errors,
    frozen=protocol.get('candidate_code_frozen_utc'),
    case_results_present=bool(list((EXPERIMENT/'results').iterdir())))
print(json.dumps(summary,indent=2))
print((EXPERIMENT/'qa/UNIT_TESTS.txt').read_text())
assert not errors
snapshot = {'verified_at_utc':datetime.now(timezone.utc).isoformat(),'all_protocol_pins_match':not errors,'files':{}}
for name in ('geometry_engine.py','run_sessions.py','groq_adapter.py'):
    path=EXPERIMENT/name
    current={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}
    snapshot['files'][name]=dict(current,unchanged_from_frozen_protocol=current==protocol['pins'][str(path)])
(Path(__file__).parent/'FINAL_FROZEN_SOURCE_SNAPSHOT.json').write_text(json.dumps(snapshot,indent=2))
print(json.dumps(snapshot,indent=2))
# END CHANGE AGD-AGENTIC-QA-FREEZE | 2026-10-31T15:12:48Z | EDITED | Author: agentic_qa
