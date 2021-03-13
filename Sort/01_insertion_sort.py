from time import perf_counter
from random import randint, seed
seed(100)


def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
print(insertion_sort(T))
end = perf_counter()
print(end-start)
