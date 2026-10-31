# START CHANGE AGD-AGENTIC-TOOLS-TEST | 2026-10-31T11:54:38Z | EDITED | Author: geometry_tools
"""Synthetic-only tool contract controls; no evaluator inputs or provider."""
import json
from pathlib import Path
import tempfile
import unittest
import numpy as np
from geometry_engine import GeometryToolEngine, geometry_tool_schemas, validate_tool_value

REPO = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
WORK = Path.cwd()/'work'


def synthetic_trace(tid, points):
    return {'trace_id': tid, 'source_points_xy': points, 'length_px': float(np.linalg.norm(np.diff(points,axis=0),axis=1).sum())}


class EngineContractTests(unittest.TestCase):
    def make_engine_fixture(self, traces=None, items=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        rgb = np.full((32,32,3),255,np.uint8)
        rgb[8:10,:] = 0
        source = traces or [synthetic_trace(0,[[2,8],[8,8],[14,8],[24,8]])]
        return GeometryToolEngine(rgb,source,items or [],Path(directory.name)/'session',REPO,WORK)

    def test_strict_tools_schema(self):
        engine = self.make_engine_fixture()
        for name, args in [('exec',{'command':'x'}),('get_candidates',{'roi':[0,0,1,1],'limit':True}),('inspect_region',{'roi':[0,0,float('nan'),1]}),('inspect_region',{'roi':[0,0,1,1],'path':'outside'}),('stage_candidates',{'trace_ids':[0,0]})]:
            result=engine.dispatch(name,args)
            self.assertIn('error',result)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertTrue(all(x['arguments'] is None for x in engine.events))

    def test_atomic_commit_and_exact_rollback(self):
        engine=self.make_engine_fixture()
        before=engine.state_hash()
        staged=engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertEqual(staged['added_paths'],1)
        self.assertEqual(engine.state_hash(),before)
        committed=engine.dispatch('commit_change',{})
        self.assertEqual(committed['status'],'committed')
        self.assertNotEqual(engine.state_hash(),before)
        engine.dispatch('rollback_change',{})
        self.assertEqual(engine.state_hash(),before)
        self.assertEqual(len(engine.items),0)

    def test_pending_rejection_and_rollback(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertIn('error',engine.dispatch('stage_candidates',{'trace_ids':[0]}))
        self.assertEqual(engine.dispatch('rollback_change',{})['status'],'pending_discarded')
        self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_existing_trace_not_duplicated(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]});engine.dispatch('commit_change',{})
        out=engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertNotIn('error',out,repr(out))
        self.assertEqual(out['added_paths'],0)
        self.assertEqual(out['ledger'][0]['reason'],'existing_trace')
        self.assertIn('error',engine.dispatch('commit_change',{}))
        self.assertEqual(len(engine.items),1)

    def test_closed_loop_corner_and_junction_contract(self):
        traces=[synthetic_trace(0,[[4,4],[20,4],[20,20],[4,20],[4,4]]),synthetic_trace(1,[[20,4],[26,4],[28,4]])]
        engine=self.make_engine_fixture(traces)
        out=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertGreaterEqual(out['added_paths'],1)
        engine.dispatch('commit_change',{})
        closed=[x for x in engine.items if x.get('closed')]
        self.assertEqual(len(closed),1)
        cc=np.asarray(closed[0]['curves'])
        self.assertTrue(np.array_equal(cc[0,0],cc[-1,-1]))
        self.assertTrue(np.array_equal(cc[:-1,-1],cc[1:,0]))

    def test_replay_same_geometry_hash(self):
        plan=[('get_candidates',{'roi':[0,0,1,1],'limit':4}),('stage_candidates',{'trace_ids':[0]}),('commit_change',{}),('validate_geometry',{})]
        first,second=self.make_engine_fixture(),self.make_engine_fixture()
        for engine in [first,second]:
            for name,args in plan:engine.dispatch(name,args)
        self.assertEqual(first.state_hash(),second.state_hash())
        self.assertEqual(first.replay_decision_hash(),second.replay_decision_hash())
        self.assertEqual(first.source_pin,second.source_pin)
        for event in first.events:
            self.assertEqual(json.loads((first.output/('event_%03d.json'%event['sequence'])).read_text())['record_hash'],event['record_hash'])

    def test_actual_svg_renderer(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]});engine.dispatch('commit_change',{})
        for scale in [1,4,16]:
            result=engine.dispatch('render_geometry',{'scale':scale})
            self.assertNotIn('error',result)
            svg=(engine.output/result['svg']).read_text()
            self.assertIn(' C',svg)
            self.assertNotIn('<image',svg)
            self.assertTrue((engine.output/result['png']).exists())

    def test_roi_and_scale_bounds(self):
        engine=self.make_engine_fixture()
        self.assertIn('error',engine.dispatch('inspect_region',{'roi':[.8,0,.2,1]}))
        self.assertIn('error',engine.dispatch('render_geometry',{'scale':2}))
        self.assertIn('error',engine.dispatch('stage_candidates',{'trace_ids':[999]}))
        self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_duplicate_geometry_different_source_id(self):
        points=[[2,8],[8,8],[14,8],[24,8]]
        engine=self.make_engine_fixture([synthetic_trace(0,points),synthetic_trace(1,points)])
        result=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertEqual(result['added_paths'],1)
        self.assertEqual(result['ledger'][1]['rejections'][0]['reason'],'duplicate_curve')

    def test_nested_closed_boundaries_not_semantic_holes(self):
        engine=self.make_engine_fixture([synthetic_trace(0,[[2,2],[28,2],[28,28],[2,28],[2,2]]),synthetic_trace(1,[[8,8],[20,8],[20,20],[8,20],[8,8]])])
        staged=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertEqual(staged['added_paths'],2)
        engine.dispatch('commit_change',{})
        diagnostic=engine.dispatch('validate_geometry',{})
        self.assertEqual(diagnostic['closed_paths'],2)
        self.assertEqual(diagnostic['region_ownership'],'NOT_ESTABLISHED')

    def test_allowlisted_tool_does_not_accept_path_or_code(self):
        engine=self.make_engine_fixture()
        result=engine.dispatch('render_geometry',{'scale':1,'renderer':'untrusted'})
        self.assertIn('error',result)
        self.assertEqual(len(list(engine.output.glob('*.svg'))),0)
        self.assertIn('error',engine.dispatch([],{}))
        self.assertIn('error',engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':10**1000}))

    def test_usable_candidate_not_hidden_by_short_noise(self):
        short=[synthetic_trace(tid,[[2,8],[3,8]]) for tid in range(20)]
        long=synthetic_trace(99,[[2,24],[12,24],[24,24]])
        engine=self.make_engine_fixture(short+[long])
        result=engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':4})
        self.assertEqual(result['candidates'][0]['trace_id'],99)
        self.assertTrue(result['candidates'][0]['eligible'])
        self.assertFalse(result['candidates'][1]['eligible'])

if __name__=='__main__':unittest.main()
# END CHANGE AGD-AGENTIC-TOOLS-TEST | 2026-10-31T11:54:38Z | EDITED | Author: geometry_tools
