# We get as input a directed acyclic graph (DAG - Directed Acyclic Graph) as a list of edges and pair
# of vertices s and t. Find how many possible paths is between s and t.


def dfs(graph, source, visited, DP):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DP[v] = 1
            dfs(graph, v, visited, DP)
        elif visited[v]:
            DP[v] += 1
            dfs(graph, v, visited, DP)


def paths_in_DAG(edges, start, end):
    max_vertex = 0
    for i in range(len(edges)):
        max_vertex = max(max_vertex, max(edges[i]))
    graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
    DP = [0] * len(graph)
    visited = [False] * len(graph)
    dfs(graph, start, visited, DP)
    return DP[end]


edges = [[0, 1], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 6], [6, 5]]
start = 1
end = 4
print(paths_in_DAG(edges, start, end))
