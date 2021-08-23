# Dany jest ciąg przedziałów postaci [a[i], b[i]]. Dwa przedziały można skleić jeśli mają dokładnie
# jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
#     1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
#     2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
#     3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.


def dfs(graph, visited, u):
    visited[u] = True
    for v in range(len(graph)):
        if not visited[v] and graph[u][v] == 1:
            visited[v] = True
            dfs(graph, visited, v)


def stick_the_intervals(intervals, a, b):
    intervals.sort(key=lambda x: x[1])
    graph = [[0] * (intervals[-1][1] + 1) for _ in range(intervals[-1][1] + 1)]
    for i in range(len(intervals)):
        graph[intervals[i][0]][intervals[i][1]] = 1
    visited = [False] * len(graph)
    dfs(graph, visited, a)
    return visited[b]


intervals = arr = [(2, 4), (3, 8), (1, 4), (2, 3), (6, 7), (5, 9), (1, 2), (4, 7), (8, 9), (3, 6)]
print(stick_the_intervals(intervals, 2, 8))
