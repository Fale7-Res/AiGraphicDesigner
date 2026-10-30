# START CHANGE AGD-EXPORT-QA-AUDIT-ARTIFACTS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
"""Passive XML/PNG integrity; saved results only."""
import json,xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_EXPORTER_DISCOVERY_01')
EXT=Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\exporter_discovery\external_results')
svg_count=png_count=0;forbidden=[];errors=[]
for base in [ROOT/'results',ROOT/'phase_a',EXT]:
    for path in sorted(base.rglob('*')):
        try:
            if path.suffix=='.svg':
                svg_count+=1
                for element in ET.parse(path).getroot().iter():
                    if element.tag.rsplit('}',1)[-1] in ['image','script','foreignObject']:forbidden.append(str(path))
            elif path.suffix=='.png':
                png_count+=1
                with Image.open(path) as image:image.verify()
        except Exception as exc:errors.append({'path':str(path),'error':str(exc)})
report={'SVGs_parsed':svg_count,'PNGs_verified':png_count,'forbidden_elements':forbidden,'errors':errors,
 'limitations':'File decoding/XML integrity only; owner review and certified vector topology not implied. Legacy defective exports intentionally preserved.'}
(Path(__file__).parent/'artifact_audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
assert not errors and not forbidden,report
print(json.dumps(report))

# END CHANGE AGD-EXPORT-QA-AUDIT-ARTIFACTS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
