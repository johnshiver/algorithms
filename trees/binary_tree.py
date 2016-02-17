

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

    def delete(self, delete_value):
        # TODO: this is under construction
        if delete_value is None:
            raise ValueError("Cannot delete None!")
        try:
            deleted_node = self.search_for_value(delete_value)
        except ValueError:
            "Couldnt delete node, it wasnt there!"
        else:
            if not deleted_node.parent:
                raise ValueError("cant delete the root node!")
            if deleted_node.parent.right == deleted_node:
                if not deleted_node.right and not deleted_node.left:
                    deleted_node.parent == None
                    deleted_node.parent.right == None

                else:
                    deleted_node.parent.right = max(filter(None, deleted_node.left, deleted_node.right))
            else:
                if not deleted_node.right and not deleted_node.left:
                    deleted_node.parent == None
                    deleted_node.parent.left == None
                else:
                    deleted_node.parent.right = max(filter(None, deleted_node.left, deleted_node.right))

        return deleted_node

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

