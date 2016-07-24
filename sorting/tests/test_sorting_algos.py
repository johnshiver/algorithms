import random

from sorting import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort

import unittest


class TestSorts(unittest.TestCase):

    def setUp(self):
        list_of_100 = range(100)
        self.test_list = [random.choice(list_of_100) for _ in range(100)]

    def tearDown(self):
        self.test_list = None

    def test_bubble_sort(self):
        """Tests that test list is correctly sorted."""
        self.assertEqual(sorted(self.test_list), bubble_sort(self.test_list))

    def test_selection_sort(self):
        """Tests that test list is correctly sorted."""
        self.assertEqual(sorted(self.test_list), selection_sort(self.test_list))

    def test_insertion_sort(self):
        """Tests that test list is correctly sorted."""
        self.assertEqual(sorted(self.test_list), insertion_sort(self.test_list))

    def test_shell_sort(self):
        """Tests that test list is correctly sorted."""
        self.assertEqual(sorted(self.test_list), shell_sort(self.test_list))

    def test_merge_sort(self):
        """Tests that test list is correctly sorted."""
        self.assertEqual(sorted(self.test_list), merge_sort(self.test_list))
