# START CHANGE AGD-GROQ-GATE-QA | 2026-10-31T15:54:41Z | CREATED | Author: agentic_qa
"""Read-only preparation gate audit. No provider, credential or experiment run."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import hashlib
import json
import re

ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_GROQ_BURGER_PILOT_01')
gate=json.loads((ROOT/'LIVE_GATE.json').read_text())
preview=Path(gate['first_preview']['path'])
assert hashlib.sha256(preview.read_bytes()).hexdigest()==gate['first_preview']['sha256']
assert preview.stat().st_size==gate['first_preview']['bytes']
assert gate['first_preview']['permission']=='NOT_GIVEN'
assert gate['status']=='STOPPED_AT_LIVE_GATE'
assert gate['requests_made']==0 and gate['actual_cost_usd']==0
assert gate['AI_performance']=='NOT_TESTED'
assert gate['maximum_requests']==2 and gate['maximum_cost_usd']==0
assert gate['maximum_reserved_tokens_total']<=15000
assert gate['tool_calls']==12 and gate['commits']==2 and gate['candidates_per_edit']==2
assert gate['source_fit_gate_px']==.6
for key in ('account_model_access','account_free_only_billing','remaining_account_quota'):
    assert gate[key]=='NOT_VERIFIED'

class PilotGateLinkAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(value for key,value in attrs if key in ('href','src') and value)

links=PilotGateLinkAudit()
links.feed((ROOT/'review.html').read_text())
broken=[]
for value in links.links:
    url=urlparse(value)
    if url.scheme=='file':
        path=Path(unquote(url.path).lstrip('/'))
    elif url.scheme=='':
        path=ROOT/unquote(url.path)
    else:
        continue
    if not path.exists():
        broken.append(value)
assert not broken
assert not any(re.search(rb'gsk_[A-Za-z0-9_-]{20,}',p.read_bytes()) for p in ROOT.rglob('*') if p.is_file())
result=dict(status='PASSED_PREPARATION_ONLY',preview_sha256_verified=True,
    preview_bytes=preview.stat().st_size,dashboard_links=len(links.links),broken_links=broken,
    requests_executed_by_QA=0,credential_values_read_by_QA=0,
    live_readiness='BLOCKED',AI_performance='NOT_TESTED')
(Path(__file__).parent/'GATE_AUDIT.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
# END CHANGE AGD-GROQ-GATE-QA | 2026-10-31T15:54:41Z | CREATED | Author: agentic_qa
