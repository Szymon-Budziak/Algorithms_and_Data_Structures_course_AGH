# Chef Monocarp has just put n dishes into an oven. He knows that the i-th dish has its optimal
# cooking time equal to ti minutes. At any positive integer minute T Monocarp can put no more than
# one dish out of the oven. If the i-th dish is put out at some minute T, then its unpleasant value
# is |T − t[i]| — the absolute difference between T and t[i]. Once the dish is out of the oven, it
# can't go back in. Monocarp should put all the dishes out of the oven. What is the minimum total
# unpleasant value Monocarp can obtain?
from math import inf


def chef_monocarp(n, T):
    T.sort()
    DP = [[inf] * (2 * n + 1) for _ in range(n + 1)]
    for i in range(2 * n + 1):
        DP[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, 2 * n + 1):
            DP[i][j] = min(DP[i][j - 1], DP[i - 1][j - 1] + abs(T[i - 1] - j))
    return DP[-1][-1]


n = 12
T = [4, 11, 12, 4, 10, 12, 9, 3, 4, 11, 10, 10]
print(chef_monocarp(n, T))
