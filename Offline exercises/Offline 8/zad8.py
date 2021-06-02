from copy import deepcopy
from math import inf


def dijkstra_algorithm(G, source):
    visited = [False] * len(G)
    distance = [inf] * len(G)
    distance[source] = 0
    parent = [None] * len(G)
    parent[source] = source
    minimal_cycle = inf
    actual_edge = None
    for i in range(len(G)):
        actual_distance = inf
        actual_index = -1
        for j in range(len(G)):
            if not visited[j] and actual_distance > distance[j]:
                actual_distance = distance[j]
                actual_index = j
        visited[actual_index] = True
        for j in range(len(G)):
            if G[actual_index][j] > -1:
                if distance[j] > distance[actual_index] + G[actual_index][j]:
                    distance[j] = distance[actual_index] + G[actual_index][j]
                    parent[j] = actual_index
                if j != parent[actual_index] and visited[j]:
                    if minimal_cycle > distance[j] + distance[actual_index] + G[actual_index][j]:
                        minimal_cycle = distance[j] + distance[actual_index] + G[actual_index][j]
                        actual_edge = (j, actual_index)
    if actual_edge is None:
        return None, None
    possible_cycle = []
    vertex_1 = actual_edge[0]
    while vertex_1 != parent[vertex_1]:
        possible_cycle.append(vertex_1)
        vertex_1 = parent[vertex_1]
    vertex_2 = actual_edge[1]
    while vertex_2 != parent[vertex_1]:
        possible_cycle.insert(0, vertex_2)
        vertex_2 = parent[vertex_2]
    possible_cycle.insert(0, vertex_2)
    return minimal_cycle, possible_cycle


def min_cycle(G):
    minimal_distance = minimal_length = inf
    best_result = []
    for i in range(len(G)):
        distance, actual_result = dijkstra_algorithm(G, i)
        if distance is not None:
            if minimal_distance > distance or (minimal_distance == distance and len(actual_result) < minimal_length):
                minimal_distance = distance
                best_result = actual_result
                minimal_length = len(actual_result)
    return best_result


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
