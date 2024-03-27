import numpy as np


def solver(s, t, edges_count, n, undirected_graph, directed_graph):
    equations = [[0 for _ in range(edges_count)] for _ in range(edges_count)]

    for row in undirected_graph:
        print(row, undirected_graph[row], directed_graph[row])

    def first_kirchhoff_law():
        for v in range(n - 1):
            for edge_index, u, edge_weight in undirected_graph[v]:
                if (edge_index, u, edge_weight) in directed_graph[v]:
                    equations[v][edge_index] = -1
                else:
                    equations[v][edge_index] = 1

        for row in equations:
            print(row)

    first_kirchhoff_law()


