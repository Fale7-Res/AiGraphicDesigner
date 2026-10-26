# START CHANGE VTRACER-ICC | 2026-10-24T23:42:53Z | CREATED | Author: parent
"""Smoke test for declared sRGB input normalization, not arbitrary ICC conformance."""
import unittest,tempfile
from pathlib import Path
import numpy as np
from PIL import Image,ImageCms
from search import prepare_input
class ICCSmoke(unittest.TestCase):
    def test_declared_srgb_matches_untagged_assumption(self):
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);rng=np.random.default_rng(91);a=rng.integers(0,256,(32,32,3),dtype=np.uint8)
            p=folder/'tagged.png';q=folder/'normalized.png'
            profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
            Image.fromarray(a).save(p,icc_profile=profile);info=prepare_input(p,q)
            self.assertTrue(info['icc_present']);np.testing.assert_array_equal(a,np.array(Image.open(q)))
if __name__=='__main__':unittest.main()

# END CHANGE VTRACER-ICC | 2026-10-24T23:42:53Z | CREATED | Author: parent
