# We are given an infinite array A in which the first n indexes contain sorted natural numbers
# and the reminder of the array have None values. The value of n is not given. Find algorithm
# that for a given natural number x finds the index in the array with the value of x. If there
# is not such an index, algorithm should return None.


def binary_search(T, x, l, r):
    if r >= l:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            return binary_search(T, x, l, mid - 1)
        else:
            return binary_search(T, x, mid + 1, r)
    else:
        return None


def find_index(T, x):
    i = 1
    while T[i] is not None and T[i] <= x:
        i *= 2
    return binary_search(T, x, 0, i)


T = [1, 2, 3, 5, 6, 8, 10, 21, 22, 24, 32, 65, 65, 71, 74, None, None, None, None, None, None, None, None]
print(find_index(T, 24))
