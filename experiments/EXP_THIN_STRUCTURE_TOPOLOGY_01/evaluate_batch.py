# START CHANGE AGD-THIN-EVALUATION-BATCH | 2026-10-29T11:43:50Z | CREATED | Author: root
"""Evaluate saved primary/combined outputs; never selects or modifies geometry."""
from study import ROOT,CASES,destination,dump,digest
from evaluate_study import evaluate_candidate
import json,time

def main():
    rows=[]
    for case in CASES:
        for name in ['baseline','A','B','AB']:
            out=destination(case);target=out/(name+'.json')
            if not target.exists():continue
            m=evaluate_candidate(case,name)
            audit=json.loads((out/(name+'_audit.json')).read_text(encoding='utf-8'))
            row={k:m[k] for k in ['case','condition','raw_nonzero_fit_degenerate_rings','invalid_fit_rings','invalid_raw_rings','crossing_or_overlap_pairs','shared_reference_failures','max_junction_gap_px','self_intersecting_chains','near_intersection_unresolved_pairs','chains','cubics','geometry_acceptance','raw_to_fit']}
            if 'known_geometry' in m:row['known_geometry']=m['known_geometry']
            if 'arabic_source_proxy' in m:row['arabic_source_proxy']=m['arabic_source_proxy']
            row['accepted_bridges']=audit.get('accepted_bridges',0);row['accepted_chains']=len(audit.get('accepted_chains',[]))
            row['coverage']=m['coverage'];rows.append(row);dump(ROOT/'reports/SUMMARY.json',rows)
            print(json.dumps({k:v for k,v in row.items() if k not in ['known_geometry','arabic_source_proxy','raw_to_fit','coverage']}),flush=True)
    return rows

if __name__=='__main__':main()

# END CHANGE AGD-THIN-EVALUATION-BATCH | 2026-10-29T11:43:50Z | CREATED | Author: root
