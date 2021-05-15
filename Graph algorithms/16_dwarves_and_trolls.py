# Let's imagine an underground labyrinth composed of huge caves connected by narrow corridors. In one
# of caves, the dwarves have built their settlement and each of the other caves has a number of trolls.
# The dwarves want to plan their defense in case of being attacked by trolls. They intend to sneak in
# and plant an explosive load in one of the corridors, so that the trolls living beyond this corridor
# have no path to reach the dwarven settlement. Which of the corridors should be blown up to cut off
# trolls' access to the dwarven settlement.
from math import inf
from queue import Queue


def dfs(graph, source, visited, parents, time_visit, time, low):
    visited[source] = True
    time_visit[source] = time
    time += 1
    low[source] = time_visit[source]
    for v in graph[source]:
        if not visited[v]:
            parents[v] = source
            dfs(graph, v, visited, parents, time_visit, time, low)
            low[source] = min(low[source], low[v])
        elif parents[source] != v:
            low[source] = min(low[source], time_visit[v])


def bfs(graph, start, source, trolls):
    queue = Queue()
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    visited[start] = True
    trolls_number = trolls[source]
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                trolls_number += trolls[v]
                queue.put(v)
                visited[v] = True
    return trolls_number


def dwarves_and_trolls(graph, trolls, source):
    visited = [False] * len(graph)
    time_visit = [0] * len(graph)
    low = [inf] * len(graph)
    parents = [None] * len(graph)
    time = 0
    bridges = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, source, visited, parents, time_visit, time, low)
    for i in range(len(graph)):
        if time_visit[i] == low[i] and parents[i] is not None:
            bridges.append((parents[i], i))
    max_trolls, corridor = 0, 0
    for bridge in bridges:
        trolls_number = bfs(graph, bridge[0], bridge[1], trolls)
        if trolls_number > max_trolls:
            max_trolls = trolls_number
            corridor = bridge
    return corridor


graph = [[1, 2, 3, 4], [0, 2, 5, 6], [0, 1, 3], [0, 2], [0, 9, 10], [1, 7, 8],
         [1], [5, 8], [5, 7], [4, 10], [4, 9, 11], [10]]
trolls = [inf, 2, 8, 7, 17, 4, 13, 3, 12, 3, 1, 11]
print(dwarves_and_trolls(graph, trolls, 0))
