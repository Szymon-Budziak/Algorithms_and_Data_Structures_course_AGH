# Proszę zaimplementować wybrany przez siebie algorytm obliczania minimalnego drzewa rozpinającego dla
# wybranej reprezentacji grafu.
# Algorytm Kruskala dla grafu w postaci macierzy sąsiedztwa.


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
        for j in range(len(graph)):
            if graph[i][j] != 0 and (j, i, graph[i][j]) not in edges:
                edges.append((i, j, graph[i][j]))
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


graph = [[0, 7, 8, 3, 2, 0],
         [7, 0, 1, 0, 0, 0],
         [8, 1, 0, 12, 0, 4],
         [3, 0, 12, 0, 0, 6],
         [2, 0, 0, 0, 0, 5],
         [0, 0, 4, 6, 5, 0]]
print(kruskal_algorithm(graph))
