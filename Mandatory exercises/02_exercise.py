# Proszę zaimplementować wstawianie dowolnego elementu do kopca.
from math import inf


def heap_insert(T, key):
    T += [-inf]
    print(len(T))
    heap_increase_key(T, len(T)-1, key)
    return T


def heap_increase_key(T, i, key):
    if key < T[i]:
        return False
    T[i] = key
    while i > 1 and T[(i-1)//2] < T[i]:
        T[i], T[(i-1)//2] = T[(i-1)//2], T[i]
        i = (i-1)//2


T = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
heap_insert(T, 12)
print(T)
