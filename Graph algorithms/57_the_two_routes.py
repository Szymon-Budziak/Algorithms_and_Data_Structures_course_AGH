# In Absurdistan, there are n towns (numbered 1 through n) and m bidirectional railways. There is also
# an absurdly simple road network — for each pair of different towns x and y, there is a bidirectional
# road between towns x and y if and only if there is no railway between them. Travelling to a different
# town using one railway or one road always takes exactly one hour. A train and a bus leave town 1 at
# the same time. They both have the same destination, town n, and don't make any stops on the way
# (but they can wait in town n). The train can move only along railways and the bus can move only along
# roads. You've been asked to plan out routes for the vehicles; each route can use any road/railway
# multiple times. One of the most important aspects to consider is safety — in order to avoid
# accidents at railway crossings, the train and the bus must not arrive at the same town (except
# town n) simultaneously. Under these constraints, what is the minimum number of hours needed for
# both vehicles to reach town n (the maximum of arrival times of the bus and the train)? Note, that bus
# and train are not required to arrive to the town n at the same moment of time, but are allowed to do so.
from queue import Queue


def the_two_routes(n, m, edges):
    graph = [[0] * n for _ in range(n)]
    for i in range(m):
        u, v = edges[i]
        graph[u][v] = graph[v][u] = 1
    queue = Queue()
    visited = [False] * n
    visited[0] = True
    time = [-1] * n
    time[0] = 0
    queue.put(0)
    if graph[0][-1] == 1:
        for i in range(n):
            for j in range(n):
                graph[i][j] = 1 - graph[i][j]
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] == 1:
                time[v] = time[u] + 1
                visited[v] = True
                queue.put(v)
    return time[-1]


n = 4
m = 5
edges = [(0, 2), (1, 0), (2, 3), (3, 1), (1, 2)]
print(the_two_routes(n, m, edges))
