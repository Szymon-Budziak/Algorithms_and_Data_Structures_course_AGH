# The eulerian path is one that passes through each edge exactly ones.


def dfs(graph, source, result):
    for i in range(len(graph)):
        if graph[source][i] == 1:
            graph[source][i], graph[i][source] = 0, 0
            dfs(graph, i, result)
    result.append(source)


def eulerian_path(graph):
    for i in range(len(graph)):
        edges = 0
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return False
    result = []
    dfs(graph, 0, result)
    result.reverse()
    return result


graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]

print(eulerian_path(graph))
