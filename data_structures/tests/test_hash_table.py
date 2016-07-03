import sys
import os.path

sys.path.append(os.path.join(os.path.abspath(os.pardir), "hash_table"))

from hash_table.hash_table import HashTable
import unittest

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(4)

    def tearDown(self):
        self.hash_table = None

    def test_create_table(self):
        self.assertTrue(self.hash_table.table == [[], [], [], []])

    def test_remainder_method(self):
        self.assertTrue(self.hash_table.remainder_method(30) == 2)

    def test_mid_square_method(self):
        self.assertTrue(self.hash_table.mid_square_method(55) == 2)

    def test_hash_string(self):
        self.assertTrue(self.hash_table.hash_string('abc') == 2)

    def test_insert_with_linear_addressing(self):
        self.hash_table .insert('abc')
        self.assertTrue(self.hash_table.table[2] == ['abc'])
