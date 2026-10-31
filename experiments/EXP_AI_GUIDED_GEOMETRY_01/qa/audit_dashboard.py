# START CHANGE AGD-AGENTIC-QA-DASHBOARD | 2026-10-31T15:06:45Z | CREATED | Author: agentic_qa
"""Independent dashboard references and saved raster decodability audit."""
from pathlib import Path
from html.parser import HTMLParser
import json
from urllib.parse import unquote,urlparse
from PIL import Image

EXPERIMENT = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01')


class DashboardLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(value for key,value in attrs if key in ('src','href') and value)


report = dict(dashboards=[],pngs=0,broken=[])
for page in [EXPERIMENT/'review.html',Path.cwd()/'outputs/agentic_geometry_review/review.html']:
    if not page.exists():
        continue
    parser=DashboardLinks()
    parser.feed(page.read_text(encoding='utf-8'))
    local=0
    for value in parser.links:
        url=urlparse(value)
        if url.scheme not in ('','file') or not url.path:
            continue
        path=Path(unquote(url.path).lstrip('/')) if url.scheme=='file' else page.parent/unquote(url.path)
        if not path.exists():
            report['broken'].append(dict(page=str(page),reference=value))
        local+=1
    report['dashboards'].append(dict(path=str(page),local_references=local))
for path in EXPERIMENT.rglob('*.png'):
    with Image.open(path) as im:
        im.verify()
    report['pngs']+=1
(Path(__file__).parent/'DASHBOARD_AUDIT.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
assert not report['broken']
# END CHANGE AGD-AGENTIC-QA-DASHBOARD | 2026-10-31T15:06:45Z | CREATED | Author: agentic_qa
