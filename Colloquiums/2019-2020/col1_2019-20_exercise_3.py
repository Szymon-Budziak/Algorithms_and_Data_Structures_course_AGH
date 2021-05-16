# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba
# z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie
# jak najszybszy. Proszę oszacować jego złożoność obliczeniową.
from math import inf


def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quick_sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quick_sort(T, p, q-1)
        p = q+1


def check_number(T, x):
    p = 0
    q = len(T)-1
    while p < q:
        if T[p] + T[q] == x:
            return True
        elif T[p] + T[q] > x:
            q -= 1
        else:
            p += 1
    return False


def find_sum(T):
    minimum = inf
    for i in range(len(T)):
        minimum = min(minimum, T[i])
    quick_sort(T, 0, len(T)-1)
    # Quick sort has an expected complexity of O(n*log(n))
    for i in range(len(T)):
        if T[i] == minimum:
            continue
        if not check_number(T, T[i]):
            return False
    # This loop in the worst case has complexity of O(n^2)
    # The whole algorithm at the worst case has complexity of O(n^2*log(n))
    return True


T = [2, 1, 1, 3, 5, 7, 9, 4, 13, 17, 16]
print(find_sum(T))
