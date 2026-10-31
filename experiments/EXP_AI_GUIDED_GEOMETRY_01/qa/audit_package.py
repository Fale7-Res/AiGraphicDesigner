# START CHANGE AGD-AGENTIC-QA-PACKAGE | 2026-10-31T15:01:23Z | CREATED | Author: agentic_qa
"""Read-only package inventory and secret-shaped token scan; never prints values."""
from pathlib import Path
import json
import re

ROOT = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01')
files = [p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc']
secret_files = []
for path in files:
    if path.suffix.lower() in ('.py','.json','.md','.txt','.html','.ps1','.log','.svg'):
        if re.search(rb'gsk_[A-Za-z0-9_-]{20,}',path.read_bytes()):
            secret_files.append(str(path.relative_to(ROOT)))
report = dict(files=len(files),bytes=sum(p.stat().st_size for p in files),
    largest_bytes=max((p.stat().st_size for p in files),default=0),
    files_over_50MiB=[str(p.relative_to(ROOT)) for p in files if p.stat().st_size>50*1024**2],
    credential_shaped_token_files=secret_files,
    forbidden_files=[str(p.relative_to(ROOT)) for p in files if p.name=='.env' or p.suffix in ('.onnx','.pt','.pth','.safetensors')])
(Path(__file__).parent/'PACKAGE_AUDIT.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
assert not secret_files and not report['files_over_50MiB'] and not report['forbidden_files']
# END CHANGE AGD-AGENTIC-QA-PACKAGE | 2026-10-31T15:01:23Z | CREATED | Author: agentic_qa
