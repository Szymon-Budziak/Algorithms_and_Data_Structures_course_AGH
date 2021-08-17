# Dany jest graf nieskierowany G = (V, E). Mówimy, że spójność krawędziowa G wynosi k jeśli usunięcie
# pewnych k krawędzi powoduje, że G jest niespójny, ale usunięcie dowolnych k−1 krawędzi nie rozspójnia
# go. Proszę podać algorytm, który oblicza spójność krawędziową danego grafu.
from math import inf
from queue import Queue
from copy import deepcopy


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


def count_edges(graph):
    edges = []
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                if (i, j, graph[i][j]) not in edges:
                    edges.append((i, j, graph[i][j]))
                    count += 1
    return count


def edge_consistency(graph):
    new_graph = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            new_graph[i][j] = 1
    edges = int(count_edges(new_graph) / 2)
    actual_graph = [[0] * (len(new_graph) + edges) for _ in range(len(new_graph) + edges)]
    vertex = len(new_graph)
    for i in range(len(new_graph)):
        for j in range(len(new_graph)):
            if new_graph[i][j] != 0 and i < j:
                actual_graph[i][j] = new_graph[i][j]
                actual_graph[j][vertex] = actual_graph[vertex][i] = new_graph[i][j]
                vertex += 1
    min_max_flow = inf
    for i in range(1, len(new_graph)):
        current_graph = deepcopy(actual_graph)
        result = ford_fulkerson_algorithm(current_graph, 0, i)
        min_max_flow = min(min_max_flow, result)
    return min_max_flow


graph = [[1, 4, 5],
         [0, 2, 3],
         [1, 3],
         [1, 2, 4],
         [0, 3, 5],
         [0, 4]]
print(edge_consistency(graph))
