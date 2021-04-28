# Tankowanie czołgu
# L - pojemność baku czołgu (litry)
# Si - odległość stacji od punktu 0 (km)
# czołg spala 1 l/km
# Czołg startuje z pełnym bakiem. Obliczyć minimalną liczbę tankowań, żeby dotrzeć
# do punktu końcowego.


def tank_fueling(distance, fuel_tank, stops):
    refills = 0
    current_refill = 0
    limit = fuel_tank
    while limit < distance:
        if current_refill >= len(stops) or stops[current_refill] > limit:
            return False
        while current_refill < len(stops)-1 and stops[current_refill+1] <= limit:
            current_refill += 1
        refills += 1
        limit = stops[current_refill] + fuel_tank
        current_refill += 1
    return refills


distance = 21
fuel_tank = 5
stops = [2, 3, 5, 8, 11, 13, 17]
print(tank_fueling(distance, fuel_tank, stops))
