from linked_list import Node, LinkedList
import pytest


def test_insert():
    l_list = LinkedList()
    l_list.insert("David")
    assert l_list.head.get_data() == "David"
    assert l_list.head.get_next() is None


def test_insert_two():
    l_list = LinkedList()
    l_list.insert("David")
    l_list.insert("Thomas")
    assert l_list.head.get_data() == "Thomas"
    head_next = l_list.head.get_next()
    assert head_next.get_data() == "David"


# def test_nextNode():
#     l_list = LinkedList()
#     one = Node('Jacob')
#     two = Node('Pallymay')
#     three = Node('Rasmus')
#     l_list.insert(one)
#     l_list.insert(two)
#     l_list.insert(three)
#     assert l_list.head == three
#     assert l_list.head.nextNode == two


# def test_search():
#     l_list = LinkedList()
#     one = Node('Jacob')
#     two = Node('Pallymay')
#     three = Node('Rasmus')
#     l_list.insert(one)
#     l_list.insert(two)
#     l_list.insert(three)


# def test_searchNone():
#     l_list = LinkedList()
#     one = Node('Jacob')
#     two = Node('Pallymay')
#     l_list.insert(one)
#     l_list.insert(two)
#     with pytest.raises(ValueError):
#         l_list.search(l_list, 'Portugal')


# def test_delete():
#     l_list = LinkedList()
#     one = Node('Jacob')
#     two = Node('Pallymay')
#     three = Node("Fawcet")
#     l_list.insert(one)
#     l_list.insert(two)
#     l_list.insert(three)
#     l_list.delete(two)
#     assert l_list.head.nextNode == one


# def test_delete_empty():
#     l_list = LinkedList()
#     one = Node('Pork')
#     with pytest.raises(ValueError):
#         l_list.delete(one)


# def test_delete_when_second_no_item():
#     l_list = LinkedList()
#     one = Node("Peanut")
#     two = Node("Butter")
#     l_list.insert(one)
#     with pytest.raises(ValueError):
#         l_list.delete(two)
