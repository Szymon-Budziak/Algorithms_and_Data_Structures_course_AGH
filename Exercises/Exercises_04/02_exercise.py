# Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie ∣B∣ = log(n).
# Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.
from math import log2


def counting_sort(T, k):
    count = [0] * k
    result = [0] * len(T)
    for i in range(len(T)):
        count[T[i]] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for i in range(len(T) - 1, -1, -1):
        count[T[i]] -= 1
        result[count[T[i]]] = T[i]
    for i in range(len(T)):
        T[i] = result[i]


def insertion_sort(T):
    for i in range(len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def binary_search(A, r, x, p=0):
    if r >= p:
        mid = (p + r) // 2
        if A[mid] == x:
            return False
        elif A[mid] < x:
            return binary_search(A, r, x, mid + 1)
        else:
            return binary_search(A, mid - 1, x, p)
    return True


def sort(T):
    A = [0] * int(log2(len(T)))
    for i in range(len(T)):
        if binary_search(A, len(A) - 1, T[i]):
            A[0] = T[i]
            insertion_sort(A)
    for i in range(len(T)):
        for j in range(len(A)):
            if T[i] == A[j]:
                T[i] = j
    counting_sort(T, len(A))
    for i in range(len(T)):
        for j in range(len(A)):
            if T[i] == j:
                T[i] = A[j]
    return T


T = [38, 19, 38, 38, 271, 271, 19, 271, 271, 33, 33, 33, 19, 33, 19, 33]
print(sort(T))
