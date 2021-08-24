# Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać z miasta (wierzchołka) s do
# miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę.
# Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby opłat. W ogólności
# graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.
from collections import deque
from math import inf


def edges_01(graph, source):
    queue = deque()
    queue.appendleft(source)
    cost = [inf] * len(graph)
    cost[source] = 0
    visited = [False] * len(graph)
    while len(queue):
        u = queue.popleft()
        for v in range(len(graph)):
            if graph[u][v] != -1 and not visited[v]:
                cost[v] = min(cost[v], cost[u] + graph[v][u])
                if graph[u][v] == 0:
                    queue.appendleft(v)
                else:
                    queue.append(v)
                visited[u] = True
    return cost[-1]


graph = [[-1, 1, 0, 1, -1, -1, -1, -1],
         [1, -1, 1, -1, 0, 0, -1, -1],
         [0, 1, -1, -1, -1, 1, -1, -1],
         [1, -1, -1, -1, -1, -1, 1, -1],
         [-1, 0, -1, -1, -1, -1, -1, 1],
         [-1, 0, 1, -1, -1, -1, 1, -1],
         [-1, -1, -1, 1, -1, 1, -1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1], ]
print(edges_01(graph, 0))
