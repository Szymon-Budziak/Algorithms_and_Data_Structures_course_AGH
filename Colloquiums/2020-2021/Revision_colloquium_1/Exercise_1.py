# Drzewo BST T reprezentowane jest przez obiekty klasy Node:
# class Node:
#     def __init__(self):
#         self.left = None # lewe poddrzewo
#         self.right = None # prawe poddrzewo
#         self.parent = None # rodzic drzewa jeśli istnieje
#         self.value = None # przechowywana wartość
# Proszę zaimplementować funkcję:
# def ConvertTree(T):
#    ...
# która przekształca drzewo T na drzewo o minimalnej wysokości, w którym węzły spełniają warunek:
# największy element na danym poziomie jest mniejszy od najmniejszego elementu na kolejnym poziomie.
# Funkcja zwraca korzeń nowego drzewa. Poziomy numerujemy od korzenia do liści. Funkcja powinna być
# możliwie jak najszybsza oraz - jako kryterium drugiego rzędu - używać jak najmniejszej ilości pamięci
# (poza pamięcią już wykorzystaną na reprezentacje drzewa). Proszę oszacować złożoność czasową oraz
# pamięciową użytego algorytmu.
from Exercise_1_tests import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None


def traverse_tree(T, array):
    if T is not None:
        traverse_tree(T.left, array)
        array.append(T)
        traverse_tree(T.right, array)


def ConvertTree(T):
    array = []
    traverse_tree(T, array)
    for i in range(len(array)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(array):
            array[i].left = array[left]
            array[left].parent = array[i]
            array[left].left = array[left].right = None
        if right < len(array):
            array[i].right = array[right]
            array[right].parent = array[i]
            array[right].left = array[right].right = None
    return array[0]


runtests(ConvertTree)
