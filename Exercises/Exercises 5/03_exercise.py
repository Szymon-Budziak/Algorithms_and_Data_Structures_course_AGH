# Znajdź długość najdłuższego wspólnego podciągu A[n], B[n].


def longest_common_subsequence(A, B):
    len_a = len(A)
    len_b = len(B)
    T = [[0]*(len_a+1) for _ in range(len_b+1)]
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i == 0 or j == 0:
                T[i][j] = 0
            if A[i-1] == B[j-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T[len_a][len_b]


A = [1, 5, 4, 2, 0]
B = [4, 5, 2, 0, 9]
print(longest_common_subsequence(A, B))
