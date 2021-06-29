# We are given a weighted graph with positive weights. Find the length of the shortest cycle in graph.
# Algorithm should return False if there is no cycle.
from math import inf


def dijkstra_algorithm(graph, source):
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = 0
    parent = [None] * len(graph)
    parent[source] = source
    minimal_cycle = inf
    actual_edge = None
    for i in range(len(graph)):
        actual_distance = inf
        actual_index = -1
        for j in range(len(graph)):
            if not visited[j] and actual_distance > distance[j]:
                actual_distance = distance[j]
                actual_index = j
        visited[actual_index] = True
        for j in range(len(graph)):
            if graph[actual_index][j] > 0:
                if distance[j] > distance[actual_index] + graph[actual_index][j]:
                    distance[j] = distance[actual_index] + graph[actual_index][j]
                    parent[j] = actual_index
                if j != parent[actual_index] and visited[j]:
                    if minimal_cycle > distance[j] + distance[actual_index] + graph[actual_index][j]:
                        minimal_cycle = distance[j] + distance[actual_index] + graph[actual_index][j]
                        actual_edge = (j, actual_index)
    if actual_edge is None:
        return None
    return minimal_cycle


def the_shortest_cycle(graph):
    minimal_distance = inf
    for i in range(len(graph)):
        distance = dijkstra_algorithm(graph, i)
        if distance is not None:
            minimal_distance = min(minimal_distance, distance)
    return minimal_distance


graph = [[0, 2, 0, 1, 0, 0, 3],
         [2, 0, 0, 7, 2, 2, 0],
         [0, 0, 0, 1, 1, 0, 5],
         [1, 7, 1, 0, 0, 4, 0],
         [0, 2, 1, 0, 0, 0, 0],
         [0, 2, 0, 4, 0, 0, 0],
         [3, 0, 5, 0, 0, 0, 0]]
print(the_shortest_cycle(graph))
