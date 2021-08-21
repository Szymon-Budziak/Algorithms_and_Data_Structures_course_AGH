# Dany jest ciąg przedziałów domkniętych [a1, b1], ..., [an, bn]. Proszę zapropnować algorytm, który
# znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej innych przedziałów.

def partition(T, p, r, index):
    pivot = T[r][index]
    i = p - 1
    for j in range(p, r):
        if T[j][index] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r, index):
    while p < r:
        q = partition(T, p, r, index)
        if q - p <= r - q:
            quicksort(T, p, q - 1, index)
            p = q + 1
        else:
            quicksort(T, q, r, index)
            r = q - 1


def the_most_intervals(T):
    quicksort(T, 0, len(T) - 1, 0)
    for i in range(len(T)):
        T[i] = (T[i][0], T[i][1], i)
    quicksort(T, 0, len(T) - 1, 1)
    for i in range(len(T)):
        T[i] = (T[i][0], T[i][1], T[i][2], i)
    max_interval = max_index = 0
    for i in range(len(T)):
        if T[i][3] - T[i][2] > max_interval:
            max_interval = T[i][3] - T[i][2]
            max_index = i
    return T[max_index][0], T[max_index][1]


T = [(4, 8), (5, 9), (1, 2), (1, 3), (2, 8), (3, 7), (4, 6), (8, 9), (6, 10), (6, 11), (9, 14), (11, 16), (3, 4)]
print(the_most_intervals(T))
