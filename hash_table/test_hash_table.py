from hash_table import HashTable
import pytest


def test_remainder_method():
    ht = HashTable()
    ht.table.extend([1, 2, 3, 4])
    assert ht.remainder_method(30) == 2
