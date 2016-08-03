
def depth_first_search_for_tree(tree_root, node_to_find):
    """
    method for walking through a tree or graph wher you go as
    deep as possible down a path before "fanning out"

    your set of visited nodes will shoot out from the starting point
    along one path, with more single paths progressively shotting
    off of that one as each path hits a dead end

    Advantages:
        df traversal on binary tree generally requires less memory than bfs
        df traversal can be easily implemented with recursion

    Disadvantages:
        dfs doesnt necessarily find the shortest path to a node, while
        BFS does
    """

    node_stack = list()
    node_stack.append(tree_root)

    while len(node_stack):
        node = node_stack.pop()
        if node == node_to_find:
            return node_to_find

        if node.left:
            node_stack.append(node.left)
        if node.right:
            node_stack.append(node.right)


def dfs_for_graph(graph):
    """
    """