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
    queue.put((0, source))
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
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
