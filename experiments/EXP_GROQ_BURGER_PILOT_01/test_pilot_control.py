# START CHANGE AGD-PILOT-TEST | 2026-10-31T16:16:43Z | CREATED | Author: root
"""Adversarial controls, injected synthetic provider only; no key/environment access."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import tempfile,unittest,json,hashlib,copy
E=Path(__file__).resolve().parent
sys.path[:0]=[str(E),str(E.parent/'EXP_AI_GUIDED_GEOMETRY_01')]
from pilot_control import PilotSession,PilotStop,observation,digest
from groq_adapter import GroqAdapter


def reply(cid='call_1', content=None):
    obs=dict(missing_components=['unverified local contour'],roi=[0,0,1,1],uncertainty=.7,chosen_action='inspect candidates',unavailable_capabilities=['new boundaries'],stop_reason='')
    return dict(status='SYNTHETIC',message=dict(content=content or json.dumps(obs),tool_calls=[dict(id=cid,type='function',function=dict(name='get_candidates',arguments='{"roi":[0,0,1,1],"limit":2}'))]),usage=dict(prompt_tokens=80,completion_tokens=20,total_tokens=100))


class FakeEngine:
    def __init__(self):
        from geometry_engine import geometry_tool_schemas
        self.items=[];self.pending=None;self.history=[];self.events=[];self.commits=0;self.source_pin='source'
        self.schemas={t['function']['name']:t['function']['parameters'] for t in geometry_tool_schemas()}
    def state_hash(self):return digest(self.items)
    def dispatch(self,name,args):
        self.events.append(dict(tool=name,arguments=args));return dict(status='observed')


class SyntheticAdapter:
    live=False
    def __init__(self,value=None):self.value=value or reply();self.calls=0
    def _prepare(self,*args):return b'',args[0][0]['hashes'],1000
    def request(self,*args):self.calls+=1;return copy.deepcopy(self.value)


class ControlsTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.engine=FakeEngine();self.s=PilotSession(self.root/'s')
        p=self.root/'image.png';p.write_bytes(b'synthetic preview zero');self.h=hashlib.sha256(p.read_bytes()).hexdigest()
        self.s.create('test',self.engine,dict(file='preview_00.png',sha256=self.h),{},preview_source=p)
    def tearDown(self):self.tmp.cleanup()
    def build(self,e,s):return [dict(hashes=[s['preview']['sha256']])],[]
    def preview(self,e,s):
        e.dispatch('render_geometry',{})
        p=self.s.directory/f"preview_{s['requests']:02d}.png";p.write_bytes(str(s['requests']).encode())
        return dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()),{}
    def approve(self):
        state,_,_=self.s.read();self.s.approve('test',state['requests'],state['preview']['sha256'])
    def step(self,a=None,clock=100):return self.s.step(self.engine,a or SyntheticAdapter(),self.build,self.preview,lambda:clock)
    def test_two_steps_restart_preserves_budget(self):
        self.approve();first=self.step();self.assertEqual(first['phase'],'WAITING_APPROVAL')
        self.s=PilotSession(self.s.directory);self.engine=FakeEngine()
        with self.assertRaises(PilotStop):self.step(SyntheticAdapter(reply('call_2')),200)
        self.approve();second=self.step(SyntheticAdapter(reply('call_2')),200)
        self.assertEqual((second['requests'],second['reserved_tokens'],second['completion_tokens']),(2,2000,40))
        self.assertEqual(len(second['actions']),2)
        with self.assertRaises(PilotStop):self.step(clock=300)
    def test_wrong_identity_index_and_hash(self):
        for ident,index,h in [('other',0,self.h),('test',1,self.h),('test',0,'0'*64)]:
            with self.assertRaises(PilotStop):self.s.approve(ident,index,h)
    def test_preview_substitution(self):
        self.approve();(self.s.directory/'preview_00.png').write_bytes(b'changed');a=SyntheticAdapter()
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
    def test_duplicate_call_no_reexecution(self):
        self.approve();self.step();self.approve();a=SyntheticAdapter(reply())
        with self.assertRaises(PilotStop):self.step(a,200)
        self.assertEqual(self.s.read()[0]['phase'],'HALTED');self.assertEqual(len(self.engine.events),3)
    def test_invalid_model_consumes_reservation_and_halts(self):
        self.approve();a=SyntheticAdapter(reply(content='not JSON'))
        with self.assertRaises(PilotStop):self.step(a)
        state,_,_=self.s.read();self.assertEqual((state['requests'],state['reserved_tokens'],state['phase']),(1,1000,'HALTED'))
        with self.assertRaises(PilotStop):self.step(a,200)
        self.assertEqual(a.calls,1)
    def test_ambiguous_provider_failure_never_retried(self):
        class Fail(SyntheticAdapter):
            def request(self,*a):raise RuntimeError('do not log arbitrary provider body')
        self.approve()
        with self.assertRaises(PilotStop):self.step(Fail())
        self.assertNotIn('arbitrary', ''.join(p.read_text() for p in self.s.directory.glob('record*')))
        with self.assertRaises(PilotStop):self.step(clock=200)
    def test_reserved_crash_state_blocks_resume(self):
        s,_,_=self.s.read();s['phase']='RESERVED';s['requests']=1;s['reserved_tokens']=1000;self.s.append(s,'REQUEST_RESERVED')
        with self.assertRaises(PilotStop):self.step()
    def test_journal_tampering_and_missing_record(self):
        self.approve();p=self.s.directory/'record_001.json';data=json.loads(p.read_text());data['state']['requests']=1;p.write_text(json.dumps(data))
        with self.assertRaises(PilotStop):self.s.read()
    def test_lock_blocks_competing_process(self):
        (self.s.directory/'LOCK').write_text('')
        with self.assertRaises(PilotStop):self.approve()
    def test_observation_sanitized_without_authority(self):
        raw=json.loads(reply()['message']['content']);raw['chosen_action']='gsk_SYNTHETIC_NOT_A_REAL_CREDENTIAL Bearer dummysecret'
        self.approve();self.step(SyntheticAdapter(reply(content=json.dumps(raw))))
        text=''.join(p.read_text() for p in self.s.directory.glob('record*'))
        self.assertNotIn('dummysecret',text);self.assertNotIn('gsk_SYNTHETIC',text);self.assertIn('UNTRUSTED_PLANNER_OBSERVATION',text)
    def test_observation_extra_keys_nan_and_degenerate_roi(self):
        raw=json.loads(reply()['message']['content'])
        for key,value in [('authority','accepted'),('roi',[0,0,0,1]),('uncertainty',float('nan'))]:
            bad=dict(raw);bad[key]=value
            with self.assertRaises(PilotStop):observation(json.dumps(bad))
        with self.assertRaises(PilotStop):observation('{"roi":[],"roi":[]}')
    def test_image_set_and_token_limits_before_transport(self):
        self.approve();a=SyntheticAdapter()
        a._prepare=lambda *x:(b'', ['wrong'],1000)
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
        a._prepare=lambda *x:(b'',[self.h],15001)
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
    def test_tool_budget_never_refilled(self):
        state,_,_=self.s.read();state['engine']['events']=[{}]*12;self.s.append(state,'TEST_EXHAUSTED');self.approve()
        with self.assertRaises(PilotStop):self.step()
        self.assertEqual(self.s.read()[0]['phase'],'HALTED')
    def test_live_adapter_cannot_enter_synthetic_session(self):
        self.approve();a=SyntheticAdapter();a.live=True
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)


if __name__=='__main__':unittest.main()
# END CHANGE AGD-PILOT-TEST | 2026-10-31T16:16:43Z | CREATED | Author: root
