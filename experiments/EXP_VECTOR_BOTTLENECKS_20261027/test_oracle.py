# START CHANGE AGD-BOTTLENECK-ORACLE-TEST | 2026-10-27T15:30:59Z | CREATED | Author: /root/appearance_fit
import tempfile
import json
import hashlib
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
from oracle import SVG, flat_initialization


class OracleTests(unittest.TestCase):
    def test_saved_oracle_artifact_geometry_and_gradient_limits(self):
        results = Path(__file__).parent / "results/oracle"
        if not results.exists():
            self.skipTest("Oracle outputs not generated")
        for folder in results.iterdir():
            if not folder.is_dir():
                continue
            signatures = []
            for name in ("oracle_truth", "oracle_init", "oracle_C", "oracle_D"):
                root = ET.parse(folder / f"{name}.svg").getroot()
                signatures.append([dict((k,v) for k,v in path.attrib.items() if k != "fill") for path in root.iter(f"{{{SVG}}}path")])
                self.assertFalse(list(root.iter(f"{{{SVG}}}image")))
            self.assertTrue(all(signature == signatures[0] for signature in signatures))
            root = ET.parse(folder / "oracle_D.svg").getroot()
            for kind in ("linearGradient", "radialGradient"):
                for gradient in root.iter(f"{{{SVG}}}{kind}"):
                    self.assertLessEqual(len(list(gradient)), 4)

    def test_saved_native_mse_matches_actual_render(self):
        results = Path(__file__).parent / "results/oracle"
        if not results.exists():
            self.skipTest("Oracle outputs not generated")
        for folder in results.iterdir():
            if not folder.is_dir():
                continue
            record = json.loads((folder / "result.json").read_text())
            if "oracle_truth" in record["conditions"]:
                self.assertEqual(record["conditions"]["oracle_truth"]["metrics"]["white"]["mse"], 0)
                self.assertTrue(record["ground_truth_reuse"]["fresh_native_svg_check_performed"])
                self.assertTrue(record["representability"]["all_regions_refitted_from_samples"])
            source = np.asarray(Image.open(folder / "source.png").convert("RGB"), dtype=float)
            for condition in ("oracle_init", "oracle_C", "oracle_D"):
                render = np.asarray(Image.open(folder / condition / "white.png").convert("RGB"), dtype=float)
                self.assertEqual(float(np.mean((source - render) ** 2)), record["conditions"][condition]["metrics"]["white"]["mse"])
            self.assertEqual(hashlib.sha256((folder / "oracle_truth.svg").read_bytes()).hexdigest(), record["ground_truth_reuse"]["svg_sha256"])

    def test_init_preserves_every_geometry_attribute_and_solid_paint(self):
        source = f'<svg xmlns="{SVG}" width="20" height="20"><defs><linearGradient id="g"><stop offset="0" stop-color="#000"/></linearGradient></defs><path d="M0 0H20V20H0Z" fill="#abcdef"/><path transform="translate(1 2)" fill-rule="evenodd" d="M1 1L5 1L5 5Z" fill="url(#g)"/></svg>'
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/"a.svg", Path(directory)/"b.svg"
            a.write_text(source)
            self.assertEqual(flat_initialization(a, b), [1])
            original, changed = ET.parse(a).getroot(), ET.parse(b).getroot()
            old_paths, new_paths = list(original.iter(f"{{{SVG}}}path")), list(changed.iter(f"{{{SVG}}}path"))
            self.assertEqual(len(old_paths), len(new_paths))
            for old, new in zip(old_paths, new_paths):
                self.assertEqual({k:v for k,v in old.attrib.items() if k != "fill"}, {k:v for k,v in new.attrib.items() if k != "fill"})
            self.assertEqual(new_paths[0].get("fill"), "#abcdef")
            self.assertEqual(new_paths[1].get("fill"), "#777777")
            self.assertEqual(len(list(changed.iter(f"{{{SVG}}}linearGradient"))), 0)


if __name__ == "__main__":
    unittest.main()
# END CHANGE AGD-BOTTLENECK-ORACLE-TEST | 2026-10-27T15:30:59Z | CREATED
