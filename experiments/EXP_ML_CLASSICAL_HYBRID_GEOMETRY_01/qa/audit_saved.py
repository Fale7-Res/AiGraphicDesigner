# START CHANGE AGD-ML-INDEPENDENT-QA | 2026-10-30T08:05:08Z | CREATED | Author: ml_geometry_qa
"""Read-only candidate/inference audit. Writes only independent QA evidence."""
from pathlib import Path
import sys,json,hashlib,re,xml.etree.ElementTree as ET,subprocess
import numpy as np
from scipy.special import expit
import cv2
from PIL import Image
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01'
W=Path.cwd()/'work';OUT=W/'ml_geometry/qa';OUT.mkdir(exist_ok=True)
policy=json.loads((E/'protocol.json').read_text())
checks={'pins':[],'inference':[],'candidates':[],'errors':[]}
for name,record in policy['pins'].items():
    p=Path(name);ok=p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==record['sha256']
    checks['pins'].append({'path':name,'ok':ok})
    if not ok:checks['errors'].append('Frozen pin mismatch '+name)
weight=W/'ml_geometry/weights/edge_detection_dexined_2024sep.onnx'
checks['weight_sha256']=hashlib.sha256(weight.read_bytes()).hexdigest()
assert checks['weight_sha256']==policy['ML']['sha256']
cases=list(policy['cases'])
holdout=E/'reports/HOLDOUT_FREEZE.json'
if holdout.exists():cases += [x['case'] for x in json.loads(holdout.read_text())['cases']]
for case in cases:
    root=W/'ml_geometry/local_only'/case if case=='fine_features' else E/'results'/case
    pred=np.load(root/'ML/predictions.npz');meta=json.loads((root/'ML/inference.json').read_text())
    logits=pred['raw_outputs'];actual=pred['native_sigmoid'];expected=cv2.resize(expit(np.squeeze(logits[-1])),tuple(meta['native_size']),interpolation=cv2.INTER_LINEAR)
    error=float(np.max(np.abs(expected-actual)))
    checks['inference'].append({'case':case,'raw_shape':list(logits.shape),'finite':bool(np.isfinite(logits).all()),'sigmoid_reconstruction_max':error,'shape':list(actual.shape),'resolution':meta['inference_shape']})
    if error>1e-7:checks['errors'].append('Sigmoid transform mismatch '+case)
    for arm in ['Classical','ML','Hybrid']:
        folder=root/arm;p=folder/'construction.json'
        if not p.exists():continue
        report=json.loads(p.read_text());svg=ET.fromstring((folder/'stable.svg').read_text())
        tags=[x.tag.split('}')[-1] for x in svg.iter()]
        assert not any(x in tags for x in ['image','script','foreignObject','rect'])
        paths=svg.findall('{http://www.w3.org/2000/svg}path')
        assert len(paths)==len(report['accepted'])
        for node,item in zip(paths,report['accepted']):
            d=node.attrib['d'];commands=re.findall('[A-Za-z]',d)
            assert commands.count('M')==1 and commands.count('C')==len(item['curves'])
            assert node.attrib['fill']=='none'
            values=np.array([float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?',d)])
            curves=np.array(item['curves']);expected=np.concatenate([curves[0,0],curves[:,1:].reshape(-1)])
            assert np.array_equal(values,expected),'SVG commands differ from saved controls'
            assert all(np.array_equal(a[3],b[0]) for a,b in zip(curves,curves[1:]))
        image=OUT/(case+'_'+arm+'_native.png')
        subprocess.run([str(W/'resvg/resvg.exe'),str(folder/'stable.svg'),str(image)],check=True,capture_output=True,timeout=30)
        rgba=Image.open(image).convert('RGBA');white=Image.new('RGBA',rgba.size,'white');white.alpha_composite(rgba);white.convert('RGB').save(image.with_name(image.stem+'_white.png'))
        checks['candidates'].append({'case':case,'arm':arm,'paths':len(paths),'cubics':report['postfit']['cubics'],'stroke_widths':sorted(set(x.attrib['stroke-width'] for x in paths)),'rendered':True,'non_simple_fit_count':sum(not x['fit']['curve_is_simple_numerical'] for x in report['accepted'])})
(OUT/'AUDIT_SAVED.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2));assert not checks['errors']
# END CHANGE AGD-ML-INDEPENDENT-QA | 2026-10-30T08:05:08Z | CREATED | Author: ml_geometry_qa
