# Dijkstra's algorithm for finding the shortest paths in weighted graph on adjacency list.
from queue import PriorityQueue
from math import inf


def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
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
            for v in graph[u]:
                if relax(u, v, distance, parent):
                    queue.put(v[0])
    return parent, distance


graph = [[(1, 1), (2, 12)],
         [(0, 1), (2, 7), (3, 5)],
         [(0, 12), (1, 2), (3, 6), (4, 2)],
         [(1, 5), (2, 6), (4, 4), (5, 100)],
         [(2, 2), (3, 4), (5, 9)],
         [(3, 100), (4, 9)]]

parent, distance = dijkstra_algorithm(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i])
    i -= 1
