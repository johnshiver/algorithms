import sys
import os.path

sys.path.append(os.path.join(os.path.abspath(os.pardir), "linked_list"))

from linked_list.linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list = None

    def test_insert(self):
        self.list.insert("David")

        self.assertTrue(self.list.head.get_data() == "David")
        self.assertTrue(self.list.head.get_next() is None)

    def test_insert_two(self):
        self.list.insert("David")
        self.list.insert("Thomas")

        self.assertTrue(self.list.head.get_data() == "Thomas")

        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "David")

    def test_nextNode(self):
        self.list.insert("Jacob")
        self.list.insert("Pallymay")
        self.list.insert("Rasmus")

        self.assertTrue(self.list.head.get_data() == "Rasmus")

        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "Pallymay")

        last = head_next.get_next()
        self.assertTrue(last.get_data() == "Jacob")

    def test_positive_search(self):
        self.list.insert("Jacob")
        self.list.insert("Pallymay")
        self.list.insert("Rasmus")

        found = self.list.search("Jacob")
        self.assertTrue(found.get_data() == "Jacob")

        found = self.list.search("Pallymay")
        self.assertTrue(found.get_data() == "Pallymay")

        found = self.list.search("Jacob")
        self.assertTrue(found.get_data() == "Jacob")

    def test_searchNone(self):
        self.list.insert("Jacob")
        self.list.insert("Pallymay")

        # make sure reg search works
        found = self.list.search("Jacob")

        self.assertTrue(found.get_data() == "Jacob")

        with self.assertRaises(ValueError):
            self.list.search("Vincent")

    def test_delete(self):
        self.list.insert("Jacob")
        self.list.insert("Pallymay")
        self.list.insert("Rasmus")

        # Delete the list head
        self.list.delete("Rasmus")
        self.assertTrue(self.list.head.get_data() == "Pallymay")

        # Delete the list tail
        self.list.delete("Jacob")
        self.assertTrue(self.list.head.get_next() is None)

    def test_delete_value_not_in_list(self):
        self.list.insert("Jacob")
        self.list.insert("Pallymay")
        self.list.insert("Rasmus")

        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def test_delete_empty_list(self):
        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def test_delete_next_reassignment(self):
        self.list.insert("Jacob")
        self.list.insert("Cid")
        self.list.insert("Pallymay")
        self.list.insert("Rasmus")

        self.list.delete("Pallymay")
        self.list.delete("Cid")

        self.assertTrue(self.list.head.next_node.get_data() == "Jacob")
