# We are given a weighted graph G and a spanning tree T that contains the vertex s. Find algorithm that
# checks if T is a tree of the shortest paths from the vertex s.
from queue import PriorityQueue
from math import inf


def relax(distance, u, v):
    if distance[v[0]] > distance[u] + v[1] and distance[v[0]] != inf:
        return True
    return False


def tree_of_the_shortest_paths(graph, source):
    queue = PriorityQueue()
    queue.put(source)
    distance = [inf] * len(graph)
    distance[source] = 0
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if distance[v[0]] > distance[u] + v[1] and distance[v[0]] == inf:
                distance[v[0]] = distance[u] + v[1]
                queue.put(v[0])
            else:
                if relax(distance, u, v):
                    return False
    return True


graph = [[(1, 1), (2, 3), (3, 8), (4, 7), (5, 3), (6, 11)],
         [(0, 1), (2, 5)],
         [(0, 3), (1, 5)],
         [(0, 8), (4, 1)],
         [(0, 7), (3, 1), (5, 2)],
         [(0, 3), (4, 2), (6, 3)],
         [(0, 11), (5, 3)]]
print(tree_of_the_shortest_paths(graph, 0))
