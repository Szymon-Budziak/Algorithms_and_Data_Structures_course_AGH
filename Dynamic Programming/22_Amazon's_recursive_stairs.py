# We are given an array A with natural numbers that are not less than 1. At the beginning we
# stand at position 0, the value A[i] informs us what us the maximum length of the jump to the
# next position. Example = [1, 3, 2, 1, 0]. From position 0, we can move to position 1. From
# position 1 we can move to position 2, 3, 4. Count on how many ways is it possible to go from
# position 0 to position n-1, respecting the rules of an array.


def recursive_stairs(T):
    DP = [0] * len(T)
    DP[len(T) - 2] = 1
    for i in range(len(T) - 3, -1, -1):
        actual_jump = T[i]
        for j in range(1, actual_jump + 1):
            if i + j == len(T) - 1:
                DP[i] += 1
            else:
                DP[i] += DP[i + j]
    return DP[0]


T = [2, 1, 3, 2, 1, 0]
print(recursive_stairs(T))
