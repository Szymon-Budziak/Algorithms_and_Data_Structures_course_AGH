# We are given a mxn matrix witch each cell having a value corresponding to the
# cost. Find the minimum cost to reach (m,n) from (0,0) and print this path.
# We can move from a cell only to its adjacent right cell and adjacent down cell.


def minimum_cost_path(T, rows, cols):
    A = [[0]*cols for _ in range(rows)]
    for i in range(cols):
        A[0][i] = T[0][i]
    for i in range(rows):
        A[i][0] = T[i][0]
    for i in range(1, cols):
        A[0][i] += A[0][i-1]
    for i in range(1, rows):
        A[i][0] += A[i-1][0]
    for i in range(1, rows):
        for j in range(1, cols):
            A[i][j] = min(A[i-1][j], A[i][j-1]) + T[i][j]
    i = j = 0
    print(T[i][j], end=" ")
    while i != rows-1 and j != cols-1:
        if T[i+1][j] < T[i][j+1]:
            print(T[i+1][j], end=" ")
            i += 1
        else:
            print(T[i][j+1], end=" ")
            j += 1
    if i == rows-1 or j == rows-1:
        print(T[-1][-1])
    return A[rows-1][cols-1]


T = [[1, 3, 5, 8],
     [4, 2, 1, 7],
     [4, 3, 2, 8],
     [7, 2, 9, 1]]
rows = 4
cols = 4
print(minimum_cost_path(T, rows, cols))
