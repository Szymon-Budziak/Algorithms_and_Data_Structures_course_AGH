# Bellman-Ford algorithm for finding the shortest paths from source vertex to all other vertices in
# a given graph in which edge weights may be negative.
from math import inf


def relax(graph, distance, parent, j):
    if distance[graph[j][1]] > distance[graph[j][0]] + graph[j][2]:
        distance[graph[j][1]] = distance[graph[j][0]] + graph[j][2]
        parent[graph[j][1]] = graph[j][0]


def bellman_ford_algorithm(graph, source):
    V = 0
    for i in range(len(graph)):
        V = max(V, graph[i][0], graph[i][1])
    E = len(graph)
    distance = [inf] * (V + 1)
    parent = [None] * (V + 1)
    distance[source] = 0
    for i in range(V - 1):
        for j in range(E):
            relax(graph, distance, parent, j)
    for i in range(E):
        if distance[graph[i][1]] > distance[graph[i][0]] + graph[i][2]:
            return False, _, _
    return True, distance, parent


graph = [[0, 1, 6], [0, 2, 7], [1, 2, 8], [1, 3, 5], [1, 4, -4], [2, 3, -3],
         [2, 4, 9], [3, 1, -2], [4, 0, 2], [4, 3, 7]]
result, distance, parent = bellman_ford_algorithm(graph, 0)
if result:
    i = len(parent) - 1
    while parent[i] != None:
        print(distance[i], i)
        i = parent[i]
else:
    print("Graph contains negative weight cycle.")
