import os.path
import sys
import unittest

sys.path.append(os.path.join(os.path.abspath(os.pardir), "trees"))

from ..adjacency_list import Graph
from ..prims_algorithm import prims_algo


class TestPrimsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('a', 'b', 1)
        self.graph.add_edge('a', 'c', 4)
        self.graph.add_edge('a', 'd', 3)
        self.graph.add_edge('b', 'd', 2)
        self.graph.add_edge('c', 'd', 5)

    def tearDown(self):
        self.graph = None

    def test_prims_algroithm(self):
        start = self.graph.get_vertex('a')
        prims_algo(self.graph, start)
        total = 0
        for v in self.graph:
            total += v.distance
        self.assertEqual(total, 7)
