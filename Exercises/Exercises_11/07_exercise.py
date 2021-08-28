# Dany jest graf skierowany G = (V, E) oraz wierzchołki s i t. Proszę zaproponować algorytm znajdujący
# maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.
from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]


def ford_fulkerson_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def max_number_of_separate_paths(graph, s, t):
    new_graph = [[0] * (2 * len(graph)) for _ in range(2 * len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            new_graph[2 * i + 1][2 * j] = 1
    for i in range(len(graph)):
        if i == s or i == t:
            new_graph[2 * i][2 * i + 1] = inf
        else:
            new_graph[2 * i][2 * i + 1] = 1
    return ford_fulkerson_algorithm(new_graph, 2 * s, 2 * t + 1)


graph = [[1, 2, 3], [0, 4], [0, 4], [0, 5, 6], [1, 2, 8], [3, 7], [3, 7], [5, 6, 9], [4, 9], [7, 8]]
s = 0
t = 9
print(max_number_of_separate_paths(graph, s, t))
