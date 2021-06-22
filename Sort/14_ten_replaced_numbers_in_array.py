# We are given an array with n (n >= 11) natural numbers in the range [0, k]. 10 numbers from this array
# were replaced with random numbers outside this range (e.g. much greater or negative numbers). Find
# algorithm that sorts the array in the O(n) time.
from math import inf


def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def replaced_numbers(T, k):
    normal_numbers = []
    out_of_range_numbers = []
    for i in range(len(T)):
        if T[i] >= 0 and T[i] <= k:
            normal_numbers.append(T[i])
        else:
            out_of_range_numbers.append(T[i])
    insertion_sort(out_of_range_numbers)
    result = merge(normal_numbers, out_of_range_numbers)
    return result


def merge(array1, array2):
    result = [0] * (len(array1) + len(array2))
    array1.append(inf)
    array2.append(inf)
    i = j = k = 0
    while array1[i] != inf and array2[j] != inf:
        if array1[i] <= array2[j]:
            result[k] = array1[i]
            i += 1
            k += 1
        else:
            result[k] = array2[j]
            j += 1
            k += 1
    while array1[i] != inf:
        result[k] = array1[i]
        i += 1
        k += 1
    while array2[j] != inf:
        result[k] = array2[j]
        j += 1
        k += 1
    return result


T = [1, -100, 2, 3, 32, 6, 7, 7, -203, 8, 9, -42, 14, 15, 57, 16, 67, 18, 46, 19, 65, 19, 20, 91, 134, 21, 25]
k = 25
print(replaced_numbers(T, k))
