# Given list of values. We play a game against the opponent and we always grab
# one value from either left or right side of our list of values. Our opponent
# does the same move. What is the maximum value we can grab if our opponent
# plays optimally, just like us.


def optimal_values(V):
    T = [[0]*(len(V)+1) for _ in range(len(V)+1)]
    for i in range(1, len(V)+1):
        T[0][i] = i
    for i in range(1, len(V)+1):
        T[i][0] = i
    for i in range(1, len(T)):
        T[i][i] = (V[i-1], 0)
    for value in range(2, len(V)+1):
        for i in range(1, len(T)-value+1):
            j = i+value-1
            for k in range(i, j):
                first = max(T[i][j-1][1] + V[j-1], T[i+1][j][1]+V[i-1])
                second = min(T[i][j-1][0], T[i+1][j][0])
                T[i][j] = (first, second)
    return T[1][-1][0]


V = [3, 8, 4, 5, 1, 7, 6]
print(optimal_values(V))
