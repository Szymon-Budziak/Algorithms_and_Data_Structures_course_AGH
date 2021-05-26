# Dijkstra's algorithm for finding the shortest paths in weighted graph on adjacency list.
from queue import PriorityQueue
from math import inf


# 1st solution:


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


# 2nd solution:


def dijkstra_algorithm_2(graph, source):
    queue = PriorityQueue()
    distance = [inf] * len(graph)
    counter = len(graph)
    queue.put((0, source))
    while not queue.empty() and counter > 0:
        dist, v = queue.get()
        if dist < distance[v]:
            counter -= 1
            distance[v] = dist
            for edge in graph[v]:
                u, length = edge
                queue.put((dist + length, u))
    return distance


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
print("----------")
distance_2 = dijkstra_algorithm_2(graph, 0)
i = len(parent) - 1
while i != 0:
    print(i, distance_2[i])
    i -= 1
