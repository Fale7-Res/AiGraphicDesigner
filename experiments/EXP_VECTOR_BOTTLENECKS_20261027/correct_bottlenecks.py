"""Paired coverage intervention at uniform detail192; every result retained."""
# START CHANGE AGD-BOTTLENECK-CORRECTION | 2026-10-28T03:34:28Z | EDITED | Author: root
from pathlib import Path
import argparse,json,sys,time
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT));import bottlenecks as b
from coverage import correct_coverage

def corrected_case(case):
    source=ROOT/'results/granularity'/case['id'];baseline=source/'192/D/output.svg'
    out=ROOT/'results/corrections'/case['id'];out.mkdir(parents=True,exist_ok=True)
    if (out/'result.json').exists():
        saved=json.loads((out/'result.json').read_text())
        assert b.inherited.digest(out/'output.svg')==saved['sha256']
        assert b.inherited.digest(baseline)==saved['baseline_svg_sha256']
        return
    if any(out.iterdir()):raise FileExistsError('Preserve partial correction evidence')
    start=time.perf_counter();change=correct_coverage(baseline,out/'output.svg',.25)
    row=b.inherited.evaluate_condition(source/'source.png',out/'output.svg',out)
    old=json.loads((source/'result.json').read_text())['levels']['192']['conditions']['D']
    original=ET.parse(baseline).getroot();modified=ET.parse(out/'output.svg').getroot()
    def signature(root):
        for node in root.iter():
            for key in ['stroke','stroke-width','stroke-linejoin','stroke-linecap','paint-order']:node.attrib.pop(key,None)
        return ET.tostring(root,encoding='utf-8')
    assert signature(original)==signature(modified)
    original_alpha=np.asarray(Image.open(source/'192/D/render.png').convert('RGBA'))[:,:,3]
    new_alpha=np.asarray(Image.open(out/'render.png').convert('RGBA'))[:,:,3]
    target=np.asarray(Image.open(source/'source.png').convert('RGBA'))[:,:,3]
    row.update(baseline_detail=192,baseline_svg_sha256=b.inherited.digest(baseline),baseline_metrics=old['metrics'],
       correction=change,delta={bg:{key:row['metrics'][bg][key]-old['metrics'][bg][key] for key in ['ssim','mse','worst_32px_tile_rmse']} for bg in ['white','black','bluegray']},
       alpha_support={'baseline_alpha_mae':float(np.abs(target.astype(float)-original_alpha).mean()),'new_alpha_mae':row['alpha_mae'],
       'new_support_pixels_source_alpha_zero':int(((target==0)&(new_alpha>0)).sum()),'baseline_support_pixels_source_alpha_zero':int(((target==0)&(original_alpha>0)).sum()),
       'alpha_increase_pixels':int((new_alpha>original_alpha).sum()),'alpha_decrease_pixels':int((new_alpha<original_alpha).sum())},
       wall_seconds=time.perf_counter()-start,interpretation='Same path d/order/fills/masks, explicitly overlapping narrowstrokes. Coverage can improve while contours/colors worsen. Not topology repair or accepted default.',architecture='NOT_APPROVED')
    b.inherited.save_json(out/'result.json',row)
    print('CORRECTION',case['id'],row['delta']['white'],'alpha',row['alpha_support'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--case');a=p.parse_args();cases=json.loads((ROOT/'inputs/manifest.json').read_text())['cases']
    for c in cases:
        if not a.case or a.case==c['id']:corrected_case(c)
# END CHANGE AGD-BOTTLENECK-CORRECTION | 2026-10-28T03:34:28Z | EDITED | Author: root
