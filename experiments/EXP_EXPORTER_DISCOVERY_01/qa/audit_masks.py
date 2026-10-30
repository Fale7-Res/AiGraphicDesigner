# START CHANGE AGD-EXPORT-QA-AUDIT-MASKS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
"""Passive decoding of saved SVG renders; independent IoU/topology recount."""
import json
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_EXPORTER_DISCOVERY_01')
WORK=Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work')
refs=json.loads((ROOT.parent/'EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/known_control_reference_manifest.json').read_text())['references']
def topo(mask):
    components=ndi.label(mask)[1]
    holes=ndi.label(ndi.binary_fill_holes(mask)&~mask)[1]
    return {'components_4_connected':int(components),'holes_4_connected':int(holes)}
def stats(truth,pred):
    return {'iou':float((truth&pred).sum()/(truth|pred).sum()),'pred_topology':topo(pred),'truth_topology':topo(truth)}
output={}
for case in ['fine_features','K01_linear_corner_hole','G06_arabic']:
    folder=(WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case
    if case=='G06_arabic':
        src=np.asarray(Image.open(folder/'working.png').convert('RGB')).astype(float)
        truth=np.repeat(np.repeat(np.linalg.norm(src-src[0,0],axis=2)>8,8,axis=0),8,axis=1)
    else:
        ref=next(r for r in refs if r['id']==case);truth=np.asarray(Image.open(ref['local_only_mask_path']).convert('L'))>=128
    output[case]={}
    for name in ['O','R','B','A','RB']:
        path=folder/(f'{name}_arabic_foreground.png' if case=='G06_arabic' else f'{name}_foreground_8x.png')
        pred=np.asarray(Image.open(path).convert('RGBA'))[...,3]>=128
        output[case][name]=stats(truth,pred)
    for label,file in [('proposal_only','proposals_8x.png'),('hypothetical_union','hypothetical_union.png')]:
        pred=np.asarray(Image.open(folder/'discovery'/file).convert('RGBA'))[...,3]>=128
        output[case][label]=stats(truth,pred)
(Path(__file__).parent/'mask_audit.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
print(json.dumps(output,indent=2))

# END CHANGE AGD-EXPORT-QA-AUDIT-MASKS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
