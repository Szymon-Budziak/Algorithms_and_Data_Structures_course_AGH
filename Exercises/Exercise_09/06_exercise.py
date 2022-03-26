# Mamy dany graf G = (V, E) z wagami w: E → N-{0} (dodatnie liczby naturalne). Chcemy znalezc scieżkę
# z wierzchołka u do v tak, by iloczyn wag był minimalny.
from queue import PriorityQueue
from math import inf, log10


def relax(source, adj, distance, parent):
    if distance[adj[0]] > distance[source] + log10(adj[1]):
        distance[adj[0]] = distance[source] + log10(adj[1])
        parent[adj[0]] = source
        return True
    return False


def minimum_product(graph, u, v):
    queue = PriorityQueue()
    queue.put((0, u))
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[u] = 0
    while not queue.empty():
        dist, vertex = queue.get()
        for adj in graph[vertex]:
            if not visited[adj[0]] and relax(vertex, adj, distance, parent):
                queue.put((distance[adj[0]], adj[0]))
        visited[vertex] = True
    path = []
    while v != parent[u]:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path


graph = [[(1, 20), (2, 30)],
         [(0, 20), (3, 12), (4, 11)],
         [(0, 30), (3, 18), (5, 2700)],
         [(1, 12), (2, 18), (8, 22), ],
         [(1, 11), (6, 15)],
         [(2, 2700), (7, 19), (8, 3)],
         [(4, 15), (8, 8)],
         [(5, 19)],
         [(3, 22), (5, 3), (6, 8)]]

u, v = 0, 7
print(minimum_product(graph, u, v))
