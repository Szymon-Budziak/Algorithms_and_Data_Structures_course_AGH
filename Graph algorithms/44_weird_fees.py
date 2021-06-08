# Public transport in a certain city is quite strangely organized. There is a separate charge for
# each section between two stations. However, the total cost incurred from the start of the journey
# is subtracted from this amount (if it is negative you just pay nothing). We are given a connection
# graph in any representation (undirected, weighted). Find the minimum cost of driving this route.
from queue import PriorityQueue
from math import inf


def relax(u, v, cost):
    if v[1] > cost[u] and v[1] < cost[v[0]]:
        cost[v[0]] = v[1]
        return True
    elif v[1] < cost[u] and cost[u] < cost[v[0]]:
        cost[v[0]] = cost[u]
        return True
    return False


def weird_fees(graph, start):
    queue = PriorityQueue()
    cost = [inf] * len(graph)
    cost[start] = 0
    visited = [False] * len(graph)
    queue.put((0, start))
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, cost):
                queue.put((cost[v[0]], v[0]))
        visited[u] = True
    return cost


graph = [[(1, 60), (3, 120), (4, 40)],
         [(0, 60), (2, 80)],
         [(1, 80), (4, 100), (7, 70)],
         [(0, 120), (6, 150)],
         [(0, 40), (2, 100), (5, 90)],
         [(4, 90), (6, 60)],
         [(3, 150), (5, 60), (7, 90)],
         [(2, 70), (6, 90)]]
print(weird_fees(graph, 0))
