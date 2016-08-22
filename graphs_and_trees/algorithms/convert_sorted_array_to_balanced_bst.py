# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ConvertArrayToBST(object):

    def sorted_array_to_bst(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.create_bst(nums, 0, len(nums) - 1)

    def create_bst(self, array, start, end):
        if start > end:
            return

        mid = (start + end) / 2
        node = TreeNode(array[mid])
        node.left = self.create_bst(array, start, mid - 1)
        node.right = self.create_bst(array, mid + 1, end)
        return node