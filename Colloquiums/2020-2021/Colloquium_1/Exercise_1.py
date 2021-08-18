# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby są
# parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak aby
# elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
# Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
# jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
# podać złożoność czasową i pamięciową zaproponowanego algorytmu.
from Exercise_1_tests import runtests


def swap(T, value_1, value_2):
    T[value_1 // len(T)][value_1 % len(T)], T[value_2 // len(T)][value_2 % len(T)] = \
        T[value_2 // len(T)][value_2 % len(T)], T[value_1 // len(T)][value_1 % len(T)]


def partition(T, l, r):
    pivot = T[r // len(T)][r % len(T)]
    i = l - 1
    for j in range(l, r):
        if T[j // len(T)][j % len(T)] <= pivot:
            i += 1
            swap(T, i, j)
    swap(T, i + 1, r)
    return i + 1


def binary_search(T, l, r, x):
    if x > 0 and r - l + 1 >= x:
        idx = partition(T, l, r)
        if idx - l + 1 == x:
            return idx
        elif idx - l + 1 > x:
            return binary_search(T, l, idx - 1, x)
        else:
            return binary_search(T, idx + 1, r, x + l - idx - 1)
    return -1


def Median(T):
    n = len(T)
    diagonal = 0
    for i in range(n):
        diagonal += i
    binary_search(T, 0, n * n - 1, diagonal)
    binary_search(T, 0, n * n - 1, diagonal + n - 1)
    index = 0
    for i in range(diagonal, diagonal + n):
        swap(T, i, index)
        index += (n + 1)
    lower_index = current_lower_index = n * (n - 1)
    upper_index = current_upper_index = n - 1
    while current_lower_index != 0 or current_upper_index != 0:
        while T[current_lower_index // n][current_lower_index % n] <= T[0][0] and current_lower_index != 0:
            if current_lower_index // n == n - 1:
                lower_index -= n
                current_lower_index = lower_index
            else:
                current_lower_index += (n + 1)
        while T[current_upper_index // n][current_upper_index % n] > T[0][0] and current_upper_index != 0:
            if current_upper_index % n == n - 1:
                upper_index -= 1
                current_upper_index = upper_index
            else:
                current_upper_index += (n + 1)
        swap(T, current_upper_index, current_lower_index)
    return T


runtests(Median)
