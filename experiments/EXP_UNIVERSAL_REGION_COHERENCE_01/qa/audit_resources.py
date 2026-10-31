# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:57:08Z | CREATED | Author: universal_qa
import json
from pathlib import Path
root=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_UNIVERSAL_REGION_COHERENCE_01')
rows=json.loads((root/'reports/RESOURCES.json').read_text())
validation=json.loads((root/'reports/MONITOR_VALIDATION.json').read_text())
failures=[]
for row in rows:
    if row['status']!='COMPLETED' or row['exit_code']!=0:failures.append(row['case']+': worker failure')
    if len(row['observed_pid_peak_bytes'])<2:failures.append(row['case']+': no descendant monitored')
    if row['sample_count']<=0:failures.append(row['case']+': no samples')
    if row['sampled_tree_RSS_peak_mib']>768:failures.append(row['case']+': memory over budget')
    if row['wall_seconds']>300:failures.append(row['case']+': wall over budget')
result={'workers':len(rows),'failures':failures,'passed':not failures,
        'last_case':rows[-1]['case'] if rows else None,
        'summed_worker_wall_seconds':sum(r['wall_seconds'] for r in rows),
        'max_sampled_tree_RSS_mib':max([r['sampled_tree_RSS_peak_mib'] for r in rows],default=0),
        'monitor_validation_reviewed':True,
        'limitations':'Sampled process-tree RSS can miss peaks and double count shared pages; not exact allocation maximum.'}
Path(__file__).with_name('RESOURCE_AUDIT.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:57:08Z | CREATED | Author: universal_qa
