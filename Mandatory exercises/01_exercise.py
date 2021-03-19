# Proszę zaimplementować QuickSort tak, żeby używał najwyżej O(logn) dodatkowej pamięci.
from random import randint


def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        p = q+1


T = [randint(1, 100) for _ in range(20)]
print(T)
quicksort(T, 0, len(T)-1)
print(T)
