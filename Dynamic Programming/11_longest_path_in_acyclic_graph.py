# Find the longest path in acyclic directed graph (DAG).
#    <-  5  ->
#    3   |   4 ->
#  | ->  3  ->   2
#    1 --------->


def add_edge(edges, index, val):
    edges[index].append(val)


def DFS(edges, T, visited, index):
    visited[index] = True
    for i in range(len(edges[index])):
        if not visited[edges[index][i]]:
            DFS(edges, T, visited, edges[index][i])
        T[index] = max(T[index], T[edges[index][i]]+1)


def longest_path(edges, n):
    T = [0]*(n+1)
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            DFS(edges, T, visited, i)
    return max(T)


n = 5
edges = [[]for i in range(n+1)]
add_edge(edges, 1, 2)
add_edge(edges, 1, 3)
add_edge(edges, 4, 1)
add_edge(edges, 4, 2)
add_edge(edges, 4, 5)
add_edge(edges, 5, 2)
add_edge(edges, 5, 3)
add_edge(edges, 3, 2)
print(longest_path(edges, n))
