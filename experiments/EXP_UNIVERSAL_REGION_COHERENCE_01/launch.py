# START CHANGE AGD-UNIVERSAL-LAUNCH | 2026-10-31T11:07:29Z | EDITED | Author: root
from pathlib import Path
import sys,json,time,hashlib
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01';L=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01';W=Path.cwd()/'work'
sys.path.insert(0,str(L));from monitor import supervise
def launch_universal():
 protocol=json.loads((E/'protocol.json').read_text());records=[];started=time.monotonic()
 for name,pin in protocol['pins'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==pin['sha256'],name
 # Validate tree monitoring with a deliberately touched64MiBchild before claims.
 child=W/'universal_geometry/monitor_child.py';parent=W/'universal_geometry/monitor_parent.py'
 child.write_text('import time\nx=bytearray(64*1024*1024)\nfor i in range(0,len(x),4096):x[i]=1\ntime.sleep(2)\n')
 parent.write_text('import subprocess,sys\nsubprocess.run([sys.executable,r"'+str(child)+'"],check=True)\n')
 a=supervise([sys.executable,parent],E/'reports/monitor_normal.log',wall_seconds=8,memory_mib=256,reserve_mib=0,interval=.02);b=supervise([sys.executable,parent],E/'reports/monitor_stopped.log',wall_seconds=8,memory_mib=48,reserve_mib=0,interval=.02)
 assert a['exit_code']==0 and a['sampled_tree_RSS_peak_mib']-a['sampled_root_RSS_peak_mib']>48 and b['status']=='STOPPED_MEMORY'
 (E/'reports/MONITOR_VALIDATION.json').write_text(json.dumps(dict(normal=a,stop=b,passed=True),indent=2))
 for case in protocol['cases']:
  if time.monotonic()-started>5400:raise RuntimeError('totalbudget')
  out=(W/'universal_geometry/local_only'/case if case=='fine_features' else E/'results'/case)
  if (out/'WORKER.json').exists():raise RuntimeError('Do not rerun completed case')
  result=supervise([sys.executable,E/'universal_run.py',case],E/'reports'/(case+'.log'))
  records.append(dict(case=case,**result));(E/'reports/RESOURCES.json').write_text(json.dumps(records,indent=2));print(case,result['status'],result['wall_seconds'],result['sampled_tree_RSS_peak_mib'],flush=True)
if __name__=='__main__':launch_universal()
# END CHANGE AGD-UNIVERSAL-LAUNCH | 2026-10-31T11:07:29Z | EDITED | Author: root
