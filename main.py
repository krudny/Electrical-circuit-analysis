from gen_graph import gen_graph
from show_graph import show_graph
from circuit_direction import find_circuit_direction
from solver import solver


def main():
    s = 0
    t = 1
    n = 5
    max_weight = 10

    undirected_graph, edges_count = gen_graph(s, t, n, max_weight)
    directed_graph = find_circuit_direction(s, t, undirected_graph)

    # solver(0, 1, edges_count, n, undirected_graph, directed_graph)

    for row in undirected_graph:
        print(row, undirected_graph[row])

    show_graph(s, t, directed_graph, True)

main()