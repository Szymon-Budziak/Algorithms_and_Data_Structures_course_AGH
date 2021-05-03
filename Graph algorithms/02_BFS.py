# BFS - Breadth First Search
from queue import Queue


def BFS(graph, root):
    queue = Queue()
    visited = [False] * (len(graph) + 1)
    queue.put(root)
    visited[root] = True
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
