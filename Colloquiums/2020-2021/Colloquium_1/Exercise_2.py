# Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
# class Node:
#     def __init__(self):
#         self.value = None
#         self.next = None
# Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste
# a[1], a[2], ..., a[n] (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego
# elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
# o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
# [1, 0, 3, 2, 4, 6, 5], a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
# Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
# Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
# oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
# listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log(n))
# oraz k = Θ(n).
from Exercise_2_tests import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def insertion_sort(head):
    is_sorted = None
    actual = head
    while actual is not None:
        nex_node = actual.next
        is_sorted = sorted_insert(is_sorted, actual)
        actual = nex_node
    head = is_sorted
    return head


def sorted_insert(head, new_node):
    if head is None or head.val >= new_node.val:
        new_node.next = head
        head = new_node
    else:
        actual = head
        while actual.next is not None and actual.next.val < new_node.val:
            actual = actual.next
        new_node.next = actual.next
        actual.next = new_node
    return head


def SortH(p, k):
    if k == 0:
        return p
    return insertion_sort(p)


runtests(SortH)
