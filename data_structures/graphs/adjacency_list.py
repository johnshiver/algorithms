"""
Every vertex is a node

Each vertex has a reference to a list

The list contains all other nodes this vertex connects to directly

If a vertex V has an edge leading to another vertex U,
then U is present in V's list

Cons:
    - the order of vertices in adjacency list matter
    - the same graph can have multiple representations
    - certain operations become tricky e.g. deleting a node
      involves looking through all adjacency lists to remove the node from all lists
"""


class Node(object):

    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        # list of adjacent nodes
        nodes = []


class AdjacencyListGraph(object):

    def __init__(self):
        # list of nodes
        vertices = []