# An edge in consistent undirected graph is called a bridge if its removal spreads the graph.
from math import inf


def bridge(graph):
    visited = [False] * len(graph)
    time_visit = [0] * len(graph)
    low = [inf] * len(graph)
    parent = [None] * len(graph)
    time = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, parent, time_visit, time, low)
    for i in range(len(graph)):
        if time_visit[i] == low[i] and parent[i] is not None:
            print(parent[i], i)


def dfs(graph, source, visited, parent, time_visit, time, low):
    visited[source] = True
    time_visit[source] = time
    time += 1
    low[source] = time_visit[source]
    for v in graph[source]:
        if not visited[v]:
            parent[v] = source
            dfs(graph, v, visited, parent, time_visit, time, low)
            low[source] = min(low[source], low[v])
        elif parent[source] != v:
            low[source] = min(low[source], time_visit[v])


graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
bridge(graph)
