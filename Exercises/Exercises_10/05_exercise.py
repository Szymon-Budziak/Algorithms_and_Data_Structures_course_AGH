# Dana jest tabela kursów walut. Dla każdych dwóch walut 'x' oraz 'y' wpis K[x][y] oznacza ile trzeba
# zapłacić waluty 'x' żeby otrzymać jednostkę waluty 'y'. Proszę zaproponować algorytm, który sprawdza
# czy istnieje taka waluta 'z', że za jednostkę 'z' można uzyskać więcej niż jednostkę 'z' przez serię
# wymian walut.


def relax(currencies, cost, parent, j):
    if cost[currencies[j][1]] < currencies[j][2] * cost[currencies[j][0]]:
        cost[currencies[j][1]] = currencies[j][2] * cost[currencies[j][0]]
        if currencies[j][0] == parent[currencies[j][1]]:
            parent[currencies[j][1]] = currencies[j][0]
            return True
        parent[currencies[j][1]] = currencies[j][0]
    return False


def currency_exchange(currencies, ):
    max_vertex = 0
    for i in range(len(currencies)):
        max_vertex = max(max_vertex, currencies[i][0], currencies[i][1])
    E = len(currencies)
    cost = [0] * (max_vertex + 1)
    parent = [None] * (max_vertex + 1)
    cost[0] = 1
    for i in range(max_vertex - 1):
        for j in range(E):
            if i != 0:
                if relax(currencies, cost, parent, j):
                    return True
            else:
                relax(currencies, cost, parent, j)
    return False


currencies = [(0, 1, 4.5),
              (0, 2, 4),
              (2, 0, 0.25),
              (1, 2, 0.75),
              (3, 2, 100),
              (0, 3, 0.4),
              (1, 4, 6),
              (3, 4, 2)]
print(currency_exchange(currencies))
