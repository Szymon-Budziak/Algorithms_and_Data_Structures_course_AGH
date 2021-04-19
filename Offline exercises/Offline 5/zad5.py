from math import inf, sqrt


def count_distance(city1, city2):
    x_distance = city1[1] - city2[1]
    y_distance = city1[2] - city2[2]
    return sqrt(x_distance**2 + y_distance**2)


def print_solution(C, path):
    solution = [[], []]
    flag = 0
    solution[0].append(len(C)-1)
    solution[1].append(len(C)-2)
    i = len(C)-2
    j = len(C)-1
    while True:
        if path[i][j] == -1:
            break
        solution[flag].append(path[i][j])
        if path[i][j] < i:
            temporary = path[i][j]
            j = i
            i = temporary
            flag = not flag
        else:
            j = path[i][j]
    solution1, solution2 = solution
    if solution1[-1] != 0:
        solution1.append(0)
    solution1.reverse()
    if solution2[-1] != 0:
        solution2.append(0)
    solution1.extend(solution2)
    return solution1


def travelling_salesman(i, j, F, D, path):
    if F[i][j] != inf:
        return F[i][j]
    if i == j-1:
        best = inf
        index = -1
        for k in range(j-1):
            minimum = min(best, travelling_salesman(k, j-1, F, D, path)
                          + D[k][j])
            if minimum < best:
                best = minimum
                index = k
        F[j-1][j] = best
        path[j-1][j] = index
    else:
        F[i][j] = travelling_salesman(i, j-1, F, D, path)+D[j-1][j]
        path[i][j] = j-1
    return F[i][j]


def bitonicTSP(C):
    C.sort(key=lambda x: x[1])
    D = [[count_distance(C[i], C[j]) for j in range(len(C))]
         for i in range(len(C))]
    F = [[inf]*len(C) for _ in range(len(C))]
    F[0][1] = D[0][1]
    path = [[-1]*len(C) for _ in range(len(C))]
    minimum_distance = inf
    best_distance = None
    for i in range(len(C)-1):
        actual_distance = min(minimum_distance,
                              travelling_salesman(i, len(C)-1, F, D, path) + D[i][len(C)-1])
        if actual_distance < minimum_distance:
            minimum_distance = actual_distance
            best_distance = path
    solution = print_solution(C, best_distance)
    for i in range(len(solution)):
        if i != len(solution)-1:
            print(C[solution[i]][0], end=" ")
        else:
            print(C[solution[i]][0], end="\n")
    return minimum_distance


C = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2],
     ["Kraków", 2, 1], ["Szczecin", 7, 3], ["Rzeszów", 0.5, 4]]
print(bitonicTSP(C))
