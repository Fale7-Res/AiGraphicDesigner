# START CHANGE AGD-CONTOUR-QA-CANDIDATES | 2026-10-30T08:45:00Z | CREATED | Author: contour_qa
"""Independent read-only saved-geometry audit, no construction imports/reruns."""
import hashlib,json,math,re,sys,subprocess
from pathlib import Path
from xml.etree import ElementTree as ET
W=Path(__file__).resolve().parents[2]
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'
protocol=json.loads((E/'protocol.json').read_text())
amendment=json.loads((E/'reports/PRE_EXECUTION_SOURCE_FREEZE.json').read_text())
pins=[]
for path,meta in protocol['pins'].items():
    expected=amendment['files'].get(path,meta['sha256'])
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==expected,path
    pins.append(path)
for path,digest in amendment['files'].items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,path
rows=[]
renders=Path(__file__).parent/'native_renders';renders.mkdir(exist_ok=True)
number=re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?')
for case,config in protocol['cases'].items():
  for arm in protocol['arms']:
    old=json.loads((Path(config['base'])/arm/'construction.json').read_text())
    old_by_id={x['trace_id']:x for x in old['traces']}
    base=(W/'contour_construction/local_only'/case if case=='fine_features' else E/'results'/case)/arm
    for condition in ['P','Q']:
      path=base/(condition+'.json')
      if not path.exists() or not (base/(condition+'.svg')).exists():continue
      data=json.loads(path.read_text());assert len(data['traces'])==len(old['traces'])
      retained=0.;lost=0.;accepted_parts={};source_by_id={}
      for trace in data['traces']:
        tid=trace['trace_id'];source=old_by_id[tid]['source_points_xy'];source_by_id[tid]=source
        n=len(source)-1;cover=[0]*n
        assert trace['closed_source']==(source[0]==source[-1])
        for item in trace['ledger']:
          lo,hi=item['lo'],item['hi'];assert 0<=lo<hi<=n
          for j in range(lo,hi):cover[j]+=1
          length=sum(math.dist(a,b) for a,b in zip(source[lo:hi],source[lo+1:hi+1]))
          assert math.isclose(length,item['length_px'],abs_tol=1e-7)
          if item['status']=='accepted':
            retained+=length;accepted_parts[tid,item['partition_id']]=item
            assert item['final_fit']['numerical_upper_envelope_px']<=.6
          else:lost+=length;assert item['reason']!='accepted'
        assert set(cover)=={1}
      assert math.isclose(retained,data['summary']['accepted_length_px'],abs_tol=1e-6)
      assert math.isclose(lost,data['summary']['lost_length_px'],abs_tol=1e-6)
      assert math.isclose(retained+lost,data['summary']['raw_length_px'],abs_tol=1e-6)
      seen=set();cubics=0;closed=0
      for chain in data['accepted']:
        tid=chain['trace_id'];points=source_by_id[tid];cc=chain['curves'];cubics+=len(cc)
        assert all(math.isfinite(v) for c in cc for p in c for v in p)
        for a,b in zip(cc,cc[1:]):assert a[-1]==b[0]
        for part in chain['partition_ids']:
          key=(tid,part);assert key in accepted_parts and key not in seen;seen.add(key)
        first=accepted_parts[tid,chain['partition_ids'][0]];last=accepted_parts[tid,chain['partition_ids'][-1]]
        assert cc[0][0]==points[first['lo']] and cc[-1][-1]==points[last['hi']]
        if chain['closed']:assert cc[0][0]==cc[-1][-1];closed+=1
      assert seen==set(accepted_parts)
      assert cubics==data['summary']['cubics']<=4096
      assert closed==data['summary']['closed_retained_traces']
      svg=base/(condition+'.svg');root=ET.parse(svg).getroot()
      assert all(x.tag.split('}')[-1] in ['svg','path'] for x in root.iter())
      paths=list(root);assert len(paths)==len(data['accepted'])
      for node,chain in zip(paths,data['accepted']):
        commands=re.findall('[A-Za-z]',re.sub(r'[eE][-+]?\d+','',node.attrib['d']))
        assert commands==['M']+['C']*len(chain['curves'])+(['Z'] if chain['closed'] else [])
        values=list(map(float,number.findall(node.attrib['d'])))
        expected=chain['curves'][0][0]+[v for c in chain['curves'] for p in c[1:] for v in p]
        assert values==expected
        assert node.attrib.get('fill')=='none'
      if condition=='Q':
        target=renders/(case+'_'+arm+'.png')
        subprocess.run([str(W/'resvg/resvg.exe'),str(svg),str(target)],check=True,capture_output=True,timeout=30)
      rows.append({'case':case,'arm':arm,'condition':condition,'raw_traces':len(data['traces']),'intervals':sum(len(x['ledger']) for x in data['traces']),'accepted_parts':len(seen),'paths':len(paths),'cubics':cubics,'closed':closed,'retained_length_px':retained,'lost_length_px':lost,'source_trace_sha256':hashlib.sha256((Path(config['base'])/arm/'construction.json').read_bytes()).hexdigest()})
out={'frozen_pins_checked':len(pins),'audited_conditions':len(rows),'checks':'Every source edge exactlyonce; length sums; accepted interval membership; no duplicate retained intervals; finite exact endpoints; cubic/SVG roundtrip; .6 metadata gate; native Q rendering. Crossing and deviation recomputation independent audit follows.','rows':rows}
(Path(__file__).parent/'CANDIDATE_AUDIT.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'frozen_pins_checked':len(pins),'audited_conditions':len(rows),'closed_Q':sum(x['closed'] for x in rows if x['condition']=='Q'),'checks_passed':True},indent=2))
# END CHANGE AGD-CONTOUR-QA-CANDIDATES | 2026-10-30T08:45:00Z | CREATED | Author: contour_qa
