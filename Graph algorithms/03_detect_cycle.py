# Check if undirected graph has a cycle


def detect_cycle(graph, source):
    visited = [False] * len(graph)
    return dfs(graph, source, visited, 0)


def dfs(graph, source, visited, parent):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            parent = source
            dfs(graph, v, visited, parent)
        elif visited[v] and v != parent:
            return True
    return False


# graph has a cycle
graph1 = [[1, 2, 3], [0, 7], [0, 5], [0, 5], [0, 6, 7], [2, 3, 6], [4, 5], [1, 4]]
print(detect_cycle(graph1, 0))

# graph doesn't have a cycle
graph2 = [[1, 2, 5], [0, 3], [0, 4, 7, 8], [1], [2, 6], [0], [4], [2], [2]]
print(detect_cycle(graph2, 0))
