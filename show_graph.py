from pyvis.network import Network


def show_graph(s, t, graph, directed):
    net = Network(directed=directed)

    for v in graph:
        net.add_node(v, label=f"{v}")

    net.add_edge(s, t, color="red", label=f"electromotive force")

    for v in graph:
        for edge_index, u, edge_weight in graph[v]:
            net.add_edge(v, u, label=f"({edge_index}, {edge_weight})")



    net.show_buttons(filter_=['physics'])
    net.show(f"{directed}-graph.html", notebook=False)