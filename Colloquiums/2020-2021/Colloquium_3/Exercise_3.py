# Dany jest ważony graf nieskierowany reprezentowany przez macierz T o rozmiarach n × n (dla
# każdych i, j zachodzi T[i][j] = T[j][i]; wartość T[i][j] > 0 oznacza, że istnieje krawędź między
# wierzchołkiem i a wierzchołkiem j z wagą T[i][j]). Dana jest także liczba rzeczywista d. Każdy
# wierzchołek w G ma jeden z kolorów: zielony lub niebieski. Zaproponuj algorytm, który wyznacza
# największą liczbę naturalną l, taką że w grafie istnieje l par wierzchołków (p, q) ∈ V × V
# spełniających warunki:
#   1) q jest zielony, zaś p jest niebieski,
#   2) odległość między p i q (liczona jako suma wag krawędzi najkrótszej ścieżki) jest nie mniejsza niż d,
#   3) każdy wierzchołek występuje w co najwyżej jednej parze.
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def BlueAndGreen(T, K, D):
#     ...
# która przyjmuje:
#   T: graf reprezentowany przez kwadratową macierz sąsiedztwa, gdzie wartość 0 oznacza brak krawędzi,
# a liczba większa od 0 przedstawia odległość pomiędzy wierzchołkami,
#   K: listę przedstawiającą kolory wierzchołków,
#   D: odległość o której mowa w warunku 2 opisu zadania.
# Funkcja powinna zwrócić liczbę l omawianą w treści zadania.
from Exercise_3_tests import runtests
from Exercise_3_edmonds_karp import edmonds_karp
from math import inf


def Floyd_Warshall_algorithm(graph):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance


def BlueAndGreen(T, K, D):
    graph = [[0] * (len(T) + 2) for _ in range(len(T) + 2)]
    distance = Floyd_Warshall_algorithm(T)
    for i in range(len(T)):
        for j in range(len(T)):
            if distance[i][j] >= D and distance[i][j] != inf:
                if K[i] == 'B' and K[j] == 'G':
                    graph[i][j] = graph[j][len(T) + 1] = graph[len(T)][i] = 1
    return edmonds_karp(graph, len(T), len(T) + 1)


runtests(BlueAndGreen)
