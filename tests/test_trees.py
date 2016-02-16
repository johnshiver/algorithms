import sys
import os.path
import unittest


sys.path.append(os.path.join(os.path.abspath(os.pardir), "trees"))
from trees.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(0)

    def tearDown(self):
        self.root = None

    def test_init_root(self):
        self.assertEqual(None, self.root.parent)

    def test_add_right(self):
        self.root.value = 5
        bigger_tree = BinaryTree(10)
        self.root.add_tree(bigger_tree)
        self.assertEqual(bigger_tree, self.root.right)

    def test_add_left(self):
        self.root.value = 5
        smaller_tree = BinaryTree(1)
        self.root.add_tree(smaller_tree)
        self.assertEqual(smaller_tree, self.root.left)

    def test_add_right_parent(self):
        self.root.value = 5
        bigger_tree = BinaryTree(10)
        self.root.add_tree(bigger_tree)
        self.assertEqual(self.root, bigger_tree.parent)

    def test_add_left_parent(self):
        self.root.value = 5
        smaller_tree = BinaryTree(1)
        self.root.add_tree(smaller_tree)
        self.assertEqual(self.root, smaller_tree.parent)

    def test_add_two_right(self):
        self.root.value = 5
        bigger_tree = BinaryTree(10)
        even_bigger_tree = BinaryTree(15)
        self.root.add_tree(bigger_tree)
        self.root.add_tree(even_bigger_tree)
        self.assertEqual(even_bigger_tree, self.root.right.right)

    def test_add_two_left(self):
        self.root.value = 5
        smaller_tree = BinaryTree(3)
        even_smaller_tree = BinaryTree(1)
        self.root.add_tree(smaller_tree)
        self.root.add_tree(even_smaller_tree)
        self.assertEqual(even_smaller_tree, self.root.left.left)

    def test_add_two_right_one_nested_left(self):
        self.root.value = 5
        bigger_tree = BinaryTree(10)
        even_bigger_tree = BinaryTree(15)
        self.root.add_tree(bigger_tree)
        self.root.add_tree(even_bigger_tree)
        middle_tree = BinaryTree(13)
        self.root.add_tree(middle_tree)
        self.assertEqual(middle_tree, self.root.right.right.left)

    def test_add_two_left_one_nested_right(self):
        self.root.value = 15
        smaller_tree = BinaryTree(10)
        even_smaller_tree = BinaryTree(3)
        self.root.add_tree(smaller_tree)
        self.root.add_tree(even_smaller_tree)
        middle_tree = BinaryTree(7)
        self.root.add_tree(middle_tree)
        self.assertEqual(middle_tree, self.root.left.left.right)
