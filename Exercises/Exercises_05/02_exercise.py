# W problemie sumy podzbioru mamy dany ciąg liczb naturalnych A[0], ..., A[n-1]
# oraz liczbę T. Należy stwierdzić czy istnieje podciąg sumujący się dokładnie do T.


def sub_sum(T, s):
    if s < 0:
        return False
    q = [[False for _ in range(s+1)] for _ in range(len(T)+1)]
    for i in range(len(T)+1):
        q[i][0] = True
    for i in range(1, len(T)+1):
        for j in range(1, s+1):
            if T[i-1] > j:
                q[i][j] = q[i-1][j]
            else:
                q[i][j] = (q[i-1][j] or q[i-1][j-T[i-1]])
    return q[len(T)][s]


T = [14, 5, 19, 3, 20, 14, 8, 7, 2]
s = 34
print(sub_sum(T, s))
