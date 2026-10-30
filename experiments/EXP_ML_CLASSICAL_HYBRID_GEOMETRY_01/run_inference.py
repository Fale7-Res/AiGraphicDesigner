# START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
from pathlib import Path
import subprocess,psutil,time,sys,json
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01';W=Path.cwd()/'work'
existing=E/'reports/INFERENCE_RESOURCES.json'
records=json.loads(existing.read_text()) if existing.exists() else []
cases=json.loads((E/'protocol.json').read_text())['cases']
if (E/'reports/HOLDOUT_FREEZE.json').exists():cases += [x['case'] for x in json.loads((E/'reports/HOLDOUT_FREEZE.json').read_text())['cases']]
for case in cases:
    root=W/'ml_geometry/local_only'/case if case=='fine_features' else E/'inputs'/case
    out=W/'ml_geometry/local_only'/case/'ML' if case=='fine_features' else E/'results'/case/'ML'
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():print(case,'preserved existing',flush=True);continue
    if psutil.virtual_memory().available<700*2**20:raise RuntimeError('Insufficient available memory to start')
    log=out.parent/'inference.log';start=time.monotonic();peak=0;status='COMPLETED';minimum=psutil.virtual_memory().available
    with log.open('w') as f:
        process=subprocess.Popen([sys.executable,str(W/'ml_geometry/infer_dexined.py'),str(root/'working.png'),str(W/'ml_geometry/weights/edge_detection_dexined_2024sep.onnx'),str(out)],stdout=f,stderr=subprocess.STDOUT)
        while process.poll() is None:
            try:
                p=psutil.Process(process.pid);rss=sum(x.memory_info().rss for x in [p]+p.children(recursive=True));peak=max(peak,rss)
            except psutil.Error:pass
            minimum=min(minimum,psutil.virtual_memory().available)
            if peak>1536*2**20 or minimum<700*2**20 or time.monotonic()-start>180:
                status='STOPPED_RESOURCE';process.kill();break
            time.sleep(.1)
        code=process.wait()
    record={'case':case,'status':status if code==0 or status!='COMPLETED' else 'FAILED','exit_code':code,'wall_seconds':time.monotonic()-start,'sampled_tree_RSS_peak_mib':peak/2**20,'minimum_available_mib':minimum/2**20,'sampling_interval_seconds':.1}
    records.append(record);(E/'reports/INFERENCE_RESOURCES.json').write_text(json.dumps(records,indent=2));print(record,flush=True)
    if status=='STOPPED_RESOURCE':break

# END CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
