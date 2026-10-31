# START CHANGE AGD-GROQ-LOOP-TEST | 2026-10-31T15:16:13Z | EDITED | Author: root
import unittest,tempfile,json
from pathlib import Path
import numpy as np
from groq_pilot import strict_call_arguments,run_visual_planner,wait_for_pilot_cadence,R,W
from geometry_engine import GeometryToolEngine
from groq_adapter import GroqAdapter,ProviderGateError
class PilotTests(unittest.TestCase):
 def make_engine(self,path):
  image=np.full((32,32,3),255,dtype=np.uint8);image[8,2:24]=0
  points=[[float(x),8.] for x in range(2,24)]
  return GeometryToolEngine(image,[dict(trace_id=0,source_points_xy=points,length_px=21)],[],path,R,W)
 def test_json_duplicate_and_nonfinite(self):
  for text in ['{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}']:
   with self.assertRaises(ValueError):strict_call_arguments(text)
 def test_dryrun_no_network(self):
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'dry');r=run_visual_planner(engine,GroqAdapter(), 'synthetic')
   self.assertEqual(r['status'],'DRY_RUN');self.assertEqual(r['requests'],0);self.assertFalse(engine.items)
 def test_unverified_live_denied(self):
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'deny')
   with self.assertRaises(ProviderGateError):run_visual_planner(engine,GroqAdapter(live=True),'synthetic')
 def test_explicit_bounded_pacing_no_real_sleep(self):
  clock=[100.];adapter=GroqAdapter(live=True,clock=lambda:clock[0]);adapter._last_request=100.;waits=[]
  def advance(seconds):waits.append(seconds);clock[0]+=seconds
  wait_for_pilot_cadence(adapter,advance);self.assertEqual(waits,[30.,30.,1.]);self.assertEqual(clock[0],161.)
 def test_frozen_clock_cannot_extend_pacing_budget(self):
  adapter=GroqAdapter(live=True,clock=lambda:100.);adapter._last_request=100.;waits=[]
  with self.assertRaises(ProviderGateError):wait_for_pilot_cadence(adapter,lambda t:waits.append(t))
  self.assertEqual(sum(waits),61.)
 def test_feedback_and_invalid_stage_preserves_commit(self):
  class RecordedAdapter:
   def __init__(self):self.messages=[]
   def request(self,messages,tools,case):
    self.messages.append(messages)
    stage=next(t for t in tools if t['function']['name']=='stage_candidates');assert stage['function']['parameters']['properties']['trace_ids']['maxItems']==2
    args={'trace_ids':[0]} if len(self.messages)==1 else {'trace_ids':[999]}
    return dict(status='LIVE',reserved_tokens=1,message=dict(tool_calls=[dict(id='fixture_'+str(len(self.messages)),type='function',function=dict(name='stage_candidates',arguments=json.dumps(args)))]))
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'fixture');adapter=RecordedAdapter();r=run_visual_planner(engine,adapter,'synthetic')
   self.assertEqual(engine.commits,1);self.assertEqual(len(engine.items),1);self.assertLessEqual(len(engine.events),12);self.assertIsNone(engine.pending)
   self.assertIn('committed',adapter.messages[1][-1]['content'][0]['text']);self.assertIn('geometry_diagnostics',adapter.messages[1][-1]['content'][0]['text']);self.assertEqual(adapter.messages[1][1]['role'],'assistant');self.assertEqual(adapter.messages[1][2]['role'],'tool')
if __name__=='__main__':unittest.main()
# END CHANGE AGD-GROQ-LOOP-TEST | 2026-10-31T15:16:13Z | EDITED | Author: root
