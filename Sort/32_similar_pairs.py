# We call two numbers x and y similar if they have the same parity (the same remainder when divided
# by 2), or if |x−y|=1. For example, in each of the pairs (2,6), (4,3), (11,7), the numbers are similar
# to each other, and in the pairs (1,4), (3,12), they are not. We are given an array a of n (n is even)
# positive integers. Check if there is such a partition of the array into pairs that each element of
# the array belongs to exactly one pair and the numbers in each pair are similar to each other.
# Print YES if the such a partition exists, NO otherwise.


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


def similar_pairs(T):
    for i in range(len(T)):
        quicksort(T[i], 0, len(T[i]) - 1)
    for i in range(len(T)):
        even = odd = 0
        for j in range(len(T[i])):
            if T[i][j] % 2 == 0:
                even += 1
            else:
                odd += 1
        if even % 2 != odd % 2:
            print('NO')
        elif even % 2 == 0 and odd % 2 == 0:
            print('YES')
        else:
            flag = False
            for j in range(len(T[i]) - 1):
                for k in range(j + 1, len(T[i])):
                    if T[i][j] % 2 != T[i][k] % 2 and abs(T[i][k] - abs(T[i][j])) == 1:
                        flag = True
                        break
            if flag:
                print('YES')
            else:
                print('NO')


T = [[11, 14, 16, 12], [1, 8], [21, 80, 22, 45, 11, 67, 67, 74, 91, 4], [54, 62, 25, 35], [1, 12, 3, 10, 5, 8]]
similar_pairs(T)
