# In one of the Chinese provinces, it was decided to build a series of machines to protect the
# population against the coronavirus. The province can be visualized as an array of values 1 and 0,
# which arr[i] = 1 means that in city [i] it is possible to build a machine and value 0 that it can't.
# There is also a number k, which means that if we put the machine in the city [i], then the cities with
# indices [j] such that that abs(i-j) < k are through it protected. Find the minimum number of machines
# are needed to provide security in each city, or -1 if that is impossible.


def machines_saving_people(T, k):
    count = 0
    distance = -1
    protected = distance + k
    while distance + k < len(T):
        if protected > len(T) - 1:
            protected = len(T) - 1
        while T[protected] == 0 and protected >= distance + 1:
            protected -= 1
        if protected == distance:
            return -1
        else:
            distance = protected
            protected += 2 * k - 1
            count += 1
    return count


T = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
k = 4
print(machines_saving_people(T, k))
