# Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie
# raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm,
# który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.


def dfs(graph, source, visited, result):
    visited[source] = True
    for v in range(len(graph)):
        if not visited[v] and graph[source][v] == 1:
            dfs(graph, v, visited, result)
    result.insert(0, source)


def topological_sort(graph):
    visited = [False] * len(graph)
    result = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, result)
    return result


def hamiltonian_path(graph):
    result = topological_sort(graph)
    for i in range(1, len(result) + 1):
        if i != len(result):
            if graph[result[i - 1]][result[i]] == 0:
                return False
        elif i == len(result):
            if graph[result[i - 1]][result[0]] == 0:
                return False
    return True


graph = [[0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [1, 0, 0, 1, 0, 0, 0]]
print(hamiltonian_path(graph))
