# Dane jest drzewo BST zbudowane z węzłów
# class BNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.value = value
# Klucze w tym drzewie znajdują się w polach value i są liczbami całkowitymi. Mogą zatem mieć wartości
# zarówno dodatnie, jak i ujemne. Proszę napisać funkcję, która zwraca wartość będącą minimalną możliwą
# sumą kluczy zbioru wierzchołków oddzielających wszystkie liście od korzenia w taki sposób, że na
# każdej ścieżce od korzenia do liścia znajduje się dokładnie jeden wierzchołek z tego zbioru. Zakładamy,
# że korzeń danego drzewa nie jest bezpośrednio połączony z żadnym liściem (ścieżka od korzenia do
# każdego liścia prowadzi przez co najmniej jeden dodatkowy węzeł). Jako liść jest rozumiany węzeł
# W typu BNode taki że W.left = W.right = None.
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def cutthetree(T):
#     ...
# która przyjmuje korzeń danego drzewa BST i zwraca wartość rozwiązania. Nie wolno zmieniać definicji
# class BNode.
from Exercise_2_tests import runtests
from math import inf


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
    if T is None:
        return 0
    if T.right is None and T.left is None:
        return inf
    actual_value = inf
    if T.parent is not None:
        actual_value = T.value
    actual_value = min(actual_value, cutthetree(T.right) + cutthetree(T.left))
    return actual_value


runtests(cutthetree)
