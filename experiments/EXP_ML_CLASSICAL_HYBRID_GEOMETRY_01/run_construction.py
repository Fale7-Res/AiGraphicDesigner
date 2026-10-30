# START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
from pathlib import Path
import subprocess,psutil,time,sys,json,hashlib
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01';W=Path.cwd()/'work'
files=[W/'ml_geometry/construct_geometry.py',W/'ml_geometry/fitting_control/stable_fit.py']
(E/'reports/CONSTRUCTION_FREEZE.json').write_text(json.dumps({'utc':time.time(),'files':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'policy':'No case-specific parameters or evaluator inputs.120seconds per arm,384seconds per case,768MiB monitor; stable_fit30s local bound; source masks never geometry truth.'},indent=2))
existing=E/'reports/CONSTRUCTION_RESOURCES.json'
records=json.loads(existing.read_text()) if existing.exists() else []
cases=json.loads((E/'protocol.json').read_text())['cases']
if (E/'reports/HOLDOUT_FREEZE.json').exists():cases += [x['case'] for x in json.loads((E/'reports/HOLDOUT_FREEZE.json').read_text())['cases']]
for case in cases:
    base=W/'ml_geometry/local_only'/case if case=='fine_features' else E/'results'/case
    if (base/'Hybrid/construction.json').exists():continue
    start=time.monotonic();peak=0;status='COMPLETED'
    with (E/'reports'/(case+'_construction.log')).open('w') as f:
        p=subprocess.Popen([sys.executable,str(files[0]),case],stdout=f,stderr=subprocess.STDOUT)
        while p.poll() is None:
            try:
                process=psutil.Process(p.pid)
                peak=max(peak,sum(child.memory_info().rss for child in [process]+process.children(recursive=True)))
            except psutil.Error:pass
            if peak>768*2**20 or time.monotonic()-start>384:status='STOPPED_RESOURCE';p.kill();break
            time.sleep(.1)
        code=p.wait()
    row={'case':case,'exit_code':code,'status':status if code==0 or status!='COMPLETED' else 'FAILED','wall_seconds':time.monotonic()-start,'sampled_RSS_peak_mib':peak/2**20,'sampling_seconds':.1,'memory_scope':'process tree'};records.append(row);print(row,flush=True)
    (E/'reports/CONSTRUCTION_RESOURCES.json').write_text(json.dumps(records,indent=2))

# END CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
