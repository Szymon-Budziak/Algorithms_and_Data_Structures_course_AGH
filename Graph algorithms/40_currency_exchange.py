# There is a list of triples on the boards in the exchange office (currency_1, currency_2, exchange_rate).
# Each of those triples means that exchange office will buy n of currency_2 at the rate of
# n*currency_1.
#   1) Find the most advantageous sequence for converting currency A to currency B.
#   2) Is there such a sequence of currency exchange that starts and ends in the same currency and
# we ends up with more money than we started?


def relax(currencies, cost, parent, j):
    if cost[currencies[j][1]] < currencies[j][2] * cost[currencies[j][0]]:
        cost[currencies[j][1]] = currencies[j][2] * cost[currencies[j][0]]
        parent[currencies[j][1]] = currencies[j][0]


def currency_exchange(currencies, currency_a, currency_b):
    E = len(currencies)
    max_vertex = 0
    for i in range(len(currencies)):
        max_vertex = max(max_vertex, currencies[i][0], currencies[i][1])
    E = len(currencies)
    cost = [0] * (max_vertex + 1)
    parent = [None] * (max_vertex + 1)
    cost[currency_a] = 1
    for i in range(max_vertex - 1):
        for j in range(E):
            relax(currencies, cost, parent, j)
    exchange = []
    while currency_b is not None:
        if exchange.count(currency_b) >= 1:
            exchange.append(currency_b)
            break
        exchange.append(currency_b)
        currency_b = parent[currency_b]
    exchange.reverse()
    currency = []
    for i in range(len(parent)):
        if parent[i] in currency:
            return True, exchange
        currency.append(parent[i])
    return False, exchange


currencies = [(0, 1, 4.5),
              (0, 2, 4),
              (2, 0, 0.25),
              (1, 2, 0.75),
              (3, 2, 100),
              (0, 3, 0.4),
              (1, 4, 6),
              (3, 4, 2)]

currency_a = 0
currency_b = 4
print(currency_exchange(currencies, currency_a, currency_b))
