# Given an array of numbers that represent each coin. The number of coins we have are
# infinity, so we do not need to worry about how many coins are at uor disposal. Then
# we are given an amount and asked to find the minimum number of coins that are needed
# to make that amount.


def coin_change(coins, amount):
    coins.sort(reverse=True)
    idx = count = 0
    while idx <= len(coins) - 1:
        if coins[idx] <= amount:
            amount -= coins[idx]
            count += 1
        else:
            idx += 1
    return count


amount = 237
coins = [1, 10, 100, 25, 5]
print(coin_change(coins, amount))
