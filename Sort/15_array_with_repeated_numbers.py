# We are given an array with integers. It contains a lot of repetitions. Moreover, only O(log(n))
# numbers are unique (the rest are repetitions). Find algorithm that sorts such an array in
# O(n*log(log(n))) time.


def insertion_sort(T):
    for i in range(len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j][0] > key[0]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def binary_search(A, r, x, l=0):
    if r >= l:
        mid = (r + l) // 2
        if A[mid][0] == x:
            return mid
        elif A[mid][0] < x:
            return binary_search(A, r, x, mid + 1)
        else:
            return binary_search(A, mid - 1, x, l)
    return -1


def repeated_numbers(T):
    A = []
    for i in range(len(T)):
        result = binary_search(A, len(A) - 1, T[i])
        if result == -1:
            A.append([T[i], 1])
            insertion_sort(A)
        else:
            A[result][1] += 1
    idx = 0
    for i in range(len(A)):
        for j in range(A[i][1]):
            T[idx] = A[i][0]
            idx += 1
    return T


T = [173, 11, 173, 173, 39, 11, 39, 4, 39, 4, 4, 11, 4, 11, 4, 39]
print(repeated_numbers(T))
