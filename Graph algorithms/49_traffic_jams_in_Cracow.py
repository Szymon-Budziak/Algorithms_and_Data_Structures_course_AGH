# There are traffic jams in Cracow during rush hours. Therefore drivers are more concerned with time than
# with the real distance between two points. We are given a map of Cracow, distances and travel times are
# marked between road intersections. There are one-way streets and two-way streets in Cracow. Drivers need
# an app to help them find the roads that allow them to get from intersection A to B in the shortest
# possible time and among those with the shortest time it selects and returns the shortest in terms of
# distance. We have to process Q queries represented as (intersectionA, intersectionB) and answer each of
# them with a pair (time, distance) of the best way. All queries refer to the same graph.
# What solution gives the best complexity in each of the following cases?
#   1) Q = O(1), E = O(V)
#   2) Q = O(1), E = O(V^2)
#   3) Q = O(V), E = O(V)
#   4) Q = O(V), E = O(V^2)

# Solution:
# 1) Dijkstra algorithm will have complexity O(V^2*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Dijkstra algorithm.
# 2) Dijkstra algorithm will have complexity O(V^3*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Floyd-Warshall algorithm.
# 3) Dijkstra algorithm will have complexity O(V^2*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Dijkstra algorithm.
# 4) Dijkstra algorithm will have complexity O(V^3*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Floyd-Warshall algorithm.
# We can see that for sparse graph (1 and 3 cases) the better choice in this exercise is Dijkstra algorithm,
# but for dense graph (2 and 4 cases) the better option is to use Floyd-Warshall algorithm.
from math import inf


def traffic_jams(graph):
    time = [[inf] * len(graph) for _ in range(len(graph))]
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                time[i][j] = 0
                distance[i][j] = 0
            elif graph[i][j] != 0:
                time[i][j] = graph[i][j][0]
                distance[i][j] = graph[i][j][1]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if time[u][k] + time[k][v] < time[u][v] or \
                        (time[u][k] + time[k][v] == time[u][v] and distance[u][k] + distance[k][v] < distance[u][v]):
                    time[u][v] = time[u][k] + time[k][v]
                    distance[u][v] = distance[u][k] + distance[k][v]
    result = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(result)):
        for j in range(len(result)):
            result[i][j] = (time[i][j], distance[i][j])
    return result


# (time, distance)
graph = [[0, (3, 2), (4, 1), 0, 0, 0, 0, 0, 0, 0],
         [(3, 2), 0, 0, (2, 3), 0, 0, 0, 0, 0, 0],
         [(4, 1), 0, 0, 0, 0, 0, (2, 5), 0, 0, 0],
         [0, 0, 0, 0, (1, 1), (1, 4), 0, 0, 0, 0],
         [0, 0, 0, (1, 1), 0, 0, 0, (5, 5), 0, 0],
         [0, 0, 0, 0, 0, 0, (6, 1), 0, (3, 2), 0],
         [0, 0, (2, 5), 0, 0, 0, 0, 0, (3, 2), 0],
         [0, 0, 0, 0, (5, 3), 0, 0, 0, 0, (4, 5)],
         [0, 0, 0, 0, 0, 0, (3, 3), 0, 0, (4, 2)],
         [0, 0, 0, 0, 0, 0, 0, (5, 6), (4, 2), 0]]
result = traffic_jams(graph)
for i in range(len(result)):
    print(result[i])
