#! /usr/bin/env python
import sys

class Graph():
    '''Adjacency list representation of undirected graph.'''
    adj_list = []

    def __init__(self, V):
        for v in range(V):
            self.adj_list.append([])

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def adj(self, v):
        return self.adj_list[v]

def main():
    # Build Graph by reading edge list from stdin.
    num_vertices = 10
    g = Graph(10)
    for edge in sys.stdin:
        v = int(edge.split()[0])
        w = int(edge.split()[1])
        g.add_edge(v, w)

    # Print each vectex's adjacent vertices to standard out.
    for vertex in range(num_vertices):
        adj_str = ' '.join([str(v) for v in g.adj(vertex)])
        print('%s: %s' % (vertex, adj_str))

if __name__ == '__main__':
    main()
