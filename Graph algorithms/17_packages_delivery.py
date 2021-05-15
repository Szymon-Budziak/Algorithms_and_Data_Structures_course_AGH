# Byteland is a land containing N cities and N-1 two-way roads. The road system creates a consistent
# graph. We are given a list of K cities to which we have to deliver packages and being able to start
# and finish the route in any city, find the minimum distance that we must travel to deliver all packages.


def dfs(graph, source, visited, vertices, parents):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            vertices[v] = vertices[source] + 1
            parents[v] = source
            dfs(graph, v, visited, vertices, parents)


def packages_delivery(graph, source):
    visited = [False] * len(graph)
    vertices = [0] * len(graph)
    parents = [0] * len(graph)
    parents[source] = -1
    dfs(graph, source, visited, vertices, parents)
    max_vert = vertices.index(max(vertices))
    for i in range(len(graph)):
        visited[i] = False
        vertices[i] = 0
        parents[i] = 0
    parents[max_vert] = -1
    dfs(graph, max_vert, visited, vertices, parents)
    start = vertices.index(max(vertices))
    diameter = [start]
    i = start
    while parents[i] != -1:
        diameter.append(parents[i])
        i = parents[i]
    route = 0
    for j in range(len(graph)):
        if j == start:
            continue
        if j not in diameter:
            route += 2
        else:
            route += 1
    return route


graph = [[1], [0, 2], [1, 3, 4], [2, 6], [2, 5], [4], [3, 7, 8], [6], [6, 9, 10, 11],
         [8], [8], [8, 12, 16], [11, 13, 14], [12, 15], [12], [13], [11, 17, 18], [16], [16]]
print(packages_delivery(graph, 0))
