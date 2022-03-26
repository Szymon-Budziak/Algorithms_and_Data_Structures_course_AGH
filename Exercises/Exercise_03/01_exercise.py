# Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby zawsze
# używał najwyżej O(log(n)) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji
# partition.


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q - p < r - q:
            quicksort(T, p, q - 1)
            p = q + 1
        else:
            quicksort(T, q + 1, r)
            r = q - 1
    return T


T = [27, 8, 19, 7, 21, 15, 33, 12, 26, 40, 38, 19, 28, 25, 6]
print(quicksort(T, 0, len(T) - 1))
