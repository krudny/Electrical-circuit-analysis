from pyvis.network import Network


def show_graph(s, t, graph, directed, values):
    net = Network(directed=directed)

    for v in graph:
        net.add_node(v, label=f"{v}", size=10)

    for v in graph:
        for edge_index, u, edge_weight in graph[v]:
            if v == s and u == t:
                net.add_edge(s, t, color="red", label=f"EF, I={round(values[edge_index], 2)}", font={"size": 14})
            else:
                net.add_edge(v, u, label=f"R={edge_weight}, I={round(values[edge_index], 2)}", font={"size": 14})

    net.options = {
        "physics": {
            "hierarchicalRepulsion": {
                "centralGravity": 0.0,
                "springLength": 100,
                "springConstant": 0.04,
                "nodeDistance": 150,
                "damping": 0.09
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based"
        }
    }
    net.show(f"graph.html", notebook=False)
