# We are given n points (x, y) that are in circle with radius k (natural number)
# i.e. 0 <= x^2 + y^2 <= k which are evenly distributed in it (The probability of finding a point
# in a given area is proportional to the area of this whole area). Find algorithm that in time
# O(n) will sort the points by their distance to the point (0, 0) i.e. d = sqrt(x^2 + y^2).
from math import sqrt


def insertion_sort(T):
    for i in range(1, len(T)):
        value = T[i][0] ** 2 + T[i][1] ** 2
        key = T[i]
        j = i - 1
        while j >= 0 and T[j][0] ** 2 + T[j][1] ** 2 > value:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def bucket_sort(T, k):
    buckets = []
    i = 1
    j = 0
    first = k / (len(T) / 5)
    while j < k:
        j = first * sqrt(i)
        buckets.append([])
        i += 1
    for i in range(len(T)):
        d = sqrt(T[i][0] ** 2 + T[i][1] ** 2) / k
        idx = int(len(buckets) * d)
        buckets[idx].append(T[i])
    for i in range(len(buckets)):
        insertion_sort(buckets[i])
    result = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])
    return result


T = [(0, 0), (0.7, 0.1), (1, 1), (-1, -1), (0, 1), (-1, -2), (1.3, 0.2), (1.5, -1.5), (1.7, -1.3),
     (0.4, 1.9), (0.3, 0.1), (1.6, 0.2), (0.3, 0.3)]
k = 4
print(bucket_sort(T, k))
