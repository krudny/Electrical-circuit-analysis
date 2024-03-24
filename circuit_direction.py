from collections import deque


# finds approximate circuit direction
def find_circuit_direction(s, t, graph):
    visited = set()
    q = deque()
    q.append(t)
    directed_graph = {v: set() for v in range(len(graph))}

    while q:
        u = q.popleft()
        visited.add(u)

        for edge_index, v, edge_weight in graph[u]:
            if v not in visited:
                if v == s and u == t or v == t and u == s:
                    continue

                q.append(v)
                directed_graph[u].add((edge_index, v, edge_weight))

    return directed_graph


