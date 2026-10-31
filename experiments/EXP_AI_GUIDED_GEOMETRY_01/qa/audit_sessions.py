# START CHANGE AGD-AGENTIC-QA-SESSION | 2026-10-31T12:03:37Z | CREATED | Author: agentic_qa
"""Independent saved event/state/SVG audit. Never calls controller or provider."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01')


def session_audit_digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def saved_session_audit(case, condition):
    folder = ROOT/'results'/case
    state = json.loads((folder/(condition+'.json')).read_text())
    original = json.loads((folder/'A.json').read_text())['accepted']
    assert state['initial_hash'] == session_audit_digest(original)
    assert state['state_hash'] == session_audit_digest(state['accepted'])
    assert state['accepted'][:len(original)] == original, 'Inherited geometry changed/deleted'
    assert state['api_requests'] == 0 and state['actual_api_cost_usd'] == 0
    assert state['AI_performance'] == 'NOT_TESTED'
    assert state['calls'] <= 12 and state['commits'] <= 2
    previous = state['source_pin']
    last_geometry = state['initial_hash']
    semantic = []
    for index,event in enumerate(state['tool_events']):
        disk = json.loads((folder/condition/f'event_{index:03d}.json').read_text())
        assert disk == event
        assert event['sequence'] == index
        assert event['previous_record_hash'] == previous
        assert event['before_hash'] == last_geometry
        record = dict(event)
        previous = record.pop('record_hash')
        assert session_audit_digest(record) == previous
        last_geometry = event['after_hash']
        result = event['result']
        if event['tool'] != 'commit_change':
            assert event['before_hash'] == event['after_hash']
        ledger = []
        for row in result.get('ledger',[]):
            intervals = [{key: interval.get(key) for key in ('lo','hi','status','reason','cubics')}
                         for interval in row.get('interval_ledger',[])]
            ledger.append(dict(trace_id=row['trace_id'],status=row['status'],
                accepted_paths=row.get('accepted_paths',0),rejections=row.get('rejections',[]),intervals=intervals))
        semantic.append(dict(tool=event['tool'],arguments=event['arguments'],status=event['status'],
            before_hash=event['before_hash'],after_hash=event['after_hash'],
            decision=result.get('status'),error=result.get('error'),ledger=ledger))
    assert last_geometry == state['state_hash']
    assert session_audit_digest(semantic) == state['decision_hash']
    assert not state['pending']
    root = ET.fromstring((folder/(condition+'.svg')).read_bytes())
    tags = [node.tag.rsplit('}',1)[-1] for node in root.iter()]
    assert not set(tags).intersection({'image','rect','script','foreignObject'})
    paths = [node for node in root.iter() if node.tag.rsplit('}',1)[-1] == 'path']
    assert len(paths) == len(state['accepted'])
    count_cubics = 0
    number = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?')
    for path,item in zip(paths,state['accepted']):
        d = path.attrib['d']
        assert not set(re.findall(r'[A-DF-Za-df-z]',d)).difference({'M','C','Z'}), 'Unexpected command'
        coords = [float(v) for v in number.findall(d)]
        expected = list(item['curves'][0][0])
        for curve in item['curves']:
            for point in curve[1:]:
                expected.extend(point)
        assert len(coords) == len(expected)
        assert all(abs(a-b) < 1e-10 for a,b in zip(coords,expected)), 'SVG control point mutation'
        assert d.count('C') == len(item['curves'])
        count_cubics += len(item['curves'])
    assert count_cubics <= 4096
    return dict(case=case,condition=condition,events=len(state['tool_events']),
        paths=len(paths),cubics=count_cubics,added_paths=len(paths)-len(original),
        geometry_hash=state['state_hash'],decision_hash=state['decision_hash'],passed=True)


if __name__ == '__main__':
    protocol = json.loads((ROOT/'protocol.json').read_text())
    rows, incomplete = [], []
    for case in protocol['cases']:
        for condition in ('B','M'):
            if not (ROOT/'results'/case/(condition+'.json')).exists():
                incomplete.append([case,condition])
                continue
            rows.append(saved_session_audit(case,condition))
    report = dict(sessions=rows,incomplete=incomplete,passed=not incomplete)
    destination = Path(__file__).parent/'SESSION_AUDIT.json'
    destination.write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
# END CHANGE AGD-AGENTIC-QA-SESSION | 2026-10-31T12:03:37Z | CREATED | Author: agentic_qa
