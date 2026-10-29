# START CHANGE AGD-THIN-TEST-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root
"""Checks scientific measurement safeguards, not reconstruction acceptance."""
import unittest
import numpy as np
from evaluate_study import separation_errors

class MeasurementSafeguards(unittest.TestCase):
    def test_false_join_of_two_disjoint_structures(self):
        truth=np.zeros((8,12),bool);truth[2:6,1:4]=True;truth[2:6,8:11]=True
        pred=truth.copy();pred[3,4:8]=True
        self.assertEqual(separation_errors(truth,pred)['false_join_excess'],1)

    def test_false_split_of_one_structure(self):
        truth=np.zeros((8,12),bool);truth[2:6,1:11]=True
        pred=truth.copy();pred[:,5]=False
        self.assertEqual(separation_errors(truth,pred)['false_split_excess'],1)

    def test_empty_reference_never_passes(self):
        result=separation_errors(np.zeros((8,8),bool),np.ones((8,8),bool))
        self.assertEqual(result['status'],'EMPTY_REFERENCE_NOT_EVALUABLE')

if __name__=='__main__':unittest.main()

# END CHANGE AGD-THIN-TEST-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root
