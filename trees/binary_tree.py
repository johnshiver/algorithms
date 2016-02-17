

class BinaryTree(object):

    def __init__(self, value, compare=None):
        """
        Simple implementation of BinaryTree

        Args:
             value (any type you want, but be consistent)
        Kwargs:
             compare (function to compare two values)
        """

        self.value = value

        # if a tree lacks a parent, it must be the root
        self.parent = None
        self.right = None
        self.left = None

        # can easily change criteria
        if not compare:
            self.compare = lambda x, y: x > y
        else:
            self.compare = compare

    def add_tree(self, new_value):
        if self.compare(new_value, self.value):
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

    def search_for_value(self, search_value):
        if search_value is None:
            raise ValueError("Cannot search for None!")
        if self.value == search_value:
            return self
        if self.right:
            return self.right.search_for_value(search_value)
        if self.left:
            return self.left.search_for_value(search_value)
        raise ValueError("{} not in my tree", search_value)