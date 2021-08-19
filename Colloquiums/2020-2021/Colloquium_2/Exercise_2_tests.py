# Exercise_2_tests.py

G1 = [[1, 2],
      [0, 2],
      [0, 1]]
s1 = 0
t1 = 2
r1 = (0, 2)

G2 = [[1, 4],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
s2 = 0
t2 = 3
r2 = None

s3 = 0
t3 = 2
r3 = [(0, 1), (1, 2)]

G4 = [[1, 4, 3],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5, 0],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
s4 = 0
t4 = 2
r4 = None

TESTS = [(G1, s1, t1, r1),
         (G2, s2, t2, r2),
         (G2, s3, t3, r3),
         (G4, s4, t4, r4)
         ]


def runtests(f):
    OK = True
    for (G, s, t, r) in TESTS:
        print("----------------------")
        print("G: ", G)
        print("s: ", s)
        print("t: ", t)
        print("oczekiwany wynik: ", r)
        sol = f(G, s, t)
        print("uzyskany wynik  : ", sol)
        if not ((sol == r) or (sol in r)):
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")
