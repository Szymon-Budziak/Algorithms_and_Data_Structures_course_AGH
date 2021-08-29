# We are given an array of n numbers [a1, a2, ..., an]. Rearrange these numbers to satisfy
# |a[1] − a[2]| <= |a[2] − a[3]| <= ... <= |a[n−1] − a[n]|, where |x| denotes absolute value of x.
# It's always possible to find such rearrangement. Note that all numbers in a are not necessarily
# different. In other words, some numbers of a may be same. Return the rearranged version of array
# which satisfies given condition. If there are multiple valid rearrangements, return any of them.
from math import inf


def merge(T, p, q, r):
    L = T[p:q + 1]
    R = T[q + 1:r + 1]
    L.append(inf)
    R.append(inf)
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def merge_sort(T, p, r):
    if len(T) <= 1:
        return T
    elif p < r:
        m = (p + r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m + 1, r)
        merge(T, p, m, r)


def sorted_adjacent_differences(T):
    merge_sort(T, 0, len(T) - 1)
    i = (len(T) - 1) // 2
    result = [T[i]]
    j = i - 1
    k = i + 1
    while j > -1 or k < len(T):
        if k < len(T):
            result.append(T[k])
            k += 1
        if j > -1:
            result.append(T[j])
            j -= 1
    return result


T = [-6, -7, 5, -10, -5, 3, 7, 4, -3]
print(sorted_adjacent_differences(T))
