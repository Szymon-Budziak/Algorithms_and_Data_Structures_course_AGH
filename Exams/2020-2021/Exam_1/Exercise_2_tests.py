tests = [
    {
        'L':  # 0123456789
            ["XXXXXXXXXX",  # 0
             "X X      X",  # 1
             "X XXXXXX X",  # 2
             "X        X",  # 3
             "XXXXXXXXXX",  # 4
             ],
        'A': (1, 1),
        'B': (8, 3),
        'sol': 440
    },
    {
        'L':  # 0123456789
            ["XXXXXXXXXX",  # 0
             "X        X",  # 1
             "X XXXXXX X",  # 2
             "X XXXXXX X",  # 3
             "X        X",  # 4
             "XXXXXXXXXX",  # 5
             ],
        'A': (1, 1),
        'B': (8, 4),
        'sol': 425
    },
    {
        'L':  # 0123456789
            ["XXXXXXXXXX",  # 0
             "X        X",  # 1
             "X  XXXXXXX",  # 2
             "X        X",  # 3
             "X XXXXXX X",  # 4
             "X        X",  # 5
             "XXXXXXXXXX",  # 6
             ],
        'A': (1, 1),
        'B': (8, 4),
        'sol': 545
    },
    {
        'L':  # 01234567890123456789
            ["XXXXXXXXXXXXXXXXXXXX",  # 0
             "X      X           X",  # 1
             "X    X     X    X  X",  # 2
             "X X     X          X",  # 3
             "X   X       X     XX",  # 4
             "XX       X     X   X",  # 5
             "X    X       X     X",  # 6
             "X         X        X",  # 7
             "X     X       X    X",  # 8
             "XXXXXXXXXXXXXXXXXXXX",  # 9
             ],
        'A': (1, 1),
        'B': (18, 8),
        'sol': 1165
    },
    {
        'L':  # 01234567890123456789
            ["XXXXXXXXXXXXXXXXXXXX",  # 0
             "X      X           X",  # 1
             "X    X     X    X  X",  # 2
             "X X     X          X",  # 3
             "X   X       X     XX",  # 4
             "XX       X     X   X",  # 5
             "X    X       X     X",  # 6
             "X         X       XX",  # 7
             "X     X       X  X X",  # 8
             "XXXXXXXXXXXXXXXXXXXX",  # 9
             ],
        'A': (1, 1),
        'B': (18, 8),
        'sol': None
    },
    {  # 111111111122222222223333333333
        'L':  # 0123456789012345678901234567890123456789
            ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 0
             "X                                      X",  # 1
             "X                                      X",  # 2
             "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 3
             "X                                      X",  # 4
             "X                                      X",  # 5
             "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX",  # 6
             "X                                      X",  # 7
             "X                                      X",  # 8
             "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 9
             "X                                      X",  # 10
             "X                                      X",  # 11
             "X        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 12
             "X                                      X",  # 13
             "X                                      X",  # 14
             "X                                      X",  # 15
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X",  # 16
             "X                                      X",  # 17
             "X                                      X",  # 18
             "X                                      X",  # 19
             "X                                      X",  # 20
             "X                                      X",  # 21
             "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 22
             "X                                      X",  # 23
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X",  # 24
             "X                                      X",  # 25
             "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 26
             "X                                      X",  # 27
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 28
             ],
        'A': (1, 27),
        'B': (38, 1),
        'sol': 6580
    },
    {  # 111111111122222222223333333333
        'L':  # 0123456789012345678901234567890123456789
            ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 0
             "X  X     X     X                    X  X",  # 1
             "X X  X  X     X                     XXXX",  # 2
             "X   X  X  X  X  XXXXXXX     X     X    X",  # 3
             "X  X  X  X  X  X       X     X     X   X",  # 4
             "X X  X  X  X  X         X     X     X  X",  # 5
             "XX  X  X  X  X           X     X       X",  # 6
             "X  X  X  X  X             X     X      X",  # 7
             "X    X  X  X               X     X     X",  # 8
             "X   X  X  X                 X     X    X",  # 9
             "X  X  X  X                   X     X   X",  # 10
             "X X  X  X                     X     X  X",  # 11
             "XX  X  X       XXXXXXX         X       X",  # 12
             "X  X  X       X       X         X      X",  # 13
             "X X  X       X         X         X     X",  # 14
             "X   X       X           X         X    X",  # 15
             "X  X       X             X         X   X",  # 16
             "X X       X               X         X  X",  # 17
             "XX       X                 X         X X",  # 18
             "X       X                   X          X",  # 19
             "X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 20
             "X X     X     X     X     X     X    X X",  # 21
             "X          X               XXXX        X",  # 22
             "X         X X      XXXX    X   X       X",  # 23
             "X        X   X    X        X   X       X",  # 24
             "X       XXXXXXX    XXXX    X   X       X",  # 25
             "X      X       X       X   XXXX        X",  # 26
             "X                  XXXX                X",  # 27
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 28
             ],
        'A': (1, 1),
        'B': (38, 27),
        'sol': 14060
    }

]


def runtests(f):
    errors = 0
    for t in tests[:]:
        L = t['L']
        A = t['A']
        B = t['B']
        S = t['sol']

        for i in range(len(L)):
            print(L[i])
        print("A :", A)
        print("B :", B)
        print("oczekiwany wynik :", S)

        R = f(L, A, B)

        print("Uzyskany wynik   :", R)

        if R != S:
            print("Problem! Błędny wynik!")
            errors += 1
            continue

    print("===============================")
    if errors == 0:
        print('Wszystko OK!')
    else:
        print("Problemy!")
        print("Niezaliczone testy :", errors)
