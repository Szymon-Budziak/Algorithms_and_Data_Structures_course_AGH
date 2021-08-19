# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować
# i zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm
# powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego poprawność
# i oszacować złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
# def enlarge(G, s, t):
#     ...
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą warunki
# zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list sąsiadów,
# t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0. Funkcja powinna
# zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest krawędź spełniająca warunki
# zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie nie było ścieżki z s do t
# to funkcja powinna zwrócić None.
from Exercise_2_tests import runtests
from queue import Queue
from math import inf


def bfs(G, visited, distances, parents, s):
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                parents[v] = u
                distances[v] = min(distances[v], distances[u] + 1)


def enlarge(G, s, t):
    visited = [False] * len(G)
    visited[s] = True
    distances = [inf] * len(G)
    distances[s] = 0
    parents = [-1] * len(G)
    bfs(G, visited, distances, parents, s)
    dist = distances[t]
    if dist == inf:
        return None
    vertices = []
    i = t
    while parents[i] != -1:
        vertices.append((parents[i], i))
        i = parents[i]
    for vertex in vertices:
        G[vertex[0]].remove(vertex[1], )
        G[vertex[1]].remove(vertex[0], )
        for i in range(len(G)):
            visited[i] = False
            distances[i] = inf
            parents[i] = -1
        visited[s] = True
        distances[s] = 0
        bfs(G, visited, distances, parents, s)
        new_dist = distances[t]
        if new_dist > dist:
            return vertex
        G[vertex[0]].append(vertex[1])
        G[vertex[1]].append(vertex[0])
    return None


runtests(enlarge)
