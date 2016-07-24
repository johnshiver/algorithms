import random

from sorting.selection_sort import selection_sort

import unittest


class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        list_of_100 = range(100)
        self.test_list = [random.choice(list_of_100) for _ in range(100)]

    def tearDown(self):
        self.test_list = None

    def test_sorting_list(self):
        """Tests that test list is correctly sorted."""

        self.assertEqual(sorted(self.test_list), selection_sort(self.test_list))
