# Dyrektor działu handlowego pewnej firmy odbywa podróż służbową z miasta A do miasta B. W pewnych
# punktach zaplanowanej trasy znajdują się stacje benzynowe. Niestety, ze względu na problemy
# z dostawami surowca, stacje limitują objętość paliwa, którą może zatankować pojedynczy klient.
# Co więcej, z powodu modyfikacji zmierzających do zwiększenia głośności i mocy silnika, samochód
# dyrektora spala aż 1 litr paliwa na 1 kilometr trasy. Dyrektor się spieszy - musi więc tak
# zaplanować podróż, by zatrzymać się na jak najmniejszej liczbie stacji. Jest to o tyle niełatwe, że
# każda stacja ma własny limit litrów paliwa, które można na niej zatankować. Dodatkową przeszkodą
# jest fakt, że w celu zmniejszenia masy pojazdu zmodyfikowano w nim zbiornik paliwa, który obecnie
# mieści jedynie q litrów benzyny. Zaproponuj i zaimplementuj algorytm wskazujący na których stacjach
# dyrektor powinien tankować paliwo (tak, by tankować możliwie najmniejszą liczbę razy). Algorytm
# powinien być możliwie jak najszybszy i zużywać jak najmniej pamięci. Uzasadnij jego poprawność
# i oszacuj złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
# def iamlate(T, V, q, l):
#     ...
# która przyjmuje:
# 1. Tablicę liczb naturalnych T z pozycjami stacji benzynowych, wyrażonymi jako kilometry od
# początku trasy. Pierwsza stacja znajduje się na początku trasy, t.j. T[0] = 0. Kolejne stacje
# umieszczone są w T w kolejności odleglości od początku trasy.
# 2. Tablicę dodatnich liczb naturalnych V zawierającą limity paliwa, które może zatankować
# pojedynczy klient. Tak więc V[i] to liczba litrów paliwa, którą można zatankować na stacji
# w pozycji T[i]. Na danej stacji można tankować tylko raz.
# 3. Dodatnią liczbę naturalną q będącą pojemnością baku samochodu (liczba litrów paliwa, które
# mieszczą się w baku). Zakładamy, że przed pierwszym tankowaniem w baku nie ma paliwa.
# 4. Dodatnią liczbę naturalną l będącą długością trasy w kilometrach.
# Funkcja powinna zwrócić listę numerów stacji, na których należy tankować paliwo (w kolejności
# tankowania). Jeśli warunki zadania uniemożliwiają dotarcie do celu, funkcja powinna zwrócić pustą
# listę. Stacje numerujemy od 0. Stacja na początku trasy stanowi część rozwiązania.
from Exercise_3_tests import runtests
from math import inf


def relax(DP, T, parent, actual, i, j, k):
    if T[k] - T[i] <= actual and DP[i][j] + 1 < DP[k][actual - T[k] + T[i]]:
        DP[k][actual - T[k] + T[i]] = DP[i][j] + 1
        parent[k][actual - T[k] + T[i]] = (i, j)
        return True
    return False


def iamlate(T, V, q, l):
    T.append(l)
    V.append(0)
    DP = [[inf] * (q + 1) for _ in range(len(T))]
    parent = [[(-1, 0)] * (q + 1) for _ in range(len(T))]
    for i in range(q + 1):
        DP[0][i] = 0
    actual = V[0]
    if actual > q:
        actual = q
    for i in range(1, len(T) - 1):
        if T[i] <= actual:
            DP[i][actual - T[i]] = 1
            parent[i][actual - T[i]] = (0, actual - T[i])
    for i in range(1, len(T)):
        for j in range(q + 1):
            if DP[i][j] != inf:
                actual = V[i] + j
                if actual > q:
                    actual = q
                for k in range(i + 1, len(T)):
                    if relax(DP, T, parent, actual, i, j, k):
                        continue
                    else:
                        break
    best = inf
    index = None
    for i in range(q + 1):
        if DP[len(T) - 1][i] < best:
            best = DP[len(T) - 1][i]
            index = i
    result = []
    if best == inf:
        return result
    i = len(T) - 1
    p = inf
    while p != 0:
        p = parent[i][index][0]
        result.append(p)
        index = parent[i][index][1]
        i = p
    result.reverse()
    return result


runtests(iamlate)
