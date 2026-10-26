# START CHANGE VTRACER-REFINE-TEST | 2026-10-24T23:41:56Z | CREATED | Author: vtracer_engine
"""Visible-ownership refit must preserve geometry and reject unsupported scenes."""
import tempfile,unittest,xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image
from refine import refine,inspect_pixel_document,NS

class RefitTests(unittest.TestCase):
    def test_visible_support_refit_exact_on_overlapping_flat_regions(self):
        with tempfile.TemporaryDirectory() as directory:
            d=Path(directory);a=np.zeros((16,16,3),np.uint8);a[:]=[200,40,20];a[4:12,4:12]=[20,180,40];Image.fromarray(a).save(d/'source.png')
            svg=f'<svg xmlns="{NS}" width="16" height="16"><path d="M0 0 L16 0 L16 16 L0 16 Z" fill="#808080"/><path d="M4 4 L12 4 L12 12 L4 12 Z" fill="#000000"/></svg>'
            (d/'source.svg').write_text(svg);r=refine(d/'source.png',d/'source.svg',{'mode':'pixel'},d/'out')
            self.assertTrue(r['conditions']['visible_color_refit']['metrics']['identical'])
            self.assertEqual(r['ownership_audit']['ambiguous_pixels'],0)
            original=ET.fromstring(svg);refitted=ET.parse(d/'out/visible_color_refit.svg').getroot()
            self.assertEqual([p.get('d') for p in original],[p.get('d') for p in refitted])
    def test_refuses_spline_and_opacity(self):
        root=ET.fromstring(f'<svg xmlns="{NS}"><path d="M0 0L1 0L1 1Z" fill="#123456" opacity=".5"/></svg>')
        with self.assertRaises(ValueError):inspect_pixel_document(root,{'mode':'spline'})
        with self.assertRaises(ValueError):inspect_pixel_document(root,{'mode':'pixel'})

if __name__=='__main__':unittest.main()

# END CHANGE VTRACER-REFINE-TEST | 2026-10-24T23:41:56Z | CREATED | Author: vtracer_engine
