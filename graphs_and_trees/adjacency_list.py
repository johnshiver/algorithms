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

import sys


class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.neighbors = {}
        self.distance = 1000000
        self.predecessor = None

    def __repr__(self):
        return 'Vertex ' + str(self.id) + ': connected to: ' + str([x.id for x
                                                        in self.neighbors])

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_edge_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph(object):

    graph_types = {
        'directed',
        'undirected'
    }

    def __init__(self, graph_type='undirected'):
        if graph_type not in self.graph_types:
            raise ValueError("graph_type must be one of {}".format(self.graph_types))

        self.vertices = {}
        self.type_ = graph_type
        self.num_vertices = 0
        self.num_edges = 0

    def __repr__(self):
        return "Graph with {} vertices".format(self.num_vertices)

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, key):
        return key in self.vertices

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def add_edge(self, v1, v2, cost=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_neighbor(self.vertices[v2], cost)
        if self.type_ == 'undirected':
            self.vertices[v2].add_neighbor(self.vertices[v1], cost)
        self.num_edges += 1

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            raise "{} not in graph!".format(key)

    def get_vertices(self):
        return self.vertices.keys()
