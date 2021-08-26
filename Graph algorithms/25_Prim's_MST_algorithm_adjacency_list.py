# Prim's algorithm for finding MST - minimum spanning tree on adjacency list.
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
        for v in graph[u]:
            if key[v[0]] > v[1] and not visited[v[0]]:
                parent[v[0]] = u
                key[v[0]] = v[1]
                queue.put((key[v[0]], v[0]))
    result = []
    for i in range(len(parent)):
        if parent[i] is not None:
            result.append((i, parent[i], key[i]))
    return result


graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]
print(prim_algorithm(graph, 0))
