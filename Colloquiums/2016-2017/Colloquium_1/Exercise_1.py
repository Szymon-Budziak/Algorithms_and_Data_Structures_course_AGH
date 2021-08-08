# Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
# struct Node{ Node* next; double value; } Proszę zaimplementować funkcję void Sort(Node* list),
# która otrzymuje na wejściu listę liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie
# z rozkładem jednostajnym na przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej.
# Funkcja powinna być możliwie jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować
# złożoność zaimplementowanej funkcji.
from math import ceil, floor


class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def traverse_list(L):
    length = 1
    p = L
    max_number = p.value
    while p.next is not None:
        p = p.next
        max_number = max(max_number, p.value)
        length += 1
    return length, max_number


def print_list(L, flag):
    while L is not None:
        print(L.value, "->", end=" ")
        L = L.next
    if flag:
        print("|")


def tab_to_list(T):
    H = Node()
    C = H
    for i in range(len(T)):
        X = Node()
        X.value = T[i]
        C.next = X
        C = X
    return H.next


def insertion_sort(head):
    sort = None
    current = head
    while current is not None:
        next = current.next
        sort = sorted_insert(sort, current)
        current = next
    head = sort
    return head


def sorted_insert(head, new_node):
    if head is None or head.value >= new_node.value:
        new_node.next = head
        head = new_node
    else:
        current = head
        while current.next is not None and current.next.value < new_node.value:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return head


def bucket_sort(head, max_number):
    buckets = [Node() for _ in range(ceil(max_number))]
    C = [i for i in buckets]
    p = head
    while p is not None:
        C[floor(p.value)].next = p
        C[floor(p.value)] = C[floor(p.value)].next
        previous = p
        p = p.next
        previous.next = None
    for i in buckets:
        i = insertion_sort(i.next)
        print_list(i, False)
        print("->", end=" ")


def sort(head):
    length, max_number = traverse_list(head)
    # Finding length and max_number takes O(n) time because we have to traverse
    # whole list
    bucket_sort(head, max_number)
    # Bucket sort complexity at the expected case is O(n)
    # Complexity of the whole algorithm is 2*O(n) = O(n)


T = [1.8, 5.8, 5.8, 9.8, 2.2, 9.0, 5.0, 9.3, 4.4, 5.5, 6.4, 1.4, 6.8, 1.5, 1.0, 9.4, 5.8, 3.3, 0.6]
head = tab_to_list(T)
sort(head)
