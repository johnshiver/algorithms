class BSTMinDepth(object):
    def get_min_depth(self, node):
        if not node:
            return 0

        if not node.left:
            return 1 + self.get_min_depth(node.right)

        if not node.right:
            return 1 + self.get_min_depth(node.left)

        return min(self.get_min_depth(node.left),
                   self.get_min_depth(node.right)) + 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_min_depth(root)
