# Given a string and a list of words. Determine if the string can be segmented
# into a space-separated sequences of one or more list wordsself.


def word_break(words, string, T):
    n = len(string)
    if n == 0:
        return True
    if T[n] == -1:
        T[n] = 0
        for i in range(1, n+1):
            actual = string[:i]
            if actual in words and word_break(words, string[i:], T):
                T[n] == 1
                return True
    return T[n] == 1


words = ["self", "th", "is", "famous", "Word", "break", "b", "r", "e", "a",
         "k", "br", "bre", "break", "ak", "problem"]
string = "Wordbreakproblem"
T = [-1]*(len(string)+1)
print(word_break(words, string, T))
