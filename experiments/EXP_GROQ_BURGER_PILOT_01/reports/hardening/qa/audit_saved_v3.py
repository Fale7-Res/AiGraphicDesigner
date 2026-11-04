# START CHANGE AGD-PILOT-SAVED-QA | 2026-11-04T15:36:30Z | CREATED | Author: agentic_qa
"""Read-only audit of saved synthetic evidence; never execute requests/tools."""
from pathlib import Path
import hashlib,json
import xml.etree.ElementTree as ET
from PIL import Image
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_GROQ_BURGER_PILOT_01')
OLD=ROOT.parent/'EXP_AI_GUIDED_GEOMETRY_01'

def saved_digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def unique_saved_pairs(pairs):
    out={}
    for key,value in pairs:
        assert key not in out
        out[key]=value
    return out

def read_saved(path):
    return json.loads(path.read_text(),object_pairs_hook=unique_saved_pairs)

def inspect_saved_session(folder):
    previous='ROOT';prior_requests=0;prior_reserved=0;reserved=0;usage_records=0
    records=sorted(folder.glob('record_*.json'))
    for i,path in enumerate(records):
        assert path.name==f'record_{i:03d}.json'
        record=read_saved(path);supplied=record.pop('hash')
        assert saved_digest(record)==supplied
        assert record['sequence']==i and record['previous']==previous
        previous=supplied;state=record['state']
        if i==0:source_pin=state['source_pin'];implementation=state['implementation_pin']
        assert state['source_pin']==source_pin and state['implementation_pin']==implementation
        if record['kind']=='REQUEST_RESERVED':
            reserved+=1
            assert state['requests']==prior_requests+1 and state['reserved_tokens']>prior_reserved
        else:assert state['requests']==prior_requests and state['reserved_tokens']==prior_reserved
        prior_requests=state['requests'];prior_reserved=state['reserved_tokens']
        if record['kind']=='USAGE_RECEIVED':usage_records+=1
        for usage in state.get('usage',[]):
            assert set(usage)=={'prompt_tokens','completion_tokens','total_tokens'}
            assert all(type(v) is int and v>=0 for v in usage.values())
            assert usage['prompt_tokens']+usage['completion_tokens']==usage['total_tokens']
        assert all(obs['authority']=='UNTRUSTED_PLANNER_OBSERVATION' for obs in state['observations'])
        assert hashlib.sha256((folder/state['preview']['file']).read_bytes()).hexdigest()==state['preview']['sha256']
        assert len(state['engine']['events'])<=12 and state['engine']['commits']<=2
    assert records and state['phase']=='COMPLETE' and state['mode']=='synthetic'
    assert (reserved,usage_records,state['requests'])==(2,2,2)
    assert [a['request_index'] for a in state['approvals']]==[0,1]
    assert len(state['call_ids'])==len(set(state['call_ids']))==2
    assert state['geometry_hash']==saved_digest(state['engine']['items'])
    prior_event=source_pin
    for i,event in enumerate(state['engine']['events']):
        assert read_saved(folder/'initial_engine'/f'event_{i:03d}.json')==event
        row=dict(event);supplied=row.pop('record_hash')
        assert saved_digest(row)==supplied and event['previous_record_hash']==prior_event
        prior_event=supplied
    files=[ROOT/'pilot_control.py',ROOT/'hardened_pilot.py',OLD/'geometry_engine.py',
        ROOT.parent/'EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01/partition_fit.py',
        ROOT.parent/'EXP_EXPORTER_DISCOVERY_01/svg_exporter.py']
    current_pin=saved_digest({str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    rendered=next(e['result'] for e in reversed(state['engine']['events']) if e['tool']=='render_geometry')
    svg=ET.parse(folder/'initial_engine'/rendered['svg']).getroot()
    tags=[el.tag.rsplit('}',1)[-1] for el in svg.iter()]
    assert not set(tags)&{'image','rect','script','foreignObject'}
    assert tags.count('path')==len(state['engine']['items'])==132
    with Image.open(folder/'initial_engine'/rendered['png']) as image:image.verify()
    summary=read_saved(folder/'SUMMARY.json')
    assert summary['real_requests']==0 and summary['AI_performance']=='NOT_TESTED'
    return dict(folder=folder.name,records=len(records),requests_synthetic=state['requests'],
        reserved_tokens=state['reserved_tokens'],completion_tokens=state['completion_tokens'],
        tool_calls=len(state['engine']['events']),commits=state['engine']['commits'],
        geometry_hash=state['geometry_hash'],implementation_pin=implementation,
        current_implementation_matches=implementation==current_pin,
        final_preview_sha256=state['preview']['sha256'],passed=True),summary

if __name__=='__main__':
    first,a=inspect_saved_session(ROOT/'results/synthetic_two_step_v4')
    second,b=inspect_saved_session(ROOT/'results/synthetic_two_step_replay_v4')
    assert a==b
    report=dict(status='PASS_SAVED_SYNTHETIC_ONLY',sessions=[first,second],
        identical_summary_and_geometry=True,provider_requests_by_QA=0,credential_access_by_QA=0)
    assert first['current_implementation_matches'] and second['current_implementation_matches']
    (Path(__file__).parent/'SAVED_V4_AUDIT.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
# END CHANGE AGD-PILOT-SAVED-QA | 2026-11-04T15:36:30Z | CREATED | Author: agentic_qa
