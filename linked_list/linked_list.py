class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class linkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, node):

        if not self.head:
            self.head = node
            self.size += 1
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node
            self.size +=1

    def search(self, lList, value):
        if self.head.data == value:
            return self.head
        else:
            if lList.head.nextNode:
                self.search(linkedList(lList.head.nextNode), value)
            else:
                raise ValueError("Node not in Linked List")

    def size(self):
        return self.size

    def delete(self, node):
        if self.size < 1:
            raise ValueError("No items in List")
        if self.head == node:
            self.head = self.head.nextNode
            self.size -= 1
        if self.size > 1:
            found = False
            previous = self.head
            current = self.head.nextNode
            while not found:
                if current == node:
                    previous.nextNode = current.nextNode
                    self.size -= 1
                    found = True
                elif current.nextNode:
                    previous = current
                    current = current.nextNode
                else:
                    raise ValueError("Node not in List")
        else:
            raise ValueError("Node not in List")



