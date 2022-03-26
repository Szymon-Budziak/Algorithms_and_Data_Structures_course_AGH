# Proszę zaimplementować algorytm który policzy liczbę spójnych składowych w grafie (reprezentacja macierzowa).
from queue import Queue


def components(graph):
    queue = Queue()
    visited = [False] * len(graph)
    result = [0] * len(graph)
    count = 0
    for vertex in range(len(graph)):
        if result[vertex] == 0:
            queue.put(vertex)
            count += 1
            result[vertex] = count
            visited[vertex] = True
            while not queue.empty():
                u = queue.get()
                for v in range(len(graph)):
                    if not visited[v] and graph[u][v] == 1:
                        queue.put(v)
                        visited[v] = True
                        result[v] = count
    return count


graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0]]
print(components(graph))
