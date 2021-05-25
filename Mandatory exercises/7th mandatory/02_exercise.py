# Proszę zaimplementować algorytm Kruskala.


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


def convert_to_edges(graph):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j][0], i, graph[i][j][1]) not in edges:
                edges.append((i, graph[i][j][0], graph[i][j][1]))
    return edges


def kruskal_algorithm(graph):
    edges = convert_to_edges(graph)
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


graph = [[(1, 1), (2, 8)],
         [(0, 1), (2, 7), (3, 3)],
         [(0, 8), (1, 7), (4, 12), (5, 2)],
         [(1, 3), (4, 7)],
         [(2, 12), (3, 7), (5, 4)],
         [(2, 2), (4, 4), (6, 6), (7, 10)],
         [(5, 6), (7, 5)],
         [(5, 10), (6, 5)]]
print(kruskal_algorithm(graph))
