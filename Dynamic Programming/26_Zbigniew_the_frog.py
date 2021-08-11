# Zbigniew the frog jumps on the number line. He has to go from 0 to n-1 only jumping towards the larger
# numbers. Jump from i to j (j > i) costs Zbigniew 5 units of energy and his energy cannot drop below 0.
# At the beginning, Zbigniew has 0 units of energy but luckily some numbers (also on 0) contain snacks
# with a certain energy value (the value of a snack adds to the current energy of Zbigniew).
# Implement a function called zbigniew(A) which gets as an input an array A of length len(A) = n, where
# each field contains the energy value of the snack lying on the corresponding number. The function should
# return the minimum number of jumps needed for Zbigniew to get from 0 to n-1 or return -1 if it not possible.
from math import inf


def zbigniew(A):
    count = 0
    for i in range(len(A)):
        count += A[i]
    DP = [[inf] * (count + 1) for _ in range(len(A))]
    DP[0][A[0]] = 0
    for i in range(len(A)):
        for j in range(count):
            if DP[i][j] != inf:
                k = i + 1
                while k < len(A) and j >= k - i:
                    index = i + j + A[k] - k
                    DP[k][index] = min(DP[k][index], DP[i][j] + 1)
                    k += 1
    return min(DP[-1])


A = [4, 5, 2, 2, 6, 8, 47, 1, 4, 1, 2, 0]
print(zbigniew(A))
