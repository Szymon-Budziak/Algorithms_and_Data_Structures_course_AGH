# There is a civil war going on in one country. As part of the sabotage, the rebels want to prevent
# telegraphic communication from A to B. We are given a list of cities and telegraph lines between them.
# Telegraphic lines are directed. Each line has a cost associated with destroying it. We want to select
# a set of connections to be destroyed with a total minimum cost. We are not only interested in the cost,
# but also which specific telegraph lines are to be destroyed.
from queue import Queue
from math import inf
from copy import deepcopy


def dfs(graph, source, visited, S):
    visited[source] = True
    S.append(source)
    for i in range(len(graph)):
        if visited[i] is False and graph[source][i] != 0:
            dfs(graph, i, visited, S)


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


def sabotage(graph, A, B):
    new_graph = deepcopy(graph)
    parent = [None] * len(new_graph)
    max_flow = 0
    s, t = A, B
    while bfs(new_graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, new_graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            new_graph[u][v] -= current_flow
            new_graph[v][u] += current_flow
            v = parent[v]
    S = []
    T = []
    visited = [False] * len(graph)
    dfs(new_graph, 0, visited, S)
    for i in range(len(new_graph)):
        if i not in S:
            T.append(i)
    edges = []
    for i in range(len(S)):
        for j in range(len(T)):
            if graph[S[i]][T[j]] != 0:
                edges.append((S[i], T[j]))
    return max_flow, edges


graph = [[0, 8, 5, 0, 0, 0, 0, 0],
         [0, 0, 0, 4, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 0, 0],
         [0, 0, 0, 0, 0, 0, 2, 0],
         [0, 0, 0, 3, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 6],
         [0, 0, 0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 0, 0, 0]]
A, B = 0, 7
print(sabotage(graph, A, B))
