# We are given two sets of numbers that are represented as arrays of size m and n in which
# m is significantly less than n. Find algorithm that checks if the sets are disjoint.


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
        quicksort(T, p, q - 1)
        p = q + 1


def binary_search(T, p, r, x):
    if r >= p:
        mid = (p + r) // 2
        if T[mid] == x:
            return True
        elif T[mid] > x:
            return binary_search(T, p, mid - 1, x)
        else:
            return binary_search(T, mid + 1, r, x)
    return False


def disjoint_sets(m, n):
    quicksort(m, 0, len(m) - 1)
    for i in range(len(n)):
        if binary_search(m, 0, len(m) - 1, n[i]):
            return False
    return True


m = [8, 5, 17, 3, 1]
n = [14, 12, 4, 9, 31, 9, 2, 22, 31, 7, 20, 6, 11, 18]
print(disjoint_sets(m, n))
