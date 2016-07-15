"""
Adjacency Matrix:

Pros:
    - works well when the graph is well connected, i.e many nodes
      are connected with many other nodes
    - overhead of v^2 space is worth it when the number of connections is large

Adjacency List / Set

Pros:
    - a sparse graph with few connections between nodes might be more efficiently
      represented using an adjacency list or set

Algorithmic Analysis of Operations
e = number of edges
v = number of vertices

# Adjacency Matrix

space:   v^2
is edge present:  O(1)
iterate over edges on a vertex:  O(v)

# Adjacency List

space:   e + v
is edge present:  degree of v (number of edges v connects to)
iterate over edges on a vertex:  degree of v


# Adjacency Set

space: e + v
is edge present:  log(degree of v)
iterate over edges on a vertex:  degree of v

"""