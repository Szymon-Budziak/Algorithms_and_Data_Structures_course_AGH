# BFS - Breadth First Search
from queue import Queue


def BFS(graph, root):
    queue = Queue()
    visited = [False] * len(graph)
    result = []
    queue.put(root)
    visited[root] = True
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for v in range(len(graph)):
            if visited[v] is False and graph[u][v] == 1:
                queue.put(v)
                visited[v] = True
    return result


graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(BFS(graph, 0))
