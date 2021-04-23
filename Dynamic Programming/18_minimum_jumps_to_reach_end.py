# Given an array of steps that can be made forward from actual element. What is
# the minimum number of jumps it takes to go from start of an array to the end of
# an array.
from math import inf


def print_solution(B, T):
    i = len(B)-1
    solution = list()
    solution.append(len(T)-1)
    while B[i] != -1:
        solution.append(B[i])
        i = B[i]
    solution.reverse()
    for i in range(len(solution)):
        print(solution[i], end=" ")
    print()


def jumps_to_end(T):
    A = [inf]*len(T)
    A[0] = 0
    B = [0]*len(T)
    B[0] = -1
    for i in range(1, len(T)):
        for j in range(i):
            if j+T[j] >= i:
                if A[j]+1 < A[i]:
                    B[i] = j
                A[i] = min(A[i], A[j]+1)
    print_solution(B, T)
    return A[-1]


T = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
print(jumps_to_end(T))
