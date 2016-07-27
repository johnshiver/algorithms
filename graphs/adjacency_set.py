"""
Very similar to adjacency list

Instead of using a list to maintain adjacent vertices, we use a set

Much faster + more efficient

"""


class Node(object):

    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.nodes = set()

    def add_edge(self, vertex_number):
        """Adds vertex node's adjacent nodes set
        :param vertex_number: int
        :return: None
        """
        self.nodes.add(vertex_number)

    def get_adjacent_vertices(self):
        """Returns sorted list of adjacent vertices.
        :return: List of ints
        """
        return_list = list(self.nodes)
        return sorted(return_list)


class AdjacencySetGraph(object):

    valid_graph_types = {
        'DIRECTED',
        'UNDIRECTED',
    }

    def __init__(self, num_vertices=0, graph_type='DIRECTED'):
        # inner list contains ints
        self.num_vertices = num_vertices
        self.graph_type = graph_type if graph_type in self.valid_graph_types else 'DIRECTED'
        self.vertex_list = []

        for i in range(self.num_vertices):
            self.vertex_list.add(Node(i))

    def add_edge(self, v1, v2):
        """Adds edge between v1 and v2
        :param v1: int
        :param v2: int
        :return: none
        """
        if v1 >= self.num_vertices or v1 < 0 or v2 >= self.num_vertices or v2 < 0:
            raise ValueError('invalid vertex number')

        self.vertex_list[v1].add_edge(v2)
        if self.graph_type == 'UNDIRECTED':
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError('invalid vertex number')

        return self.vertex_list[v].get_adjacent_vertices()