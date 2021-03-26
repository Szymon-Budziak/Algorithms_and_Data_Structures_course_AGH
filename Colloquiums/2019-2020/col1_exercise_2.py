# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco
# względem wzrostu. Proszę zaimplementować funkcję: section(T, p, q) która zwróci
# tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy
# opis algorytmu oraz proszę oszacować jego złożoność czasową.


def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] > pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quickselect(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quickselect(T, p, q-1)
        p = q+1


def section(T, p, r):
    quickselect(T, 0, r)
    # Average quickselect performance is O(n)
    quickselect(T, p, r)
    # The whole algorithm complexity at the average case is 2*O(n) = O(n)
    return T[p:r+1]


T = [37, 98, 175, 172, 143, 134, 172, 189, 210, 225, 179, 183, 152, 146]
print(section(T, 3, 9))
