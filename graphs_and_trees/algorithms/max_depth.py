class MaxDepthBST(object):
    def get_depth(self, node):
        if not node:
            return 0
        left_depth = 1 + self.get_depth(node.left)
        right_depth = 1 + self.get_depth(node.right)
        return max(left_depth, right_depth)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_depth(root)
