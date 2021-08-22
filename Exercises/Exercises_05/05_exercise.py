# Dany jest cięg macierzy A[1], A[2], ..., A[n]. Ktoś chce policzyć iloczyn A[1]A[2]...A[n]. Macierze
# nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej kolejnosci
# wykonujemy mnożenia, koszt obliczeniowy moze byc różny — należy podać algorytm znajdujący koszt
# mnożenia przy optymalnym doborze kolejności.
from math import inf


def matrix_multiplication(T):
    min_multi = [[0] * len(T) for _ in range(len(T))]
    for i in range(1, len(T)):
        min_multi[i][i] = 0
    for L in range(2, len(T)):
        for i in range(1, len(T) - L + 1):
            k = i + L - 1
            min_multi[i][k] = inf
            for j in range(i, k):
                p = min_multi[i][j] + min_multi[j + 1][k] + (T[i - 1] * T[j] * T[k])
                if p < min_multi[i][k]:
                    min_multi[i][k] = p
    return min_multi[1][len(T) - 1]


T = [2, 4, 5, 7, 3]
print(matrix_multiplication(T))
