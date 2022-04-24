P1 = ([(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)], 6)
R1 = [0, 1]

P2 = ([(8, 2, 6, 2), (9, 4, 8, 5), (9, 8, 9, 2), (3, 10, 15, 1), ], 7)
R2 = [0, 2, 3]

P3 = ([(7, 23, 24, 1), (2, 10, 14, 3), (7, 17, 22, 1), (9, 20, 22, 2), (4, 19, 22, 8), (2, 2, 6, 1)], 10)
R3 = [0, 1, 2, 5]

P4 = ([(1, 8, 12, 5), (4, 7, 8, 2), (3, 2, 3, 6), (9, 7, 8, 5), (8, 21, 22, 8), (5, 4, 7, 10), (1, 21, 24, 10),
       (7, 14, 16, 1)], 32)
R4 = [0, 2, 4, 5, 7]

TESTS = [(P1, R1),
         (P2, R2),
         (P3, R3),
         (P4, R4)]


def runtests(f):
    OK = True
    for (P, R) in TESTS:
        print("----------------------")
        print("P =", P)
        res = f(P[0], P[1])

        w = s = 0
        for a in range(len(res)):
            w += P[0][res[a]][3]
            s += P[0][res[a]][0] * (P[0][res[a]][2] - P[0][res[a]][1])
        print("otrzymany wynik  =", res, 'wart =', w, 'stud =', s)

        w = s = 0
        for a in range(len(R)):
            w += P[0][R[a]][3]
            s += P[0][R[a]][0] * (P[0][R[a]][2] - P[0][R[a]][1])
        print("oczekiwany wynik =", R, 'wart =', w, 'stud =', s)

        if res != R:
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")
