# Dany jest acykliczny, spójny, nieskierowany, ważony graf T (czyli T jest tak naprawdę ważonym
# drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek t, z którego odległość do
# najdalszego wierzchołka jest minimalna.
from math import inf


def dfs(graph, source, visited, distances, parent):
    visited[source] = True
    for v in graph[source]:
        if not visited[v[0]]:
            if distances[source] + v[1] > distances[v[0]]:
                distances[v[0]] = distances[source] + v[1]
            else:
                distances[v[0]] = distances[source]
            parent[v[0]] = source
            dfs(graph, v[0], visited, distances, parent)


def minimum_distance(graph, source):
    distances = [0] * len(graph)
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dfs(graph, source, visited, distances, parent)
    max_vert = distances.index((max(distances)))
    for i in range(len(graph)):
        distances[i] = 0
        visited[i] = False
        parent[i] = None
    dfs(graph, max_vert, visited, distances, parent)
    dist = max(distances)
    start = distances.index(dist)
    result = []
    while start is not None:
        result.append((distances[start], abs(distances[start] - dist), start))
        start = parent[start]
    min_difference = inf
    min_vertex = 0
    for i in range(len(result)):
        if abs(result[i][0] - result[i][1]) < min_difference:
            min_difference = abs(result[i][0] - result[i][1])
            min_vertex = result[i][2]
    return min_vertex


graph = [[(1, 12)],
         [(0, 12), (2, 10), (3, 15), (4, -5)],
         [(1, 10)],
         [(1, 15)],
         [(1, -5), (5, 2), (6, 4)],
         [(4, 2)],
         [(4, 4), (7, -6)],
         [(6, -6), (8, 1), (9, 20), (10, 4)],
         [(7, 1)],
         [(7, 20)],
         [(7, 4)]]
print(minimum_distance(graph, 0))
