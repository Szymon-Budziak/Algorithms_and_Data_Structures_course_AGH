# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
# miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci
# (x, y, c), gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na grupki tak, żeby
# każda grupka mogła przebyć trasę bez rozdzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
# dostali się z A do B.
from queue import PriorityQueue
from math import inf, ceil


def relax(graph, u, v, distance, parent):
    actual_distance = min(distance[u], graph[u][v])
    if actual_distance > distance[v]:
        distance[v] = actual_distance
        parent[v] = u
        return True
    return False


def tour_guide(graph, city_a, city_b, K):
    max_vertex = 0
    max_weight = 0
    for i in range(len(graph)):
        max_vertex = max(max_vertex, graph[i][0], graph[i][1])
        max_weight = max(max_weight, graph[i][2])
    new_graph = [[0] * (max_vertex + 1) for _ in range(max_vertex + 1)]
    for i in range(len(graph)):
        new_graph[graph[i][0]][graph[i][1]] = graph[i][2]
        new_graph[graph[i][1]][graph[i][0]] = graph[i][2]
    max_weight += 1
    queue = PriorityQueue()
    queue.put((max_weight, city_a))
    visited = [False] * len(new_graph)
    distance = [0] * len(new_graph)
    distance[city_a] = inf
    parent = [None] * len(new_graph)
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(new_graph[u])):
            if not visited[v] and new_graph[u][v] != 0:
                if relax(new_graph, u, v, distance, parent):
                    queue.put((max_weight - distance[v], v))
        visited[u] = True
    min_weight = inf
    tour = []
    while city_b is not None:
        tour.append(city_b)
        min_weight = min(min_weight, distance[city_b])
        city_b = parent[city_b]
    number_of_groups = ceil(K / min_weight)
    tour.reverse()
    return number_of_groups, tour


graph = [(0, 1, 12), (0, 2, 10), (1, 3, 11), (1, 4, 7), (2, 4, 8), (2, 6, 14),
         (3, 5, 8), (4, 6, 8), (5, 7, 11), (6, 7, 6)]
city_a = 0
city_b = 7
print(tour_guide(graph, city_a, city_b, 20))
