# W roku 2050 Maksymilian odbywa podróż przez pustynię z miasta A do miasta B. Droga pomiędzy miastami
# jest linią prostą na której w pewnych miejscach znajdują się plamy ropy. Maksymilian porusza się
# 24-kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy. Cysterna wyposażona jest w pompę
# pozwalającą zbierać ropę z plam. Aby dojechać z miasta A do miasta B Maksymilian będzie musiał zebrać
# ropę z niektórych plam (by nie zabrakło paliwa), co każdorazowo wymaga zatrzymania cysterny. Niestety,
# droga jest niebezpieczna. Maksymilian musi więc tak zaplanować trasę, by zatrzymać się jak najmniej
# razy. Na szczęście cysterna Maksymiliana jest ogromna - po zatrzymaniu zawsze może zebrać całą ropę
# z plamy (w cysternie zmieściłaby się cała ropa na trasie).
# Zaproponuj i zaimplementuj algorytm wskazujący, w których miejscach trasy Maksymilian powinien się
# zatrzymać i zebrać ropę. Algorytm powinien być możliwe jak najszybszy i zużywać jak najmniej pamięci.
# Uzasadnij jego poprawność i oszacuj złożoność obliczeniową.
# Dane wejściowe reprezentowane są jako dwuwymiarowa tablica liczb naturalnych T, w której wartość
# T[u][v] to objętość ropy na polu o współrzędnych (u, v) (objętość 0 oznacza brak ropy). Współrzędne
# u należą do zbioru {0, 1, ..., n−1} a współrzędne v do zbioru {0, 1, ..., m−1}. Miasto A znajduje się
# na polu (0, 0), zaś miasto B na polu (0, m−1). Maksymilian porusza się jedynie po polach
# (0, 0), (0, 1),..., (0, m−1). Bok każdego pola ma długość 1 kilometra. Plamą ropy jest dowolny spójny
# obszar pól zawierających ropę. Dwa pola należą do spójnego obszaru jeśli mają wspólny bok lub są
# połączone sekwencją pól (zawierających ropę) o wspólnych bokach. Zakładamy, że początkowo cysterna
# jest pusta, ale pole (0, 0) jest częścią plamy ropy, którą można zebrać przed wyruszeniem w drogę.
# Zakładamy również, że zadanie posiada rozwiązanie, t.j. da się dojechać z miasta A do miasta B.
# Algorytm należy zaimplementować w funkcji:
# def plan(T):
#     ...
# która przyjmuje tablicę z opisem zadania i zwraca listę współrzędnych v pól na których należy
# zatrzymać cysternę w celu zebrania ropy (cysterna porusza się po tylko polach (0, v), więc wystarczy
# zwrócić współrzędną v). Lista powinna być posortowana w kolejności postojów. Postój na polu (0, 0)
# również jest częścią rozwiązania.
from Exercise_3_tests import runtests
from queue import PriorityQueue


def take_fuel(T, row, col, actual_fuel):
    actual_fuel[0] += T[row][col]
    T[row][col] = 0
    new_row = [row - 1, row + 1, row, row]
    new_col = [col, col, col - 1, col + 1]
    for i in range(len(new_row)):
        if new_row[i] >= 0 and new_row[i] < len(T) and new_col[i] >= 0 and new_col[i] < len(T[0]):
            if T[new_row[i]][new_col[i]] != 0:
                take_fuel(T, new_row[i], new_col[i], actual_fuel)


def plan(T):
    stops = []
    limit = len(T[0])
    actual_fuel = [0]
    i = 0
    while i < limit:
        if T[0][i] != 0:
            actual_fuel[0] = 0
            take_fuel(T, 0, i, actual_fuel)
            T[0][i] = actual_fuel[0]
        i += 1
    queue = PriorityQueue()
    total_fuel = 0
    for i in range(limit - 1):
        if T[0][i] != 0:
            queue.put((-T[0][i], i))
        if total_fuel == 0:
            actual_value = queue.get()
            total_fuel -= actual_value[0]
            stops.append(actual_value[1])
        total_fuel -= 1
    stops.sort()
    return stops


runtests(plan)
