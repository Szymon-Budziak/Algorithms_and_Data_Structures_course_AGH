# A certain land consists of islands between which there are air, ferry and bridge connections.
# There is at most one type of connection between two islands. The cost of the overflight from
# island to island costs 8B, ferry crossing costs 5B and for bridge crossing you have to pay 1B.
# Find route from island A to island B which on each subsequent island changes the transport
# to a different one and minimizes the cost of the trip. We are given an array G that specifies
# the cost of connections between the islands. Value 0 means that there is no direct connection.
# Implement islands(G, A, B) function that returns the minimum travels cost from island A
# to island B. If such a route doesn't exist, the function should return None.
from queue import PriorityQueue
from math import inf


def relax(distance, u, v, cost, queue):
    if cost == 1:
        if distance[u][0] + cost < distance[v][1]:
            distance[v][1] = distance[u][0] + cost
            queue.put((distance[v][1], v))
        if distance[u][0] + cost < distance[v][2]:
            distance[v][2] = distance[u][0] + cost
            queue.put((distance[v][2], v))
    elif cost == 5:
        if distance[u][1] + cost < distance[v][0]:
            distance[v][0] = distance[u][1] + cost
            queue.put((distance[v][0], v))
        if distance[u][1] + cost < distance[v][2]:
            distance[v][2] = distance[u][1] + cost
            queue.put((distance[v][2], v))
    else:
        if distance[u][2] + cost < distance[v][0]:
            distance[v][0] = distance[u][2] + cost
            queue.put((distance[v][0], v))
        if distance[u][1] + cost < distance[v][1]:
            distance[v][1] = distance[u][1] + cost
            queue.put((distance[v][1], v))


def islands(G, A, B):
    distance = [[inf] * 3 for _ in range(len(G))]
    for i in range(3):
        distance[A][i] = 0
    queue = PriorityQueue()
    queue.put((0, A))
    visited = [False] * len(G)
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(G)):
            if not visited[v] and G[u][v] != 0:
                relax(distance, u, v, G[u][v], queue)
        visited[u] = True
    return min(distance[B])


G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]
print(islands(G, 5, 2))
