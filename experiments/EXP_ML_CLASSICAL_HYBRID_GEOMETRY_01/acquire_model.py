# START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
from pathlib import Path
import urllib.request,hashlib,json,time,shutil
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01';C=Path('work/ml_geometry/weights');C.mkdir(parents=True,exist_ok=True)
revision='01a752eb4006688376e576dc24941c54608f6dd0';name='edge_detection_dexined_2024sep.onnx';url=f'https://huggingface.co/opencv/edge_detection_dexined/resolve/{revision}/{name}'
expected='a50d01dc8481549c7dedb9eb3e0123b810a016520df75e4669a504609982cdd0';p=C/name
if not p.exists():
    start=time.monotonic()
    with urllib.request.urlopen(url,timeout=90) as response,p.open('wb') as out:shutil.copyfileobj(response,out)
    print('Download seconds',time.monotonic()-start)
sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==expected and p.stat().st_size==47235563
record={'url':url,'revision':revision,'sha256':sha,'bytes':p.stat().st_size,'cache_path':str(p.resolve()),'license_url':f'https://huggingface.co/opencv/edge_detection_dexined/blob/{revision}/LICENSE','format':'ONNX only; no checkpoint Python execution','code_license':'MIT per upstream model directory','weight_license':'MIT declared for all files in model directory; preserved upstream LICENSE','downloaded':True}
(E/'reports/MODEL_PROVENANCE.json').write_text(json.dumps(record,indent=2))
shutil.copy2('work/ml_geometry/model_selection/LICENSE',E/'reports/DEXINED_LICENSE.txt')
publisher=Path('outputs/ml_geometry_review');publisher.mkdir(parents=True,exist_ok=True)
s=Path('outputs/exporter_discovery_review/Publish-Research.ps1').read_text(encoding='utf-8').replace('EXP_EXPORTER_DISCOVERY_01','EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01').replace('Preserve SVG exporter and source-driven discovery evidence','Record controlled pretrained ML geometry research')
(publisher/'Publish-Research.ps1').write_text(s,encoding='utf-8')
print(json.dumps(record,indent=2))

# END CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
