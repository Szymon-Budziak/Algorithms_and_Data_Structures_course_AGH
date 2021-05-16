# Henry the sailor lives on island of an archipelago. All islands including archipelago are so small that
# they can be represented as points in R^2 space. The positions of all islands are given as the sequence
# W = ((x1, y1), ..., (xn, yn)). Henry lives on the island (x1, y1), but he wants to move to the island
# (xn, yn). Normally every day he can sail to an island that is at most Z distance (in standard Euclidean
# distance). He can also sail up to 2Z distance, provided that he will rest all the next day. Henry
# always must stay overnight on some island. Find minimum number of days Henry needs to get to his
# target island (or states that it is impossible).
from math import sqrt, inf
from queue import Queue


def count_distance(point1, point2):
    x = abs(point1[0] - point2[0])
    y = abs(point1[1] - point2[1])
    return sqrt(x ** 2 + y ** 2)


def the_sailr_Henry(W, Z, start):
    graph = [[] for _ in range(len(W))]
    for i in range(len(W)):
        for j in range(len(W)):
            if i != j:
                distance = count_distance(W[i], W[j])
                if distance <= Z:
                    graph[i].append([j, 1])
                elif distance > Z and distance <= 2 * Z:
                    graph[i].append([j, 2])
    queue = Queue()
    queue.put([start, 0])
    visited = [False] * len(graph)
    visited[start] = True
    parents = [-1] * len(W)
    DP = [inf] * len(W)
    DP[start] = 0
    while not queue.empty():
        u, dist = queue.get()
        if dist == 2:
            while dist == 2:
                dist -= 1
                queue.put((u, dist))
                u, dist = queue.get()
        for v in graph[u]:
            if not visited[v[0]]:
                parents[v[0]] = u
                if v[1] == 1:
                    DP[v[0]] = min(DP[v[0]], DP[parents[v[0]]]) + 1
                else:
                    DP[v[0]] = min(DP[v[0]], DP[parents[v[0]]]) + 2
                visited[v[0]] = True
                queue.put(v)
    if DP[-1] != inf:
        i = len(parents) - 1
        while i != -1:
            print(W[i], end=" ")
            i = parents[i]
        print()
        return DP[-1]
    return False


Z = 1
W = [(0, 0), (0, 1), (2, 1), (1, 3), (2, 5), (3, 2), (5, 2), (4, 4), (3, 4), (4, 1), (2, 4), (5, 5)]
print(the_sailr_Henry(W, Z, 0))
