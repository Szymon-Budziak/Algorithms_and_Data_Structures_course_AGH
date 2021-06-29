# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , |E|} (wagi krawędzi są
# parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o
# najmniejszej sumie wag, która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki
# nie ma to zwracamy inf).
from queue import PriorityQueue
from math import inf


def find_path(graph, s, t):
    graph.repeated_numbers()
    queue = PriorityQueue()
    queue.put((0, inf, s))
    visited = [False] * (len(graph))
    best_distance = inf
    while not queue.empty():
        dist, weight, u = queue.get()
        if u == t:
            best_distance = min(dist, best_distance)
        for i in range(len(graph)):
            if graph[i][0] == u and not visited[i]:
                if graph[i][2] < weight:
                    queue.put((dist + graph[i][2], graph[i][2], graph[i][1]))
                    visited[i] = True
    return best_distance


graph = [(0, 1, 15), (0, 2, 2), (0, 3, 6), (1, 2, 14), (1, 4, 7), (2, 5, 3), (2, 6, 4), (3, 7, 2),
         (4, 8, 6), (5, 9, 2), (6, 8, 5), (7, 9, 8), (8, 10, 5), (9, 10, 1)]
s = 0
t = 10
print(find_path(graph, s, t))
