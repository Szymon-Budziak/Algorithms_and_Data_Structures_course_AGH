# Proszę zaimplementować algorytm Dijkstry dla wybranej reprezentacji grafu.
# Reprezentacja grafu w postaci listy sąsiedztwa.
from queue import PriorityQueue
from math import inf


def dijkstra_algorithm(graph, source):
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
print(dijkstra_algorithm(graph, 0))
