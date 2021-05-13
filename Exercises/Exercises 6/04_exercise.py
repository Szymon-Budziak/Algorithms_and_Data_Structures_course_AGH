# Pewna żaba skacze po osi liczbowej. Ma się dostać z 0 do n-1., skacząc wyłącznie
# w kierunku większych liczb. Skok z liczby i do j (j>i) kosztuje ją j-i jednostek
# energii, a jej energia nigdy nie może spaść poniżej 0. Na początku żaba ma 0
# jednostek energi, ale na szczęście na niektórych liczbach - także na 0 - leżą
# przekąski o określonej wartości energetycznej (wartości przekąski dodaje się do
# aktualnej energii żaby). Proszę zaproponować algorytm, który oblicza minimalną
# liczbę skoków potrzebną na dotarcie z 0 do n-1 mając daną tablicę A z wartościami
# energetycznymi przekąsek na każdej z liczb.
from math import inf


def jumping_frog(A):
    count = 0
    for i in range(len(A)):
        count += A[i]
    DP = [[inf]*count for _ in range(len(A))]
    DP[0][A[0]] = 0
    for i in range(1, len(A)):
        for j in range(count):
            for k in range(1, i+1):
                if j+k-A[i] >= 0 and j+k-A[i] < count:
                    DP[i][j] = min(DP[i][j], DP[i-k][j+k-A[i]]+1)
    return min(DP[-1])


A = [4, 5, 2, 4, 1, 2, 1, 0]
print(jumping_frog(A))
