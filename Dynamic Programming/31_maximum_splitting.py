# We are given a single positive integer n. We are to represent n as a sum of maximum possible number
# of composite summands and print this maximum number, or print -1, if there are no such splittings.
# An integer greater than 1 is composite, if it is not prime, i.e. if it has positive divisors not
# equal to 1 and the integer itself. Return the maximum possible number of summands in a valid
# splitting to composite summands, or -1, if there are no such splittings.


def maximum_splitting(number):
    if number < 3:
        return -1
    else:
        DP = [-1] * 17
        DP[0] = 0
        for j in range(4, 17):
            for k in [4, 6, 9]:
                if j >= k and DP[j - k] != -1:
                    DP[j] = max(DP[j], DP[j - k] + 1)
        if 4 < number < 16:
            return DP[number]
        else:
            index = (number - 16) // 4 + 1
            return DP[number - index * 4] + index


number = 18
print(maximum_splitting(number))
