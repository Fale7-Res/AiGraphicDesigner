# START CHANGE AGD-PILOT-INDEPENDENT-QA | 2026-11-04T15:39:40Z | EDITED | Author: agentic_qa
"""Independent adversarial session tests. No provider/env/credential access."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch

E=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_GROQ_BURGER_PILOT_01')
sys.path[:0]=[str(E),str(E.parent/'EXP_AI_GUIDED_GEOMETRY_01')]
from pilot_control import PilotSession,PilotStop,digest,strict_json_record
from geometry_engine import geometry_tool_schemas


class IndependentEngineDouble:
    def __init__(self):
        self.items=[];self.pending=None;self.history=[];self.events=[];self.commits=0
        self.source_pin='independent-frozen-source'
        self.schemas={t['function']['name']:t['function']['parameters'] for t in geometry_tool_schemas()}
    def state_hash(self):
        return digest(self.items)
    def dispatch(self,name,args):
        self.events.append(dict(tool=name,arguments=args))
        return dict(status='observed')


def independent_response(call_ids=('q1',)):
    obs=dict(missing_components=['Unverified boundary'],roi=[0,0,1,1],uncertainty=.8,
        chosen_action='Inspect only',unavailable_capabilities=['region ownership'],stop_reason='')
    calls=[dict(id=cid,type='function',function=dict(name='get_candidates',arguments='{"roi":[0,0,1,1],"limit":1}')) for cid in call_ids]
    return dict(status='SYNTHETIC',message=dict(content=json.dumps(obs),tool_calls=calls),
        usage=dict(prompt_tokens=70,completion_tokens=20,total_tokens=90))


class IndependentAdapterDouble:
    live=False
    def __init__(self,response=None):
        self.calls=0;self.response=response or independent_response()
    def _prepare(self,messages,tools):
        return b'',messages[0]['image_hashes'],2000
    def request(self,*_):
        self.calls+=1
        return copy.deepcopy(self.response)


class IndependentHardeningAudit(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.engine=IndependentEngineDouble()
        self.session=PilotSession(self.base/'session')
        file=self.base/'source.png';file.write_bytes(b'independent synthetic image')
        self.sha=hashlib.sha256(file.read_bytes()).hexdigest()
        self.session.create('independent',self.engine,dict(file='preview_00.png',sha256=self.sha),{},preview_source=file)
    def approve_current(self):
        state,_,_=self.session.read()
        self.session.approve(state['identity'],state['requests'],state['preview']['sha256'])
    def request_builder(self,engine,state):
        return [dict(image_hashes=[state['preview']['sha256']])],[]
    def next_preview(self,engine,state):
        engine.dispatch('render_geometry',{})
        file=self.session.directory/f"preview_{state['requests']:02d}.png"
        file.write_bytes(str(state['requests']).encode())
        return dict(file=file.name,sha256=hashlib.sha256(file.read_bytes()).hexdigest()),{}
    def run_step(self,adapter=None,now=100):
        return self.session.step(self.engine,adapter or IndependentAdapterDouble(),
            self.request_builder,self.next_preview,lambda:now)

    def test_source_identity_or_no_approval_stops_before_transport(self):
        adapter=IndependentAdapterDouble()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.approve_current();self.engine.source_pin='different-source'
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_bool_index_and_stale_preview_approval_fail(self):
        with self.assertRaises(PilotStop):self.session.approve('independent',False,self.sha)
        self.approve_current();self.run_step()
        with self.assertRaises(PilotStop):self.session.approve('independent',0,self.sha)

    def test_all_proposals_validate_before_any_effect(self):
        self.approve_current()
        bad=independent_response(('same','same'))
        with self.assertRaises(PilotStop):self.run_step(IndependentAdapterDouble(bad))
        self.assertEqual(self.engine.events,[])
        state,_,_=self.session.read()
        self.assertEqual((state['phase'],state['requests'],state['reserved_tokens']),('HALTED',1,2000))

    def test_ambiguous_failure_is_reserved_and_not_resumable(self):
        class FailingAdapter(IndependentAdapterDouble):
            def request(self,*_):
                self.calls+=1
                raise RuntimeError('Bearer synthetic-marker-never-log')
        adapter=FailingAdapter();self.approve_current()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.session=PilotSession(self.session.directory)
        with self.assertRaises(PilotStop):self.run_step(adapter,200)
        self.assertEqual(adapter.calls,1)
        self.assertNotIn('synthetic-marker-never-log',''.join(p.read_text() for p in self.session.directory.glob('record*')))

    def test_restart_does_not_refund_tokens_tools_or_requests(self):
        self.approve_current();first=self.run_step()
        self.engine=IndependentEngineDouble();self.session=PilotSession(self.session.directory)
        self.approve_current();second=self.run_step(IndependentAdapterDouble(independent_response(('q2',))),200)
        self.assertEqual((second['requests'],second['reserved_tokens'],second['completion_tokens']),(2,4000,40))
        self.assertEqual(len(second['engine']['events']),6)
        with self.assertRaises(PilotStop):self.run_step(now=300)

    def test_different_request_image_stops_without_reservation(self):
        self.approve_current();adapter=IndependentAdapterDouble()
        adapter._prepare=lambda *_:(b'', ['f'*64],2000)
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_journal_chain_gap_or_tampering_fail_closed(self):
        self.approve_current()
        file=self.session.directory/'record_001.json'
        file.rename(self.session.directory/'record_002.json')
        with self.assertRaises(PilotStop):self.session.read()

    def test_journal_duplicate_json_key_rejected(self):
        file=self.session.directory/'record_000.json'
        text=file.read_text()
        file.write_text('{"sequence":999,'+text[1:])
        with self.assertRaises(PilotStop):self.session.read()

    def test_private_proof_duplicate_key_rejected(self):
        file=self.base/'proof.json'
        file.write_text('{"free_plan":false,"free_plan":true}')
        with self.assertRaises(PilotStop):strict_json_record(file)

    def test_missing_geometry_event_stops_before_reservation(self):
        self.engine.events=[dict(sequence=0,tool='get_candidates')]
        self.engine._validate_state=lambda _:None
        self.engine.output=self.base/'engine_records'
        self.engine.output.mkdir()
        preview=self.session.directory/'preview_00.png'
        self.session=PilotSession(self.base/'evidence_session')
        self.session.create('independent',self.engine,dict(file='preview_00.png',sha256=self.sha),{},preview_source=preview)
        self.approve_current();adapter=IndependentAdapterDouble()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_observation_records_remain_untrusted_and_redacted(self):
        self.approve_current();response=independent_response()
        obs=json.loads(response['message']['content'])
        obs['missing_components']=['Bearer synthetic-observation-secret']
        obs['unavailable_capabilities']=['authorization=synthetic-auth-token']
        response['message']['content']=json.dumps(obs)
        state=self.run_step(IndependentAdapterDouble(response))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn('synthetic-observation-secret',saved)
        self.assertNotIn('synthetic-auth-token',saved)
        self.assertEqual(state['observations'][0]['authority'],'UNTRUSTED_PLANNER_OBSERVATION')

    def test_usage_extras_are_not_persisted(self):
        self.approve_current();response=independent_response()
        response['usage']['unexpected_private_debug']='Bearer synthetic-unvalidated-usage-marker'
        self.run_step(IndependentAdapterDouble(response))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn('synthetic-unvalidated-usage-marker',saved)
        self.assertNotIn('unexpected_private_debug',saved)

    def test_known_usage_survives_invalid_observation(self):
        self.approve_current();response=independent_response()
        response['message']['content']=None
        with self.assertRaises(PilotStop):self.run_step(IndependentAdapterDouble(response))
        state,_,_=self.session.read()
        self.assertEqual(state['phase'],'HALTED')
        self.assertEqual(state['completion_tokens'],20)
        self.assertEqual(state['usage'][0]['total_tokens'],90)

    def test_changed_implementation_stops_before_transport(self):
        self.approve_current();adapter=IndependentAdapterDouble()
        with patch('pilot_control.implementation_pin',return_value='different-implementation'):
            with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_credential_shaped_tool_identity_is_not_journaled(self):
        marker='gsk_'+'qa_marker'
        self.approve_current()
        with self.assertRaises(PilotStop):
            self.run_step(IndependentAdapterDouble(independent_response((marker,))))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn(marker,saved)
        self.assertEqual(self.engine.events,[])
        self.assertEqual(self.session.read()[0]['phase'],'HALTED')


if __name__=='__main__':unittest.main()
# END CHANGE AGD-PILOT-INDEPENDENT-QA | 2026-11-04T15:39:40Z | EDITED | Author: agentic_qa
