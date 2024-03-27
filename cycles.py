def find_index(cycle, u):
    for i, v in enumerate(cycle):
        if u == v:
            return i


def find_cycles(graph):
    visited = set()
    parent = [None] * len(graph)
    cycles = set()
    result = []

    def check_electromotive_force():
        for cycle in result:
            if 0 not in cycle:
                result.remove(cycle)

    def dfs_visit(v, path_vertices, path_edges):
        visited.add(v)

        for edge_index, u, weight in graph[v]:
            if u in path_vertices and parent[v] != u:  # cycle detected
                cycle_start = find_index(path_vertices, u)  # searching for cycle start
                curr_cycle = path_vertices[cycle_start:]  # extracting cycle
                sorted_cycle = tuple(sorted(curr_cycle))

                if sorted_cycle not in cycles:  # checking if cycle was not detected previously
                    cycles.add(sorted_cycle)
                    result.append(path_edges + [edge_index])

            if u not in visited:
                parent[u] = v
                dfs_visit(u, path_vertices + [u], path_edges + [edge_index])

    for v in graph:
        dfs_visit(v, [v], [])
        visited = set()

    check_electromotive_force()

    return result

