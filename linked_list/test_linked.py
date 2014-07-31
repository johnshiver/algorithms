from linked_list import *


def test_insert():
    linkedlist = linkedList()
    one = Node('Jacob')
    linkedlist.insert(one)
    assert linkedlist.head.data == 'Jacob'


def test_search():
    linkedlist = linkedList()
    one = Node('Jacob')
    two = Node('Pallymay')
    linkedlist.insert(one)
    linkedlist.insert(two)
    assert linkedlist.search(linkedlist, 'Pallymay') == two