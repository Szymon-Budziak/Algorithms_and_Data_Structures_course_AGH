# Proszę zaimplementować funkcję heavy_path(T), która na wejściu otrzymuje drzewo T z ważonymi
# krawędziami (wagi to liczby całkowite, mogą być zarówno dodatnie, ujemne, jak i o wartości zero)
# i zwraca długość (wagę) najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane jest za
# pomocą obiektów typu Node:
#   class Node:
#       def __init__(self):
#           self.children = 0 - liczba dzieci węzła
#           self.child = []   - lista par (dziecko, waga krawędzi)
#           ...               - wolno dopisać własne pola
# Poniższy kod tworzy drzewo z korzeniem A, który ma dwoje dzieci, węzły B i C, do których prowadzą
# krawędzie o wagach 5 i −1:
# A = Node()
# B = Node()
# C = Node()
# A.children = 2
# A.child = [(B, 5), (C, -1)]
# Rozwiązaniem dla drzewa A jest 5 (osiągnięte przez ścieżkę A-B; ścieżka B-A-C ma wagę 5 − 1 = 4.
# Proszę skrótowo wyjaśnić ideę algorytmu oraz oszacować jego złożoność czasową.


class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.longest_path = 0


def heavy_path(T):
    first_path, second_path = 0, 0
    for child, weight in T.child:
        actual_length = heavy_path(child) + weight
        if actual_length > first_path:
            second_path, first_path = first_path, actual_length
        elif actual_length > second_path:
            second_path = actual_length
    if first_path + second_path > T.longest_path:
        T.longest_path = first_path + second_path
    return first_path


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.child = [(C, -1), (E, 7)]
B.child = [(D, 2), (A, 5), (F, 8)]
C.child = [(E, 3), (F, 5)]
D.child = [(F, 4), (A, 11)]
E.child = [(F, -5)]
print(heavy_path(B))
