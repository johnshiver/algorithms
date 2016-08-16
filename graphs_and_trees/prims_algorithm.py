from stacks_queues import PriorityDict
from .adjacency_list import Graph


def prims_algo(graph, start):
    priority_queue = PriorityDict()
    start.distance = 0
    for v in graph:
        priority_queue[v] = v.distance
    while len(priority_queue):
        current_vertex = priority_queue.pop_smallest()
        for next_vertex in current_vertex.get_neighbors():
            new_cost = current_vertex.get_edge_weight(next_vertex)
            if next_vertex in priority_queue and new_cost < next_vertex.distance:
                next_vertex.predecessor = current_vertex
                next_vertex.distance = new_cost
                priority_queue[next_vertex] = new_cost


def load_graph_from_file():
    f = open('/home/john/projects/algorithms/graphs_and_trees/test_graph.txt', 'r')
    #f = open("/home/john/projects/algorithms/graphs_and_trees/mohit_test_data.txt", "r")
    g = Graph()
    edges = []
    for line in f:
        edges.append(line.rstrip('\n'))

    for edge in edges:
        edge = edge.split(' ')
        edge = map(int, edge)
        v1, v2, weight = edge[0], edge[1], edge[2]
        g.add_edge(v1, v2, weight)
    return g


def get_min_spanning_cost(graph):
    final = 0
    for v in graph:
        final += v.distance

    return final

if __name__ == '__main__':
    graph = load_graph_from_file()
    start = graph.get_vertex(1)
    prims_algo(graph, start)
    print(get_min_spanning_cost(graph))