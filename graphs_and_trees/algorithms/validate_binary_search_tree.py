import sys


class BSTAlgos(object):
    def __init__(self):
        self.previous = -sys.maxint
        self.valid = True

    def in_order(self, node):
        if not node or not self.valid:
            return
        self.in_order(node.left)
        if node.val <= self.previous:
            self.valid = False
            return
        else:
            self.previous = node.val
        self.in_order(node.right)

    def is_valid_bst(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.in_order(root)
        return self.valid


# And now without recursion

class BSTCheckerNoRecursion(object):

    def is_valid_bst(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        previous = -sys.maxint
        stack = []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.val > previous:
                    previous = current.val
                else:
                    return False
                current = current.right
        return True
