import sys
import os.path

sys.path.append(os.path.join(os.path.abspath(os.pardir), "binary_search"))

from binary_search.binary_search import bSearch
import unittest


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.list = [i for i in range(100)]

    def tearDown(self):
        self.list = None

    def test_list_containg_e(self):
        found = bSearch(self.list, 10)
        self.assertTrue(found)

    def test_list_without_e(self):
        found = bSearch(self.list, 101)
        self.assertFalse(found)
