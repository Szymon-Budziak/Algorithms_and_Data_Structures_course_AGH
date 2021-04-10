# We are given an array of numbers that represent each coin. The number of coins
# we have are infinity, so we do not need to worry about how many coins are
# at uor disposal. Then we are given an amount and asked to find the minimum
# number of coins that are needed to make that amount.


def count_coin_changes(coins, number):
    ways = [0]*(number+1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(len(ways)):
            if coins[i] <= j:
                ways[j] += ways[j-coins[i]]
    return ways[number]


number = 11
coins = [1, 2, 10]
print(count_coin_changes(coins, number))
