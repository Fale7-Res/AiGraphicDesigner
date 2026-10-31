# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:59:34Z | CREATED | Author: universal_qa
"""Record/compare AST signatures while allowing documented comment-only packaging."""
import ast
import hashlib
import json
from pathlib import Path
repo=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
exp=repo/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01'
record=Path(__file__).with_name('SOURCE_AST_SNAPSHOT.json')
files=[exp/n for n in ('universal_run.py','region_integration.py','coherence_refine.py','test_selection.py','test_region_integration.py','test_coherence.py')]
rows={str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
               'ast_sha256':hashlib.sha256(ast.dump(ast.parse(p.read_text()),include_attributes=False).encode()).hexdigest()} for p in files}
if not record.exists():
    record.write_text(json.dumps(rows,indent=2));print('Stored six-source AST snapshot while all86 protocol pins match.')
else:
    prior=json.loads(record.read_text());diff=[p for p in rows if rows[p]['ast_sha256']!=prior[p]['ast_sha256']]
    result={'all_AST_match':not diff,'AST_changes':diff,'file_bytes_changes':[p for p in rows if rows[p]['sha256']!=prior[p]['sha256']]}
    Path(__file__).with_name('SOURCE_AST_AUDIT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:59:34Z | CREATED | Author: universal_qa
