# START CHANGE AGD-ISOLATION-TEST-ISOLATION | 2026-10-29T06:48:34Z | CREATED | Author: root
"""Interface/measurement safeguards, not acceptance tests for reconstruction."""
import json,unittest
import numpy as np
from geometry_eval import flatten_cubic,signed_area,svg_graph,compare_samples

class GeometryIsolationTests(unittest.TestCase):
    def test_cubic_flattening_analytic_parabola(self):
        # Quadratic x=t,y=tÂ² elevated to cubic, analytic distance check.
        p=np.array([[0,0],[1/3,0],[2/3,1/3],[1,1]],float)
        from shapely.geometry import LineString,Point
        line=LineString(flatten_cubic(p,epsilon=.001))
        self.assertLessEqual(max(line.distance(Point(t,t*t)) for t in np.linspace(0,1,501)),.00101)

    def test_ring_area_detects_collapsed_cell(self):
        self.assertEqual(signed_area([[0,0],[1,0],[1,1],[0,1],[0,0]]),1.)
        self.assertEqual(signed_area([[0,0],[1,1],[0,0]]),0.)

    def test_distance_is_symmetric_and_exposes_missing_detail(self):
        a=np.array([[0,0],[1,0],[10,0]],float);b=a[:2]
        r=compare_samples(a,b)
        self.assertEqual(r['a_recall_at_1px'],2/3)
        self.assertGreater(r['symmetric_p95_px'],1)

    def test_svg_preserves_shared_reversal_hole(self):
        graph={'width':4,'height':4,'chains':[],'faces':{'1':[[{'chain':0,'forward':True}],[{'chain':1,'forward':False}]],'2':[[{'chain':1,'forward':True}]]}}
        for i,p in enumerate([[[0,0],[4,0],[4,4],[0,4],[0,0]],[[1,1],[3,1],[3,3],[1,3],[1,1]]]):
            graph['chains'].append({'id':i,'closed':True,'adjacent_face_labels':[0,1] if i==0 else [1,2],
              'pixel_crack_vertices':p,'segments':[{'type':'L','p0':a,'p3':b} for a,b in zip(p,p[1:])]})
        from xml.etree import ElementTree as ET
        xml=ET.fromstring(svg_graph(graph,regions=True,foreground={1}))
        path=next(iter(xml));self.assertEqual(path.attrib['fill-rule'],'evenodd')
        self.assertNotIn('image',ET.tostring(xml).decode())
        self.assertEqual(path.attrib['d'].count('M'),2)
        import subprocess,tempfile
        from pathlib import Path
        from isolation import WORK
        from PIL import Image
        with tempfile.TemporaryDirectory(dir=WORK) as folder:
            src=Path(folder)/'hole.svg';png=src.with_suffix('.png');src.write_text(ET.tostring(xml,encoding='unicode'))
            subprocess.run([str(WORK/'resvg/resvg.exe'),str(src),str(png)],check=True,capture_output=True)
            alpha=np.asarray(Image.open(png).convert('RGBA'))[...,3]
            self.assertEqual(alpha[1,1],0);self.assertEqual(alpha[0,0],255)

    def test_common_face_mapping_rejects_changed_boundaries(self):
        from common_geometry import normalize_to_common_faces
        a={'chains':[{'id':0,'adjacent_face_labels':[1,2],'pixel_crack_vertices':[[0,0],[1,0]],'segments':[]}]}
        b={'chains':[{'id':9,'adjacent_face_labels':[1,2],'pixel_crack_vertices':[[1,0],[0,0]],'segments':[]}]}
        result=normalize_to_common_faces(a,b)
        self.assertTrue(result['normalization']['chain_mapping'][0]['reversed'])
        b['chains'][0]['pixel_crack_vertices']=[[1,1],[0,0]]
        with self.assertRaises(KeyError):normalize_to_common_faces(a,b)

    def test_only_closed_rings_gain_svg_closure(self):
        from geometry_eval import chain_points
        ch={'closed':False,'segments':[{'type':'L','p0':[0,0],'p3':[1,1]}]}
        self.assertEqual(len(chain_points(ch)),2)
        ch['closed']=True;self.assertEqual(len(chain_points(ch)),3)

    def test_protocol_prevents_truth_selection(self):
        from pathlib import Path
        p=json.loads((Path(__file__).parent/'protocol.json').read_text())
        self.assertIn('No candidate',p['policy']['truth_selection'])
        self.assertEqual(p['architecture'],'NOT_APPROVED')
        self.assertEqual(p['budgets']['combinations_max_per_case'],4)

if __name__=='__main__':unittest.main()

# END CHANGE AGD-ISOLATION-TEST-ISOLATION | 2026-10-29T06:48:34Z | CREATED | Author: root
