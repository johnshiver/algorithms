

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

    def add(self, new_value):
        if self.compare(new_value, self.value):
            if not self.right:
                self.right = BinaryTree(new_value)
                self.right.parent = self
            else:
                self.right.add(new_value)
        else:
            if not self.left:
                self.left = BinaryTree(new_value)
                self.left.parent = self
            else:
                self.left.add(new_value)

    def delete(self, tree):
        if not tree.parent:
            raise ValueError("cant delete the root node!")
        # if on right side
        if tree.parent.right == tree:
            if self._is_leaf(tree):
                tree.parent.right = None
            elif self._has_one_branch(tree):
                replacement = tree.right if tree.right else tree.left
                tree.parent.right = replacement
            else:  # can assume two branches
                replacement = tree.right
                while not self._is_leaf(replacement):
                    replacement = replacement.left
                tree.parent.right.value = replacement.value
                self.delete(replacement)
            # if on left side
        else:
            if self._is_leaf(tree):
                tree.parent.left = None
            elif self._has_one_branch(tree):
                replacement = tree.left if tree.left else tree.right
                tree.parent.left = replacement
            else:  # can assume two branches
                replacement = tree.right
                while not self._is_leaf(replacement):
                    replacement = replacement.left
                tree.parent.left.value = replacement.value
                self.delete(replacement)

    def search_for_value(self, search_value):
        if search_value is None:
            raise ValueError
        if self.value == search_value:
            return self
        if self.right:
            return self.right.search_for_value(search_value)
        if self.left:
            return self.left.search_for_value(search_value)
        raise ValueError

    def max_depth(self):

        if not self.right and not self.left:
            return 0
        right = left = 0
        if self.right:
            right = 1 + self.right.max_depth()
        if self.left:
            left = 1 + self.left.max_depth()
        return max(right, left)

    @staticmethod
    def _is_leaf(tree):
        return all(branch is None for branch in (tree.left, tree.right))

    @staticmethod
    def _has_one_branch(tree):
        return not all((tree.left, tree.right))

    @staticmethod
    def _hash_two_branches(tree):
        return all((tree.left, tree.right))


