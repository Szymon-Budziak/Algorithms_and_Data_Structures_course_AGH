# We are given a weighted graph G with positive weights. There is also given a list of edges E' that
# do not belong to the graph, but they are edges between the vertices in G. The two vertices s and t
# are also given. Determine which edge from E' should be added to the graph G to reduce the distance
# between s and t as much as possible. If neither edge lower the distance between s and t, the
# algorithm should return False.
from math import inf
from queue import PriorityQueue


def first_relax(graph, distance, u, v):
    if distance[v][0] > distance[u][0] + graph[u][v]:
        distance[v][0] = distance[u][0] + graph[u][v]
        return True
    return False


def second_relax(graph, distance, u, v, E, parent, queue):
    if (u, v, graph[u][v]) in E or (v, u, graph[u][v]) in E:
        if distance[v][1] > distance[u][0] + graph[u][v]:
            distance[v][1] = distance[u][0] + graph[u][v]
            parent[v] = (u, v)
            queue.put((distance[v][1], v))
    else:
        if distance[u][1] != inf:
            if distance[v][1] > distance[u][1] + graph[u][v]:
                distance[v][1] = distance[u][1] + graph[u][v]
                queue.put((distance[v][1], v))
                parent[v] = parent[u]
        else:
            queue.put((distance[v][0], v))


def edge_reducing_the_distance(graph, E, s, t):
    queue = PriorityQueue()
    queue.put((0, s))
    visited = [False] * len(graph)
    distance = [[inf] * 2 for _ in range(len(graph))]
    distance[0][0] = 0
    distance[0][1] = inf
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph[u])):
            if graph[u][v] != 0 and not visited[v]:
                if first_relax(graph, distance, u, v):
                    queue.put((distance[v][0], v))
        visited[u] = True
    for i in range(len(E)):
        graph[E[i][0]][E[i][1]] = E[i][2]
        graph[E[i][1]][E[i][0]] = E[i][2]
    queue.put((0, s))
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph[u])):
            if graph[u][v] != 0 and not visited[v]:
                second_relax(graph, distance, u, v, E, parent, queue)
        visited[u] = True
    if distance[t][1] >= distance[t][0]:
        return False
    return parent[t]


graph = [[0, 0, 1, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 0, 0],
         [1, 0, 0, 6, 4, 8, 0, 0],
         [2, 0, 6, 0, 0, 0, 0, 0],
         [0, 5, 4, 0, 0, 0, 0, 6],
         [0, 0, 8, 0, 0, 0, 4, 1],
         [0, 0, 0, 0, 0, 4, 0, 7],
         [0, 0, 0, 0, 6, 1, 7, 0]]
E = [(0, 1, 3), (3, 5, 5), (3, 6, 6), (4, 5, 3)]
s = 0
t = len(graph) - 1
print(edge_reducing_the_distance(graph, E, s, t))
