from gen_graph import gen_graph
from show_graph import show_graph
from circuit_direction import find_circuit_direction


def main():
    s = 0
    t = 1
    n = 10
    max_weight = 10

    undirected_graph = gen_graph(s, t, n, max_weight)

    for row in undirected_graph:
        print(row, undirected_graph[row])

    directed_graph = find_circuit_direction(s, t, undirected_graph)
    show_graph(s, t, undirected_graph, False)
    show_graph(s, t, directed_graph, True)



main()