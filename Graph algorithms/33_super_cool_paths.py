# We are given a weighted graph G. Super cool path is one that is not only the shortest weighted path
# between v and u, but also has the fewest edges (in other words we are looking for the shortest paths
# in terms of the number of edges among the shortest paths in the weight sense). Find algorithm that
# for a given starting vertex s will find super cool paths to other vertices.
from queue import PriorityQueue
from math import inf


def relax(u, v, distance, vertices_length, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        vertices_length[v[0]] = vertices_length[u] + 1
        parent[v[0]] = u
        return True
    elif distance[v[0]] == distance[u] + v[1]:
        if vertices_length[v[0]] > vertices_length[u] + 1:
            vertices_length[v[0]] = vertices_length[u] + 1
            parent[v[0]] = u
            return True
    return False


def super_cool_paths(graph, source):
    queue = PriorityQueue()
    queue.put(source)
    distance = [inf] * len(graph)
    distance[source] = 0
    vertices_length = [inf] * len(graph)
    vertices_length[source] = 0
    parent = [None] * len(graph)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if relax(u, v, distance, vertices_length, parent):
                queue.put(v[0])
    return distance, parent, vertices_length


graph = [[(1, 1), (5, 1), (7, 2)],
         [(0, 1), (2, 1)],
         [(1, 1), (3, 1)],
         [(2, 1), (4, 1)],
         [(3, 1), (6, 1), (7, 2)],
         [(0, 1), (6, 2)],
         [(5, 2), (4, 1)],
         [(0, 2), (4, 2)]]

distance, parent, vertices_length = super_cool_paths(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i], vertices_length[i])
    i -= 1
