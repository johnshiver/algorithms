from hash_table import HashTable
import pytest


def test_remainder_method():
    ht = HashTable()
    ht.table.extend([1, 2, 3, 4])
    assert ht.remainder_method(30) == 2


def test_mid_square_method():
    ht = HashTable()
    ht.table.extend([1, 2, 3, 4])
    ht.remainder_method(55) == 2


def test_hash_string():
    ht = HashTable()
    ht.table.extend([1, 2, 3, 4])
    ht.hash_string('abc') == 1
    