# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać
# na prom. Prom ma dwa pasy (lewy i prawy) oba długości L. Proszę napisać program,
# który wyznacza, które samochody powinny pojechać na który pas, żeby na promie
# zmieściło się jak najwięcej aut. Auta muszą wjeżdżać w takiej kolejności, w jakiej
# są podane w tablicy A.
from math import inf


def cars_on_ferry(A, L):
    n = len(A)
    DP = [[[-inf]*(L+1) for _ in range(L+1)] for _ in range(n)]
    for i in range(L):
        for j in range(L):
            DP[0][i][j] = 0
    return solution(A, DP, 0, L, L)


def solution(A, DP, i, j, k):
    if DP[i][j][k] != -inf:
        return DP[i][j][k]
    a = b = 0
    if A[i] <= j:
        a = solution(A, DP, i+1, j-A[i], k) + 1
    if A[i] <= k:
        b = solution(A, DP, i+1, j, k-A[i]) + 1
    DP[i][j][k] = max(a, b)
    return DP[i][j][k]


A = [1, 1, 2, 3, 5, 8, 13]
L = 8
print(cars_on_ferry(A, L))
