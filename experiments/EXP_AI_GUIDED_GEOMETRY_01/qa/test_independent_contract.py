# START CHANGE AGD-AGENTIC-QA-TEST | 2026-10-31T15:07:18Z | EDITED | Author: agentic_qa
"""Independent adversarial tool tests; synthetic inputs, no provider or truth data."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

import numpy as np

BASE = Path.cwd()
ENGINE_PATH = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01\geometry_engine.py')
spec = importlib.util.spec_from_file_location('independent_engine_target', ENGINE_PATH)
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def independent_record_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


class IndependentEngineAudit(unittest.TestCase):
    def audit_fixture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        rgb = np.full((32, 32, 3), 255, dtype=np.uint8)
        rgb[4:5, 4:24] = 0
        traces = [
            {'trace_id': 1, 'source_points_xy': [[4,4],[24,4],[24,24],[4,24],[4,4]]},
            {'trace_id': 2, 'source_points_xy': [[4,4],[4,1],[12,1]]},
        ]
        return target.GeometryToolEngine(rgb, traces, [], Path(temp.name)/'session',
            Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner'), BASE/'work')

    def test_reject_arbitrary_execution_and_argument_injection(self):
        attacks = [
            ('__class__', {}), ('exec', {'code': 'arbitrary'}),
            ('render_geometry', {'scale': 1, 'path': '../escape.svg'}),
            ('inspect_region', {'roi': [0,0,1,1], 'url': 'https://invalid.example'}),
            ('stage_candidates', {'trace_ids': [True]}),
            ('get_candidates', {'roi': [0,0,1,1], 'limit': 1.0}),
            ('inspect_region', {'roi': [0,0,float('inf'),1]}),
            ('stage_candidates', {'trace_ids': [1,1]}),
            ('stage_candidates', {'trace_ids': [999999]}),
        ]
        for name,args in attacks:
            engine = self.audit_fixture()
            result = engine.dispatch(name,args)
            self.assertIn('error', result, (name,args))
            self.assertEqual(engine.state_hash(), engine.initial_hash)
            self.assertEqual(len(engine.events), 1)

    def test_huge_integer_and_nonstring_tool_fail_closed(self):
        for name,args in [('stage_candidates', {'trace_ids': [10**1000]}),
                          ([], {}), (None, {}),
                          ('get_candidates', {'roi':[0,0,1,1], 'limit':10**1000})]:
            engine = self.audit_fixture()
            result = engine.dispatch(name,args)
            self.assertIn('error',result)
            self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_transaction_revert_does_not_erase_audit_or_refund_calls(self):
        engine = self.audit_fixture()
        staged = engine.dispatch('stage_candidates', {'trace_ids':[1]})
        self.assertGreater(staged['added_paths'],0)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertEqual(engine.dispatch('commit_change',{})['status'],'committed')
        changed = engine.state_hash()
        self.assertNotEqual(changed,engine.initial_hash)
        self.assertEqual(engine.dispatch('rollback_change',{})['status'],'committed_edit_reverted')
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertEqual(len(engine.events),3)
        self.assertEqual(engine.commits,1)
        previous = engine.source_pin
        for index,event in enumerate(engine.events):
            self.assertEqual(event['sequence'],index)
            self.assertEqual(event['previous_record_hash'],previous)
            disk = json.loads((engine.output/f'event_{index:03d}.json').read_text())
            self.assertEqual(disk,event)
            record = dict(disk)
            supplied = record.pop('record_hash')
            self.assertEqual(independent_record_digest(record),supplied)
            previous = supplied
        modified = copy.deepcopy(engine.events[1])
        modified['after_hash'] = '0'*64
        recorded = modified.pop('record_hash')
        self.assertNotEqual(independent_record_digest(modified),recorded)

    def test_rejected_calls_consume_finite_budget(self):
        engine = self.audit_fixture()
        for _ in range(engine.max_calls):
            self.assertIn('error',engine.dispatch('not_a_tool',{}))
        with self.assertRaises(ValueError):
            engine.dispatch('validate_geometry',{})
        self.assertEqual(len(engine.events),engine.max_calls)
        self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_replay_geometry_and_real_svg_are_identical(self):
        plan = [('inspect_region',{'roi':[0,0,1,1]}),
                ('get_candidates',{'roi':[0,0,1,1],'limit':4}),
                ('stage_candidates',{'trace_ids':[1,2]}),
                ('commit_change',{}), ('validate_geometry',{}),
                ('render_geometry',{'scale':1})]
        first, second = self.audit_fixture(), self.audit_fixture()
        rendered = []
        for engine in (first,second):
            for name,args in plan:
                answer = engine.dispatch(name,args)
                self.assertNotIn('error',answer)
            svg = (engine.output/answer['svg']).read_bytes()
            rendered.append(svg)
            root = ET.fromstring(svg)
            tags = [node.tag.rsplit('}',1)[-1] for node in root.iter()]
            self.assertNotIn('image',tags)
            self.assertNotIn('rect',tags)
            self.assertNotIn('script',tags)
            self.assertNotIn('foreignObject',tags)
            self.assertEqual(tags.count('path'),len(engine.items))
            self.assertTrue((engine.output/answer['png']).exists())
        self.assertEqual(first.source_pin,second.source_pin)
        self.assertEqual(first.state_hash(),second.state_hash())
        self.assertEqual(rendered[0],rendered[1])
        self.assertEqual([e['status'] for e in first.events],[e['status'] for e in second.events])


if __name__ == '__main__':
    unittest.main()
# END CHANGE AGD-AGENTIC-QA-TEST | 2026-10-31T15:07:18Z | EDITED | Author: agentic_qa
