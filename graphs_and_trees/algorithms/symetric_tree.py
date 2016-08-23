# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_stack, right_stack = list(), list()
        left, right = root, root
        while (left_stack and right_stack) or (right and left):
            if left and right:
                left_stack.append(left)
                right_stack.append(right)
                left = left.left
                right = right.right
            elif (left_stack and right_stack) and (not left and not right):
                left = left_stack.pop()
                right = right_stack.pop()
                if left.val != right.val:
                    return False
                right = right.left
                left = left.right
            else:
                return False
        return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isSymmetric(p, q):
            if p and q:
                return p.val == q.val and _isSymmetric(p.left, q.right) and _isSymmetric(p.right, q.left)
            else:
                return p == q
        return _isSymmetric(root, root)
