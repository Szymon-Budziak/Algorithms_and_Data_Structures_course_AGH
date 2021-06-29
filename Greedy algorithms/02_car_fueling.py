# We are given the distance which is the distance in km to covered by a car on a single road.
# We are also give stops that are gas station and total capacity of the fuel tank. Each station
# is defined by its distance from point 0 i.e. s is the distance between the [i]-th station
# and point 0. Find algorithm that will calculate the minimum number of refills (number of
# stations the car must stop at) on the entire route.


def car_fueling(distance, full_tank, stops):
    refills = 0
    current_refill = 0
    limit = full_tank
    while limit < distance:
        if current_refill >= len(stops) or stops[current_refill] > limit:
            return False
        while current_refill < len(stops) - 1 and stops[current_refill + 1] <= limit:
            current_refill += 1
        refills += 1
        limit = stops[current_refill] + full_tank
        current_refill += 1
    return refills


distance = 950
full_tank = 400
stops = [200, 375, 550, 750]
print(car_fueling(distance, full_tank, stops))
