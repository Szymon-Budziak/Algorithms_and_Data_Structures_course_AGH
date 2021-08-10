# Dany jest zbiór przedziałów otwartych A = [(a[1], b[1]), ..., (a[n], b[n])]. Proszę zaproponować
# algorytm, który znajduje taki zbiór X, X ⊆ [1, ..., n] że:
#       (a) |X| = k (gdzie k ∈ N to dany parametr wejściowy),
#       (b) dla każdych i, j ∈ X, przedziały (a[i], b[i]) oraz (a[j], b[j]) nie nachodzą na siebie,
#       (c) wartość max j ∈ X b[j] − min i ∈ X a[i] jest minimalna.
# Jeśli podzbioru spełniającego warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. Algorytm
# powinien być możliwie jak najszybszy (ale przede wszystkim poprawny).
from math import inf


def open_intervals(T, k):
    T.sort(key=lambda x: x[1])
    best_result = inf
    result = []
    for i in range(len(T) - k):
        actual = [T[i]]
        j = 1
        l = i + 1
        while j < k and l < len(T):
            if actual[j - 1][1] <= T[l][0]:
                actual.append(T[l])
                j += 1
            l += 1
        actual_result = actual[j - 1][1] - actual[0][0]
        if actual_result < best_result and j == k:
            best_result = actual_result
            result = actual[:]
    if len(result) == 0:
        return False
    return result


T = [(1, 7), (2, 5), (3, 4), (8, 10), (3, 6), (2, 4), (5, 9), (7, 8), (1, 5), (1, 2), (2, 5)]
print(open_intervals(T, 2))
