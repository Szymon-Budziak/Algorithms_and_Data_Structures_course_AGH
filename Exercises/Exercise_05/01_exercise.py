# Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym
# problemie plecakowym. Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów
# oraz sumy ich profitów (O(n*sum(i=0, n-1)P[i])).
from math import inf


def knapsack_problem(weights, values, max_W):
    n = len(weights)
    sum_val = sum(values)
    T = [[inf] * (sum_val + 1) for _ in range(n)]
    for i in range(values[0] + 1):
        T[0][i] = weights[0]
    for i in range(1, n):
        for j in range(sum_val):
            if j < sum_val:
                T[i][j] = min(T[i - 1][j], T[i - 1][j - values[i]] + weights[i])
            else:
                T[i][j] = T[i - 1][j]
    for i in range(sum_val, -1, -1):
        if T[-1][i] <= max_W:
            return i


values = [10, 8, 4, 5, 3, 7]
weights = [4, 5, 12, 9, 1, 13]
max_W = 24
print(knapsack_problem(weights, values, max_W))
