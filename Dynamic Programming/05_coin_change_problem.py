# We are given an array of numbers that represent each coin. The number of coins we have are infinity,
# so we do not need to worry about how many coins are at our disposal. Then we are given an amount and
# asked to find how many ways can we make the change.


def count_coin_changes(coins, total_money):
    ways = [0] * (total_money + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(len(ways)):
            if coins[i] <= j:
                ways[j] += ways[j - coins[i]]
    return ways[total_money]


total_money = 11
coins = [1, 2, 10]
print(count_coin_changes(coins, total_money))
