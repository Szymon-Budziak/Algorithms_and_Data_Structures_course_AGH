# Given a list of edges of the tree (not necessary binary) and highlighted vertex - the root.
# Each vertex creates its own sub-tree. For each vertex, find the number of vertices in its subtree.


def dfs(graph, source, visited, vertices):
    visited[source] = True
    for v in graph[source]:
        if len(graph[source]) == 1:
            vertices[source] += 1
        if not visited[v]:
            dfs(graph, v, visited, vertices)
            count = 0
            for i in graph[source]:
                if visited[i]:
                    count += 1
            if count == len(graph[source]):
                for i in graph[source]:
                    if vertices[i] > 0:
                        vertices[source] += vertices[i]
                vertices[source] += 1


def subtree_size(edges, source):
    max_vertex = 0
    for i in range(len(edges)):
        max_vertex = max(max_vertex, max(edges[i]))
    graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])
    visited = [False] * len(graph)
    vertices = [0] * len(graph)
    dfs(graph, source, visited, vertices)
    return vertices


edges = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [5, 11], [5, 12], [7, 13],
         [7, 14], [8, 15], [9, 16], [9, 17], [11, 18], [11, 19], [11, 20], [12, 21]]
print(subtree_size(edges, 0))
