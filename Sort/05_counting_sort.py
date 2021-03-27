from time import perf_counter
from random import randint, seed
seed(100)


def counting_sort(T, k):
    C = [0]*k
    B = [0]*len(T)
    for i in range(len(T)):
        C[T[i]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        C[T[i]] -= 1
        B[C[T[i]]] = T[i]
    for i in range(len(T)):
        T[i] = B[i]


k = 10000
T = [randint(0, k-1) for _ in range(10000)]
start = perf_counter()
counting_sort(T, k)
print(T)
end = perf_counter()
print(end-start)
