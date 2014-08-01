from linked_list import *
import pytest


def test_insert():
    linkedlist = linkedList()
    one = Node('Jacob')
    linkedlist.insert(one)
    assert linkedlist.head.data == 'Jacob'


def test_search():
    linkedlist = linkedList()
    one = Node('Jacob')
    two = Node('Pallymay')
    three = Node('Rasmus')
    linkedlist.insert(one)
    linkedlist.insert(two)
    linkedlist.insert(three)
    assert linkedlist.search(linkedlist, 'Rasmus') == three


def test_searchNone():
    linkedlist = linkedList()
    one = Node('Jacob')
    two = Node('Pallymay')
    linkedlist.insert(one)
    linkedlist.insert(two)
    with pytest.raises(ValueError):
        linkedlist.search(linkedlist, 'Peter')
