class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def dodaj(T, key):
    W = BNode(key)
    if key < T.value:
        if T.left == None:
            T.left = W
            W.parent = T
        else:
            dodaj(T.left, key)
    else:
        if T.right == None:
            T.right = W
            W.parent = T
        else:
            dodaj(T.right, key)


def createtree(keys):
    T = BNode(keys[0])
    for i in range(1, len(keys)):
        dodaj(T, keys[i])
    return T


TESTS = [
    ([10, -5, -6, -7, 1, 12, 11], 7),
    ([1, -1, -2, 4, 5, 6, 7], 3),
    ([5, 2, 1, 6, 7, 8], 8),
    ([0, -2, -3, -1, 4, 3, 5], 2),
    ([5, 6, 7, 10, 8, 11, 3, -1, -5, -10, -2], 1),
    ([10, 3, 15, 11, 17, -1, -5, 0], 14),
    ([10, 2, 1, 3, 12, 11], 14),
    ([-1000, -1002, -1003, -1001, 10, -200, 100, -201, -199, 99, 101], -1002 + (-200) + 100),
    ([-1000, -1002, -1003, -1001, 10, -100, 200, -101, -99, 199, 201], -1002 + 10)
]


def runtests(f):
    problems_count = 0
    for i, x in enumerate(TESTS):
        print()
        print(f"--- (test #{i + 1}) ----------------------")
        Tr = createtree(x[0])
        v = f(Tr)
        print("Dane wejściowe", x[0])
        print("Uzyskany wynik: ", v)
        print("Oczekiwany wynik: ", x[1])
        if v == x[1]:
            print("OK!")
        else:
            print("PROBLEM!")
            problems_count += 1

    print()
    print("------------------------------------")
    print("------------------------------------")
    if problems_count > 0:
        print(f"Jest {problems_count} problemów!")
    else:
        print("Wszystko OK!")
