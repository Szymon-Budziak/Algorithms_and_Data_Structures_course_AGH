# Dany jest nieskierowany graf G = (V, E) oraz dwa wierzchołki, s i t. Proszę zaimplementować funkcję:
# def paths(G, s, t):
#     ...
# która zwraca liczbę krawędzi e takich, że e występuje na pewnej najkrótszej ścieżce z s do t. Graf
# dany jest jako lista list sąsiedztwa w postaci [(v0, w0), (v1, w1), ...], gdzie: v[i] to numer
# wierzchołka, w[i] to waga krawędzi prowadzącej do wierzchołka v[i]. Wagi krawędzi są dodatnie.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
# użytego algorytmu.
from Exercise_3_tests import runtests
from queue import PriorityQueue
from math import inf


def relax(u, v, distance):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        return True
    return False


def dijkstra_algorithm(graph, source):
    queue = PriorityQueue()
    queue.put((0, source))
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    return distance


def paths(G, s, t):
    edges = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            edges.append((i, G[i][j][0], G[i][j][1]))
    distance_from_s = dijkstra_algorithm(G, s)
    distance_from_t = dijkstra_algorithm(G, t)
    count = 0
    if distance_from_s[t] == inf or distance_from_t[s] == inf:
        return 0
    for i in range(len(edges)):
        if (distance_from_s[edges[i][0]] + distance_from_t[edges[i][1]] + edges[i][2] == distance_from_s[t] or
                distance_from_s[edges[i][0]] + distance_from_t[edges[i][1]] + edges[i][2] == distance_from_t[s]):
            count += 1
    return count


runtests(paths)
