T1 = [[1, 2], [3, 4]]
T2 = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
T3 = [[2, 5, 2, 5], [2, 5, 5, 2], [2, 5, 2, 2], [2, 5, 5, 5]]
T4 = [[43, 74, 53, 97], [80, 61, 61, 19], [61, 73, 89, 93], [42, 17, 89, 80]]

TESTS = [T1, T2, T3, T4]


def isok(T):
    N = len(T)
    for r in range(1, N):
        for c in range(r):
            for d in range(N):
                if T[r][c] > T[d][d]:
                    return False
                if T[c][r] < T[d][d]:
                    return False
    return True


def printT(T):
    for row in T:
        print(row)
    print()


def runtests(f):
    OK = True
    for T in TESTS:
        print("----------------------")
        print("Dane:")
        printT(T)
        f(T)
        print("Wynik:")
        printT(T)

        if not isok(T):
            print("Blad!")
            OK = False
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")
