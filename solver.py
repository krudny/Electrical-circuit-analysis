import numpy as np
from cycles import find_cycles


def solver(s, t, edges_count, n, undirected_graph, directed_graph, electromotive_force):
    equations = [[0 for _ in range(edges_count)] for _ in range(edges_count)]
    values = [0 for _ in range(edges_count)]

    def check_electromotive_force(cycle):
        if cycle[0] == s and cycle[::-1] == t or cycle[0] == t and cycle[::-1] == s:
            return True

        for i in range(len(cycle) - 1):
            if cycle[i] == s and cycle[i + 1] == t or cycle[i] == t and cycle[i + 1] == s:
                return True

        return False

    def vert_to_dict(graph):
        E = {}  # (u, v) = (edge_index, weight)

        for v in graph:
            for edge_index, u, weight in graph[v]:
                E[(v, u)] = (edge_index, weight)
                E[(u, v)] = (edge_index, weight)

        return E

    def edges_to_dict(graph):
        E = {}  # edge_index = (u, v, weight)

        for v in graph:
            for edge_index, u, weight in graph[v]:
                E[edge_index] = (v, u, weight)

        return E

    def first_kirchhoff_law():
        for v in range(n - 1):
            for edge_index, u, edge_weight in undirected_graph[v]:
                if (edge_index, u, edge_weight) in directed_graph[v]:
                    equations[v][edge_index] = -1
                else:
                    equations[v][edge_index] = 1

        return 1

    def second_kirchhoff_law():
        cycles = find_cycles(undirected_graph)
        if len(cycles) < (edges_count - n + 1):
            return 0

        eq = n - 1

        for cycle in cycles:
            for i in range(len(cycle) - 1):
                v, u = cycle[i], cycle[i + 1]
                edge_index, weight = vert_dict[(v, u)]

                if (edge_index, u, weight) in directed_graph[v]:
                    equations[eq][edge_index] = -weight
                else:
                    equations[eq][edge_index] = weight

            if check_electromotive_force(cycle):
                values[eq] = electromotive_force
            eq += 1

            if eq >= edges_count:
                return 1

    def solve():
        X = np.linalg.solve(np.array(equations), np.array(values))

        for i, value in enumerate(X):
            if value < 0 and i != 0:
                X[i] *= (-1)
                u, v, weight = edge_dict[i]

                directed_graph[u].remove((i, v, weight))
                directed_graph[v].add((i, u, weight))

        return X

    vert_dict = vert_to_dict(directed_graph)
    edge_dict = edges_to_dict(directed_graph)

    if first_kirchhoff_law() and second_kirchhoff_law():
        return solve()
    else:
        return None


