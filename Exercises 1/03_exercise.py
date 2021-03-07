# Proszę zaimplementować usuwanie z listy jednokierunkowej największej liczby.


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def delete_max(L):
    first = L
    p = L.next
    p_prev = L
    q = L
    L = L.next
    while L is not None:
        if L.value > p.value:
            p_prev = q
            p = L
        q = L
        L = L.next

    p_prev.next = p.next
    return first


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
node1.value = 1
L.next = node1
node2 = Node()
node2.value = 2
node1.next = node2
printList(L)

node3 = Node()
node3.value = 3
insert_to_node(node3, L)
printList(L)

node4 = Node()
node4.value = 5
insert_to_node(node4, L)
printList(L)

node5 = Node()
node5.value = 7
insert_to_node(node5, L)
printList(L)

for i in range(5):
    delete_max(L)
    printList(L)
