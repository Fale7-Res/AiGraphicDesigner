# START CHANGE AGD-ISOLATION-VERIFY-DELIVERY | 2026-10-29T06:58:24Z | CREATED | Author: root
"""Read-only byte-integrity and immutable-reference verification."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
inventory=json.loads((root/'reports/ARTIFACT_INVENTORY.json').read_text(encoding='utf-8'))
errors=[]
for item in inventory:
    path=root/item['path']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:
        errors.append(item['path'])
print(json.dumps({'verified_files':len(inventory),'errors':errors,'status':'FAIL' if errors else 'PASS'},indent=2))
sys.exit(bool(errors))

# END CHANGE AGD-ISOLATION-VERIFY-DELIVERY | 2026-10-29T06:58:24Z | CREATED | Author: root
