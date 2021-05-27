# Floyd-Warshall algorithm for finding the shortest paths between every pair of vertices in a given
# directed weighted graph.
from math import inf


def Floyd_Warshall_algorithm(graph):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance


def print_solution(distance):
    for i in range(len(distance)):
        print(distance[i])


graph = [[0, 0, 0, 0, -1, 0],
         [1, 0, 0, 2, 0, 0],
         [0, 2, 0, 0, 0, 10],
         [-4, 0, 0, 0, 3, 0],
         [0, 7, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0]]
distance = Floyd_Warshall_algorithm(graph)
print_solution(distance)
