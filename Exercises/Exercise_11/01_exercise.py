# Mamy dany graf skierowany G = (V, E) oraz funkcję c: E → N opisującą przepustowość każdej krawędzi
# (liczbę jednostek towaru na godzinę, które mogą się przemieszczać krawędzią). Poza tym mamy dany zbiór
# wierzchołków-fabryk S = {s1, ..., sn} oraz zbiór wierzchołków-sklepów T = {t1, ..., tm}. Dla każdej
# fabryki s[i] znamy liczbę p[i] określającą ile jednostek towaru na godzinę fabryka może maksymalnie
# produkować. Jednocześnie dla każdego sklepu t[j] mamy liczbę q[j], która mówi ile jednostek towaru
# na godzinę musi do tego sklepu docierać. Proszę podać algorytm, który sprawdza, czy da się zapewnić,
# żeby do każdego sklepu docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga
# jednocześnie nie zmuszając żadnej fabryki do przekroczenia swoich możliwości produkcyjnych i nie
# przekraczając przepustowości żadnej z krawędzi.
from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]


def ford_fulkerson_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def factories_and_shops(graph, factories, shops):
    new_graph = [[0] * (len(graph) + 2) for _ in range(len(graph) + 2)]
    for i in range(len(graph)):
        for j in range(len(graph)):
            new_graph[i][j] = graph[i][j]
    fact = len(graph) - 2
    shop = len(graph) - 1
    for i in range(len(factories)):
        new_graph[fact][factories[i][0]] = factories[i][1]
    for i in range(len(shops)):
        new_graph[shops[i][0]][shop] = shops[i][1]
    max_flow = ford_fulkerson_algorithm(new_graph, fact, shop)
    summary = 0
    for i in range(len(shops)):
        summary += shops[i][1]
    if summary == max_flow:
        return True
    return False


graph = [[0, 10, 0, 8, 0, 0, 0],
         [0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0],
         [0, 5, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 12],
         [0, 0, 0, 0, 11, 0, 6],
         [0, 0, 0, 0, 0, 0, 0]]
factories = [(1, 12), (0, 9)]
shops = [(4, 4), (6, 6)]
print(factories_and_shops(graph, factories, shops))
