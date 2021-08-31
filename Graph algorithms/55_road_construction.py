# A country has n cities. Initially, there is no road in the country. One day, the king decides to
# construct some roads connecting pairs of cities. Roads can be traversed either way. He wants those
# roads to be constructed in such a way that it is possible to go from each city to any other city
# by traversing at most two roads. You are also given m pairs of cities — roads cannot be constructed
# between these pairs of cities. Our task is to construct the minimum number of roads that still satisfy
# the above conditions. The constraints will guarantee that this is always possible.


def road_construction(n, m, T):
    s = n - 1
    result = []
    for i in range(1, n + 1):
        if i in T:
            continue
        for j in range(1, n + 1):
            if i == j:
                continue
            result.append((i, j))
        break
    return s, result


n = 4
m = 1
T = [1, 3]
print(road_construction(n, m, T))
