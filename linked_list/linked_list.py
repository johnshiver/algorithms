class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class linkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, node):

        if not self.head:
            self.head = node
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node

    def search(self, lList, value):
        if self.head.data == value:
            return self.head
        else:
            if lList.head.nextNode:
                self.search(linkedList(lList.head.nextNode), value)
            else:
                raise ValueError("Node not in Linked List")

    def delete(self, node):

