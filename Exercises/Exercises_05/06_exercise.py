# Rozważmy ciąg (a[0], ..., a[n−1]) liczb naturalnych. Załóżmy, że został podzielony na k spójnych
# podciągów: (a[0], ..., a[l1]), (a[l1 +1], ..., a[l2]), ..., (a[lk−1 + 1], ..., a[n−1]). Przez wartość
# i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej
# wartości (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego
# podciągu. Zadanie polega na znalezienie podziału ciągu (a[0], ..., a[n−1]) o maksymalnej wartości.


def divide_sequence(T, k):
    DP = [[0] * len(T) for _ in range(k)]
    count = 0
    for i in range(len(T)):
        count += T[i]
        DP[0][i] = count
    for i in range(1, k):
        for j in range(i, len(T)):
            summary = 0
            for m in range(j - 1, i - 2, -1):
                summary += T[m + 1]
                DP[i][j] = max(DP[i][j], min(DP[i - 1][m], summary))
    return DP[k - 1][len(T) - 1]


T = [6, 2, 8, 19, 25, 31, 4, 22, 11, 18, 13, 38, 33, 15, 7]
k = 5
print(divide_sequence(T, k))
