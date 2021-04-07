# We are given a sequence (chain) [A1, A2, ..., An] of n matrices, where for
# i= (1, 2, ..., n), matrix Ai has dimension p[i-1]xp[i], fully parenthesize the
# product A1*A2*...*An in a way that minimizes the number of scalar multiplications.
from math import inf


def matrix_chain_order(T):
    min_multi = [[0 for _ in range(len(T))] for _ in range(len(T))]
    size = [[0 for _ in range(len(T))] for _ in range(len(T))]
    for x in range(1, len(T)):
        min_multi[x][x] = 0
    for L in range(2, len(T)):
        for i in range(1, len(T)-L+1):
            k = i+L-1
            min_multi[i][k] = inf
            for j in range(i, k):
                q = min_multi[i][j] + min_multi[j+1][k] + (T[i-1]*T[j]*T[k])
                if q < min_multi[i][k]:
                    min_multi[i][k] = q
                    size[i][k] = q
    return min_multi[1][len(T)-1], size


T = [30, 35, 15, 5, 10, 20, 25]
min_multi, size = matrix_chain_order(T)
print(min_multi)
