# Given a set of cities and distance between every pair of cities. Find the shortest
# possible route that visits every city exactly once and returns to the starting city.
# This is a bitonic solution with time complexity of O(n^2).
from math import sqrt, inf


def count_distance(city1, city2):
    x_distance = city1[0] - city2[0]
    y_distance = city1[1] - city2[1]
    return sqrt(x_distance**2 + y_distance**2)


def travelling_salesman(i, j, F, D):
    if F[i][j] != inf:
        return F[i][j]
    if i == j-1:
        best = inf
        for k in range(j-1):
            best = min(best, travelling_salesman(k, j-1, F, D)+D[k][j])
        F[j-1][j] = best
    else:
        F[i][j] = travelling_salesman(i, j-1, F, D)+D[j-1][j]
    return F[i][j]


C = [[0, 1], [11, 5], [4, 2], [2, 1], [1, 3]]
C.sort(key=lambda x: x[1])
D = [[count_distance(C[i], C[j]) for j in range(len(C))]
     for i in range(len(C))]
F = [[inf]*len(C) for _ in range(len(C))]
F[0][1] = D[0][1]
minimum_distance = inf
for i in range(len(C)-1):
    minimum_distance = min(minimum_distance,
                           travelling_salesman(i, len(C)-1, F, D) + D[i][len(C)-1])
print(minimum_distance)
