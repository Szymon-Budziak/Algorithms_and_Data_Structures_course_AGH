# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można
# osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf
# zawiera dobry początek.
from math import inf


def dfs(graph, visited, time_visit, source, time):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, visited, time_visit, v, time)
    time[0] += 1
    time_visit[source] = time[0]


def dfs_check(graph, visited, source):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs_check(graph, visited, v)


def mother_vertex(graph):
    visited = [False] * len(graph)
    time_visit = [inf] * len(graph)
    time = [0]
    time_visit[0] = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, visited, time_visit, i, time)
    for i in range(len(graph)):
        visited[i] = False
    for i in range(len(time_visit)):
        if time_visit[i] == len(time_visit):
            dfs_check(graph, visited, i)
            for j in range(len(time_visit)):
                if visited[j] == False:
                    return False
            return True


graph = [[1],
         [2],
         [0, 3],
         [4],
         []]
print(mother_vertex(graph))
