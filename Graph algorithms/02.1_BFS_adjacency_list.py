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
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
    return result


graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6]]

result = BFS(graph, 1)
print(result)
