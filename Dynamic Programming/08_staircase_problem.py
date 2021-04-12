# We are given a distance n. Count the total number of ways to cover the distance
# using 1, 2, 3 steps.


# 1st solution: time complexity O(n) and space complexity O(n)


def staircase_jump(n):
    dp = [0] * (n+1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]


# 2nd solution: time complexity O(n) and space complexity O(1)


def staircase_jump2(n):
    if n == 0:
        return 0
    if n <= 2:
        return n
    jump0 = 1
    jump1 = 1
    jump2 = 2
    result = 0
    for i in range(3, n+1):
        result = jump0+jump1+jump2
        jump0 = jump1
        jump1 = jump2
        jump2 = result
    return result


n = 6
print(staircase_jump(n))
print(staircase_jump2(n))
