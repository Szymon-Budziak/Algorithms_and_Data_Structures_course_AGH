# We are given a function dict(word) that always works in O(1) time, which returns if a word is
# a correct word of the language. We are given as an input a string without a space. Find an algorithm
# that will find out if it is possible to insert spaces in the input string so that the string of
# word we receive creates word from the given language.
# For example: “alamakotainiemapsa” we can split as “ala ma kota i nie ma psa".
# The algorithm should be fast, but the most important thing is that it should be correct.


def dict(word):
    words = ['ala', 'ma', 'kota', 'i', 'nie', 'ma', 'psa']
    if word in words:
        return True
    return False


def correct_word(string):
    DP = [False] * (len(string) + 1)
    DP[0] = True
    for i in range(len(string) + 1):
        for j in range(i, -1, -1):
            if DP[i]:
                break
            actual_word = string[j: i]
            if dict(actual_word):
                DP[i] = DP[j]
    return DP[-1]


string = "alamakotainiemapsa"
print(correct_word(string))
