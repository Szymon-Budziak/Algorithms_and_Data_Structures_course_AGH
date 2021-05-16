# We are given a string with some letters that are repeated in it. Find algorithm that will remove from
# string duplicates so that the resulting string will be lexicographically the smallest.
# Example: cbacdcbc, the answer is acdb


def the_smallest_lexicographically_string(string):
    count = [0] * 26
    for i in range(len(string)):
        count[ord(string[i]) - 97] += 1
    i = 0
    while i < len(count):
        if count[i] == 0:
            count.remove(count[i])
        else:
            i += 1
    visited = [False] * len(count)
    result = []
    a_ord = ord("a")
    for i in range(len(string)):
        count[ord(string[i]) - a_ord] -= 1
        if not visited[ord(string[i]) - a_ord]:
            if len(result) > 0 and result[-1] > string[i] and count[ord(result[-1]) - a_ord] > 0:
                visited[ord(result[-1]) - a_ord] = False
                result.pop()
            result.append(string[i])
            visited[ord(string[i]) - a_ord] = True
    return result


string = 'cbacdcbc'
print(the_smallest_lexicographically_string(string))
