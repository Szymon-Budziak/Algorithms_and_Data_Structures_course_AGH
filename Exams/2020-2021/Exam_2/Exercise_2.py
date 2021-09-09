# Dane jest drzewo T zawierające n wierzchołków. Każda krawędź e drzewa ma wagę w(e) ∈ N oraz unikalny
# identyfikator id(e) ∈ N. Wagą drzewa jest suma wag jego krawędzi. Proszę napisać funkcję:
# def balance(T):
#     ...
# która zwraca identyfikator takiej krawędzi e drzewa, że usunięcie e dzieli drzewo na takie dwa,
# których różnica wag jest minimalna. Proszę szacować złożoność czasową i pamięciową użytego algorytmu.
# Reprezentacja drzewa.
# Drzewo reprezentowane jest przy pomocy węzłów typu Node:
# class Node:
#     def __init__(self):  # stwórz węzeł drzewa
#         self.edges = []  # lista węzłów do których są krawędzie
#         self.weights = []  # lista wag krawędzi
#         self.ids = []  # lista identyfikatorów krawędzi
#
#     def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
#         self.edges.append(x)  # o wadze w i identyfikatorze id
#         self.weights.append(w)
#         self.ids.append(id)
# Pole edges zawiera listę obiektów typu Node. Pola edges, weights oraz ids to listy równej długości.
# Należy założyć, że drzewo ma conajmniej jedną krawędź. Dopuszczalne jest dopisywanie własnych
# pól do Node.
from Exercise_2_tests import runtests
from math import inf


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.sum_of_edges = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def count_sum_of_edges(T):
    for e in T.edges:
        count_sum_of_edges(e)
    for i in range(len(T.edges)):
        T.sum_of_edges += T.weights[i] + T.edges[i].sum_of_edges


def find_best_edge(root, node, best_index, best_diff):
    for i in range(len(node.edges)):
        actual_index, actual_diff = find_best_edge(root, node.edges[i], best_index, best_diff)
        root_subtree = root.sum_of_edges - node.edges[i].sum_of_edges - node.weights[i]
        node_subtree = node.edges[i].sum_of_edges
        if actual_diff < best_diff:
            best_diff = actual_diff
            best_index = actual_index
        if abs(root_subtree - node_subtree) < best_diff:
            best_diff = abs(root_subtree - node_subtree)
            best_index = node.ids[i]
    return best_index, best_diff


def balance(T):
    count_sum_of_edges(T)
    best_index, best_diff = find_best_edge(T, T, None, inf)
    return best_index


runtests(balance)
