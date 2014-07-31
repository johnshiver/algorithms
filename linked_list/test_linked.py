from linked_list import *


def test_insert():
    linkedlist = linkedList()
    one = Node('Jacob')
    linkedlist.insert(one)
    assert linkedlist.head.data == 'Jacob'

