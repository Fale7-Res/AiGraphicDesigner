# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:53:38Z | CREATED | Author: universal_qa
"""Independent saved-output audit; never runs candidate algorithms."""
import collections
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image

repo = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
exp = repo/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01'
work = Path(__file__).resolve().parents[2]
out = Path(__file__).parent
protocol = json.loads((exp/'protocol.json').read_text())
token = re.compile(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?')
reports = []
failures = []

def check(ok, message):
    if not ok:
        failures.append(message)

def sampled(curves, count=65):
    u = np.linspace(0, 1, count)[:,None]
    pieces = [((1-u)**3*c[0] + 3*(1-u)**2*u*c[1] + 3*(1-u)*u*u*c[2] + u**3*c[3]) for c in np.asarray(curves)]
    return np.concatenate([x[:-1] for x in pieces]+[pieces[-1][-1:]])

def parse_svg(path, expected=None):
    root = ET.parse(path).getroot()
    all_paths = []
    for element in root.iter():
        tag = element.tag.rsplit('}',1)[-1]
        check(tag in ('svg','path'), str(path)+': unexpected SVG element '+tag)
        if tag != 'path':
            continue
        tokens = token.findall(element.attrib.get('d',''))
        i = 0
        substart = None
        current = None
        curves = []
        closes = 0
        while i < len(tokens):
            command=tokens[i];i+=1
            if command=='M':
                current=np.array([float(x) for x in tokens[i:i+2]]);i+=2;substart=current.copy()
            elif command=='C':
                check(current is not None,str(path)+': cubic before move')
                coords=np.array([float(x) for x in tokens[i:i+6]]).reshape(3,2);i+=6
                curves.append(np.vstack([current,coords]));current=coords[-1]
            elif command=='Z':
                check(substart is not None,str(path)+': close before move')
                check(np.array_equal(current,substart),str(path)+': unintended close line')
                current=substart.copy();closes+=1
            else:
                raise AssertionError(str(path)+': unexpected command '+command)
        all_paths.append({'curves':curves,'closes':closes})
    if expected is not None:
        check(len(all_paths)==len(expected),str(path)+': path count does not match accepted records')
        for a,b in zip(all_paths,expected):
            check(np.array_equal(np.asarray(a['curves']),np.asarray(b['curves'])),str(path)+': controls differ from accepted record')
    return len(all_paths)

for case,config in protocol['cases'].items():
    folder = work/'universal_geometry/local_only'/case if case=='fine_features' else exp/'results'/case
    if not (folder/'WORKER.json').exists():
        reports.append({'case':case,'pending':True});continue
    frozen=json.loads((folder/'frozen_traces.json').read_text())
    original={r['trace_id']:r for r in frozen['traces']}
    p=json.loads((folder/'P.json').read_text())
    s=json.loads((folder/'S.json').read_text())
    c=json.loads((folder/'C.json').read_text())
    r=json.loads((folder/'R_graph.json').read_text())
    ra=json.loads((folder/'R_audit.json').read_text())
    ca=json.loads((folder/'C_audit.json').read_text())
    check(len(original)==len(frozen['traces']),case+': duplicate trace IDs')
    if config['cached']:
        for tag,base,name in [('O',config['baseline'],'stable.svg'),('P',config['partitioned'],'P.svg')]:
            check((folder/(tag+'.svg')).read_bytes()==(Path(base)/name).read_bytes(),case+': saved '+tag+' not byte-identical')
    ledger_counts={}
    for tag,result in [('P',p),('S',s)]:
        check(set(original)=={row['trace_id'] for row in result['traces']},case+': missing '+tag+' trace')
        for row in result['traces']:
            points=np.asarray(original[row['trace_id']]['source_points_xy']);n=len(points)-1
            coverage=np.zeros(n,dtype=int)
            for entry in row['ledger']:
                coverage[entry['lo']:entry['hi']]+=1
                length=float(np.linalg.norm(np.diff(points[entry['lo']:entry['hi']+1],axis=0),axis=1).sum())
                check(abs(length-entry['length_px'])<1e-6,case+': incorrect ledger length '+tag)
            check(np.all(coverage==1),case+': missing or duplicate ledger edges '+tag)
        ledger_counts[tag]=len(result['traces'])
    scores={row['trace_id']:row for row in s['selection_scores']}
    for row in scores.values():
        expected=.35*row['persistence']+.25*row['contrast']+.15*row['closed']+.15*row['junction']+.1*row['coherence']
        check(abs(expected-row['score'])<1e-12,case+': S formula mismatch')
    ordered=sorted(original,key=lambda tid:(-scores[tid]['score'],tid))
    expected_selected=[tid for tid in ordered if original[tid]['length_px']>=6][:128]
    selected=[row['trace_id'] for row in s['traces'] if row['selection']=='selected']
    check(selected==expected_selected,case+': S selected IDs differ from frozen rank rule')
    check(len(r['chains'])==len(p['accepted']),case+': R removed chain')
    for graph,orig in zip(r['chains'],p['accepted']):
        cc=np.asarray([[seg[x] for x in ('p0','p1','p2','p3')] for seg in graph['segments']])
        check(np.array_equal(cc,np.asarray(orig['curves'])),case+': R changed geometry')
    check(ra['integrated_paths']+ra['preserved_unintegrated_paths']==len(p['accepted']),case+': R chain accounting failure')
    check(len(c['accepted'])==len(p['accepted']),case+': C removed chain')
    changed=[]
    for index,(old,new) in enumerate(zip(p['accepted'],c['accepted'])):
        a=np.asarray(old['curves']);b=np.asarray(new['curves'])
        check(np.array_equal(a[0,0],b[0,0]) and np.array_equal(a[-1,-1],b[-1,-1]),case+': C moved endpoints')
        check(new.get('closed')==old.get('closed'),case+': C changed closed flag')
        check(all(np.array_equal(x[-1],y[0]) for x,y in zip(b,b[1:])),case+': C disconnected curve')
        if not np.array_equal(a,b):
            changed.append(index)
            check(len(b)<len(a),case+': C changed without cubic reduction')
    check(len(changed)==ca['accepted_changes'],case+': C audit count differs')
    for tag,records in [('O',json.loads((folder/'O.json').read_text())['accepted']),('P',p['accepted']),('S',s['accepted']),('C',c['accepted'])]:
        parse_svg(folder/(tag+'.svg'),records)
    parse_svg(folder/'R.svg')
    parse_svg(folder/'R_strokes.svg',p['accepted'])
    if (folder/'SR.svg').exists():
        parse_svg(folder/'SR.svg')
        parse_svg(folder/'SR_strokes.svg',s['accepted'])
        combined=json.loads((folder/'SR.json').read_text())
        check(combined['accepted']==s['accepted'],case+': SR changed S curves')
    decoded=0
    for png in folder.glob('*.png'):
        with Image.open(png) as image:image.verify()
        decoded+=1
    renderdir=out/'native_renders'/case
    renderdir.mkdir(parents=True,exist_ok=True)
    rendered=0
    tags=['P','S','R','C']+(['SR'] if (folder/'SR.svg').exists() else [])
    for tag in tags:
        proc=subprocess.run([str(work/'resvg/resvg.exe'),str(folder/(tag+'.svg')),str(renderdir/(tag+'.png'))],capture_output=True)
        check(proc.returncode==0,case+': actual independent resvg failed '+tag)
        rendered+=proc.returncode==0
    reports.append({'case':case,'trace_count':len(original),'ledger_counts':ledger_counts,
                    'R_atomic_faces':ra['bounded_atomic_faces'],'C_changed_chains':len(changed),
                    'PNG_decoded':decoded,'independent_native_renders':rendered,
                    'rights':'LOCAL_ONLY' if case=='fine_features' else 'publishable_parent_policy'})

result={'cases':reports,'failures':failures,'passed':not failures,
        'limitations':['Numerical SVG/control ledger audit is not complete geometric truth.',
                       'Fine Features independent renders remain local-only.',
                       'No constructor or detector was rerun.']}
(out/'CANDIDATE_AUDIT.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'cases':len(reports),'pending':[r['case'] for r in reports if r.get('pending')],
                  'failure_count':len(failures),'failures':failures[:20]}))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:53:38Z | CREATED | Author: universal_qa
