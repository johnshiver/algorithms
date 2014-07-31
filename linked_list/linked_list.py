class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class linkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node

    def search(self, value):
        pass

    def delete(self, value):
        pass