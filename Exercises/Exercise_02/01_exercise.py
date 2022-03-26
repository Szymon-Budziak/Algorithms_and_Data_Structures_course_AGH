# Proszę zaimplementować algorytm sortowania przez scalanie dla list jednokierunkowych:
#       a) funkcja scalająca
#       b) funkcja sortująca


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab_to_list(T):
    L = Node()
    head = L
    for i in T:
        L.next = Node()
        L.next.value = i
        L = L.next
    head = head.next
    return head


def print_list(L):
    while L is not None:
        print(L.value, '->', end=" ")
        L = L.next
    print('|')


def merge(L1, L2):
    if L1 is None and L2 is None:
        return None
    if L1 is None and L1.value is None:
        return L2
    if L2 is None and L2.value is None:
        return L1
    head = Node()
    tail = head
    while L1 is not None and L2 is not None:
        if L1.value <= L2.value:
            head.next = L1
            L1 = L1.next
        else:
            head.next = L2
            L2 = L2.next
        head = head.next
    if L1 is None:
        head.next = L2
    if L2 is None:
        head.next = L1
    return tail.next


def cut_list(L):
    if L is None:
        return None
    while L.next is not None and L.next.value >= L.value:
        L = L.next
    H = L.next
    L.next = None
    return H


def merge_sort(L):
    if L is None:
        return None
    tail = cut_list(L)
    S = L
    L = tail
    while L is not None:
        tail = cut_list(L)
        S = merge(S, L)
        L = tail
    return S


T = [3, 111, 2, 632, 2, 7, 54, 3, 74, 17, 3, 1, 9, 18, 0]
L = tab_to_list(T)
print_list(L)
H = merge_sort(L)
print_list(H)
