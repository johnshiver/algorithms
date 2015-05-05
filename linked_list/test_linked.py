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


def test_nextNode():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    assert l_list.head.get_data() == "Rasmus"
    head_next = l_list.head.get_next()
    assert head_next.get_data() == "Pallymay"
    last = head_next.get_next()
    assert last.get_data() == "Jacob"


def test_positive_search():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"
    found = l_list.search("Pallymay")
    assert found.get_data() == "Pallymay"
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"


def test_searchNone():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    # make sure reg search works
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"
    with pytest.raises(ValueError):
        l_list.search("Vincent")


def test_delete():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.delete("Rasmus")
    assert l_list.head.get_data() == "Pallymay"
    l_list.delete("Jacob")
    assert l_list.head.get_next() is None


def test_delete_value_not_in_list():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    with pytest.raises(ValueError):
        l_list.delete("Sunny")


def test_delete_empty_list():
    l_list = LinkedList()
    with pytest.raises(ValueError):
        l_list.delete("Sunny")


def test_delete_next_reassignment():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Cid")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.delete("Pallymay")
    l_list.delete("Cid")
    assert l_list.head.next.get_data() == "Jacob"

