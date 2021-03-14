from math import inf
from time import perf_counter
from random import randint, seed
seed(100)


def merge_sort(T):
    current_size = 1
    while current_size < len(T)-1:
        left = 0
        while left < len(T)-1:
            mid = min((left+current_size-1), (len(T)-1))
            right = ((2*current_size + left - 1, len(T)-1)
                     [2*current_size+left-1 > len(T)-1])
            merge(T, left, mid, right)
            left += current_size*2
        current_size *= 2


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


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
merge_sort(T)
print(T)
end = perf_counter()
print(end-start)
