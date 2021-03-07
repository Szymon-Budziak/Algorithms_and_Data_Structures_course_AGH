from math import inf


def merge(T, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = T[p+i]
    for j in range(n2):
        R[j] = T[q+j+1]
    L[-1] = inf
    R[-1] = inf
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def merge_sort(T, p, r):
    if p < r:
        m = (p+r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m+1, r)
        merge(T, p, m, r)


T = [2, 4, 5, 7, 1, 2, 3, 6]
print(merge_sort(T, 0, len(T)-1))
print(T)
