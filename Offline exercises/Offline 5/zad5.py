# I am not sure if this code is correct and if it works well.
from math import inf, sqrt


def count_distance(city1, city2):
    x_distance = city1[1] - city2[1]
    y_distance = city1[2] - city2[2]
    return sqrt(x_distance**2 + y_distance**2)


def print_solution(C, index, path):
    if index != 0:
        print_solution(C, path[index], path)
    print(C[index][0], end=" ")


def travelling_salesman(i, j, F, D, path1, path2):
    if F[i][j] != inf:
        path1[j] = path2[j]
        return F[i][j]
    if i == j-1:
        best = inf
        for k in range(j-1):
            best = min(best, travelling_salesman(
                k, j-1, F, D, path1, path2) + D[k][j])
            path1[j] = k
            F[j-1][j] = best
    else:
        path1[j] = j-1
        F[i][j] = travelling_salesman(i, j-1, F, D, path1, path2)+D[j-1][j]
    return F[i][j]


def bitonicTSP(C):
    C.sort(key=lambda x: x[1])
    D = [[count_distance(C[i], C[j]) for j in range(len(C))]
         for i in range(len(C))]
    F = [[inf]*len(C) for _ in range(len(C))]
    F[0][1] = D[0][1]
    path1 = [-1]*len(C)
    path1[1] = 0
    path2 = [-1]*len(C)
    path2[1] = 0
    starting = [-1, -1]
    idx = 0
    minimum_distance = inf
    for i in range(len(C)-1):
        actual_distance = travelling_salesman(
            i, len(C)-1, F, D, path1, path2) + D[i][len(C)-1]
        if actual_distance <= minimum_distance:
            minimum_distance = actual_distance
            for j in range(len(C)):
                path2[j] = path1[j]
            starting[idx] = i
            idx = (idx+1) % 2
    print_solution(C, starting[0], path2)
    print(C[-1][0], end=" ")
    a = starting[1]
    while a != -1:
        print(C[a][0], end=" ")
        a = path2[a]
    print()
    return minimum_distance


C = [["Wrocław", 0, 1], ["Warszawa", 11, 5],
     ["Gdańsk", 4, 2], ["Kraków", 2, 1], ]
print(bitonicTSP(C))
