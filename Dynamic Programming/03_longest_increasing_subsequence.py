# Find the length of the longest subsequence of a given sequence such that
# all elements of the subsequence are sorted in increasing order. Also print
# this subsequence.


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


T = [13, 7, 21, 42, 8, 2, 44, 53]
length, F, P = longest_increasing_subsequence(T)
print(length)
print_solution(T, P, 7)
