# Proszę zaimplementować funkcję odwracającą listę jednokierunkową.


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def reverse_list(L):
    if L is None:
        return None
    p = None
    q = L.next
    while L is not None:
        L.next = p
        p = L
        L = q
        if q is not None:
            q = q.next
    printList(p)
    return q


def printList(L):
    if L is not None:
        print(L.value, end=' ')
        printList(L.next)
    else:
        print()


L = Node()
node1 = Node()
node1.value = 1
L.next = node1

node2 = Node()
node2.value = 2
node1.next = node2

node3 = Node()
node3.value = 3
node2.next = node3

node4 = Node()
node4.value = 5
node3.next = node4

node5 = Node()
node5.value = 7
node4.next = node5

printList(L)
reverse_list(L)
