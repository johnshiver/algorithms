

class BinaryTree(object):

    def __init__(self, value):
        self.value = value

        # if a tree lacks a parent, it must be the root
        self.parent = None
        self.right = None
        self.left = None

    def add_tree(self, new_value):
        if new_value > self.value:
            if not self.right:
                self.right = BinaryTree(new_value)
                self.right.parent = self
            else:
                self.right.add_tree(new_value)
        else:
            if not self.left:
                self.left = BinaryTree(new_value)
                self.left.parent = self
            else:
                self.left.add_tree(new_value)
