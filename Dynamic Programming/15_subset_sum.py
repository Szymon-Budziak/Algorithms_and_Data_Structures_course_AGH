# Given a set of non-negative integers, and a value summary. Find if there is
# a subset of the given set with sum equal to given sum.


def subset_sum(D, summary):
    T = [[False for _ in range(summary+1)] for _ in range(len(D)+1)]
    for i in range(len(D)+1):
        T[i][0] = True
    for i in range(1, len(D)+1):
        for j in range(1, summary+1):
            if D[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = (T[i-1][j] or T[i-1][j-D[i-1]])
    return T[-1][-1]


D = [14, 5, 19, 3, 20, 14, 12, 7, 1]
summary = 18
print(subset_sum(D, summary))
