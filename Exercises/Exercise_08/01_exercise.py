# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w Polsce. Jednym z głównych
# elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które tworza spójny graf
# połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo
# zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu działajacych stacji
# mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm podający
# kolejność wyłączania stacji.
# To samo zadanie, tylko inna treść:
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


graph = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [9, 10], [8], [8]]
print(delete_vertices(graph, 0))
