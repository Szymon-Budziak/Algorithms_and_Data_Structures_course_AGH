# Dany jest spójny graf nieskierowany G = (V,E). Proszę zaproponować algorytm, który znajdzie taką
# kolejność usuwania wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie przestaje
# być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie dotykające go krawędzie).
from queue import Queue


def delete_vertices(graph, source):
    queue = Queue()
    visited = [False] * len(graph)
    visited[source] = True
    result = [source]
    queue.put(source)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                result.append(v)
    result.reverse()
    return result


graph = [[1, 5, 7], [0, 2, 3], [1, 4], [2], [2, 6], [0, 6], [4, 5], [0, 8, 9],
         [7, 10], [7, 11], [8, 12], [9, 12], [10, 11]]
print(delete_vertices(graph, 0))
