# Dijkstra's algorithm for finding the shortest paths in weighted graph on adjacency matrix.
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
    queue.put((0, source))
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph[u])):
            if graph[u][v] != 0 and not visited[v]:
                if relax(graph, u, v, distance, parent):
                    queue.put((dist + graph[u][v], v))
        visited[u] = True
    return parent, distance


graph = [[0, 1, 5, 0, 0],
         [1, 0, 2, 8, 7],
         [5, 2, 0, 3, 0],
         [0, 8, 3, 0, 1],
         [0, 7, 0, 1, 0]]

parent, distance = dijkstra_algorithm(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i])
    i -= 1
