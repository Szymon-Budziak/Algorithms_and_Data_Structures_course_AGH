# Mówimy, że tablica T ma współczynnik nieuporządkowania równy k (jest k-Chaotyczna), jeśli spełnione
# są łącznie dwa warunki:
#   1) tablicę można posortować niemalejąco przenosząc każdy element A[i] o co najwyżej k pozycji
# (po posortowaniu znajduje się on na pozycji różniącej się od i co najwyżej o k),
#   2) tablicy nie da się posortować niemalejąco przenosząc każdy element o mniej niż k pozycji.
# Proszę zaproponować i zaimplementować algorytm, który otrzymuje na wejściu tablicę liczb
# rzeczywistych T i zwraca jej współczynnik nieuporządkowania. Algorytm powinien być jak najszybszy
# oraz używać jak najmniej pamięci. Proszę uzasadnić jego poprawność i oszacować złożoność
# obliczeniową. Algorytm należy zaimplementować jako funkcję:
# def chaos_index(T):
#     ...
# przyjmującą tablicę T i zwracającą liczbę całkowitą będącą wyznaczonym współczynnikiem nieuporządkowania.
from Exercise_1_tests import runtests
from math import inf


def merge(T, p, q, r):
    L = T[p:q + 1]
    R = T[q + 1:r + 1]
    L.append((inf, inf))
    R.append((inf, inf))
    i = j = 0
    for k in range(p, r + 1):
        if L[i][0] <= R[j][0]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def merge_sort(T, p, r):
    if len(T) <= 1:
        return T
    elif p < r:
        m = (p + r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m + 1, r)
        merge(T, p, m, r)


def chaos_index(T):
    for i in range(len(T)):
        T[i] = (T[i], i)
    merge_sort(T, 0, len(T) - 1)
    max_chaotic = 0
    for i in range(len(T)):
        max_chaotic = max(max_chaotic, abs(i - T[i][1]))
    return max_chaotic


runtests(chaos_index)
