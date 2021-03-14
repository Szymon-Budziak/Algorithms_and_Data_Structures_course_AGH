from time import perf_counter
from random import randint, seed
seed(100)


def partition(T, p, r):
    i = p-1
    pivot = T[r]
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quicksort(T, p, r):
    size = r-p+1
    stack = [0]*size
    top = -1
    top += 1
    stack[top] = p
    top += 1
    stack[top] = r
    while top >= 0:
        r = stack[top]
        top -= 1
        p = stack[top]
        top -= 1
        q = partition(T, p, r)
        if q-1 > p:
            top += 1
            stack[top] = p
            top += 1
            stack[top] = q-1
        if q+1 < r:
            top += 1
            stack[top] = q+1
            top += 1
            stack[top] = r


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
quicksort(T, 0, len(T)-1)
print(T)
end = perf_counter()
print(end-start)
