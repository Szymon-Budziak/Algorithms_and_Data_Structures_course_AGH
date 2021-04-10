# We are given two strings string1 and string2 and below operations that can be
# performed on string1. Find minimum number of edits (operations) required to convert
# string1 into string2.
# 1. Insert
# 2. Remove
# 3. Replace
# All the above operations are of equal cost.


def minimum_distance(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    dp = [[0]*(len1+1) for _ in range(len2+1)]
    for i in range(len1 + 1):
        dp[0][i] = i
    for i in range(len2+1):
        dp[i][0] = i
    for i in range(len2):
        for j in range(len1):
            if string1[j] == string2[i]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j], dp[i][j+1])+1
    return dp[len2][len1]


string1 = "abcdefg"
string2 = "azcefh"
print(minimum_distance(string1, string2))
