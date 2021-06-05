# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi
# łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna).
# Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V, zamieniając się za kierownicą
# w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować
# algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała
# jak najmniej kilometrów.
from math import inf
from queue import PriorityQueue


def relax(new_graph, vertex, u, idx, new_idx, dist, parent):
    if new_graph[vertex][idx] > new_graph[u][idx] + dist and idx == 0:
        new_graph[vertex][idx] = new_graph[u][idx] + dist
        new_graph[vertex][new_idx] = new_graph[u][new_idx]
        parent[vertex] = u
        return True
    elif idx == 1:
        new_graph[vertex][idx] = new_graph[u][idx] + dist
        new_graph[vertex][new_idx] = new_graph[u][new_idx]
        parent[vertex] = u
        return True
    return False


def dijkstra_algorithm(graph, new_graph, first, start, finish):
    queue = PriorityQueue()
    new_graph[0][0] = 0
    new_graph[0][1] = 0
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    queue.put((0, first, start))
    while not queue.empty():
        distance, idx, u = queue.get()
        for v in graph[u]:
            vertex, dist = v
            if not visited[vertex]:
                if idx == 0:
                    new_idx = 1
                else:
                    new_idx = 0
                if relax(new_graph, vertex, u, idx, new_idx, dist, parent):
                    queue.put((new_graph[vertex][0], new_idx, vertex))
        visited[u] = True
    return new_graph[finish][0], parent


def shortest_path(graph, start, finish):
    new_graph = [[inf] * 2 for _ in range(len(graph))]
    result_1, parent_1 = dijkstra_algorithm(graph, new_graph, 0, start, finish)
    for i in range(len(new_graph)):
        new_graph[i][0], new_graph[i][1] = inf, inf
    result_2, parent_2 = dijkstra_algorithm(graph, new_graph, 1, start, finish)
    tour = []
    if result_1 < result_2:
        while finish != parent_1[start]:
            tour.append(finish)
            finish = parent_1[finish]
        tour.reverse()
    else:
        while finish != parent_2[start]:
            tour.append(finish)
            finish = parent_2[finish]
        tour.reverse()
    return tour


graph = [[(1, 4), (2, 1), (3, 5)],
         [(0, 1), (4, 2)],
         [(0, 1), (5, 8), (6, 7)],
         [(0, 5), (5, 7)],
         [(1, 2), (7, 10)],
         [(2, 8), (3, 7), (8, 3)],
         [(2, 7), (7, 6)],
         [(4, 10), (6, 6), (9, 11)],
         [(5, 3), (9, 9)],
         [(7, 11), (8, 9)]]

start = 0
finish = len(graph) - 1
print(shortest_path(graph, start, finish))
