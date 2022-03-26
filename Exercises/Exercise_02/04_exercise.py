# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prostokątów,
# rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego górnego
# rogu i prawego dolnego rogu. Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda
# rurami spłynęła do najniźszych pojemników). Proszę zaproponować algorytm Obliczający ile pojemników
# zostało w pełni zalanych.


def fill_containers(T, total_water):
    max_y = 0
    for i in range(len(T)):
        max_y = max(max_y, T[i][1])
    count_x = [0] * (max_y + 1)
    for i in range(len(T)):
        for j in range(T[i][3] + 1, T[i][1] + 1):
            count_x[j] += (T[i][2] - T[i][0])
    height = 0
    while total_water > 0:
        total_water -= count_x[height]
        height += 1
    if total_water != 0:
        height -= 1
    filled_containers = 0
    for i in range(len(T)):
        if T[i][1] <= height:
            filled_containers += 1
    return filled_containers


T = [(1, 3, 2, 5), (2, 4, 3, 1), (5, 6, 10, 4), (9, 7, 11, 0), (3, 8, 2, 3), (1, 1, 2, 2), (2, 1, 1, 3)]
print(fill_containers(T, 15))
