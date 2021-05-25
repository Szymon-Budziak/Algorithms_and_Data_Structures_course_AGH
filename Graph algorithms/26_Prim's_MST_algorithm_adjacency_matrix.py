# Prim's algorithm for finding MST - minimum spanning tree on adjacency matrix.
from queue import PriorityQueue
from math import inf


def prim_algorithm(graph, source):
    queue = PriorityQueue()
    parent = [None] * len(graph)
    key = [inf] * len(graph)
    key[source] = 0
    visited = [False] * len(graph)
    visited[source] = True
    queue.put((0, source))
    while not queue.empty():
        dist, u = queue.get()
        visited[u] = True
        for i in range(len(graph)):
            if graph[u][i] != 0 and key[i] > graph[u][i] and not visited[i]:
                parent[i] = u
                key[i] = graph[u][i]
                queue.put((key[i], i))
    result = []
    for i in range(len(parent)):
        if parent[i] is not None:
            result.append((i, parent[i], key[i]))
    return result


graph = [[0, 7, 8, 3, 2, 0],
         [7, 0, 1, 0, 0, 0],
         [8, 1, 0, 12, 0, 4],
         [3, 0, 12, 0, 0, 6],
         [2, 0, 0, 0, 0, 5],
         [0, 0, 4, 6, 5, 0]]
print(prim_algorithm(graph, 0))
