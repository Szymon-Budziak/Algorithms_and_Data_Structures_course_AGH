from time import perf_counter
from random import randint, seed
seed(100)


def counting_sort(T, k):
    C = [0]*len(T)
    B = [0]*10
    for i in range(len(T)):
        index = int((T[i]/k) % 10)
        B[index] += 1
    for i in range(1, 10):
        B[i] += B[i-1]
    j = len(T)-1
    while j >= 0:
        index = int((T[j]/k) % 10)
        C[B[index]-1] = T[j]
        B[index] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = C[i]


def radix_sort(T):
    maximum = 0
    for i in range(len(T)):
        maximum = max(maximum, T[i])
    i = 1
    while maximum/i > 0:
        counting_sort(T, i)
        i *= 10


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
radix_sort(T)
print(T)
end = perf_counter()
print(end-start)
