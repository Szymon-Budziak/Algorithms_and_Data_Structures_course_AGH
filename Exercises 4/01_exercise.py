# Sortowanie tablicy n liczb ze zbioru {0, 1, ..., n^2-1}.
from random import randint


def countsort(T, f):
    B = [0]*len(T)
    C = [0]*len(T)
    for i in range(len(T)):
        C[f(T[i])] += 1
    for i in range(1, len(T)):
        C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        C[f(T[i])] -= 1
        B[C[f(T[i])]] = T[i]
    for i in range(len(T)):
        T[i] = B[i]


def sort_nsq(T):
    countsort(T, lambda x: x % len(T))
    countsort(T, lambda x: x//len(T))


n = 10
T = [randint(0, n**2-1) for _ in range(n)]
print(T)
sort_nsq(T)
print(T)
