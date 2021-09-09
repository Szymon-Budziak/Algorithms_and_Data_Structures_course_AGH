# Na osi liczbowej znajduje się N punktów większych od M = 10^K . Z punktu A można przeskoczyć na
# punkt B wtedy i tylko wtedy gdy A % 10^K == B // 10^K . Proszę zaimplementować funkcję:
# def order(L, K):
#     ...
# porządkującą punkty, tak aby możliwe było przejście od najwcześniejszego punktu w tym porządku,
# kolejno przez wszystkie punkty, do ostatniego. Funkcja otrzymuje listę wartości określającą
# położenie punktów na osi liczbowej i powinna zwrócić listę punktów w kolejności ich odwiedzania.
# Jeżeli uporządkowanie punktów nie jest możliwe, funkcja powinna zwrócić None. Funkcja powinna być
# możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
from Exercise_2_tests import runtests


def recursion(L, K, T, result, idx):
    if len(result) == len(T):
        return True
    for j in range(len(T)):
        if result[idx] % (10 ** K) == T[j][0] // (10 ** K) and not T[j][1]:
            result.append(T[j][0])
            T[j][1] = True
            recursion(L, K, T, result, idx + 1)
    if len(result) != len(T):
        idx -= 1
        value = result.pop()
        T[L.index(value)][1] = False


def order(L, K):
    start = min(L)
    T = [0] * len(L)
    for i in range(len(T)):
        if L[i] == start:
            T[i] = [L[i], True]
        else:
            T[i] = [L[i], False]
    result = [start]
    recursion(L, K, T, result, 0)
    return result


runtests(order)
