from time import perf_counter
from random import randint, seed
seed(100)


def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def iterative_quicksort(T):
    S = []
    p = 0
    r = len(T)-1
    S.append((p, r))
    while len(S) > 0:
        (p, r) = S.pop()
        if p < r:
            q = partition(T, p, r)
            if q-p > r-1:
                S.append((p, q-1))
                S.append((q+1, r))
            else:
                S.append((q+1, r))
                S.append((p, q-1))


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
iterative_quicksort(T)
print(T)
end = perf_counter()
print(end-start)
