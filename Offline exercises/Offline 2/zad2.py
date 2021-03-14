from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def traverse_list(L):
    p = L
    while p.next is not None:
        p = p.next
    return p


def partition(head, tail):
    pivot = q = head
    end_pivot = pivot
    first_smaller = Node()
    last_smaller = first_smaller
    first_larger = Node()
    last_larger = first_larger
    q = q.next
    while q is not tail.next:
        if q.value < pivot.value:
            last_smaller.next = q
            last_smaller = last_smaller.next
        elif q.value > pivot.value:
            last_larger.next = q
            last_larger = last_larger.next
        else:
            end_pivot.next = q
            end_pivot = end_pivot.next
        q = q.next
    first_smaller = first_smaller.next
    first_larger = first_larger.next
    return (first_smaller, last_smaller, first_larger,
            last_larger, pivot, end_pivot)


def quicker_sort(head, tail):
    if head is not tail:
        f_s, l_s, f_l, l_l, p, e_p = partition(head, tail)
        if f_s is not None and l_s is not None:
            f_s, l_s = quicker_sort(f_s, l_s)
            head = f_s
            l_s.next = p
            e_p.next = None
        else:
            head = p
            e_p.next = None
        if f_l is not None and l_l is not None:
            f_l, l_l = quicker_sort(f_l, l_l)
            e_p.next = f_l
            tail = l_l
            l_l.next = None
        else:
            tail = e_p
    return head, tail


def qsort(L):
    last = traverse_list(L)
    L, _ = quicker_sort(L, last)
    return L


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
