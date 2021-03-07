# Proszę zaimplementować wyszukiwanie binarne w posortowanej
# tablicy, znajdujące najmniejszy indeks z daną wartością.


def binary_search(T, i, j, x):
    if i > j:
        return None
    c = (i+j) // 2
    if T[c] == x:
        value = binary_search(T, i, c-1, x)
        if value is None:
            return c
        return value
    if T[c] > x:
        return binary_search(T, i, c-1, x)
    else:
        return binary_search(T, c+1, j, x)


T = [0, 1, 2, 3, 4, 5, 5, 5, 6]
for i in range(len(T)):
    print(i, binary_search(T, 0, len(T)-1, T[i]))
