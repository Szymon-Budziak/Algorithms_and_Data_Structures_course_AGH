# Given the string. Find the longest palindromic substring which is palindrome.


def LPS(string):
    T = [[0]*(len(string)+1) for _ in range(len(string)+1)]
    longest_pal = 0
    for i in range(1, len(T)):
        T[0][i] = string[i-1]
    for i in range(1, len(T)):
        T[i][0] = string[i-1]
    for i in range(1, len(T)):
        T[i][i] = 1
    for i in range(len(T)-2):
        if string[i] == string[i+1]:
            T[i][i+1] = 1
            longest_pal = 2
    for s in range(3, len(string)+1):
        for i in range(len(T)-s):
            j = i+s-1
            if string[i] == string[j] and T[i+1][j-1] == 1:
                T[i][j] = 1
                if s > longest_pal:
                    longest_pal = s
    return longest_pal


string = "abacabacabb"
print(LPS(string))
