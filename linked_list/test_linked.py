from linked_list import *
import pytest


def test_insert():
    linkedlist = linkedList()
    one = Node('Jacob')
    linkedlist.insert(one)
    assert linkedlist.head == one
    assert linkedlist.head.data == 'Jacob'


def test_insert_two():
    linkedlist = linkedList()
    one = Node('Jacob')
    two = Node('Thomas')
    linkedlist.insert(one)
    linkedlist.insert(two)
    assert linkedlist.head == two
    assert linkedlist.head.nextNode == one


def test_nextNode():
    linked = linkedList()
    one = Node('Jacob')
    two = Node('Pallymay')
    three = Node('Rasmus')
    linked.insert(one)
    linked.insert(two)
    linked.insert(three)
    assert linked.head == three
    assert linked.head.nextNode == two


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
        linkedlist.search(linkedlist, 'Portugal')


def test_delete():
    linkedlist = linkedList()
    one = Node('Jacob')
    two = Node('Pallymay')
    three = Node("Fawcet")
    linkedlist.insert(one)
    linkedlist.insert(two)
    linkedlist.insert(three)
    linkedlist.delete(two)
    assert linkedlist.head.nextNode == one


def test_delete_empty():
    linkedlist = linkedList()
    one = Node('Pork')
    with pytest.raises(ValueError):
        linkedlist.delete(one)


def test_delete_when_second_no_item():
    linkedlist = linkedList()
    one = Node("Peanut")
    two = Node("Butter")
    linkedlist.insert(one)
    with pytest.raises(ValueError):
        linkedlist.delete(two)
