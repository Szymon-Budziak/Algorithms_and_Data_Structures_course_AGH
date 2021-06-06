# Let G = (V, E) be a directed graph. We say that u,v belong to the same strongly connected
# component if there are directed paths from u to v and from v to u.


def SCC(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    new_graph = [[] for _ in range(len(graph))]
    transpose_graph(graph, new_graph)
    for j in range(len(visited)):
        visited[j] = False
    result = [[] for _ in range(len(graph))]
    index = 0
    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(new_graph, u, visited, result, index)
            index += 1
    return result


def dfs(graph, source, visited, result, index):
    visited[source] = True
    result[index].append(source)
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result, index)


def DFSUtil(graph, source, visited, stack):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFSUtil(graph, v, visited, stack)
    stack.append(source)


def transpose_graph(graph, new_graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)


graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
print(SCC(graph))
