import random


def gen_graph(s, t, n, max_weight):
    graph = {v: set() for v in range(n)}

    edge_index = 0

    def add_edge(u, v, weight):
        nonlocal edge_index

        if u != v and u not in graph[v]:
            graph[v].add((edge_index, u, weight))
            graph[u].add((edge_index, v, weight))
            edge_index += 1

    add_edge(s, t, 0)

    for v in graph:
        while len(graph[v]) < 2:
            random_neighbour = random.randint(0, n - 1)
            random_weight = random.randint(0, max_weight)

            add_edge(v, random_neighbour, random_weight)

    return graph


gen_graph(0, 1, 5, 5)
