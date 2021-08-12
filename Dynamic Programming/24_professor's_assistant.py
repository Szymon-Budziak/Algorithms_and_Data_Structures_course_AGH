# An assistant of a famous professor was instructed to calculate the sum of a certain sequence of
# numbers (numbers can be both positive and negative). In order to minimize the rounding of errors,
# the assistant decided to perform the above additions in such a sequence that the highest in
# absolute value temporary result (the result of each addition operation; we also treat the value of
# the final sum as a temporary result) was as small as possible. To make the task easier, the assistant
# does not change the order of the numbers in the sum but only selects the order of addition operation.
# Write an opt_sum function that takes as a parameter an array of numbers n1, n2, ..., nk (in the order
# in which they appear in total; we assume that the array contains at least two numbers) and it returns
# the largest absolute value of the temporary result in the optimal order of addition.
# For example for an array: [1, -5, 2] the function should return 3, which corresponds to adding -5 and
# 2 and then adding 1 to the result.
from math import inf


def opt_sum(T):
    prefix = [0] * (len(T) + 1)
    for i in range(len(T)):
        prefix[i + 1] = prefix[i] + T[i]
    DP = [[0] * len(T) for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(len(T) - i):
            DP[j][i + j] = prefix[i + j + 1] - prefix[j]
            best_value = inf
            for k in range(j, i + j):
                best_value = min(max(abs(DP[j][k]), abs(DP[k + 1][i + j])), abs(best_value))
            DP[j][i + j] = max(abs(best_value), abs(DP[j][i + j]))
    return abs(DP[0][len(T) - 1])


T = [1, -5, 2]
print(opt_sum(T))
