# In addition to length of edges, the graph has vertex costs associated with it. Let us define the
# cost of the path as the sum of the costs of its edges and sum of the costs of the vertices (along
# with the ends). Find the cheapest paths between the starting vertex and all the other vertices.
# Find a solution for directed and undirected graph.
from queue import PriorityQueue
from math import inf


# Undirected graph - 1st solution:


def relax_undirected(u, v, distance):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        return True
    return False


def shortest_path_undirected(graph, vertices, source, finish):
    new_graph = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j][0], graph[i][j][1] + vertices[graph[i][j][0]]) not in new_graph[i]:
                new_graph[i].append((graph[i][j][0], graph[i][j][1] + vertices[graph[i][j][0]]))
            if (i, graph[i][j][1] + vertices[i]) not in new_graph[graph[i][j][0]]:
                new_graph[graph[i][j][0]].append((i, graph[i][j][1] + vertices[i]))
    queue = PriorityQueue()
    queue.put((vertices[source], source))
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = vertices[source]
    while not queue.empty():
        dist, u = queue.get()
        for v in new_graph[u]:
            if not visited[v[0]] and relax_undirected(u, v, distance):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    return distance[finish]


# Undirected graph - 2nd solution:


def shortest_path_undirected_2(graph, vertices, source, finish):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j][1] += vertices[i] / 2 + vertices[graph[i][j][0]] / 2
    queue = PriorityQueue()
    queue.put((vertices[source] / 2, source))
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = vertices[source] / 2
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax_undirected(u, v, distance):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    distance[finish] += vertices[finish] / 2
    return distance[finish]


# Directed graph:


def relax_directed(graph, u, v, distance):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        return True
    return False


def shortest_path_directed(graph, vertices, source, finish):
    queue = PriorityQueue()
    queue.put((vertices[source], source))
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = vertices[source]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                graph[i][j] += vertices[j]
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph)):
            if graph[u][v] != 0 and not visited[v]:
                if relax_directed(graph, u, v, distance):
                    queue.put((dist + graph[u][v], v))
        visited[u] = True
    return distance[finish]


undirected_graph = [[[1, 4], [2, 3]],
                    [[0, 4], [3, 6]],
                    [[0, 3], [3, 1], [4, 4], [6, 20]],
                    [[1, 6], [2, 1], [5, 3]],
                    [[2, 4], [6, 5]],
                    [[3, 3], [6, 5]],
                    [[2, 20], [4, 5], [5, 5]]]
undirected_graph_vertices = [5, 4, 1, 2, 5, 4, 3]
print(shortest_path_undirected(undirected_graph, undirected_graph_vertices, 0, 6))
print(shortest_path_undirected_2(undirected_graph, undirected_graph_vertices, 0, 6))

directed_graph = [[0, 2, 6, 4, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 5, 7, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 2, 0, 0],
                  [0, 0, 0, 0, 0, 2, 0, 0, 5, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                  [0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
directed_graph_vertices = [4, 5, 2, 6, 3, 1, 9, 1, 2, 4]
print(shortest_path_directed(directed_graph, directed_graph_vertices, 0, 9))
