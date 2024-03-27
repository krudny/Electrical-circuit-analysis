from gen_graph import gen_graph
from show_graph import show_graph
from circuit_direction import find_circuit_direction
from solver import solver

# undirected_graph = {
#     0: {(2, 1, 1), (1, 6, 1)},
#     1: {(4, 2, 6), (3, 6, 10), (2, 0, 1)},
#     2: {(6, 3, 10), (4, 1, 6), (5, 4, 1)},
#     3: {(6, 2, 10), (7, 4, 6), (10, 6, 2)},
#     4: {(7, 3, 6), (5, 2, 1), (8, 5, 6), (9, 6, 5)},
#     5: {(8, 4, 6), (0, 6, 0)},
#     6: {(1, 0, 1), (0, 5, 0), (9, 4, 5), (10, 3, 2), (3, 1, 10)}
# }


def main():
    s = 5
    t = 6
    n = 17
    max_weight = 7
    electromotive_force = 100
    undirected_graph, edges_count = gen_graph(s, t, n, max_weight)
    directed_graph = find_circuit_direction(s, t, undirected_graph)

    values = solver(s, t, edges_count, n, undirected_graph, directed_graph, electromotive_force)
    if values is not None:
        # show_graph(s, t, undirected_graph, False, values)
        show_graph(s, t, directed_graph, True, values)
    else:
        print("something unexpected happen :c")

main()