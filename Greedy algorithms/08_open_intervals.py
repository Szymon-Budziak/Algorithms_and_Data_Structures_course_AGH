# We are given a set of open intervals. Find a subset of this set such that:
#   1) its size is exactly k,
#   2) intervals are disjoint,
#   3) the difference between the earliest start and farthest end is minimal.
# If there is no solution, the algorithm should say no.
from math import inf


def open_intervals(T, k):
    T.sort(key=lambda x: x[1])
    best_result = inf
    result = []
    for i in range(len(T) - k):
        actual = [T[i]]
        j = 1
        l = i + 1
        while j < k and l < len(T):
            if actual[j - 1][1] <= T[l][0]:
                actual.append(T[l])
                j += 1
            l += 1
        actual_result = actual[j - 1][1] - actual[0][0]
        if actual_result < best_result and j == k:
            best_result = actual_result
            result = actual[:]
    if len(result) == 0:
        return False
    return result


T = [(1, 7), (2, 5), (3, 4), (8, 10), (3, 6), (2, 4), (5, 9), (7, 8), (1, 5), (1, 2), (2, 5)]
print(open_intervals(T, 3))
