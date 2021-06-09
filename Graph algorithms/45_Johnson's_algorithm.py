# Johnson's algorithm is an algorithm for finding shortest paths between every pair of vertices in
# a given weighted, directed graph (weights may be negative).
from math import inf
from queue import PriorityQueue


def bellman_ford(graph, source, V):
    distance = [inf] * len(graph)
    parent = [None] * len(graph)
    distance[source] = 0
    for i in range(1, len(graph)):
        for u in range(len(graph)):
            for v in graph[u]:
                if distance[u] + v[1] < distance[v[0]]:
                    distance[v[0]] = distance[u] + v[1]
                    parent[v[0]] = u
    for u in range(V):
        for v in graph[u]:
            if distance[u] + v[1] < distance[v[0]]:
                return False, distance, parent
    return True, distance, parent


def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def dijkstra(graph, source):
    distance = [inf] * len(graph)
    distance[source] = 0
    parent = [None] * len(graph)
    visited = [False] * len(graph)
    queue = PriorityQueue()
    queue.put((0, source))
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                queue.put((distance[v[0]], v[0]))
        visited[u] = True
    path = []
    for v in range(len(graph)):
        if parent[v] is None:
            path.append(None)
        else:
            actual_path = [v]
            while (parent[v] != source):
                actual_path.append(parent[v])
                v = parent[v]
            actual_path.append(source)
            actual_path.reverse()
            path.append(actual_path)
    return path


def johnsons_algorithm(graph):
    new_vertex = len(graph)
    V = [[i, 1] for i in range(new_vertex)]
    graph.append(V)
    result, distance, parent = bellman_ford(graph, new_vertex, len(graph))
    if not result:
        return False
    graph.pop(-1)
    for i in range(len(graph)):
        for j in graph[i]:
            j[1] = j[1] + (distance[i] - distance[j[0]])
    all_paths = []
    for v in range(len(graph)):
        path = dijkstra(graph, v)
        all_paths.append(path)
    return all_paths


graph = [[[4, -1]],
         [[0, 1], [3, 2]],
         [[1, 2], [5, 10]],
         [[0, -4], [4, 3]],
         [[1, 7]],
         [[1, 5]]]
print(johnsons_algorithm(graph))
