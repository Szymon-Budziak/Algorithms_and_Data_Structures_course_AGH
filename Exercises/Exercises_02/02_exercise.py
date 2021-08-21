# Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca liczbę
# jej inwersji (t.j. liczbę par indeksów i < j takich, że A[i] > A[j]).
from math import inf


def merge(T, p, q, r):
    L = T[p:q + 1]
    R = T[q + 1:r + 1]
    L.append(inf)
    R.append(inf)
    i = j = inversions = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
            inversions += (q - i - p + 1)
    return inversions


def number_of_inversions(T, p, r):
    inversions = 0
    if len(T) <= 1:
        return T
    elif p < r:
        mid = (p + r) // 2
        inversions += number_of_inversions(T, p, mid)
        inversions += number_of_inversions(T, mid + 1, r)
        inversions += merge(T, p, mid, r)
    return inversions


T = [4, 6, 1, 15, 8, 19, 65, 3, 29, 5]
print(number_of_inversions(T, 0, len(T) - 1))
