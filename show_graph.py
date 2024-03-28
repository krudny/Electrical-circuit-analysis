from pyvis.network import Network


def show_graph(s, t, graph, directed, values):
    net = Network(directed=directed)

    for v in graph:
        net.add_node(v, label=f"{v}")

    for v in graph:
        for edge_index, u, edge_weight in graph[v]:
            if v == s and u == t:
                net.add_edge(s, t, color="red", label=f"EF, I={round(values[edge_index], 2)}")
            else:
                net.add_edge(v, u, label=f"R={edge_weight}, I={round(values[edge_index], 2)}")



    net.show_buttons(filter_=['physics'])
    net.show(f"{directed}-graph.html", notebook=False)