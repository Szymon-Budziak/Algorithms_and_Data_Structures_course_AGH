# Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.


def insert(T, key, n):
    T[n] = key
    i = n
    while i > 0 and T[i] > T[(i-1)//2]:
        T[i], T[(i-1)//2] = T[(i-1)//2], T[i]
        i = (i-1)//2


T = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
insert(T, 9, len(T)-1)
print(T)
