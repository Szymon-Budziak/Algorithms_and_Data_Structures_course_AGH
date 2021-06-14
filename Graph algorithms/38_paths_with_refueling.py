# We are given two-dimensional array G which represents adjacency matrix of the weighted directed
# graph that corresponds to the road map (weights are the distances, the number -1 means that there
# is no edge). In some vertices there are petrol stations, we are given their list P. A full tank of
# fuel is enough to cover the distance d. When entering the station, the car is always fully refueled.
# Implement an algorithm which searches for the shortest possible route from vertex A to vertex B, if
# there is one and returns a list of consecutive visited vertices on the route (we assume that there
# is also a petrol station in vertex A, car can only travel distance d without refueling).
from math import inf


def floyd_warshall(graph):
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
    return distance, parent


def create_path(path, parent, a, b):
    path.append(b)
    if parent[a][b] != 0:
        create_path(path, parent, a, parent[a][b])


def paths_with_refueling(graph, P, d, a, b):
    distance, parent = floyd_warshall(graph)
    for i in range(len(distance)):
        for j in range(len(graph)):
            if (i not in P) or (j not in P) or distance[i][j] > d:
                if distance[i][j] <= d and j == b:
                    continue
                else:
                    distance[i][j] = -1
    new_graph, new_parent = floyd_warshall(distance)
    if new_graph[a][b] == inf:
        return None
    else:
        path = []
        create_path(path, new_parent, a, b)
        path.append(a)
        path.reverse()
        return path


graph = [[-1, 6, -1, 5, 2],
         [-1, -1, 1, 2, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, 4, -1, -1],
         [-1, -1, 8, -1, -1]]
P = [0, 1, 3]
print(paths_with_refueling(graph, P, 5, 0, 2))
