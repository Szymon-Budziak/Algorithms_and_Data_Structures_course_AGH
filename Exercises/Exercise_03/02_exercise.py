# Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.


def insert(T, key):
    T.append(key)
    i = len(T) - 1
    while i > 0 and T[i] > T[(i - 1) // 2]:
        T[i], T[(i - 1) // 2] = T[(i - 1) // 2], T[i]
        i = (i - 1) // 2
    return T


T = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
print(insert(T, 9))
