"""Saved-result and microgeometry contracts; no historical searches rerun."""
# START CHANGE AGD-BOTTLENECK-TESTS | 2026-10-28T03:34:28Z | EDITED | Author: root
from pathlib import Path
import hashlib,json,tempfile,sys,unittest,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
import bottlenecks as b
from safe_monitor import monitor
ROOT=Path(__file__).resolve().parent

class BottleneckTests(unittest.TestCase):
    def test_complete_frozen_suite_and_native_metrics(self):
        cases=json.loads((ROOT/'inputs/manifest.json').read_text())['cases'];self.assertEqual(len(cases),7)
        for case in cases:
            b.paths_for_case(case);folder=ROOT/'results/granularity'/case['id'];data=json.loads((folder/'result.json').read_text())
            self.assertEqual(set(data['levels']),{'128','192','256'})
            for detail,row in data['levels'].items():
                for name,condition in row['conditions'].items():
                    svg=folder/detail/name/'output.svg';self.assertEqual(b.inherited.digest(svg),condition['sha256'])
                    source=Image.open(folder/'source.png').convert('RGBA');ref=Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).convert('RGB')
                    pred=Image.open(folder/detail/name/'white.png').convert('RGB');mse=float(np.mean((np.asarray(ref,dtype=float)-np.asarray(pred,dtype=float))**2))
                    self.assertAlmostEqual(mse,condition['metrics']['white']['mse'],places=10)
    def test_geometry_held_across_fits_and_gradient_safety(self):
        from test_artifacts import geometry_tree
        for folder in (ROOT/'results/granularity').iterdir():
            for detail in ['128','192','256']:
                trees=[ET.parse(folder/detail/k/'output.svg').getroot() for k in 'BCD']
                self.assertEqual(geometry_tree(trees[0]),geometry_tree(trees[1]));self.assertEqual(geometry_tree(trees[1]),geometry_tree(trees[2]))
                for tree in trees:
                    for node in tree.iter():
                        self.assertNotIn(node.tag.rsplit('}',1)[-1],['image','script','foreignObject','filter'])
                        if node.tag.rsplit('}',1)[-1] in ['linearGradient','radialGradient']:self.assertLessEqual(len(node),4)
    def test_correction_pairing_and_unchanged_underlying_paths(self):
        allowed=['stroke','stroke-width','stroke-linejoin','stroke-linecap','paint-order']
        for folder in (ROOT/'results/corrections').iterdir():
            record=json.loads((folder/'result.json').read_text());self.assertEqual(record['baseline_detail'],192)
            baseline=ROOT/'results/granularity'/folder.name/'192/D/output.svg';self.assertEqual(b.inherited.digest(baseline),record['baseline_svg_sha256']);self.assertEqual(b.inherited.digest(folder/'output.svg'),record['sha256'])
            trees=[ET.parse(p).getroot() for p in [baseline,folder/'output.svg']]
            for tree in trees:
                for node in tree.iter():
                    for key in allowed:node.attrib.pop(key,None)
            self.assertEqual(ET.tostring(trees[0]),ET.tostring(trees[1]))
    def test_visibility_does_not_hide_tiny_regions_or_count_occlusion(self):
        with tempfile.TemporaryDirectory() as temporary:
            p=Path(temporary);source=p/'source.png';Image.new('RGB',(10,10),'white').save(source)
            bg='<path d="M0 0H10V10H0Z" fill="#111111"/>';cell='<path d="M3 3H4V4H3Z" fill="#eeeeee"/>'
            for name,paths,expected in [('visible',bg+cell,.01),('occluded',cell+bg,0.)]:
                svg=p/f'{name}.svg';svg.write_text(f'<svg xmlns="{b.SVG}" width="10" height="10">{paths}</svg>')
                record,_=b.visible_geometry(svg,source,p/name);self.assertEqual(record['paths_bbox_le1'],1)
                self.assertAlmostEqual(record['visible_alpha_weighted_area_tiny1_fraction'],expected,places=10)
                self.assertAlmostEqual(record['assigned_visible_alpha_fraction'],1.,places=10)
    def test_monitor_timeout_is_bounded_and_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            record=monitor([sys.executable,'-c','import time; time.sleep(5)'],Path(temporary)/'child.log',timeout=.15)
            self.assertEqual(record['termination_reason'],'timeout');self.assertLess(record['wall_seconds'],4)
            self.assertEqual(record['cleanup_unverified_pids'],[])
    def test_cycle_inventory_rejects_missing_and_modified_artifacts(self):
        import run_cycle
        old=run_cycle.ROOT
        try:
            with tempfile.TemporaryDirectory() as temporary:
                run_cycle.ROOT=Path(temporary);target=run_cycle.ROOT/'results/example';target.mkdir(parents=True)
                file=target/'output.svg';file.write_text('<svg/>');run_cycle.artifact_inventory(target)
                run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
                file.write_text('<svg>changed</svg>')
                with self.assertRaises(AssertionError):run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
                file.unlink()
                with self.assertRaises(AssertionError):run_cycle.verify_inventory(target/'FILE_INVENTORY.json')
        finally:run_cycle.ROOT=old

if __name__=='__main__':unittest.main(verbosity=2)
# END CHANGE AGD-BOTTLENECK-TESTS | 2026-10-28T03:34:28Z | EDITED | Author: root
