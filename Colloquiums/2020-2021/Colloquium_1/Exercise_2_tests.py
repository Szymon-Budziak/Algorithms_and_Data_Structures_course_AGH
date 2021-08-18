class Node:
    def __init__(self):
        self.val = None
        self.next = None


L0 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
      41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L1 = [2, 5, 3, 7, 13, 11, 17, 19, 29, 23, 31, 37,
      43, 41, 47, 53, 59, 67, 61, 73, 71, 79, 83, 89]
L2 = [2, 3, 5, 7, 11, 13, 17, 19, 31, 23, 29, 43,
      41, 37, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L5 = [2, 11, 5, 7, 3, 31, 13, 19, 37, 29, 17, 23,
      41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L10 = [2, 3, 11, 7, 5, 23, 17, 19, 13, 29, 41, 37,
       31, 89, 47, 53, 59, 61, 67, 71, 73, 43, 83, 79]
L20 = [2, 79, 5, 7, 11, 23, 17, 19, 13, 29, 3, 37,
       41, 89, 47, 53, 59, 61, 31, 71, 73, 67, 83, 43]

TESTS = [(L1, 1), (L2, 2), (L5, 5), (L10, 10), (L20, 20)]


def printList(p):
    while p != None:
        print(p.val, end=' ')
        p = p.next
    print()


def makeList(l):
    n = len(l)
    p = None
    for i in range(n - 1, -1, -1):
        q = Node()
        q.val = l[i]
        q.next = p
        p = q
    return p


def length(p):
    res = 0
    while p != None:
        res += 1
        p = p.next
    return res


def list2set(p):
    res = set()
    while p != None:
        res.add(p.val)
        p = p.next
    return res


def isorder(p):
    q = p.next
    while q != None:
        if p.val > q.val:
            return False
        p = p.next
        q = q.next
    return True


def isok(we, wy):
    if length(we) != length(wy):
        return False
    if list2set(we) != list2set(wy):
        return False
    return isorder(wy)


def runtests(f):
    OK = True
    for ls, k in TESTS:
        ll = makeList(ls)

        print("----------------------")
        print("inp = ", end='')
        printList(ll)

        res = f(ll, k)
        ll = makeList(ls)

        print("out = ", end='')
        printList(res)

        if not isok(ll, res):
            print("Blad!")
            OK = False
        else:
            print('OK')
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")
