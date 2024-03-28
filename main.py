from gen_graph import gen_graph
from show_graph import show_graph
from circuit_direction import find_circuit_direction
from solver import solver

def main():
    s = 0
    t = 7
    n = 9
    max_weight = 10
    electromotive_force = 15
    undirected_graph, edges_count = gen_graph(s, t, n, max_weight)
    directed_graph = find_circuit_direction(s, t, undirected_graph)

    values = solver(s, t, edges_count, n, undirected_graph, directed_graph, electromotive_force)
    if values is not None:
        show_graph(s, t, directed_graph, True, values)
    else:
        print("something unexpected happen :c")

main()