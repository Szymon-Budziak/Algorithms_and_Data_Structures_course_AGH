# Dane są lampki o numerach od 0 do n-1. Każda z nich może świecić na zielono, czerwono lub niebiesko
# i ma jeden przełącznik, który zmienia jej kolor (z zielonego na czerwony, z czerwonego na niebieski
# i z niebieskiego na zielony). Początkowo wszystkie lampki świecą na zielono. Operacja (a, b) oznacza
# "wciśnięcie przełącznika na każdej z lampek o numerach od a do b". Wykonanych będzie m operacji.
# Proszę napisać funkcję:
# def lamps(n, L):
#     ...
# która mając daną liczbę n lampek oraz listę L operacji (wykonywanych w podanej kolejności) zwraca
# ile maksymalnie lampek świeciło się na niebiesko (lampki są liczone na początku i po wykonaniu
# każdej operacji).
from Exercise_3_tests import runtests


def lamps(n, T):
    all_lamps = [0] * n
    max_blue = actual_blue = 0
    for i in range(len(T)):
        for j in range(T[i][0], T[i][1] + 1):
            if all_lamps[j] == 0:
                all_lamps[j] = 1
            elif all_lamps[j] == 1:
                all_lamps[j] = 2
                actual_blue += 1
            elif all_lamps[j] == 2:
                all_lamps[j] = 0
                actual_blue -= 1
        max_blue = max(max_blue, actual_blue)
    return max_blue


runtests(lamps)
