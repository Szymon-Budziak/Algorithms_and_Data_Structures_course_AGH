# We are given an integer array [a1, a2, ..., an]. The array B is called to be a subsequence of A if
# it is possible to remove some elements from A to get B. Array [b1, b2, ..., bk] is called to be good
# if it is not empty and for every i (1 <= i <= k) bi is divisible by i. Find the number of good
# subsequences in a modulo 10^9 + 7. Two subsequences are considered different if index sets of numbers
# included in them are different. That is, the values of the elements do not matter in the comparison
# of subsequences. In particular, the array a has exactly 2^n − 1 different subsequences (excluding an
# empty subsequence). Return the number of good subsequences taken modulo 10^9 + 7.
from math import sqrt


def multiplicity(T):
    mod = 10 ** 9 + 7
    DP = [0] * 1000001
    DP[0] = 1
    for i in range(len(T)):
        current = []
        for j in range(1, int(sqrt(T[i])) + 1):
            if T[i] % j == 0:
                current.append(j)
                if T[i] // j != j:
                    current.append(T[i] // j)
        current.sort(reverse=True)
        for j in range(len(current)):
            DP[current[j]] += DP[current[j] - 1]
            DP[current[j]] %= mod
    count = 0
    for i in range(1, len(T) + 1):
        count += DP[i]
    count %= mod
    return count


T = [230070, 37311, 92074, 618927, 991732, 129711, 612126, 541583, 552857, 299118, 773097, 33928]
print(multiplicity(T))
