# Exercise_1_tests.py

x1 = [0, 2, 1.1, 2]
k1 = 1

x2 = [42]
k2 = 0

x3 = [2, 1]
k3 = 1

x4 = [5, 1, 2, 3, 4]
k4 = 4

x5 = [5, 4, 3, 2, 1]
k5 = 4

x6 = [10e22, 1, 10e-16, 100]
k6 = 3

x7 = [1, 1, 1, 1, 1]
k7 = 0

x8 = [1, 2, 1, 2, 1, 2]
k8 = 2

TESTS = [
    (x1, k1),
    (x2, k2),
    (x3, k3),
    (x4, k4),
    (x5, k5),
    (x6, k6),
    (x7, k7),
    (x8, k8)
]


def runtests(f):
    OK = True
    print("hi")
    for x, k in TESTS:
        print("--------")
        print("x = ", x)

        RESULT = f(x)
        print("oczekiwana odpowiedź: k =", k)
        print("uzyskana   odpowiedź: k =", RESULT)
        if RESULT != k:
            OK = False
            print("Problem!")

    if OK:
        print("OK!")
    else:
        print("Problemy!")
