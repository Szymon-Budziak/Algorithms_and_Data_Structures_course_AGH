# We are given a sequence of strings (words) S = [s[1], ..., s[n]] and a certain string t. It is known
# that t can be written as a concatenation of a certain number of strings from S (with repetition).
# For example for S = [s[1], s[2], s[3], s[4], s[5]] in which s[1] = 'ab', s[2] = 'abab', s[3] = 'ba',
# s[4] = 'bab', s[5] = 'b', string t = 'ababbab' can be written for example as s[2]s[4] or as
# s[1]s[1]s[3]s[5]. Such a selection of s[i] is called representation. By the width of the representation
# we mean the length of the shortest s[i] that belongs to the representation - for s[2]s[4] width is 3
# and for s[1]s[1]s[3]s[5] width is 1. Implement an algorithm that has S and t as an input and finds
# the maximum width of the t representation (i.e. the shortest string in its representation is the
# longest).
from math import inf


def maximum_width_of_representation(S, t):
    DP = [-inf] * len(t)
    for i in range(len(t)):
        for j in range(len(S)):
            substring = t[i - len(S[j]) + 1:i + 1]
            if S[j] == substring:
                if i > len(S[j]):
                    DP[i] = max(DP[i], min(DP[i - len(S[j])], len(S[j])))
                else:
                    DP[i] = max(DP[i], len(S[j]))
    return DP[-1]


S = ['ab', 'abab', 'ba', 'bab', 'b']
t = 'ababbab'
print(maximum_width_of_representation(S, t))
