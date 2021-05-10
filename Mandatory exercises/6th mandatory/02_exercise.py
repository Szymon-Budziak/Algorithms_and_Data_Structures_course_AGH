# Proszę podać jak najszybszy algorytm, który znajduje w grafie cykl długości dokładnie 4
# (trywialny algorytm ma złożoność O(n^4), gdzie n to liczba wierzchołków, chodzi
# o rozwiązanie szybsze).
from queue import Queue
from math import inf


def four_length_cycle(graph):
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    queue = Queue()
    for i in range(len(graph)):
        queue.put(i)
        if i != 0:
            for a in range(i):
                visited[a] = True
        visited[i] = True
        distance[i] = 0
        while not queue.empty():
            u = queue.get()
            min_distance = inf
            for vertex in graph[u]:
                if not visited[vertex]:
                    for i in graph[vertex]:
                        min_distance = min(min_distance, distance[i])
                    distance[vertex] = min_distance + 1
                    if distance[vertex] == 2:
                        count = 0
                        for j in graph[vertex]:
                            if distance[j] == 1:
                                count += 1
                        if count >= 2:
                            return True
                    queue.put(vertex)
                    visited[vertex] = True
        for k in range(len(graph)):
            visited[k] = False
            distance[k] = inf
    return False


graph = [[1, 2], [0, 3, 4], [0, 5, 6, 7], [1, 4], [1, 3], [2, 8, 9], [2, 9, 10],
         [2, 10], [5, 11], [5, 6], [7, 11], [8, 10]]

print(four_length_cycle(graph))
