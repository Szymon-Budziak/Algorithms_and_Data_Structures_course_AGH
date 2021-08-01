# We are given n points on the one-dimensional number line. Find algorithm that determines at
# which point the house should be built, so that the sum of the Euclidean distances from this
# point to all others is minimal. The sum should also be returned.
from math import sqrt, inf


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
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


def count_distance(T, point):
    return sqrt(abs(T[0] - point) ** 2 + abs(T[-1] - point) ** 2)


def build_a_house(T):
    quicksort(T, 0, len(T) - 1)
    if len(T) % 2 == 0:
        best_point = [inf, None]
        idx = len(T) // 2 - 1
        for i in range(2):
            distance = count_distance(T, T[idx + i])
            if distance < best_point[0]:
                best_point[0] = distance
                best_point[1] = T[idx + i]
        return best_point[1]
    else:
        return T[len(T) // 2]


T = [4, 11, 8, 6, 29, 14, 41, 18, 2, 13, 22, 26, 42, 1]
print(build_a_house(T))
