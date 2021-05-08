# Given set of ranges [ai, bi]. Two ranges can be combined if they have exactly one
# common point. Find algorithm that checks if it is possible to get range [a, b] by
# combining ranges together.


def dfs(graph, start, end, visited):
    visited[start] = True
    for v in graph[start]:
        if v == end:
            return True
        elif not visited[v]:
            return dfs(graph, v, end, visited)
    return False


def find_range(ranges, source):
    max_vertex = 0
    for i in range(len(ranges)):
        max_vertex = max(max_vertex, max(ranges[i]))
    graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(ranges)):
        graph[ranges[i][0]].append(ranges[i][1])
        graph[ranges[i][1]].append(ranges[i][0])
    visited = [False] * len(graph)
    return dfs(graph, source[0], source[1], visited)


ranges = [[1, 3], [2, 3], [4, 5], [5, 7], [0, 6], [6, 7], [0, 2], [3, 4], [8, 9]]
interval = [0, 1]
print(find_range(ranges, interval))
