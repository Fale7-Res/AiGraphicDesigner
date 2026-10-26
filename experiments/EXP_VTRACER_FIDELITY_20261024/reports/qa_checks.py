# START CHANGE VTRACER-QA-REFINE | 2026-10-24T23:42:23Z | EDITED | Author: vtracer_qa
"""Independent artifact verification; does not rerun tracing or tune parameters."""
# START CHANGE VTRACER-QA | 2026-10-24T09:58:53Z | CREATED | Author: vtracer_qa
from pathlib import Path
import json,sys,hashlib,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from evaluate import compare,load_rgb,svg_structure
from search import extra_metrics,fidelity_score

def audit():
    """Decode all PNGs; reproduce trial scores/metrics and exact SVG complexity."""
    findings=[];counts={'pngs':0,'trials':0,'rankings':0,'svgs':0}
    for p in ROOT.rglob('*.png'):
        try:
            with Image.open(p) as im:im.verify()
            with Image.open(p) as im:im.load()
            counts['pngs']+=1
        except Exception as e:findings.append({'file':str(p.relative_to(ROOT)),'problem':'PNG integrity','error':str(e)})
    for p in ROOT.rglob('result.json'):
        d=json.loads(p.read_text());folder=p.parent
        if d.get('status')!='ok' or not (folder/'config.json').exists():continue
        norm=folder.parent/'normalized.png'
        if not norm.exists() and folder.parent.parent.name=='extension':norm=ROOT/'results'/folder.parent.name/'normalized.png'
        if not norm.exists():continue
        try:
            a=load_rgb(norm);b=load_rgb(folder/'render.png');m=compare(a,b)|extra_metrics(a,b)
            if m!=d['metrics']:findings.append({'file':str(p.relative_to(ROOT)),'problem':'metrics mismatch'})
            if abs(fidelity_score(m)-d['score'])>1e-12:findings.append({'file':str(p.relative_to(ROOT)),'problem':'score mismatch'})
            if svg_structure(folder/'output.svg')!=d['structure']:findings.append({'file':str(p.relative_to(ROOT)),'problem':'structure mismatch'})
            if json.loads((folder/'config.json').read_text())!=d['config']:findings.append({'file':str(p.relative_to(ROOT)),'problem':'config mismatch'})
            counts['trials']+=1
        except Exception as e:findings.append({'file':str(p.relative_to(ROOT)),'problem':'trial load','error':str(e)})
    baseline_file=ROOT/'results_baselines/summary.json'
    if baseline_file.exists():
        for row in json.loads(baseline_file.read_text()):
            folder=ROOT/'results_baselines'/row['case']/row['label'];ref=load_rgb(ROOT/'inputs'/row['source_name']);pred=load_rgb(folder/'render.png');m=compare(ref,pred)|extra_metrics(ref,pred)
            if m!=row['metrics']:findings.append({'file':str(folder.relative_to(ROOT)),'problem':'historical metric mismatch'})
            counts['historical_conditions']=counts.get('historical_conditions',0)+1
    for p in ROOT.rglob('results.json'):

        d=json.loads(p.read_text())
        if 'ownership_audit' not in d:continue
        case=p.parent.name;source=ROOT/'inputs'/(case+'.png')
        if not source.exists():
            findings.append({'file':str(p.relative_to(ROOT)),'problem':'refinement source case unresolved'});continue
        ref=load_rgb(source);baseline=None
        for label,c in d['conditions'].items():
            svg=p.parent/(label+'.svg');pred=load_rgb(p.parent/(label+'.png'));m=compare(ref,pred)|extra_metrics(ref,pred)
            if m!=c['metrics']:findings.append({'file':str(p.relative_to(ROOT)),'problem':'refinement metrics mismatch','condition':label})
            root=ET.parse(svg).getroot();geometry=[(e.tag,{k:v for k,v in e.attrib.items() if k!='fill'}) for e in root]
            if baseline is None:baseline=geometry
            elif geometry!=baseline:findings.append({'file':str(p.relative_to(ROOT)),'problem':'refinement changed geometry'})
        if d['conditions']['visible_color_refit']['metrics']['mse']>d['conditions']['crisp_control']['metrics']['mse']+1e-9:findings.append({'file':str(p.relative_to(ROOT)),'problem':'refit SSE increased'})
        counts['refinement_cases']=counts.get('refinement_cases',0)+1
    for p in ROOT.rglob('ranking.json'):

        d=json.loads(p.read_text());rows=d.get('ranked',[])
        if rows:
            if rows!=sorted(rows,key=lambda v:(-v['score'],v['trial'])):findings.append({'file':str(p.relative_to(ROOT)),'problem':'ranking order'})
            for name,trialname in [('best.svg','output.svg'),('best.png','render.png')]:
                if (p.parent/name).read_bytes()!=(p.parent/rows[0]['trial']/trialname).read_bytes():findings.append({'file':str(p.relative_to(ROOT)),'problem':'best not rank1 copy','artifact':name})
        counts['rankings']+=1
    for p in ROOT.rglob('*.svg'):
        try:
            s=svg_structure(p)
            if not s['raster_free'] or s['external_href_count'] or s['script_count']:findings.append({'file':str(p.relative_to(ROOT)),'problem':'raster/external/script'})
            counts['svgs']+=1
        except Exception as e:findings.append({'file':str(p.relative_to(ROOT)),'problem':'SVG parse','error':str(e)})
    record={'counts':counts,'findings':findings,'scope':'PNG decoding; all successful search trials metric/score/complexity reproduction; best file identity; raster exclusion. Not semantic or visual approval.'}
    (ROOT/'reports/qa_checks.json').write_text(json.dumps(record,indent=2));print(json.dumps(record,indent=2));return bool(findings)

if __name__=='__main__':raise SystemExit(audit())
# END CHANGE VTRACER-QA | 2026-10-24T09:58:53Z | CREATED | Author: vtracer_qa

# END CHANGE VTRACER-QA-REFINE | 2026-10-24T23:42:23Z | EDITED | Author: vtracer_qa
