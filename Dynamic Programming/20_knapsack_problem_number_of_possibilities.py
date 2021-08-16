# A thief breaks into a store with items with their weights and prices that are natural numbers. He
# hides them into his backpack, in which he can carry items with maximum weights of W. Yes, ew know this
# story. But this time the thief doesn't want to steal the items of the highest possible price. He is
# interested in how many ways can he select items so that their total price is at least C and their
# total weights doesn't exceed W.


def knapsack_problem(items, W, C):
    DP = [[[0] * (C + 1) for _ in range(W + 1)] for _ in range(len(items) + 1)]
    for i in range(len(items) + 1):
        DP[i][0][0] = 1
    for i in range(W + 1):
        DP[0][i][0] = 1
    for i in range(1, len(items) + 1):
        for j in range(1, W + 1):
            for k in range(C + 1):
                if j > items[i - 1][1]:
                    DP[i][j][k] = DP[i - 1][j - items[i - 1][1]][max(0, k - items[i - 1][0])] + DP[i - 1][j][k]
    return DP[-1][W][C]


# [value, weight]
items = [[4, 2], [3, 1], [1, 2], [2, 2], [4, 4], [2, 1], [2, 3]]
W = 8
C = 6
print(knapsack_problem(items, W, C))
