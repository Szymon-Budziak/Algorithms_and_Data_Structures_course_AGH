# Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja
# ta przyjmuje na wejściu dwie n 2 - elementowe tablice(A i B) i zapisuje w tablicy
# B taką permutację elementów z A, że:
# sum(n-1, i=0) B[i] <= sum(2*n-1, i=n) B[i] <= ... <= sum(n**2-1, i=n**2-n) B[i]
# Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej.
# Proszę oszacować i podać jej złożoność czasową.
from random import randint


def partition(T, p, r):
    pivot = T[r][1]
    i = p-1
    for j in range(p, r):
        if T[j][1] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        p = q+1


def sum_sort(A, B, n):
    C = [0]*n
    result = current = start = j = i = 0
    while i <= len(A):
        if current == n:
            C[j] = (A[start:i], result)
            current = 1
            if i != len(A):
                result = A[i]
                start = i
                j += 1
        else:
            current += 1
            result += A[i]
        i += 1
    quicksort(C, 0, n-1)


n = 4
A = [randint(1, 100) for _ in range(n**2)]
print(len(A))
B = [0] * (n**2)
sum_sort(A, B, n)
