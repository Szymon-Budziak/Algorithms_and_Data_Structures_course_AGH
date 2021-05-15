# We have a layout of dominoes. We have it as a list of pairs [a, b]. If we knock over block a, block
# b will also fall over. Find the minimum number of blocks that need to be knocked over by hand so that
# all dominoes are downed.


def DFSUtil(graph, source, visited, stack):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFSUtil(graph, v, visited, stack)
        stack.append(source)


def dfs(graph, source, visited, scc, index):
    visited[source] = True
    scc[index].append(source)
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, scc, index)


def DFS(graph, source, visited):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFS(graph, v, visited)


def transpose_graph(graph, new_graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)


def domino(graph, source):
    max_vertex = 0
    for i in range(len(graph)):
        max_vertex = max(max_vertex, max(graph[i]))
    new_graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(graph)):
        new_graph[graph[i][0]].append(graph[i][1])
    visited = [False] * len(new_graph)
    stack = []
    for i in range(len(new_graph)):
        if not visited[i]:
            DFSUtil(new_graph, i, visited, stack)
    modified_graph = [[] for _ in range(len(new_graph))]
    transpose_graph(new_graph, modified_graph)
    for i in range(len(new_graph)):
        visited[i] = False
    index = 0
    scc = [[] for _ in range(max_vertex)]
    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(modified_graph, u, visited, scc, index)
            index += 1
    i = 0
    while i < len(scc):
        if len(scc[i]) == 0:
            del (scc[i])
        else:
            i += 1
    for i in range(len(scc)):
        if len(scc[i]) > 1:
            for j in range(len(graph)):
                if graph[j][0] in scc[i]:
                    graph[j][0] = scc[i][0]
                if graph[j][1] in scc[i]:
                    graph[j][1] = scc[i][0]
    i = 0
    while i < len(graph):
        if graph[i][0] == graph[i][1]:
            graph.remove(graph[i])
        else:
            i += 1
    for i in range(len(graph)):
        for j in range(len(scc)):
            if graph[i][0] in scc[j]:
                graph[i][0] = j
                break
    for i in range(len(graph)):
        for j in range(len(scc)):
            if graph[i][1] in scc[j]:
                graph[i][1] = j
                break
    max_vertex = 0
    for i in range(len(graph)):
        max_vertex = max(max_vertex, max(graph[i]))
    last_graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(graph)):
        last_graph[graph[i][0]].append(graph[i][1])
    visit = [False] * (max_vertex + 1)
    count = 0
    for i in range(len(graph)):
        if not visit[i]:
            count += 1
            DFS(last_graph, i, visit)
    return count


graph = [[0, 1], [1, 2], [2, 3], [3, 1], [3, 5], [4, 2], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]
print(domino(graph, 0))
