import unittest
from group import groups_of_3

class TestCases(unittest.TestCase):
    pass

    def test_groups_of_3(self):
        self.assertEqual(groups_of_3([1,2,3,4,5,6]), [[1,2,3], [4,5,6]])

    def test_groups_of_3_incomplete(self):
        self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8]), [[1,2,3],[4,5,6], [7,8]])
