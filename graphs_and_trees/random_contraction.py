import random


class Edge(object):

    def __init__(self, node1, node2):
       self.nodes = [node1, node2]

    @property
    def ids(self):
        return [self.nodes[0]._id, self.nodes[1]._id]

    def __hash__(self):
        nodes = sorted(self.nodes, key=lambda x: x._id)
        return hash((nodes[0]._id, nodes[1]._id))

    def __eq__(self, other):
        return hash(self) == hash(other)


    def __repr__(self):
        return "{} - {}".format(self.nodes[0], self.nodes[1])



class Node(object):

    def __init__(self, id):
        self._id = id
        self.edges = []

    def __str__(self):
        return "{}".format(self._id)

    def __repr__(self):
        return "Node: {}".format(self._id)

    def add_edge(self, connecting_node):
        new_edge = Edge(self, connecting_node)
        self.edges.append(new_edge)

    def remove_edge(self, node):
        for edge in self.edges:
            if node in edge:
                self.edges.remove(edge)

class Graph(object):

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node._id] = node

    def remove_node(self, node):
        del self.nodes[node._id]

    def add_edge(self, id1, id2):
        if id1 in self.nodes:
            n1 = self.nodes[id1]
        else:
            n1 = Node(id1)
            self.nodes[id1] = n1
        if id2 in self.nodes:
            n2 = self.nodes[id2]
        else:
            n2 = Node(id2)
            self.nodes[id2] = n2

        n1.add_edge(n2)

    @property
    def edges(self):
        edges = []
        for node in set(self.nodes.values()):
            edges.extend(node.edges)
        return edges



def load_graph_from_file(test_file):
    graph = Graph()

    with open(test_file, "r") as f:
        for line in f.readlines():
            line = line.replace('\t', ' ')
            line = line.replace('\n', '')
            node, *nodes = line.split(' ')
            nodes = [n for n in nodes if n]
            for n in nodes:
                graph.add_edge(node, n)

    return graph


def random_contraction(graph):

    random_edge = random.choice(list(set(graph.edges)))

    nx, ny = random_edge.nodes

    n1 = graph.nodes[nx._id]
    n2 = graph.nodes[ny._id]

    n_string = n1._id.split("+")
    n_string.extend(n2._id.split("+"))
    super_node_id = "+".join(n_string)
    super_node = Node(super_node_id)

    new_edges = n1.edges + n2.edges
    nodes_to_update = super_node_id.split('+')
    for edge in new_edges[:]:
        if set(edge.ids) < set(nodes_to_update):
            continue
        else:
            super_node.edges.append(edge)

    for node in nodes_to_update:
        graph.nodes[node] = super_node
#    import ipdb;ipdb.set_trace()


def perform_random_contracts(graph):
    while len(set(graph.nodes.values())) > 2:
        try:
            random_contraction(graph)
        except KeyboardInterrupt:
            import ipdb;ipdb.set_trace()


def contraction_algo():
    graph = load_graph_from_file("karger_min_cut.txt")
    trials = len(graph.nodes)
    smallest_min_cut = 10000000000

    # need to perform n**2 trials
    # to guarantee min cut
    for trial in range(trials**trials):
        trial_graph = load_graph_from_file("karger_min_cut.txt")
        perform_random_contracts(trial_graph)
        small = 100000
        for node in set(trial_graph.nodes.values()):
            edge_tot = len(node.edges)
            if edge_tot < small:
                small = edge_tot
            if small < smallest_min_cut:
                smallest_min_cut = small
        print(smallest_min_cut)

    return smallest_min_cut


if __name__ == "__main__":
   print(contraction_algo())
