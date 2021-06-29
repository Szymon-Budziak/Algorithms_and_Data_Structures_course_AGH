# W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć miasta siecią autostrad, tak
# aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo
# jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy
# miastami liczona w kilometrach wyraża się wzorem len = sqrt((x1-x2)**2 + (y1-y2)**2). Z uwagi na
# oszczędność materiałów autostrada łączy dwa miasta w linii prostej. Ponieważ zbliżają się wybory
# prezydenckie, wszystkie autostrady zaczęto budować równocześnie i jako cel postanowiono zminimalizować
# czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy autostrady wyrażony w dniach
# wynosi ceil(len) (sufit z długości autostrady wyrażonej w km). Proszę zaimplementować algorytm
# wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.
from math import inf


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


def kruskal_algorithm(graph, source, vertices):
    V = []
    for i in range(vertices):
        V.append(make_set(i))
    visited = [False for _ in range(vertices)]
    start_day = end_day = 0
    for i in range(source, len(graph)):
        if start_day == 0:
            start_day = graph[i][2]
        u = graph[i][0]
        v = graph[i][1]
        if find(V[u]) != find(V[v]):
            end_day = graph[i][2]
            visited[u] = True
            visited[v] = True
            union(V[u], V[v])
    for i in range(vertices):
        if not visited[i]:
            return inf
    return end_day - start_day


def highway(graph):
    vertices = len(graph)
    edges = convert_to_edges(graph)
    edges.sort(key=lambda x: x[2])
    best_result = inf
    for i in range(vertices):
        result = kruskal_algorithm(edges, i, vertices)
        best_result = min(best_result, result)
    return best_result


graph = [[(1, 2), (2, 5)],
         [(0, 2), (3, 4), (6, 6)],
         [(0, 5), (3, 4), (4, 3)],
         [(1, 4), (2, 4), (5, 1)],
         [(2, 3), (5, 2)],
         [(3, 1), (4, 2), (7, 7)],
         [(1, 6), (7, 1)],
         [(5, 7), (6, 1)]]
print(highway(graph))
