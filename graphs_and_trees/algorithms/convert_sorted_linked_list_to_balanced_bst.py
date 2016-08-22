# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SortedLinkedListToBalancedTree(object):

    # top-down approach, O(n*logn)
    def sortedListToBST2(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        # use two pointers, one slow and one fast
        # to find the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        # cut the next pointer off, so the left will
        # only check the left half of the current list
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root

    # bottom-up approach, O(n)
    def sortedListToBST(self, head):
        list_size, p = 0, head
        while p:
            list_size += 1
            p = p.next
        self.node = head
        return self.convert(0, list_size - 1)

    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        l = self.convert(start, mid - 1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next
        root.right = self.convert(mid + 1, end)
        return root