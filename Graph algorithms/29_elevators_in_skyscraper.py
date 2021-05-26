# The skyscraper has 7 floors and n elevators, but there are no stairs. Each elevator has a list of
# the floors it travels to and the speed in seconds per floor. We are on the i floor and we want to get
# to the j floor. What is the minimum time in seconds that we have to spend in elevators to get there?
from queue import PriorityQueue
from math import inf


def relax(graph, u, v, distance, parent):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        parent[v] = u
        return True
    return False


def elevators_in_skyscraper(floors, start, end):
    graph = [[] for _ in range(len(floors) + 1)]
    for i in range(len(floors)):
        for j in floors[i][0]:
            graph[i].append((j, (j - i) * floors[i][1]))
            graph[j].append((i, (j - i) * floors[i][1]))
    queue = PriorityQueue()
    distance = [inf] * len(graph)
    counter = len(graph)
    queue.put((0, start))
    while not queue.empty() and counter > 0:
        dist, v = queue.get()
        if dist < distance[v]:
            counter -= 1
            distance[v] = dist
            for edge in graph[v]:
                u, length = edge
                queue.put((dist + length, u))
    return distance[end]


floors = [[[1, 2, 5], 3],
          [[3, 4, 5], 5],
          [[3, 6], 2],
          [[4], 3],
          [[5], 1],
          [[6], 4]]
print(elevators_in_skyscraper(floors, 1, 5))
