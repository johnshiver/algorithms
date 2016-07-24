import random

from sorting.insertion_sort import insertion_sort

import unittest


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        list_of_100 = range(100)
        self.test_list = [random.choice(list_of_100) for _ in range(100)]

    def tearDown(self):
        self.test_list = None

    def test_sorting_list(self):
        """Tests that test list is correctly sorted."""
        self.assertEqual(sorted(self.test_list), insertion_sort(self.test_list))
