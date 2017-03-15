"""
Given directed graph

Edge weights must ALL be non-negative
(see bellman-ford for that solution)

"""

from graphs_and_trees.adjacency_list import Graph
from stacks_queues import PriorityDict


def dijkstra(graph, start):
    pq = PriorityDict()
    start.distance = 0
    for node in graph.vertices.values():
        pq[node] = node.distance

    while pq:
        current_node = pq.pop_smallest()
        for next_node in current_node.get_neighbors():
            new_dist = current_node.distance + \
                       current_node.get_edge_weight(next_node)
            if new_dist < next_node.distance:
                next_node.distance = new_dist
                next_node.predecessor = current_node
                pq[next_node] = new_dist

def load_graph_from_file(graph_file):
    new_graph = Graph()
    with open(graph_file, 'rb') as f:
        for line in f.readlines():
            line = " ".join(line.split())
            line = line.split()
            current_node, nodes = line[0], line[1:]
            new_graph.add_vertex(int(current_node))
            for node in nodes:
                n, weight = node.split(",")
                new_graph.add_edge(int(current_node), int(n), int(weight))
    return new_graph


if __name__ == "__main__":
    graph = load_graph_from_file("test_dijkstra.txt")
    start_v = graph.get_vertex(1)
    dijkstra(graph, start_v)
    node_checks = [7,37,59,82,99,115,133,165,188,197]
    for node in node_checks:
        print(graph.get_vertex(node).distance)


