# We are given a set of open intervals. Find a subset of this set such that:
#   1) its size is exactly k,
#   2) intervals are disjoint,
#   3) the difference between the earliest start and farthest end is minimal.
# If there is no solution, the algorithm should say no.


def open_intervals(T, k):
    T.sort(key=lambda x: x[1])
    start = T[0]
    count = 1
    for i in range(1, len(T)):
        if start[1] <= T[i][0]:
            start = T[i]
            count += 1
            if count == k:
                return True
    return "No"


T = [(1, 7), (2, 5), (3, 4), (8, 10), (3, 6), (2, 4), (5, 9), (7, 8), (1, 5), (1, 2), (2, 5)]
k = 4
print(open_intervals(T, k))
