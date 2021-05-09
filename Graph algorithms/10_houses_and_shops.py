# We have a map of city where are houses and shops. There are also roads (each of length 1)
# that connect a house with a house or a house with a shop. We have to find for each home
# the distance to the nearest shop.
from queue import Queue
from math import inf


def bfs(graph, source, shops):
    queue = Queue()
    visited = [False] * len(graph)
    distances = [inf] * len(graph)
    queue.put(source)
    visited[source] = True
    while not queue.empty():
        u = queue.get()
        flag = False
        if u in shops:
            distances[u] = 0
            flag = True
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
            if v in shops and u not in shops:
                distances[u] = 1
                flag = True
        if not flag:
            min_distance = inf
            for i in graph[u]:
                min_distance = min(min_distance, distances[i])
                distances[u] = min_distance + 1
    return distances


def houses_and_shops(roads, shops):
    max_vertex = 0
    for i in range(len(roads)):
        max_vertex = max(max_vertex, max(roads[i]))
    graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(roads)):
        graph[roads[i][0]].append(roads[i][1])
        graph[roads[i][1]].append(roads[i][0])
    return bfs(graph, 0, shops)


roads = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [2, 7], [3, 6], [3, 8],
         [4, 8], [4, 5], [5, 7], [6, 7], [8, 9], [9, 10], [9, 11], [10, 13], [11, 12], [12, 13]]
shops = [2, 3, 9]
print(houses_and_shops(roads, shops))
