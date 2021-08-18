# Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego
# rozkładu losowego. Ten rozkład mamy zadany jako k przedziałów (a[1], b[1]), (a[2], b[2]), ..., (a[k], b[k])
# takich, że i-ty przedział jest wybierany z prawdopodobieństwem c[i], a liczba z przedziału jest
# wybierana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić, liczby a[i], b[i]
# są liczbami naturalnymi ze zbioru {1, ..., N}. Proszę zaimplementować funkcję SortTab(T,P) sortującą
# podaną tablicę. Pierwszy argument to tablica do posortowania a drugi to opis przedziałów w postaci:
# P = [(a[1], b[1], c[1]), (a[2], b[2], c[2]), ..., (a[k], b[k], c[k])].
# Na przykład dla wejścia:
# P = [(1, 5, 0.75), (4, 8, 0.25)]
# T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
# po wywołaniu SortTab(T, P) tablica T powinna być postaci:
# T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
# Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
# zaproponowanego algorytmu.
from Exercise_3_tests import runtests
from math import floor


def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def bucket_sort(T, buckets, max_min):
    for i in T:
        for j in range(len(max_min)):
            if i >= max_min[j][0] and i <= max_min[j][1]:
                index = floor((i - max_min[j][0]) / (max_min[j][1] + 1 - max_min[j][0]) * len(buckets[j]))
                buckets[j][index].append(i)
                break
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            buckets[i][j] = insertion_sort(buckets[i][j])
    idx = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            for k in range(len(buckets[i][j])):
                T[idx] = buckets[i][j][k]
                idx += 1
    return T


def SortTab(T, P):
    buckets = [[] for _ in range(len(P))]
    for i in range(len(T)):
        for j in range(len(P)):
            if T[i] > P[j][0] and T[i] < P[j][1]:
                buckets[j].append(T[i])
    max_min = []
    for i in range(len(buckets)):
        minimum = min(buckets[i])
        maximum = max(buckets[i])
        max_min.append((minimum, maximum))
    new_buckets = []
    for i in range(len(P)):
        array = [[] for _ in range(len(buckets[i]))]
        new_buckets.append(array)
    bucket_sort(T, new_buckets, max_min)


runtests(SortTab)
