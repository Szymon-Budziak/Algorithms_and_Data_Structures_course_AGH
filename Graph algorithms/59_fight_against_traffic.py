# Little town Nsk consists of n junctions connected by m bidirectional roads. Each road connects two
# distinct junctions and no two roads connect the same pair of junctions. It is possible to get from
# any junction to any other junction by these roads. The distance between two junctions is equal to
# the minimum possible number of roads on a path between them. In order to improve the transportation
# system, the city council asks mayor to build one new road. The problem is that the mayor has just
# bought a wonderful new car and he really enjoys a ride from his home, located near junction s to
# work located near junction t. Thus, he wants to build a new road in such a way that the distance
# between these two junctions won't decrease. You are assigned a task to compute the number of pairs
# of junctions that are not connected by the road, such that if the new road between these two
# junctions is built the distance between s and t won't decrease.
from queue import Queue
from math import inf


def dijkstra(graph, source):
    queue = Queue()
    queue.put((0, source))
    visited = [False] * len(graph)
    visited[source] = True
    distance = [inf] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v] and distance[v] > distance[u] + 1:
                distance[v] = distance[u] + 1
                queue.put((dist + 1, v))
        visited[u] = True
    return distance


def fight_against_traffic(n, m, s, t, T):
    s -= 1
    t -= 1
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v = T[i]
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    distance_s = dijkstra(graph, s)
    distance_t = dijkstra(graph, t)
    D = distance_s[t]
    not_connected_junctions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if j not in graph[i] and distance_s[i] + distance_t[j] + 1 >= D and distance_s[j] + distance_t[i] + 1 >= D:
                not_connected_junctions += 1
    return not_connected_junctions


n = 5
m = 6
s = 1
t = 5
T = [(1, 2), (1, 3), (1, 4), (4, 5), (3, 5), (2, 5)]
print(fight_against_traffic(n, m, s, t, T))
