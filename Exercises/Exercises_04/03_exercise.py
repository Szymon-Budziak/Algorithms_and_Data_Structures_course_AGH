# Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad alfabetem
# długości k, sprawdza czy A i B są swoimi anagramami.
# kot, tok - anagramy
# kot, kat - nie anagramy
from random import randint


def alloc(n):
    return [randint(0, 1000000000) for _ in range(n)]


def check_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    counters = alloc(2 ** 16)
    for i in range(len(word1)):
        counters[ord(word1[i])] = 0

    for i in range(len(word1)):
        counters[ord(word1[i])] += 1
        counters[ord(word2[i])] -= 1

    for i in range(len(word1)):
        if counters[ord(word1[i])] != 0:
            return False
    return True


word1 = "lo/$x3%h121b"
word2 = "h1b12ox/$%3l"
print(check_anagrams(word1, word2))
