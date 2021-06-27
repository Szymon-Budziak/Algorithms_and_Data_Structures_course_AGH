# We are given an array (m x n) filled with values. Find the longest path in this array (we can
# move to the fields adjacent by the edges), with increasing values (from field with a value 3
# we can move to fields with a value greater or equal to 4).
# We are given a starting point.


def find_path(T, DP, x, y):
    new_x = [x + 1, x - 1, x, x]
    new_y = [y, y, y + 1, y - 1]
    for i in range(len(new_x)):
        if new_x[i] >= 0 and new_y[i] >= 0 and new_x[i] < len(T) and new_y[i] < len(T):
            if T[new_x[i]][new_y[i]] > T[x][y]:
                DP[new_x[i]][new_y[i]] = max(DP[new_x[i]][new_y[i]], DP[x][y] + T[new_x[i]][new_y[i]])
                find_path(T, DP, new_x[i], new_y[i])
    return DP


def the_longest_path(T, point):
    DP = [[0] * len(T) for _ in range(len(T))]
    DP[point[0]][point[1]] = T[point[0]][point[1]]
    find_path(T, DP, point[0], point[1])
    max_distance = 0
    for i in range(len(DP)):
        max_distance = max(max_distance, max(DP[i]))
    return max_distance


T = [[3, 4, 5, 2, 1],
     [10, 2, 13, 14, 8],
     [11, 1, 4, 9, 5],
     [9, 8, 11, 7, 3],
     [6, 2, 1, 6, 9]]
starting_point = (4, 2)
print(the_longest_path(T, starting_point))
