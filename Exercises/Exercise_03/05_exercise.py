# Proszę zaimplementować funkcję partition z algorytmu QuickSort według pomysłu Hoare’a (tj. mamy dwa
# indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka i zamieniamy elementy tablicy pod
# nimi jeśli mniejszy indeks wskazuje na wartość większą od piwota, a większy na mniejszą).


def hoare_partition(T, l, r):
    pivot = T[l]
    i = l - 1
    j = r + 1
    while True:
        j -= 1
        while T[j] > pivot:
            j -= 1
        i += 1
        while T[i] < pivot:
            i += 1
        if j > i:
            T[i], T[j] = T[j], T[i]
        else:
            return j


def hoare_quicksort(T, l, r):
    if len(T) == 1:
        return T
    if l < r:
        q = hoare_partition(T, l, r)
        hoare_quicksort(T, l, q)
        hoare_quicksort(T, q + 1, r)
    return T


T = [36, 8, 11, 40, 7, 41, 38, 20, 25, 36, 32, 49, 12, 37, 29]
print(hoare_quicksort(T, 0, len(T) - 1))
