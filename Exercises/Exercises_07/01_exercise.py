# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to dokładnie jeden litr paliwa na jeden kilometr
# trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A do B to prosta, na której znajdują się
# stacje benzynowe (na pozycjach będących liczbami naturalnymi; A jest na pozycji 0). Proszę podać
# algorytmy dla następujących przypadków:
#     1. Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.


def tank_fueling(distance, fuel_tank, stops):
    refills = 0
    current_refill = 0
    limit = fuel_tank
    while limit < distance:
        if current_refill >= len(stops) or stops[current_refill] > limit:
            return False
        while current_refill < len(stops) - 1 and stops[current_refill + 1] <= limit:
            current_refill += 1
        refills += 1
        limit = stops[current_refill] + fuel_tank
        current_refill += 1
    return refills


distance = 21
fuel_tank = 5
stops = [2, 3, 5, 8, 11, 13, 17]
print(tank_fueling(distance, fuel_tank, stops))
