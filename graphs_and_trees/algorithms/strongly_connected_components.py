import sys
import time
import heapq
import resource
from itertools import groupby
from collections import defaultdict

#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

class Tracker(object):

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.visited = set()


def dfs(graph_dict, node, tracker):
    tracker.visited.add(node)
    tracker.leader[node] = tracker.current_source
    for n in graph_dict[node]:
        if n not in tracker.visited:
            dfs(graph_dict, n, tracker)
    # once recursion exits, start tracking finish times
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time


def dfs_loop(graph_dict, nodes, tracker):
    for node in nodes:
        if node not in tracker.visited:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)


def graph_reverse(graph):
    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph

def get_all_nodes(graph):
    # get all nodes
    nodes = set()
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)
    return nodes

def scc(graph):
    out = defaultdict(list)
    t1, t2 = Tracker(), Tracker()
    reversed_graph = graph_reverse(graph)
    nodes = get_all_nodes(graph)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reversed_graph, nodes, t1)
    sorted_nodes = sorted(t1.finish_time, key=t1.finish_time.get, reverse=True)
    dfs_loop(graph, sorted_nodes, t2)
    # da fuck does this do
    for lead, vertex in groupby(sorted(t2.leader, key=t2.leader.get),
                                key=t2.leader.get):
        out[lead] = list(vertex)

    return out


def main():
    start = time.time()
    graph = defaultdict(list)
    with open("scc.txt") as f:
        for line in f:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            graph[x1].append(x2)
    total = time.time() - start
    print(total)

    groups = scc(graph)

    t2 = time.time() - start
    top_5 = heapq.nlargest(5, groups, key=lambda x: len(groups[x]))
    result = []
    for i in range(5):
        try:
            result.append(len(groups[top_5[i]]))
        except:
            result.append(0)
    print result


if __name__ == "__main__":
    main()


