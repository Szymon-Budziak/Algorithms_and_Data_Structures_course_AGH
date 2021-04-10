# Find the length of the longest subsequence of a given sequence such that
# all elements of the subsequence are sorted in increasing order. Also print
# this subsequence.


# 1st solution: complexity of O(n^2)


def longest_increasing_subsequence(T):
    F = [1]*len(T)
    P = [-1]*len(T)
    for i in range(1, len(T)):
        for j in range(i):
            if T[j] < T[i] and F[j]+1 > F[i]:
                F[i] = F[j]+1
                P[i] = j
    return (max(F), F, P)


def print_solution(T, P, i):
    if P[i] != -1:
        print_solution(T, P, P[i])
    print(T[i], end=" ")


# 2nd solution: complexity of O(n*log(n))


def binary_search(A, i, j, k):
    while j-i > 1:
        m = i + (j-i)//2
        if A[m] >= k:
            j = m
        else:
            i = m
    return j


def longest_increasing_subsequence_2(T):
    A = [0]*(len(T)+1)
    A[0] = T[0]
    length = 1
    for i in range(1, len(T)):
        if T[i] < A[0]:
            A[0] = T[i]
        elif T[i] > A[length-1]:
            A[length] = T[i]
            length += 1
        else:
            index = binary_search(A, -1, length-1, T[i])
            A[index] = T[i]
    return length


T = [13, 7, 21, 42, 8, 2, 44, 53]
length, F, P = longest_increasing_subsequence(T)
print("1st:", length)
print("2nd:", longest_increasing_subsequence_2(T))
print_solution(T, P, 7)
