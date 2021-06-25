# We are given a three data sets represented as arrays: A, B and C. Find algorithm that determines
# if there is a triplet a,b and c respectively from A, B and C that a + b = c.


# 1st solution:


def partition(T, l, r):
    pivot = T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, l, r):
    while l < r:
        q = partition(T, l, r)
        if q - l <= r - q:
            quicksort(T, l, q - 1)
            l = q + 1
        else:
            quicksort(T, q, r)
            r = q - 1


def is_sum_equal_a_and_b_sort(A, B, C):
    quicksort(A, 0, len(A) - 1)
    quicksort(B, 0, len(B) - 1)
    for i in range(len(C)):
        a = 0
        b = len(B) - 1
        while a < len(A) and b >= 0:
            if A[a] + B[b] == C[i]:
                return True
            elif A[a] + B[b] > C[i]:
                b -= 1
            else:
                a += 1
    return False


# 2nd solution:


def binary_search(T, l, r, x):
    if r >= l:
        mid = (l + r) // 2
        if T[mid] == x:
            return True
        elif T[mid] > x:
            return binary_search(T, l, mid - 1, x)
        else:
            return binary_search(T, mid + 1, r, x)
    return False


def is_sum_equal_c_sort(A, B, C):
    quicksort(C, 0, len(C) - 1)
    for i in range(len(A)):
        for j in range(len(B)):
            summary = A[i] + B[j]
            if binary_search(C, 0, len(C) - 1, summary):
                return True
    return False


A = [3, 2, 56, 3, 11, 78, 5, 9]
B = [34, 7, 3, 5, 7, 2, 56, 8]
C = [53, 3, 79, 19, 65, 89, 1]
print(is_sum_equal_a_and_b_sort(A, B, C))
A = [3, 16, 7, 8, 19, 2, 11, 26]
B = [14, 5, 22, 4, 8, 16, 3, 5, 2]
C = [3, 73, 26, 37, 49, 52]
print(is_sum_equal_c_sort(A, B, C))
