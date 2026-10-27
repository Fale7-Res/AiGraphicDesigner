"""Independent artifact contract checks; no trace/search reruns."""
# START CHANGE AGD-ABLATION-QA | 2026-10-27T14:44:00Z | CREATED | Author: root
from pathlib import Path
import hashlib,json,unittest,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parent
SVG='http://www.w3.org/2000/svg'

def geometry_tree(node):
    tag=node.tag.rsplit('}',1)[-1]
    if tag in ['linearGradient','radialGradient']:return None
    if tag=='mask':return ET.tostring(node,encoding='unicode')
    attributes=dict(node.attrib)
    if tag=='path':attributes.pop('fill',None)
    children=[v for c in node if (v:=geometry_tree(c)) is not None]
    if tag=='defs' and not children:return None
    return [node.tag,attributes,children]

class SavedAblationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'inputs/manifest.json').read_text())
        cls.cases=cls.manifest['cases']
    def test_complete_frozen_suite_and_artifact_hashes(self):
        self.assertEqual(len(self.cases),9)
        for case in self.cases:
            for key in ['source','reference','geometry','ground_truth_svg']:
                if key in case:self.assertEqual(hashlib.sha256(Path(case[key]).read_bytes()).hexdigest(),case[key+'_sha256'])
            result=json.loads((ROOT/'results'/case['id']/'result.json').read_text())
            for name,row in result['conditions'].items():self.assertEqual(hashlib.sha256((ROOT/'results'/case['id']/name/'output.svg').read_bytes()).hexdigest(),row['sha256'])
    def test_strict_b_c_d_geometry_and_alpha_mask_identity(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id'];trees=[ET.parse(folder/name/'output.svg').getroot() for name in 'BCD']
            self.assertEqual(geometry_tree(trees[0]),geometry_tree(trees[1]),case['id'])
            self.assertEqual(geometry_tree(trees[1]),geometry_tree(trees[2]),case['id'])
    def test_svg_safety_gradient_capacity_and_png_integrity(self):
        for path in (ROOT/'results').rglob('*.svg'):
            root=ET.parse(path).getroot();ids={e.get('id') for e in root.iter() if e.get('id')}
            for e in root.iter():
                tag=e.tag.rsplit('}',1)[-1]
                self.assertNotIn(tag,['image','foreignObject','script','filter'],str(path))
                for k,v in e.attrib.items():
                    if k.rsplit('}',1)[-1]=='href':self.assertTrue(v.startswith('#'),str(path))
                    if v.startswith('url('):self.assertIn(v[5:-1],ids,str(path))
                if tag in ['linearGradient','radialGradient']:
                    stops=list(e);self.assertLessEqual(len(stops),4);self.assertGreaterEqual(len(stops),2)
                    offsets=[float(s.get('offset')) for s in stops];self.assertEqual(offsets,sorted(offsets))
                    self.assertEqual(e.get('gradientUnits'),'userSpaceOnUse')
                    if tag=='radialGradient':self.assertGreater(float(e.get('r')),0)
        for path in (ROOT/'results').rglob('*.png'):
            with Image.open(path) as im:im.verify()
    def test_saved_actual_white_mse_and_alpha(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id'];result=json.loads((folder/'result.json').read_text());source=Image.open(folder/'source.png').convert('RGBA')
            a=np.asarray(source)
            ref=np.asarray(Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')).astype(float)
            for name,row in result['conditions'].items():
                b=np.asarray(Image.open(folder/name/'white.png').convert('RGB')).astype(float)
                self.assertAlmostEqual(float(((ref-b)**2).mean()),row['metrics']['white']['mse'],places=10)
                alpha=np.asarray(Image.open(folder/name/'render.png').convert('RGBA'))[:,:,3]
                self.assertAlmostEqual(float(np.abs(a[:,:,3].astype(float)-alpha).mean()),row['alpha_mae'],places=10)
    def test_zoom_evidence_and_known_control_geometry(self):
        for case in self.cases:
            folder=ROOT/'results'/case['id']
            for crop in ['worst_error','center']:
                for scale in [1,4,16]:self.assertTrue((folder/f'{crop}_{scale}x.png').is_file())
            if case['known_vector']:
                g=json.loads((folder/'known_geometry.json').read_text());self.assertTrue(0<=g['foreground_iou_4x']<=1)

if __name__=='__main__':unittest.main(verbosity=2)
# END CHANGE AGD-ABLATION-QA | 2026-10-27T14:44:00Z | CREATED | Author: root
