from random import randint
from show_graph import show_graph


def gen_graph(s, t, n, max_weight):
    graph = {v: set() for v in range(n)}
    edges_added = {}
    edge_index = 0

    def add_edge(u, v, edge_weight):
        nonlocal edge_index
        nonlocal edges_added

        if u != v and len(graph[u]) < 5 and len(graph[v]) < 5:
            edge_key = tuple(sorted((u, v)))

            if edge_key not in edges_added:
                graph[u].add((edge_index, v, edge_weight))
                graph[v].add((edge_index, u, edge_weight))
                edge_index += 1
                edges_added[edge_key] = True

    for v in range(n):
        while len(graph[v]) < 2:
            new_neighbour = randint(0, n - 1)
            edge_weight = randint(1, max_weight)
            add_edge(v, new_neighbour, edge_weight)

    for row in graph:
        print(row, graph[row])

    return graph


show_graph(0, 1, gen_graph(0, 1, 17, 5), False)
