# START CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root
from pathlib import Path
import json,datetime,hashlib,sys
from monitor import supervise
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01';W=Path.cwd()/'work/contour_construction'
freeze={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Separatebudgetcapacityfrompartitioneffects usingonlythecriticalK01control. MainO/P/Qfrozenoutputsunchanged.','source_code_sha256':hashlib.sha256((W/'cap_control.py').read_bytes()).hexdigest(),'conditions':'oldstablefit512vs64cap, unchanged.6deviation/.35RDP/8rounds;no partition/periodic','cases':['K01_linear_corner_hole'],'arms':['Classical','ML','Hybrid'],'maximum_seconds_per_arm':120,'memory_mib':768,'no_new_gate_or_parameter_tuning':True}
(E/'reports/CAP512_DIAGNOSTIC_FREEZE.json').write_text(json.dumps(freeze,indent=2))
rows=[]
for arm in freeze['arms']:
    r=supervise([sys.executable,W/'cap_control.py',arm],E/'reports'/('CAP512_'+arm+'.log'),wall_seconds=120,memory_mib=768,reserve_mib=700);r['arm']=arm;rows.append(r);print(r['status'],arm,flush=True)
    (E/'reports/CAP512_RESOURCES.json').write_text(json.dumps(rows,indent=2))

# END CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root
