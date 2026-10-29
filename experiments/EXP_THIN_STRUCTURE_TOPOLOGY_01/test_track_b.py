# START CHANGE AGD-THIN-TRACK-B-TEST | 2026-10-29T11:31:15Z | EDITED | Author: /root/appearance_fit
"""Abstract geometry controls, independent of image benchmarks and annotations."""
import copy,unittest
from track_b import initialize_safe,_utilities,_ring_records

def _line(a,b):return {'type':'L','p0':list(a),'p3':list(b)}
def _chain(key,points,labels,collapsed=False,closed=False):
    return {'id':key,'adjacent_face_labels':labels,'pixel_crack_vertices':points,'closed':closed,
      'segments':[_line(points[0],points[-1])] if collapsed else [_line(a,b) for a,b in zip(points,points[1:])]}

def _hole_graph():
    frame=[[0,0],[10,0],[10,10],[0,10],[0,0]];a=[4,4];c=[5,5]
    return {'width':10,'height':10,'chains':[_chain(0,frame,[1,0],closed=True),
      _chain(1,[a,[5,4],c],[2,1],True),_chain(2,[a,[4,5],c],[1,2],True)],
      'faces':{'1':[[{'chain':0,'forward':True}],[{'chain':2,'forward':True},{'chain':1,'forward':False}]],
               '2':[[{'chain':1,'forward':True},{'chain':2,'forward':False}]]},
      'incidence':[{'xy':a,'degree':2},{'xy':c,'degree':2}]}

class GuardTests(unittest.TestCase):
    def test_short_l_area_and_hole_preserved_without_grid_fallback(self):
        graph=_hole_graph();original=copy.deepcopy(graph);candidate,audit=initialize_safe(graph)
        self.assertEqual(graph,original);self.assertEqual(audit['accepted_chains'],[1,2])
        self.assertFalse(audit['unrepaired_collapses']);self.assertEqual(candidate['faces'],graph['faces'])
        self.assertEqual(candidate['incidence'],graph['incidence'])
        for chain in candidate['chains'][1:]:
            self.assertEqual(len(chain['segments']),1);self.assertEqual(chain['segments'][0]['type'],'C')
            self.assertEqual(chain['segments'][0]['p1'],chain['pixel_crack_vertices'][1])
            self.assertEqual(chain['segments'][0]['p2'],chain['pixel_crack_vertices'][1])
            self.assertEqual(chain['segments'][0]['p0'],chain['pixel_crack_vertices'][0])
            self.assertEqual(chain['segments'][0]['p3'],chain['pixel_crack_vertices'][-1])
        utilities,area=_utilities();rings,_=_ring_records(candidate,utilities,area)
        self.assertTrue(rings[('1',0)]['poly'].contains(rings[('1',1)]['poly']))
        self.assertGreater(rings[('2',0)]['area'],.1)

    def test_shared_t_junction_endpoints_and_reversed_references_unchanged(self):
        a=[4,4];c=[5,5];origin=[0,0];end=[10,10]
        graph={'width':10,'height':10,'chains':[
          _chain(0,[origin,[10,0],end],[1,0]),_chain(1,[a,[5,4],c],[2,1],True),
          _chain(2,[a,[4,5],c],[3,2],True),_chain(3,[origin,[0,10],end],[0,3]),
          _chain(4,[origin,a],[3,1]),_chain(5,[c,end],[3,1])],
          'faces':{'1':[[{'chain':0,'forward':True},{'chain':5,'forward':False},{'chain':1,'forward':False},{'chain':4,'forward':False}]],
                   '2':[[{'chain':1,'forward':True},{'chain':2,'forward':False}]],
                   '3':[[{'chain':4,'forward':True},{'chain':2,'forward':True},{'chain':5,'forward':True},{'chain':3,'forward':False}]]},
          'incidence':[{'xy':a,'degree':3},{'xy':c,'degree':3}]}
        candidate,audit=initialize_safe(graph)
        self.assertEqual(audit['accepted_chains'],[1,2]);self.assertEqual(candidate['faces'],graph['faces'])
        for key in (0,3,4,5):self.assertEqual(candidate['chains'][key],graph['chains'][key])

    def test_new_collision_is_rejected_and_original_retained(self):
        graph=_hole_graph()
        graph['chains'].append(_chain(3,[[4.7,4.125],[5,4.125]],[4,0]))
        candidate,audit=initialize_safe(graph)
        self.assertEqual(candidate,graph);self.assertFalse(audit['accepted_chains'])
        self.assertTrue(any('new_crossing'==reason['code'] for event in audit['events'] for reason in event['rejections']))
        self.assertTrue(audit['unrepaired_collapses'])

    def test_nonunit_shape_is_not_repaired_by_grid_outline(self):
        graph=_hole_graph()
        for chain in graph['chains'][1:]:
            chain['pixel_crack_vertices']=[[x*2,y*2] for x,y in chain['pixel_crack_vertices']]
            chain['segments']=[_line(chain['pixel_crack_vertices'][0],chain['pixel_crack_vertices'][-1])]
        candidate,audit=initialize_safe(graph)
        self.assertEqual(candidate,graph);self.assertEqual(audit['eligible_chains'],[])
        self.assertTrue(audit['unrepaired_collapses'])

if __name__=='__main__':unittest.main()
# END CHANGE AGD-THIN-TRACK-B-TEST | 2026-10-29T11:31:15Z | EDITED
