# The diameter of tree is the distance between its vertices that distance from each other is
# the most. Find algorithm that, assuming a tree (not necessary a binary) presented as a list
# of edges will return its diameter.


def dfs(graph, source, visited, vertices):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            vertices[v] = vertices[source] + 1
            dfs(graph, v, visited, vertices)


def diameter(edges):
    max_vertex = 0
    for i in range(len(edges)):
        max_vertex = max(max_vertex, max(edges[i]))
    graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])
    vertices = [0] * len(graph)
    visited = [False] * len(graph)
    dfs(graph, 0, visited, vertices)
    max_vert = vertices.index((max(vertices)))
    for i in range(len(graph)):
        vertices[i] = 0
        visited[i] = False
    dfs(graph, max_vert, visited, vertices)
    distance = max(vertices)
    return distance


edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [5, 10], [7, 11],
         [7, 12], [7, 13], [8, 14], [8, 15], [11, 16], [11, 17], [13, 18], [16, 19], [19, 20]]
print(diameter(edges))
