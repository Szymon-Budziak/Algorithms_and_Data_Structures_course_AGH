# We are given a graph, in which the vertices are cities and the edges are roads between them. We know
# the fuel price in per liter for each city and the length in kilometers for each road. Our car has
# a 100 liter tank and burns one liter per kilometer. We start from city_A with an empty tank. What is
# the minimum cost that we have to pay for fuel to get to the city_B?
from math import inf
from queue import PriorityQueue


def relax(graph, vertex, source, distance, cost):
    for i in range(distance, len(graph[vertex])):
        for j in range(i - distance, len(graph[vertex])):
            graph[vertex][j] = min(graph[vertex][j], graph[source][i] + j * cost)


def cheapest_trip_with_refueling(graph, city_a, city_b, capacity):
    new_graph = [[inf] * (capacity + 1) for _ in range(len(graph))]
    for i in range(len(new_graph[0])):
        new_graph[0][i] = i * graph[0][1]
    queue = PriorityQueue()
    queue.put((0, city_a))
    visited = [False] * len(graph)
    while not queue.empty():
        distance, u = queue.get()
        for v in graph[u][0]:
            vertex, dist = v
            if not visited[vertex]:
                if dist <= capacity:
                    relax(new_graph, vertex, u, dist, graph[vertex][1])
                    queue.put((new_graph[vertex][dist], vertex))
        visited[u] = True
    return new_graph[city_b][0]


graph = [[[(1, 5), (2, 7)], 8],
         [[(0, 4), (2, 3), (3, 5)], 5],
         [[(0, 7), (1, 3), (3, 4)], 3],
         [[(1, 5), (2, 4), (4, 6)], 2],
         [[(3, 6)], 1]]
print(cheapest_trip_with_refueling(graph, 0, len(graph) - 1, 6))
