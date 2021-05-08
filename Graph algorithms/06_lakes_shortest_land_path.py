# Given 2D array [N][N] in which each cell has the value "W" representing water or "L"
# representing land. Lake is a group of water cells connected by their banks. Assuming
# that array[0][0] and array[n-1][n-1] are land. Check if it is possible to go from
# [0][0] to [n-1][n-1] by land. You can only walk sideways not diagonally. Also find
# the shortest path between this cells.
from queue import Queue
from math import inf


def possible_moves(T, row, col, parents):
    new_row = [row + 1, row, row - 1, row]
    new_col = [col, col + 1, col, col - 1]
    for i in range(len(new_row)):
        if new_row[i] >= 0 and new_row[i] < len(T) and new_col[i] >= 0 and new_col[i] < len(T):
            if T[new_row[i]][new_col[i]] == "L" and parents[new_row[i]][new_col[i]] == False:
                return new_row[i], new_col[i]
            elif parents[new_row[i]][new_col[i]] is True:
                continue
            elif parents[new_row[i]][new_col[i]] is not False and row == parents[new_row[i]][new_col[i]][0] and \
                    col == parents[new_row[i]][new_col[i]][1]:
                last_row = new_row[i]
                last_col = new_col[i]
                parents[row][col] = True
    return last_row, last_col


def lake_bfs(T, row_s, col_s):
    queue = Queue()
    distance = [[inf] * len(T) for _ in range(len(T))]
    distance[0][0] = 0
    parents = [[False] * len(T) for _ in range(len(T))]
    queue.put((row_s, col_s))
    while not queue.empty():
        row, col = queue.get()
        if distance[row][col] != inf:
            new_row, new_col = possible_moves(T, row, col, parents)
            if parents[new_row][new_col] == False:
                distance[new_row][new_col] = distance[row][col] + 1
                parents[row][col] = (new_row, new_col)
            if new_row == len(T) - 1 and new_col == len(T) - 1:
                return True, distance[-1][-1]
            if new_row == 0 and new_col == 0:
                return False, inf
            queue.put((new_row, new_col))


T = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "W", "W", "W"],
     ["W", "W", "L", "W", "L", "L", "W", "L"],
     ["L", "L", "L", "L", "L", "L", "L", "L"]]

verdict, distance = lake_bfs(T, 0, 0)
print(verdict, distance)
