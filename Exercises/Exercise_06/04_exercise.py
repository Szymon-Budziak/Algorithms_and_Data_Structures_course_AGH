# Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n−1, skacząc wyłącznie w kierunku
# większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a jej
# energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście
# na niektórych liczbach — także na zerze — leżą przekąski o określonej wartości energetycznej (wartość
# przekąski dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza
# minimalną liczbę skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami
# energetycznymi przekąsek na każdej z liczb.
from math import inf


def jumping_frog(A):
    count = 0
    for i in range(len(A)):
        count += A[i]
    DP = [[inf] * (count + 1) for _ in range(len(A))]
    DP[0][A[0]] = 0
    for i in range(len(A)):
        for j in range(count):
            if DP[i][j] != inf:
                k = i + 1
                while k < len(A) and j >= k - i:
                    index = i + j + A[k] - k
                    DP[k][index] = min(DP[k][index], DP[i][j] + 1)
                    k += 1
    return min(DP[-1])


A = [4, 5, 2, 4, 1, 2, 1, 0]
print(jumping_frog(A))
