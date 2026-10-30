# START CHANGE AGD-EXPORT-QA-AUDIT-SAVED | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
"""Passive independent frozen graphs/render/guard checks; no rerender or fitting."""
import collections,hashlib,json,xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_EXPORTER_DISCOVERY_01')
WORK=Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work')
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from phase_b import digest
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def directed(g):return {f:collections.Counter((r['chain'],r['forward']) for ring in loops for r in ring) for f,loops in g['faces'].items()}
def cross(a,b):return float(a[0]*b[1]-a[1]*b[0])
def open_area(points):return .5*sum(cross(a,b) for a,b in zip(points[:-1],points[1:]))
nodes,weights=np.polynomial.legendre.leggauss(8);t=(nodes+1)/2;weights=weights/2
def curve_area(s):
    if s['type']=='L':return cross(s['p0'],s['p3'])/2
    a,b,c,d=[np.asarray(s[k]) for k in ('p0','p1','p2','p3')];u=t[:,None]
    p=(1-u)**3*a+3*(1-u)**2*u*b+3*(1-u)*u*u*c+u**3*d
    v=3*((1-u)**2*(b-a)+2*(1-u)*u*(c-b)+u*u*(d-c))
    return float(np.sum(weights*(p[:,0]*v[:,1]-p[:,1]*v[:,0]))/2)
def collapsed(g):
    lookup={c['id']:c for c in g['chains']};total=0;rings=0
    for face,loops in g['faces'].items():
        if int(face)==0:continue
        for refs in loops:
            rawarea=fitarea=0.;rings+=1
            for ref in refs:
                c=lookup[ref['chain']];sign=1 if ref['forward'] else -1
                pts=c['pixel_crack_vertices'];rv=open_area(pts)
                if c.get('closed'):rv+=cross(pts[-1],pts[0])/2
                rawarea+=sign*rv
                value=sum(curve_area(s) for s in c['segments'])
                if c.get('closed') and c['segments']:value+=cross(c['segments'][-1]['p3'],c['segments'][0]['p0'])/2
                fitarea+=sign*value
            total+=abs(rawarea)>1e-6 and abs(fitarea)<=1e-6
    return {'rings':rings,'raw_nonzero_fit_zero':int(total)}
pins=load(ROOT/'BASELINE_PINS.json');report={}
for case,items in pins['cases'].items():
    folder=(WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case
    gs={n:load(folder/f'{n}.json') for n in ['O','R','B','RB']}
    assert gs['O']['chains']==gs['R']['chains']
    assert directed(gs['O'])==directed(gs['R'])
    assert digest(folder/'labels.npy')==items['labels.npy']['sha256']
    for name in ['O','R','B']:assert digest(folder/f'{name}.json')==items[f'{name}.json']['sha256']
    prior,candidate=gs['R'],gs['RB'];assert candidate['faces']==prior['faces']
    assert {k:v for k,v in prior.items() if k!='chains'}=={k:v for k,v in candidate.items() if k!='chains'}
    changed=[]
    for a,b in zip(prior['chains'],candidate['chains']):
        assert {k:v for k,v in a.items() if k!='segments'}=={k:v for k,v in b.items() if k!='segments'}
        if a['segments']!=b['segments']:
            changed.append(a['id']);p,q,r=a['pixel_crack_vertices']
            assert b['segments']==[{'type':'C','p0':p,'p1':q,'p2':q,'p3':r}]
    audit=load(folder/'RB_audit.json')
    if 'accepted_chains' in audit:assert changed==audit['accepted_chains']
    imagechecks=[]
    for kind,scale in [('raw_regions',1),('raw_regions',8),('regions',8)]:
        a=np.asarray(Image.open(folder/f'O_{kind}_{scale}x.png').convert('RGBA'))
        b=np.asarray(Image.open(folder/f'R_{kind}_{scale}x.png').convert('RGBA'))
        n=int(np.any(a!=b,axis=-1).sum());assert n==0;imagechecks.append({'kind':kind,'scale':scale,'differing_pixels':n})
    proposal=load(folder/'discovery/proposals.json')
    assert proposal['source_file_sha256']==digest(folder/'working.png')
    rgb=np.asarray(Image.open(folder/'working.png').convert('RGB'));assert proposal['rgb_array_sha256']==hashlib.sha256(rgb.tobytes()).hexdigest()
    assert proposal['integrated_into_shared_graph'] is False
    svg=ET.parse(folder/'discovery/proposals.svg').getroot();paths=[e for e in svg.iter() if e.tag.endswith('}path')]
    assert len(paths)==len(proposal['accepted'])
    assert not any(e.tag.rsplit('}',1)[-1] in ['image','script','foreignObject'] for e in svg.iter())
    report[case]={'changed_RB_chains':changed,'accepted_RB_count':len(changed),'matched_render_checks':imagechecks,
        'gaussian_area_counts':{n:collapsed(g) for n,g in gs.items()},
        'discovery_proposals':len(proposal['accepted']),'discovery_rejections':dict(collections.Counter(x['reason'] for x in proposal['rejected'])),
        'source_hashes_verified':True,'labels_and_O_R_B_hashes_verified':True,'source_proposals_integrated':False}
(Path(__file__).parent/'saved_output_audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))

# END CHANGE AGD-EXPORT-QA-AUDIT-SAVED | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
