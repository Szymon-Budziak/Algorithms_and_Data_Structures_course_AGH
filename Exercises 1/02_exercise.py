# Proszę zaimplementować wstawianie Node'a do posortowanej listy jednokierunkowej.


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def insert_to_node(node, L):
    start = L
    while L.next is not None and L.next.value < node.value:
        L = L.next
    node.next = L.next
    L.next = node
    return start


def printList(L):
    if L is not None:
        print(L.value, end=' ')
        printList(L.next)
    else:
        print()


L = Node()
node1 = Node()
node1.value = 2
L.next = node1
node2 = Node()
node2.value = 5
node1.next = node2
printList(L)

node3 = Node()
node3.value = 7
insert_to_node(node3, L)
printList(L)

node4 = Node()
node4.value = 8
insert_to_node(node4, L)
printList(L)

node5 = Node()
node5.value = 1
insert_to_node(node5, L)
printList(L)
