from random import randint, seed
from math import inf


def mergesort(T, p=0, r=None):
    if r is None:
        r = len(T) - 1
    if p < r:
        m = (p+r) // 2
        mergesort(T, p, m)
        mergesort(T, m+1, r)
        merge(T, p, m, r)
    return T


def merge(T, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = T[p+i]
    for j in range(n2):
        R[j] = T[q+j+1]
    L[-1] = R[-1] = inf
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
    if T[i] > T[i+1]:
        print("Błąd sortowania!")
        exit()

print("OK")
