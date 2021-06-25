# We are given an array of 2n real numbers. Find algorithm that divides these numbers into
# n pairs such that the division will have the smallest maximum sum of the numbers in pairs.
# For example, for numbers (1, 3, 5, 9) we can have ranges ((1, 3), (5, 9)), ((1, 5), (3, 9))
# and ((1, 9), (3, 5)). The sums of the pairs for these divisions are (4, 14), (6, 12)
# and (10, 8), so the maximum sums are 14, 12 and 10. It follows that the last division has
# the smallest maximum sum.


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


def the_lowest_maximum_sum(T):
    quicksort(T, 0, len(T) - 1)
    A = []
    for i in range(len(T) // 2):
        A.append((T[i], T[-1 - i]))
    return A


T = [5, 3, 78, 3, 2, 7, 4, 34, 12, 9, 26, 4, 1, 8]
print(the_lowest_maximum_sum(T))
