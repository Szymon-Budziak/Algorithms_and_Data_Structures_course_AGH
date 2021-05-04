# BFS - Breadth First Search
from queue import Queue


def BFS(graph, root):
    queue = Queue()
    visited = [False] * (len(graph) + 1)
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


graph = {
    1: [2, 9],
    2: [1],
    3: [4, 5, 6, 9],
    4: [3],
    5: [3, 8],
    6: [3, 7],
    7: [6, 9],
    8: [5, 7],
    9: [1, 3, 7]
}

result = BFS(graph, 1)
print(result)
