from math import inf
from time import perf_counter
from random import randint, seed
seed(100)


def merge(T, p, q, r):
    L = T[p:q+1]
    R = T[q+1:r+1]
    L.append(inf)
    R.append(inf)
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def merge_sort(T, p, r):
    if len(T) <= 1:
        return T
    elif p < r:
        m = (p+r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m+1, r)
        merge(T, p, m, r)


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
merge_sort(T, 0, len(T)-1)
print(T)
end = perf_counter()
print(end-start)
