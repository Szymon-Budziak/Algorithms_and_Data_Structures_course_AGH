# Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?
from math import inf


def dfs(graph, source, visited, result):
    visited[source] = True
    for v in graph[source]:
        if not visited[v[0]]:
            dfs(graph, v[0], visited, result)
    result.insert(0, source)


def shortest_paths(graph, s):
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    distance[s] = 0
    result = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, result)
    idx = result.index(s)
    for i in range(idx, len(result)):
        for v in graph[i]:
            if distance[v[0]] > distance[i] + v[1]:
                distance[v[0]] = distance[i] + v[1]
    return distance


graph = [[(1, 3), (2, 6)],
         [(2, 2), (3, 1), (5, 8)],
         [(4, 7), (3, 5)],
         [(5, 2), (4, 5)],
         [(5, 3)],
         []]
print(shortest_paths(graph, 0))
