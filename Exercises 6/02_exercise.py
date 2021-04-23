# Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], ..., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej
# 2 ciągu. Proszę zaproponować algorytm, który oblicza ile klocków należy usunąć
# z listy tak, żeby każdy kolejny spadający klocek mieścił się w całości w tamtym
# który spadł tuż przed nim.


def dropping_bricks(T):
    n = len(T)
    DP = [1]*n
    for i in range(1, n):
        for j in range(i):
            if T[i][0] >= T[j][0] and T[i][1] >= T[j][1]:
                DP[i] = DP[j] + 1
    return n - max(DP)


T = [[1, 10], [2, 5], [2, 7], [5, 8], [5, 6]]
print(dropping_bricks(T))
