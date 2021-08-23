# Dana jest posortowana tablica A zawierająca n liczb i celem jest wyznaczenie liczby x takiej, że
# wartość ∑(n−1/ i=0) ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić jego poprawność
# oraz ocenić złożoność obliczeniową.
from math import floor, ceil


def min_sum(T):
    if len(T) % 2 == 1:
        return T[len(T) // 2]
    else:
        index = (len(T) + 1) / 2 - 1
        lower = floor(index)
        upper = ceil(index)
        return (T[lower] + T[upper]) / 2


T = [1, 2, 3, 4, 5, 6, 7, 7, 8, 11, 14, 19]
print(min_sum(T))
