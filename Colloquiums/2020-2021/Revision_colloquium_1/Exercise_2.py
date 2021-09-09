# Dany jest spójny graf nieskierowany G = (V, E). Proszę zaimplementować funkcję:
# def breaking(G):
#     ...
# która zwraca taki jego wierzchołek, że jego usunięcie (razem z incydentnymi krawędziami) powoduje,
# że graf rozpadnie się na jak najwięcej nie połączonych ze sobą częsci. Funkcja przyjmuje graf
# reprezentowany przez kwadratową, symetryczną macierz sąsiedztwa i zwraca numer wierzchołka,
# z założeniem numeracji od zera. Jeśli usunięcie żadnego wierzchołka nie spowoduje tego, że graf
# przestanie być spójnym, funkcja powinna zwrócić None. Funkcja powinna być możliwie jak najszybsza.
# Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
from Exercise_2_tests import runtests
from queue import Queue


def components(graph):
    queue = Queue()
    visited = [False] * len(graph)
    result = [0] * len(graph)
    count = 0
    for vertex in range(len(graph)):
        if result[vertex] == 0:
            queue.put(vertex)
            count += 1
            result[vertex] = count
            visited[vertex] = True
            while not queue.empty():
                u = queue.get()
                for v in range(len(graph)):
                    if not visited[v] and graph[u][v] == 1:
                        queue.put(v)
                        visited[v] = True
                        result[v] = count
    return count


def breaking(G):
    to_remove = []
    max_breaking = 2
    breaking_vertex = None
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                to_remove.append(j)
        for k in range(len(to_remove)):
            G[i][to_remove[k]] = G[to_remove[k]][i] = 0
        actual_break = components(G)
        if actual_break > max_breaking:
            max_breaking = actual_break
            breaking_vertex = i
        for k in range(len(to_remove)):
            G[i][to_remove[k]] = G[to_remove[k]][i] = 1
        to_remove.clear()
    return breaking_vertex


runtests(breaking)
