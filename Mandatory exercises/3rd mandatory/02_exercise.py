# W problemie sumy podzbioru mamy dany ciąg liczb naturalnych A[0], ..., A[n-1]
# oraz liczbę T. Należy stwierdzić czy istnieje podciąg sumujący się dokładnie do T.


def is_subsequence_sum(A, summary):
    T = [[False for _ in range(summary+1)] for _ in range(len(A)+1)]
    for i in range(len(A)+1):
        T[i][0] = True
    for i in range(1, len(A)+1):
        for j in range(1, summary+1):
            if A[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = (T[i-1][j] or T[i-1][j-A[i-1]])
    return T[len(A)][summary]


A = [14, 5, 19, 3, 20, 14, 8, 7, 2]
summary = 29
print(is_subsequence_sum(A, summary))
