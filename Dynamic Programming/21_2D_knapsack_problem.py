# Algorithm for two-dimensional version of discrette knapsack problem. We are given set of P = {p1, ..., pn}
# items and for each p[i] item are given three number:
#   1. v(p[i]) - value of an item
#   2. w(p[i]) - weight of an item
#   3. h(p[i]) - height of an item
# The thief wants to select items with maximum value that total weight of an items doesn't exceed
# a given number W (that is a total weight) and a given number H (that is a total height). The items
# are packed in boxes that the thief places them on top of each other.

def knapsack_problem_2D(P, W, H):
    DP = [[[0] * (len(P) + 1) for _ in range(W + 1)] for _ in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            for k in range(1, len(P) + 1):
                value = P[k - 1][0]
                weight = P[k - 1][1]
                height = P[k - 1][2]
                if i - height >= 0 and j - weight >= 0:
                    DP[i][j][k] = max(DP[i][j][k], DP[i][j][k - 1],
                                      DP[i - height][j - weight][k - 1] + value)
                else:
                    DP[i][j][k] = max(DP[i][j][k], DP[i][j][k - 1])
    return DP[-1][-1][-1]


P = [(10, 4, 2), (8, 5, 3), (4, 12, 1), (5, 9, 7), (3, 1, 4), (7, 13, 4)]
# (value, weight, height)
W = 24
H = 9
print(knapsack_problem_2D(P, W, H))
