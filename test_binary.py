import pytest
from binary_search import bSearch


def test_list_containg_e():
    list1 = [i for i in xrange(100)]
    found = bSearch(list1, 10)
    assert found is True


def test_list_without_e():
    list1 = [i for i in xrange(50, 100)]
    found = bSearch(list1, 10)
    assert found is False

