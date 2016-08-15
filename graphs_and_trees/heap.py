"""

"""


class Heap(object):

    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def insert(self, value):
        """
        node to be inserted is placed in the first open position of the array.
        since this likely destroys the heap condition, new node must trickle
        up until it's below a node with a larger key and above a node with
        a smaller key
        """
        if not self.heapList:
            self.heapList.append(value)
            self.currentSize += 1
            return

        self.heapList[self.currentSize] = value
        self.currentSize += 1
        self._trickle_up(self.currentSize)

    def remove(self):
        """
        remove the node with the maximum key (the root) or index 0
        of the heap array.

        once the root is gone, the tree is no longer complete,
        there is an empty cell.  To fill the hole, the steps are:

        1: remove root
        2: move last node into the root
        3: trickle last node down until it's below a larger node and above
           a smaller one
        """
        root = self.heapList[0]
        self.currentSize -= 1
        self._trickle_down()
        return root

    def _trickle_up(self, index):
        parent = self.get_parent_index(index)
        bottom = self.heapList[index]

        while index > 0 and self.heapList[parent] < self.heapList[bottom]:
            # move node down
            self.heapList[index] = self.heapList[parent]
            # move index up
            index = parent
            parent = self.get_parent_index(parent)
        self.heapList[index] = bottom

    def _trickle_down(self):
        # always start by putting element at the end as root
        # then figure out the rest
        new_root = self.heapList[-1]
        self.heapList[0] = new_root
        current = 0
        while current < self.currentSize / 2:
            left_child = self.get_left_child_index(current)
            right_child = self.get_right_child_index(current)
            max_child = max(self.heapList[left_child], self.heapList[right_child])

    @staticmethod
    def get_parent_index(x):
        return (x-1) / 2

    @staticmethod
    def get_right_child_index(x):
        return (2 * x) + 1

    @staticmethod
    def get_left_child_index(x):
        return (2 * x) + 2







