"""
The row labels and column labels represent vertices

Each cell represents the relationship between the vertices i.e. edges

Representing a directed graph with an adjacency matrix:

   A B
 - - - -
A| 0 1
B| 0 0

Indicates an edge from A -> B

Representing an undirected graph with an adjacency matrix:

   A B
 - - - -
A| 0 1
B| 1 0

Indicates an edge from A <-> B

"""


class AdjacencyMatrixGraph(object):

    valid_graph_types = {
        'DIRECTED',
        'UNDIRECTED',
    }

    def __init__(self, num_vertices=0, graph_type='DIRECTED'):
        # inner list contains ints
        self.adjacency_matrix = [[]]
        self.num_vertices = num_vertices
        self.graph_type = graph_type if graph_type in self.valid_graph_types else 'DIRECTED'

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                self.adjacency_matrix[i][j] = 0

    def add_edge(self, v1, v2):
        """Adds edge between v1 and v2 to adj matrix.
        :param v1: int
        :param v2: int
        :return: none
        """
        if v1 >= self.num_vertices or v1 < 0 or v2 >= self.num_vertices or v2 < 0:
            raise ValueError('invalid vertex number')

        self.adjacency_matrix[v1][v2] = 1
        if self.graph_type == 'UNDIRECTED':
            self.adjacency_matrix[v2][v1] = 1

    def get_adjacent_vertices(self, v):
        """Given v, return list of adjacent vertices.
        :param v: int
        :return: list of ints
        """
        if v >= self.num_vertices or v < 0:
            raise ValueError('invalid vertex number')

        adjacent_vertices_list = []
        for i in range(self.num_vertices):
            if self.adjacency_matrix[v][i]:
                adjacent_vertices_list.add(i)

        # always return vertices in ascending order for consistency
        return sorted(adjacent_vertices_list)
