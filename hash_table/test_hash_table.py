from hash_table import HashTable
import pytest


def test_create_table():
    ht = HashTable(4)
    assert ht.table == [[], [], [], []]


def test_remainder_method():
    ht = HashTable(4)
    assert ht.remainder_method(30) == 2


def test_mid_square_method():
    ht = HashTable(4)
    assert ht.mid_square_method(55) == 2


def test_hash_string():
    ht = HashTable(4)
    assert ht.hash_string('abc') == 2


def test_insert_with_linear_addressing():
    ht = HashTable(4)
    ht.insert('abc')
    assert ht.table[2] == ['abc']
