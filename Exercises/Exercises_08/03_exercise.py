# Proszę zaimplementować algorytm sprawdzający czy graf jest dwudzielny (czyli zauważyć, że to
# 2-kolorowanie i użyć DFS lub BFS).
from queue import Queue


def bipartite_graph(graph, root):
    queue = Queue()
    colors = [-1] * len(graph)
    queue.put(root)
    colors[root] = 1
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if colors[v] == -1:
                colors[v] = 1 - colors[u]
                queue.put(v)
            elif colors[u] == colors[v]:
                return False
    return True


graph = [[2, 3, 4, 5], [2, 3, 4], [0, 1, 6], [0, 1], [0, 1, 6], [0, 6], [2, 4]]
print(bipartite_graph(graph, 0))
