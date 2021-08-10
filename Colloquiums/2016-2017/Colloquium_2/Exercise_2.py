# Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n−1]. Złodziej
# chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu ukraść
# dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
# def good_thief(A):
#     ...
# która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim kodeksem
# moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić poprawność algorytmu
# oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie jak najszybszy (ale przede
# wszystkim poprawny).


def good_thief(A):
    DP = [0] * len(A)
    DP[0], DP[1] = A[0], max(A[0], A[1])
    for i in range(2, len(A)):
        DP[i] = max(DP[i - 1], DP[i - 2] + A[i])
    stolen_items = [False] * len(A)
    for i in range(len(A) - 1, 1, -1):
        if DP[i - 2] + A[i] == DP[i] and (i == len(A) - 1 or stolen_items[i + 1] is False):
            stolen_items[i] = True
    if stolen_items[2] is True:
        stolen_items[0] = True
    else:
        if A[0] > A[1]:
            stolen_items[0] = True
        else:
            stolen_items[1] = True
    result = []
    for i in range(len(A)):
        if stolen_items[i]:
            result.append(A[i])
    return DP[len(A) - 1], result


A = [15, 2, 6, 18, 9, 5, 13, 14, 17, 8, 3, 24]
print(good_thief(A))
