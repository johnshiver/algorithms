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


class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x
                                                       in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]


class Graph(object):

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            raise "{} not in graph!".format(key)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, f, t, cost=0):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], cost)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())



