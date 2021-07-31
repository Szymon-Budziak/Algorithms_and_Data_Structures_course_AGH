# We are given a word as an array of n characters from the E alphabet of size |E|. We are given
# k number also. The word length is at least |E|^k. Find algorithm that will return the most frequently
# repeats string of length k in this word. The algorithm is supposed to run in O(n) time complexity
# and use O(1) memory. Moreover, the contents of the array should remain unchanged after the execution
# of the algorithm.
from math import pow


def e_conversion(actual_word, e, k):
    result = 0
    idx = 0
    for i in range(len(actual_word) - 1, -1, -1):
        result += pow(e, idx) * (actual_word[i] % k)
        idx += 1
    return int(result)


def convert_to_letter(word, index, e, k):
    result = []
    for i in range(k):
        result.append(word[index] % e)
        index = word[index] // e
    result.reverse()
    for i in range(len(result)):
        result[i] = chr(ord('a') + result[i])
    return result


def the_most_frequently_repeated_string(word, e, k):
    for i in range(len(word)):
        word[i] = ord(word[i]) - ord('a')
    for i in range(len(word) - 1):
        actual_word = word[i:i + k]
        word[e_conversion(actual_word, e, k)] += e
    maximum = index = 0
    for i in range(len(word)):
        if word[i] > maximum:
            index = i
            maximum = word[i]
    return convert_to_letter(word, index, e, k)


word = ['a', 'b', 'b', 'a', 'c', 'a', 'c', 'a', 'c', 'b']
e = 3
k = 2
print(the_most_frequently_repeated_string(word, e, k))
