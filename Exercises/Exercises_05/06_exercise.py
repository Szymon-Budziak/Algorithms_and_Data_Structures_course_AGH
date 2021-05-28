# Znajdź długość najdłuższego podciągu rosnącego A[n]:
#    1) wykorzystuje LCS
#    2) ma złożoność O(n*log(n))


def binary_search(A, i, j, k):
    while j-i > 1:
        m = i + (j-i)//2
        if A[m] >= k:
            j = m
        else:
            i = m
    return j


def longest_increasing_subsequence(A):
    T = [0]*(len(A)+1)
    T[0] = A[0]
    length = 1
    for i in range(1, len(A)):
        if A[i] < T[0]:
            T[0] = A[i]
        elif A[i] > T[length-1]:
            T[length] = A[i]
            length += 1
        else:
            index = binary_search(T, -1, length-1, A[i])
            T[index] = A[i]
    return length


A = [21, 11, 14, 15, 19, 2, 8, 55]
print(longest_increasing_subsequence(A))
