# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:59:34Z | CREATED | Author: universal_qa
"""Read-only final dashboard references and artifact inventory checks."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
root=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_UNIVERSAL_REGION_COHERENCE_01')
cwd=Path(__file__).resolve().parents[3]
pages=[root/'review.html',cwd/'outputs/universal_geometry_review/review.html']
rows=[];failures=[]

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key in ('href','src') and value:self.links.append(value)

for page in pages:
    parser=Links();parser.feed(page.read_text(encoding='utf-8'));count=0;bad=[];restricted=[]
    for ref in parser.links:
        link=urlsplit(ref)
        if not link.path or link.scheme not in ('','file'):continue
        if link.scheme=='file':
            raw=unquote(link.path)
            if raw.startswith('/') and len(raw)>2 and raw[2]==':':raw=raw[1:]
            path=Path(raw)
        else:path=page.parent/unquote(link.path)
        count+=1
        if not path.exists():bad.append(str(path))
        if page==root/'review.html' and 'fine_features' in str(path).lower():restricted.append(str(path))
    failures.extend(bad)
    failures.extend(restricted)
    rows.append({'page':str(page),'file_references':count,'broken':bad,'restricted_public_derivatives':restricted})
files=[p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
oversize=[str(p) for p in files if p.stat().st_size>50*1024**2]
disallowed=[str(p) for p in files if p.suffix.lower() in ('.onnx','.pt','.pth','.dll','.exe','.pyd') or p.name=='.env']
failures.extend(oversize+disallowed)
result={'pages':rows,'files':len(files),'total_bytes':sum(p.stat().st_size for p in files),
        'oversize_files_gt50MiB':oversize,'disallowed_artifacts':disallowed,
        'failures':failures,'passed':not failures,'publication_certified':False}
Path(__file__).with_name('DELIVERY_AUDIT.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'pages':len(rows),'references':sum(x['file_references'] for x in rows),
                  'files':len(files),'bytes':result['total_bytes'],'failures':failures[:20]}))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:59:34Z | CREATED | Author: universal_qa
