# Exercise_1_tests.py

from math import log2, floor

TESTS = [
    [5, 11, 17, 13, 2, 7, 3],
    [5, 11, 17, 13, 2, 7, 3, 19],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15],
    [5, 6, 7, 8, 4, 3, 2, 1],
    [25, 26, 27, 20, 15, 10, 17, 23, 22, 24],
    [10, 100, 1000, 9, 90, 99, 999],
    [1, 10, 20, 40, 30, 28, 32, 50, 45, 55]
]


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.right = None  # prawe poddrzewo
        self.parent = None  # rodzic drzewa jesli istnieje
        self.value = None  # przechowywana wartosc


def CreateBST(l):
    def InsertToBST(p, val):
        t = Node()
        t.value = val
        if p is None: return t

        r = p
        while r is not None:
            q = r
            if val < r.value:
                r = r.left
            else:
                r = r.right

        if val < q.value:
            q.left = t
        else:
            q.right = t

        t.parent = q
        return p

    p = None
    for val in l: p = InsertToBST(p, val)
    return p


def PrintTree(p):
    if p is not None:
        PrintTree(p.left)
        print(p.value, end=' ')
        PrintTree(p.right)


def Size(p):
    return 0 if p is None else Size(p.left) + Size(p.right) + 1


def Hight(p):
    return 0 if p is None else max(Hight(p.left), Hight(p.right)) + 1


def Tree2Set(p):
    def rek(p):
        nonlocal zb

        if p is not None:
            zb.add(p.value)
            rek(p.left)
            rek(p.right)

    zb = set()
    rek(p)
    return zb


def CheckTree(p):
    def rek(p, n=0):
        nonlocal min_level
        nonlocal max_level

        if p is not None:
            min_level[n] = min(min_level[n], p.value)
            max_level[n] = max(max_level[n], p.value)

            rek(p.left, n + 1)
            rek(p.right, n + 1)

    h = Hight(p)
    min_level = [999 for _ in range(h)]
    max_level = [0 for _ in range(h)]
    rek(p)
    # print(min_level)
    # print(max_level)
    for i in range(1, h):
        if min_level[i] <= max_level[i - 1]: return False
    return True


def CheckParents(p):
    if p is None: return True
    if p.left is not None:
        if p.left.parent != p: return False
    if p.right is not None:
        if p.right.parent != p: return False
    return CheckParents(p.left) and CheckParents(p.right)


def CheckResult(bst, result):
    if Size(result) != Size(bst): return False  # kontrola rozmiarow
    if Hight(result) != floor(log2(Size(bst)) + 1): return False  # kontrola wysokosci
    if Tree2Set(result) != Tree2Set(bst): return False  # porównanie zawartosci
    if not CheckTree(result): return False  # varunek poziomow
    if not CheckParents(result): return False  # kontrola parentow
    return True


def runtests(f):
    OK = True
    for d in TESTS:
        print("--------")
        print("dane = ", d)

        bst = CreateBST(d)
        print("BST  = ", end='')
        PrintTree(bst)
        print()

        result = f(bst)

        print("res  = ", end='')
        PrintTree(result)
        print()

        if CheckResult(CreateBST(d), result):
            print("OK")
        else:
            print("Error")
            OK = False

    print()
    if OK:
        print("Passed all tests")
    else:
        print("Failed")
