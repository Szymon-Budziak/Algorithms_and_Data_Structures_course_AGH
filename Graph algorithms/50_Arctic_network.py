# In the Arctic, settlements are very distant from each other. We are given them as pairs of
# coordinates (x, y). Some of them have satellite receivers - from such a settlement you can
# directly communicate with any other settlement that has a satellite receiver. We now want to
# place radio receivers with the same limited range D (integer) in every settlement, so that we
# can communicate (directly or indirectly) between each pair of settlements. Find the minimum D.
from math import sqrt, inf
from queue import PriorityQueue


# 1st solution using Kruskal algorithm:


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_set(v):
    return Node(v)


def kruskal_algorithm(graph, edges):
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []
    for i in range(len(graph)):
        V.append(make_set(i))
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
    return MST


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def arctic_network_kruskal(settlements, receivers):
    graph = []
    for i in range(len(settlements)):
        for j in range(i + 1, len(settlements)):
            if settlements[i] in receivers and settlements[j] in receivers:
                graph.append((i, j, 0))
            else:
                dist = distance(settlements[i], settlements[j])
                graph.append((i, j, dist))
    mst = kruskal_algorithm(settlements, graph)
    return mst[-1][2]


# 2nd solution using Prim's algorithm:


def arctic_network_prim(settlements, receivers):
    queue = PriorityQueue()
    graph = [[] for _ in range(len(settlements))]
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if settlements[i] in receivers and settlements[j] in receivers:
                graph[i].append((j, 0))
                graph[j].append((i, 0))
            else:
                dist = distance(settlements[i], settlements[j])
                graph[i].append((j, dist))
                graph[j].append((i, dist))
    queue = PriorityQueue()
    parent = [None] * len(settlements)
    key = [inf] * len(settlements)
    key[0] = 0
    visited = [False] * len(settlements)
    queue.put((0, 0))
    while not queue.empty():
        dist, u = queue.get()
        visited[u] = True
        for v in graph[u]:
            if key[v[0]] > v[1] and not visited[v[0]]:
                parent[v[0]] = u
                key[v[0]] = v[1]
                queue.put((key[v[0]], v[0]))
    mst = []
    for i in range(len(parent)):
        if parent[i] is not None:
            mst.append((i, parent[i], key[i]))
    mst.sort(key=lambda x: x[2])
    return mst[-1][2]


settlements = [(1, 1), (2, 3), (-5, -1), (-3, 1), (-2, -2), (-2, 1), (6, 4), (5, 2), (-3, -3), (-5, 4)]
receivers = [(-2, 1), (5, 2), (-3, 1)]
print(arctic_network_kruskal(settlements, receivers))
print(arctic_network_prim(settlements, receivers))
