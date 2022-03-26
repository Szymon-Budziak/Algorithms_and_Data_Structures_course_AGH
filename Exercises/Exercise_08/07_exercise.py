# Dany jest graf G =(V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , |E|} (wagi krawędzi
# są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków x i y sprawdza, czy
# istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.


def dfs(graph, source, finish, visited, result):
    if source[1] == finish[0]:
        result[0] = True
        return True
    for i in range(len(graph)):
        if graph[i][0] == source[1] and source[2] > graph[i][2] and not visited[i]:
            idx = graph.index(source)
            visited[idx] = True
            dfs(graph, graph[i], finish, visited, result)


def decreasing_edges(edges, source, finish):
    max_vertex = 0
    for i in range(len(edges)):
        max_vertex = max(max_vertex, edges[i][0], edges[i][1])
    edges.sort(key=lambda x: x[2], reverse=True)
    possible_source = [source]
    visited = [False] * len(edges)
    result = [False]
    for i in range(len(edges)):
        if edges[i][0] == source[0] and edges[i][1] != source[1]:
            possible_source.append(edges[i])
    for i in range(len(possible_source)):
        dfs(edges, possible_source[i], finish, visited, result)
        if result[0]:
            return True
    return False


edges = [(0, 1, 12), (0, 2, 7), (1, 0, 12), (1, 3, 13), (1, 4, 9), (2, 0, 7), (2, 3, 2), (2, 5, 4),
         (3, 1, 13), (3, 2, 2), (3, 4, 10), (3, 5, 3), (4, 1, 9), (4, 3, 10), (4, 6, 10), (5, 2, 4),
         (5, 3, 3), (5, 6, 2), (6, 4, 10), (6, 5, 2)]
print(decreasing_edges(edges, edges[0], edges[-1]))
