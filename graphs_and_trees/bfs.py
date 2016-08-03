import Queue


def breadth_first_search_for_tree(tree_root, node_to_find):

    node_queue = Queue.Queue()
    node_queue.put(tree_root)
    while not node_queue.empty():
        current = node_queue.get()
        if current != node_to_find:
            if current.left:
                node_queue.put(current.left)
            if current.right:
                node_queue.put(current.right)
        else:
            return node_to_find
