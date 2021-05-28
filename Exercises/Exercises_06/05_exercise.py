# Algorytm dla dwuwymiarowej wersji dyskretnego problemu plecakowego. Mamy dany
# zbiór P = {p1, ..., pn} przedmiotów i dla każdego przedmiotu pi dane są
# następujące trzy liczby:
#   1. v(pi) - wartość przedmiotu
#   2. w(pi) - waga przedmiotu
#   3. h(pi) - wysokość przedmiotu
# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie
# przekracza danej liczby W oraz których łączna wysokość nie przekracza danej
# liczby H (przedmioty zapakowane są w kartony, które złodziej układa jeden na drugim).


def knapsack_problem_2D(P, W, H):
    DP = [[[0]*(len(P)+1) for _ in range(W+1)] for _ in range(H+1)]
    for i in range(1, H+1):
        for j in range(1, W+1):
            for k in range(1, len(P)+1):
                value = P[k-1][0]
                weight = P[k-1][1]
                height = P[k-1][2]
                if i-height >= 0 and j-weight >= 0:
                    DP[i][j][k] = max(DP[i][j][k], DP[i][j]
                                      [k-1], DP[i-height][j-weight][k-1]+value)
                else:
                    DP[i][j][k] = max(DP[i][j][k], DP[i][j][k-1])
    return DP[-1][-1][-1]


P = [(10, 4, 2), (8, 5, 3), (4, 12, 1), (5, 9, 7), (3, 1, 4), (7, 13, 4)]
# (value, weight, height)
W = 24
H = 9
print(knapsack_problem_2D(P, W, H))
