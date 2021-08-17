# Proszę wskazać algorytm, który znajduje maksymalny przepływ między źródłem i ujściem w grafie
# nieskierowanym. Proszę użyć algorytmu z wykładu — dla grafów skierowanych, gdzie między każdą parą
# wierzchołków jest najwyżej jedna krawędź — jako czarnej skrzynki. Alternatywnie można opisać
# implementację bezpośrednio pracując na grafie nieskierowanym.
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


def max_flow_undirected_graph(graph, s, t):
    edges = int(count_edges(graph) / 2)
    new_graph = [[0] * (len(graph) + edges) for _ in range(len(graph) + edges)]
    vertex = len(graph)
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0 and i < j:
                new_graph[i][j] = graph[i][j]
                new_graph[j][vertex] = new_graph[vertex][i] = graph[i][j]
                vertex += 1
    return ford_fulkerson_algorithm(new_graph, s, t)


graph = [[0, 8, 7, 5, 0],
         [8, 0, 0, 3, 0],
         [7, 0, 0, 5, 4],
         [5, 3, 5, 0, 8],
         [0, 0, 4, 8, 0]]
print(max_flow_undirected_graph(graph, 0, 4))
