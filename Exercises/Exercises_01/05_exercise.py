# Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów oblicza jednocześnie
# jej największy i najmniejszy element wykonując 1.5n porównań.


def min_max(T):
    min = max = T[len(T) - 1]
    for i in range(0, len(T) - 1, 2):
        print(i)
        if T[i] < T[i + 1]:
            T[i], T[i + 1] = T[i + 1], T[i]
        if T[i] > max:
            max = T[i]
        elif T[i + 1] < min:
            min = T[i + 1]
    return min, max


T = [34, 700, 2, 344, 100, 124, 1000]
print(min_max(T))
