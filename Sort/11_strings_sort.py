# We are given an array of strings, in which the sum of the lengths of all strings is n. Find algorithm
# that sorts this array in O(n) time. It can be assumed that the strings consist only of lower case
# letters of the Latin alphabet.

def counting_sort(T, i):
    count = [0] * (ord('z') - ord('a') + 1)
    for j in range(len(T)):
        count[ord(T[j][i]) - ord('a')] += 1
    for j in range(1, len(count)):
        count[j] += count[j - 1]
    result = [0] * len(T)
    for j in range(len(T) - 1, -1, -1):
        index = ord(T[j][i]) - ord('a')
        result[count[index] - 1] = T[j]
        count[index] -= 1
    for i in range(len(T)):
        T[i] = result[i]


def radix_sort(T):
    for i in range(len(T[0]) - 1, -1, -1):
        counting_sort(T, i)


def strings_sort(strings):
    for i in range(len(strings)):
        strings[i] = (len(strings[i]), strings[i])
    maximum = 0
    for i in range(len(strings)):
        maximum = max(maximum, strings[i][0])
    buckets = [[] for _ in range(maximum + 1)]
    for i in range(len(strings)):
        buckets[strings[i][0]].append(strings[i][1])
    for i in range(len(buckets)):
        if len(buckets[i]) != 0:
            radix_sort(buckets[i])
    result = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])
    return result


strings = ["zyb", "cfv", "ge", "u", "pr", "l", "cav", "xacdf", "bfq", "qsdf", "hjgd", "bgfp",
           "fasxc", "sdfgq", "bvcn", "q", "x", "ap", "ar", "hfg", "bs"]
print(strings_sort(strings))
