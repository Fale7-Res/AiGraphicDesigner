# START CHANGE AGD-EXPORT-QA-CHECK-SAVED-SVG-SEMANTICS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
"""Independent fontTools interpretation of all corrected compound graph exports."""
import json,sys,xml.etree.ElementTree as ET
from pathlib import Path
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_EXPORTER_DISCOVERY_01')
WORK=Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work')
def interp(data):
    pen=RecordingPen();parse_path(data,pen);p=o=None;segments=[]
    for cmd,args in pen.value:
        if cmd=='moveTo':p=o=args[0]
        elif cmd=='lineTo':segments.append(('L',p,args[0]));p=args[0]
        elif cmd=='curveTo':segments.append(('C',p,*args));p=args[-1]
        elif cmd=='closePath':
            if p!=o:segments.append(('L',p,o))
            p=o
        elif cmd!='endPath':raise AssertionError(cmd)
    return segments
def expected(chain,raw,forward):
    if raw:
        pts=list(map(tuple,chain['pixel_crack_vertices']));out=[('L',a,b) for a,b in zip(pts[:-1],pts[1:])]
    else:
        out=[]
        for s in chain['segments']:
            keys=('p0','p1','p2','p3') if s['type']=='C' else ('p0','p3')
            out.append((s['type'],*(tuple(s[k]) for k in keys)))
    if chain.get('closed') and out[-1][-1]!=out[0][1]:out.append(('L',out[-1][-1],out[0][1]))
    if not forward:out=[(s[0],*reversed(s[1:])) for s in reversed(out)]
    return out
checks=[];total_paths=total_segments=0
for case in json.loads((ROOT/'BASELINE_PINS.json').read_text())['cases']:
    folder=(WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case
    for name in ['O','R','B','A','RB']:
        graph=json.loads((folder/f'{name}.json').read_text());chains={c['id']:c for c in graph['chains']}
        for raw,kind in [(False,'regions'),(True,'raw_regions')]:
            path=folder/f'{name}_{kind}.svg'
            if not path.exists():continue
            for item in ET.parse(path).getroot():
                label=item.attrib['data-region'];want=[]
                for loop in graph['faces'][label]:
                    contour=[]
                    for ref in loop:contour+=expected(chains[ref['chain']],raw,ref['forward'])
                    if contour[-1][-1]!=contour[0][1]:contour.append(('L',contour[-1][-1],contour[0][1]))
                    want+=contour
                got=interp(item.attrib['d'])
                assert got==want,(case,name,kind,label,'command/control mismatch')
                assert item.attrib['fill-rule']=='evenodd'
                total_paths+=1;total_segments+=len(got)
            checks.append(str(path))
result={'corrected_svg_files':len(checks),'region_paths':total_paths,'parsed_segments':total_segments,
 'command_controls_equal_independent_graph_traversal':True,'files':checks,
 'limitations':'Exact directed-command semantic audit; not independent global topology or structural completeness.'}
(Path(__file__).parent/'saved_svg_semantics.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print({k:v for k,v in result.items() if k!='files'})

# END CHANGE AGD-EXPORT-QA-CHECK-SAVED-SVG-SEMANTICS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
