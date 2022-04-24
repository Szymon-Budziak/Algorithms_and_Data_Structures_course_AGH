# Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków,
# z których inwestor musi wybrać podzbiór spełniając jego oczekiwania. Każdy budynek reprezentowany
# jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b, oraz cenie budowy w
# (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku może mieszkać h*(b − a)
# studentów. Proszę zaimplementować funkcję:
# def select_buildings(T, p):
#     ...
# która przyjmuje:
#   - Tablicę T zawierającą opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
# z oznaczeniami wprowadzonymi powyżej.
#   - Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
# Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych od 0),
# które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę studentów.
# Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić zbiór
# o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają punktu
# wspólnego. Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek.
# Funkcja powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo
# uzasadnić jej poprawność i oszacować złożoność obliczeniową.
from Exercise_1_tests import runtests


def get_result(DP, students, parents, cost, buildings, idx, p):
    if idx is None:
        return buildings
    if idx == 0:
        if p >= cost[0]:
            buildings.append(0)
        return buildings
    if DP[idx - 1][p] == DP[idx][p]:
        return get_result(DP, students, parents, cost, buildings, idx - 1, p)
    buildings.append(idx)
    return get_result(DP, students, parents, cost, buildings, parents[idx], p - cost[idx])


def select_buildings(T, p):
    for i in range(len(T)):
        T[i] = (i, T[i][0], T[i][1], T[i][2], T[i][3])
    T.sort(key=lambda x: x[3])
    cost = [0] * len(T)
    num_of_students = [0] * len(T)
    parents = [None] * len(T)
    DP = [[0] * (p + 1) for _ in range(len(T))]
    for i in range(len(T)):
        num_of_students[i] = (T[i][3] - T[i][2]) * T[i][1]
        cost[i] = T[i][4]
        for j in range(i - 1, -1, -1):
            if T[i][2] > T[j][3]:
                parents[i] = j
                break
    for i in range(len(T)):
        for j in range(p + 1):
            DP[i][j] = DP[i - 1][j]
            if parents[i] is not None and j >= cost[i]:
                DP[i][j] = max(DP[i][j], DP[parents[i]][j - cost[i]] + num_of_students[i])
            elif parents[i] is None and j >= cost[i]:
                DP[i][j] = max(DP[i][j], num_of_students[i])
    buildings = []
    get_result(DP, num_of_students, parents, cost, buildings, len(T) - 1, p)
    for i in range(len(buildings)):
        buildings[i] = T[buildings[i]][0]
    buildings.sort()
    return buildings


runtests(select_buildings)
