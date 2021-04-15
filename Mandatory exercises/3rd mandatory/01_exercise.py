# Proszę przedstawić algorytm problemu knapsack działający w czasie O(n*sum(i=0, n-1)P[i])
from math import inf


def knapsack(W, P, max_W):
    sum_P = sum(P)
    F = [[inf] * (sum_P+1) for _ in range(len(W))]
    for i in range(P[0]+1):
        F[0][i] = W[0]
    for i in range(1, len(W)):
        for j in range(sum_P, -1, -1):
            if j < sum_P:
                F[i][j] = min(F[i-1][j], F[i-1][j-P[i]] +
                              W[i], F[i][j], F[i][j+1])
            else:
                F[i][j] = min(F[i-1][j], F[i-1][j-P[i]]+W[i], F[i][j])
    for i in range(sum_P, -1, -1):
        if F[-1][i] <= max_W:
            return i


P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
max_W = 24
print(knapsack(W, P, max_W))
