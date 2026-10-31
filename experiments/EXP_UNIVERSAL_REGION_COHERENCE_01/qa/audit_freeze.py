# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:51:17Z | EDITED | Author: universal_qa
"""Independently verify protocol source bytes without constructing candidates."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

experiment = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_UNIVERSAL_REGION_COHERENCE_01')
protocol = json.loads((experiment/'protocol.json').read_text(encoding='utf-8'))
rows = []
for filename, expected in protocol['pins'].items():
    path = Path(filename)
    data = path.read_bytes() if path.exists() else None
    actual = hashlib.sha256(data).hexdigest() if data is not None else None
    rows.append({'path': filename, 'match': actual == expected['sha256'],
                 'actual_sha256': actual, 'expected_sha256': expected['sha256'],
                 'size_match': data is not None and len(data) == expected['bytes']})
result = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'pins': rows,
          'all_match': all(row['match'] and row['size_match'] for row in rows),
          'protocol_sha256': hashlib.sha256((experiment/'protocol.json').read_bytes()).hexdigest(),
          'candidate_execution_performed_by_qa': False}
Path(__file__).with_name('FREEZE_AUDIT.json').write_text(json.dumps(result, indent=2))
print(json.dumps({'pins': len(rows), 'all_match': result['all_match'],
                  'mismatches': [row['path'] for row in rows if not row['match'] or not row['size_match']]}))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:51:17Z | EDITED | Author: universal_qa
