# Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y, podczas
# gdy Max musi zrobić to samo, ale w przeciwną stronę. Problem polega na tym, że jeśli substancje te
# znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której absolutnie nic się nie stanie
# (ale szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się, że ich praca nie jest nikomu
# potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm planujący jednocześnie trasy Carol i Maxa
# tak, by odległość między nimi zawsze wynosiła co najmniej d. Mapa połączeń dana jest jako graf
# nieskierowany, w którym każda krawędź ma dodatnią wagę (x i y to wierzchołki w tym grafie).
# W jednostce czasu Carol i Max pokonują dokładnie jedną krawędź. Jeśli trzeba, dowolne z nich może się
# w danym kroku zatrzymać (wówczas pozostaje w tym samym wierzchołku). Carol i Max nie mogą równocześnie
# poruszać się tą samą krawędzią (w przeciwnych kierunkach).
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def keep_distance(M, x, y, d):
#     ...
# która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany przez
# kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to długość krawędzi między
# wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między wierzchołkami. W macierzy
# nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
# [(x, y), (u[1], v[1]), (u[2], v[2]), ..., (u[k], v[k]), (y, x)]
# reprezentującą ścieżki Carol i Max. W powyższej liście element (u[i], v[i]) oznacza, że Carol znajduje
# się w wierzchołku u[i], zaś Max w wierzchołku v[i]. Można założyć, że rozwiązanie istnieje.
from Exercise_1_tests import runtests
from math import inf
from queue import Queue


def bfs(graph, parent, source):
    queue = Queue()
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                queue.put(v)
                visited[v] = True
                parent[v] = u


def floyd_warshall_algorithm(graph):
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


def keep_distance(M, x, y, d):
    distance = floyd_warshall_algorithm(M)
    size = len(M) * len(M)
    graph = [[0] * size for _ in range(size)]
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j or distance[i][j] > d:
                for k in range(len(M)):
                    for m in range(len(M)):
                        if distance[k][m] < d or (k == j and m == i):
                            continue
                        if (j == m and M[i][k] != 0) or (i == k and M[j][m] != 0) or (M[i][k] != 0 and M[j][m] != 0):
                            graph[i * len(M) + j][k * len(M) + m] = 1
    parent = [None] * len(graph)
    source = x * len(M) + y
    bfs(graph, parent, source)
    result = []
    index = y * len(M) + x
    while index is not None:
        result.append((index // len(M), index % len(M)))
        index = parent[index]
    result.reverse()
    return result


runtests(keep_distance)
