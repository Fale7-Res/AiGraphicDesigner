# START CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
from pathlib import Path
import hashlib,json,sys,time,datetime,shutil
from monitor import supervise
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01';W=Path.cwd()/'work/contour_construction'
protocol=json.loads((E/'protocol.json').read_text())
# Final constructor annotation-only diagnostics were completed before candidates.
snapshot={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reason':'Final periodic-join diagnostics added after initial protocol freeze, before any benchmark. Candidate constants/inputs unchanged. Finalhash enforced before execution.','files':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [W/'run_case.py',W/'monitor.py',W/'implementation/partition_fit.py',W/'implementation/design_constants.json']}}
(E/'reports/PRE_EXECUTION_SOURCE_FREEZE.json').write_text(json.dumps(snapshot,indent=2))
for path,item in protocol['pins'].items():
    if path.endswith('partition_fit.py'):continue
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==item['sha256'],path
assert json.loads((E/'reports/MONITOR_VALIDATION.json').read_text())['passed']
records=[];start=time.monotonic()
for case in protocol['cases']:
    for arm in protocol['arms']:
        if time.monotonic()-start>3600:raise RuntimeError('Frozen totalconstruction budget exhausted')
        record=supervise([sys.executable,W/'run_case.py',case,arm],E/'reports'/(case+'_'+arm+'.log'),wall_seconds=300,memory_mib=768,reserve_mib=700,interval=.1)
        record.update(case=case,arm=arm);records.append(record)
        (E/'reports/CONSTRUCTION_RESOURCES.json').write_text(json.dumps(records,indent=2));print(case,arm,record['status'],record['wall_seconds'],record['sampled_tree_RSS_peak_mib'],flush=True)
        if record['status']!='COMPLETED':raise RuntimeError('Stop affected branch: '+str(record))

# END CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
