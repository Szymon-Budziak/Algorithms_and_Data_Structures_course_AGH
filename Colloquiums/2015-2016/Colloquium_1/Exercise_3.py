# Dana jest struktura Node opisująca listę jednokierunkową:
# class Node:
#     def __init__(self, value):
#         self.next = None
#         self.value = value
# Proszę zaimplementować funkcję def fixSortedList(L), która otrzymuje na wejściu listę jednokierunkową
# bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że powstała z listy posortowanej przez
# zmianę jednego losowo wybranego elementu na losową wartość. Funkcja powinna przepiąć elementy listy
# tak, by lista stała się posortowana i zwrócić wskaźnik do głowy tej listy. Można założyć, że wszystkie
# liczby na liście są różne i że lista ma co najmniej dwa elementy. Funkcja powinna działać w czasie
# liniowym względem długości listy wejściowej.


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def find_node_to_cut(head):
    previous = head
    current = head.next
    while current is not None and previous.value < current.value:
        previous = current
        current = current.next
    node_to_cut = current
    previous.next = current.next
    return head, node_to_cut


def fix_sorted_list(head):
    if head is None:
        return None
    head, node_to_cut = find_node_to_cut(head)
    previous = None
    current = head
    while current is not None and node_to_cut.value > current.value:
        previous = current
        current = current.next
    if previous is None:
        node_to_cut.next = head
        head = node_to_cut
    else:
        node_to_cut.next = current
        previous.next = node_to_cut
    return head


def create_linked_list(T):
    p = None
    for i in range(len(T) - 1, -1, -1):
        q = Node(T[i])
        q.next = p
        p = q
    return p


def create_list(p):
    T = []
    while p is not None:
        T.append(p.value)
        p = p.next
    return T


T = [2, 4, 6, 8, 12, 18, 24, 31, 5, 38, 41, 47, 58]
ll = create_linked_list(T)
head = fix_sorted_list(ll)
print(create_list(head))
