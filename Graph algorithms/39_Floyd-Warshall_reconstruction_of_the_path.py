# Implement the Floyd-Warshall algorithm so that it gives an information that allows the
# reconstruction of the shortest path between any two pairs of vertices over time depending on the
# length of that path.
from math import inf


def floyd_warshall_path(graph, start, end):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    parent = [[None] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != -1:
                distance[i][j] = graph[i][j]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != -1:
                parent[i][j] = i
    for u in range(len(graph)):
        for v in range(len(graph)):
            for w in range(len(graph)):
                if distance[v][w] > distance[v][u] + distance[u][w]:
                    distance[v][w] = distance[v][u] + distance[u][w]
                    parent[v][w] = parent[u][w]
    while end is not None:
        print(end, end=" ")
        end = parent[start][end]
    print()
    return parent


graph = [[-1, 7, 6, -1, -1, -1, -1, -1, -1],
         [7, -1, -1, 3, 2, -1, -1, -1, -1],
         [6, -1, -1, -1, -1, 2, -1, -1, -1],
         [-1, 3, -1, -1, -1, -1, -1, 4, -1],
         [-1, 2, -1, -1, -1, -1, 1, -1, 15],
         [-1, -1, 2, -1, -1, -1, 3, 4, -1],
         [-1, -1, -1, -1, 1, 3, -1, 6, -1],
         [-1, -1, -1, 4, -1, 4, 6, -1, -5],
         [-1, -1, -1, -1, 15, -1, -1, 5, -1]]
print(floyd_warshall_path(graph, 0, 8))
