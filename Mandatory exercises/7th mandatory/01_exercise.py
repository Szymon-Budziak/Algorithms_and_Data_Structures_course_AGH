# Proszę zaimplementować algorytm Dijkstry.
from queue import PriorityQueue
from math import inf


def relax(graph, u, v, distance, parent):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        parent[v] = u
        return True
    return False


def dijkstra_algorithm(graph, source):
    queue = PriorityQueue()
    queue.put(source)
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    for i in range(len(graph)):
        if i != source:
            queue.put(i)
    distance[source] = 0
    while not queue.empty():
        u = queue.get()
        if not visited[u]:
            visited[u] = True
            for v in range(len(graph[u])):
                if graph[u][v] != 0:
                    if relax(graph, u, v, distance, parent):
                        queue.put(v)
    return parent, distance


graph = [[0, 1, 12, 0, 0, 0],
         [1, 0, 7, 5, 0, 0],
         [12, 7, 0, 6, 2, 0],
         [0, 5, 6, 0, 4, 100],
         [0, 0, 2, 4, 0, 9],
         [0, 0, 0, 100, 9]]

parent, distance = dijkstra_algorithm(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i])
    i -= 1
