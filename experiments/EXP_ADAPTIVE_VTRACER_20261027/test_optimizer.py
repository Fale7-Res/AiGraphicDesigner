"""Regression checks for configuration applicability and evidence protection."""
# START CHANGE ADAPTIVE-TESTS | 2026-10-27T03:08:56Z | CREATED | Author: restore_execute
import tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from PIL import Image
import vtracer
from optimizer import canonical,pilots,neighborhood,optimize,OWNER

class OptimizerTests(unittest.TestCase):
    def test_surface(self):
        self.assertEqual({c['clustering'] for c in pilots()},{'color-cluster','watershed','bw'})
        self.assertEqual(pilots()[0],OWNER)
        for c in pilots():
            vtracer.Config(**c)
            for n in neighborhood(c):vtracer.Config(**n)
    def test_effective_settings(self):
        c=OWNER|{'mode':'pixel'}
        self.assertEqual(canonical(c),canonical(c|{'simplify':.25}))
        c=OWNER|{'clustering':'bw','hierarchical':'cutout'}
        self.assertIn('layer_difference',canonical(c))
        self.assertNotIn('color_precision',canonical(c))
    def test_input_and_history(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);Image.new('RGBA',(16,16),(255,0,0,100)).save(p/'a.png')
            with self.assertRaises(ValueError):optimize(p/'a.png',p/'out')
            (p/'out').mkdir();(p/'out/sentinel').write_text('preserve')
            with self.assertRaises(FileExistsError):optimize(p/'a.png',p/'out')
            self.assertEqual((p/'out/sentinel').read_text(),'preserve')
    def test_budget_and_failure_record(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);Image.new('RGB',(16,16),'white').save(p/'a.png')
            def failed(*args):return {'status':'failed','error':'test failure','config':args[2]}
            with patch('optimizer.run_trial',side_effect=failed):r=optimize(p/'a.png',p/'out',13,60)
            self.assertEqual(len(r['failed']),13);self.assertEqual(r['ranked'],[])
            self.assertTrue((p/'out/ranking.json').is_file())

if __name__=='__main__':unittest.main()
# END CHANGE ADAPTIVE-TESTS | 2026-10-27T03:08:56Z | CREATED | Author: restore_execute
