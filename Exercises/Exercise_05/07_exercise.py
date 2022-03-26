# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać
# algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, wydający
# najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).
from math import inf


def coin_change(coins, total_money):
    DP = [inf] * (total_money + 1)
    DP[0] = 0
    for i in range(len(coins)):
        for j in range(total_money - coins[i] + 1):
            DP[j + coins[i]] = min(DP[j + coins[i]], DP[j] + 1)
    return DP[total_money]


T = 18
coins = [1, 2, 5, 10]
print(coin_change(coins, T))
