# Given train timetable as a list of tuples (arrival_time, departure_time). We want to know if our
# station which has n platforms is able to handle these trains without conflict (at the moment will
# not be "train competition" for available platforms).

def train_timetable(timetable, platform):
    timetable.sort(key=lambda x: x[0])
    i = j = count = result = 0
    while i < len(timetable):
        if timetable[i][0] < timetable[j][1]:
            count += 1
            result = max(result, count)
            if result > platform:
                return False
            i += 1
        else:
            count -= 1
            j += 1
    return True


timetable = [(2, 4), (1, 5), (6, 7), (3, 5), (5, 8), (6, 8)]
platform = 3
print(train_timetable(timetable, platform))
