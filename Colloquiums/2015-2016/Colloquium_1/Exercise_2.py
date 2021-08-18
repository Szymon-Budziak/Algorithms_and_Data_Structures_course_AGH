# Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże). Wiadomo,
# że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym rozkładem)
# n różnych liczb nieparzystych i posortowano je rosnąco. Następnie wybrano losowo ceil(log(n))
# elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę zaproponować
# algorytm sortowania tak powstałych danych. Algorytm powinien być możliwie jak najszybszy.
# Proszę oszacować i podać jego złożoność czasową.
from random import randint
from math import log2, ceil, inf


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q - p <= r - q:
            quicksort(T, p, q - 1)
            p = q + 1
        else:
            quicksort(T, q, r)
            r = q - 1


def merge(T, even_numbers, odd_numbers):
    even_numbers.append(inf)
    odd_numbers.append(inf)
    i = j = 0
    for k in range(len(T)):
        if even_numbers[i] < odd_numbers[j]:
            T[k] = even_numbers[i]
            i += 1
        else:
            T[k] = odd_numbers[j]
            j += 1


def merge_sort(T):
    even_numbers = [0] * ceil(log2(len(T)))
    odd_numbers = [0] * (len(T) - len(even_numbers))
    even = odd = 0
    for i in range(len(T)):
        if T[i] % 2 == 0:
            even_numbers[even] = T[i]
            even += 1
        else:
            odd_numbers[odd] = T[i]
            odd += 1
    # This loop has O(n) complexity
    quicksort(even_numbers, 0, len(even_numbers) - 1)
    # Quicksort complexity in average case is O(n*log(n))
    merge(T, even_numbers, odd_numbers)
    return T
    # Merge complexity is O(n)
    # Whole algorithm has complexity level of O(n*log(n)) + 2*O(n) = O(n*log(n))


def odd_number(n):
    while True:
        number = randint(1, n)
        if number % 2 == 1:
            return number


def even_number(n):
    while True:
        number = randint(1, n)
        if number % 2 == 0:
            return number


def sort(T):
    quicksort(T, 0, len(T) - 1)
    i = 0
    while i < ceil(log2(len(T))):
        index = T[randint(0, n - 1)]
        if T[index] % 2 != 0:
            T[index] = even_number(n)
            i += 1
    merge_sort(T)
    return T


n = 100
T = [odd_number(n) for _ in range(n)]
print(sort(T))
