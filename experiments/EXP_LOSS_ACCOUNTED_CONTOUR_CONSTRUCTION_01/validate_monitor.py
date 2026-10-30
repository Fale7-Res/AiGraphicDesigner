# START CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
from pathlib import Path
import sys,json
from monitor import supervise
W=Path.cwd()/'work/contour_construction';R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'
child=W/'memory_child.py';parent=W/'memory_parent.py'
child.write_text('import time\nx=bytearray(64*1024*1024)\nfor i in range(0,len(x),4096):x[i]=1\ntime.sleep(2)\n')
parent.write_text('import subprocess,sys\np=subprocess.Popen([sys.executable,r"'+str(child)+'"])\np.wait()\n')
normal=supervise([sys.executable,parent],W/'monitor_normal.log',wall_seconds=8,memory_mib=256,reserve_mib=0,interval=.02)
stopped=supervise([sys.executable,parent],W/'monitor_stopped.log',wall_seconds=8,memory_mib=48,reserve_mib=0,interval=.02)
assert normal['exit_code']==0 and normal['sampled_tree_RSS_peak_mib']-normal['sampled_root_RSS_peak_mib']>48,normal
assert len(normal['observed_pid_peak_bytes'])>=2
assert stopped['status']=='STOPPED_MEMORY',stopped
result={'normal':normal,'controlled_limit_stop':stopped,'passed':True,'fixture':'ownedchild64MiBtouchallocation; rootwaits. ValidatechildinclusionandstopBEFOREbenchmarkRAMclaims.'}
(E/'reports/MONITOR_VALIDATION.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))

# END CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
