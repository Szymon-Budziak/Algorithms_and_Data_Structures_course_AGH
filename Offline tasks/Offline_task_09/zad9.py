from copy import deepcopy
from queue import PriorityQueue
from math import inf


def relax(u, v, dist, distance, parent):
    if distance[v[0]] < min(v[1], dist):
        distance[v[0]] = min(v[1], dist)
        parent[v[0]] = u
        return True
    return False


def max_extending_path(G, s, t):
    queue = PriorityQueue()
    distance = [-1] * len(G)
    distance[s] *= inf
    visited = [False] * len(G)
    parent = [None] * len(G)
    queue.put((distance[s], s))
    while not queue.empty():
        dist, u = queue.get()
        dist *= -1
        for v in G[u]:
            if not visited[v[0]] and parent[u] != v[0]:
                if relax(u, v, dist, distance, parent):
                    queue.put((-1 * distance[v[0]], v[0]))
        visited[u] = True
    path_length = 1
    i = t
    while i != s:
        path_length += 1
        i = parent[i]
    path = [0] * path_length
    for i in range(path_length):
        path[i] = t
        t = parent[t]
    path.reverse()
    return path


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
s = 0
t = 3
C = 3

GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)

if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)

capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
