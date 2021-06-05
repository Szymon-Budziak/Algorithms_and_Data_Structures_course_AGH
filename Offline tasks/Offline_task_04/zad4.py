def print_solution(A, P, T, index):
    summary = 0
    if len(P[index]) == 0:
        T.append(A[index])
        for j in range(len(T)):
            print(T[j], end=" ")
        print()
        summary += 1
        T.pop()
    for i in range(len(P[index])):
        T.append(A[index])
        summary += print_solution(A, P, T, P[index][i])
        T.pop()
    return summary


def printAllLIS(A):
    A.reverse()
    F = [1]*len(A)
    P = [[] for _ in range(len(A))]
    for i in range(1, len(A)):
        for j in range(i, -1, -1):
            if A[j] > A[i] and F[j]+1 > F[i]:
                F[i] = F[j]+1
                P[i] = [j]
            elif A[j] > A[i] and F[j]+1 == F[i]:
                P[i] += [j]
    max_len = max(F)
    T = []
    summary = 0
    for i in range(len(F)-1, -1, -1):
        if F[i] == max_len:
            summary += print_solution(A, P, T, i)
    return summary


A = [2, 1, 4, 3, 6, 2, 8, 7]
print(printAllLIS(A))
