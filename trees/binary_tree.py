

class BinaryTree(object):

    def __init__(self, value):
        self.value = value

        # if a tree lacks a parent, it must be the root
        self.parent = None
        self.right = None
        self.left = None

    def add_tree(self, new_tree):
        if new_tree.value > self.value:
            self.right = new_tree
        else:
            self.left = new_tree