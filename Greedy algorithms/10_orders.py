# We are given a list of orders. Each order requires some starting capital C[i] which we will need to
# start the order and a profit P[i] which will add to our total capital when we execute the order.
# We get a starting capital W and a number k. Choose at most k orders so that you will end up with the
# maximum possible capital.
# Example: k = 2, P = [1, 2, 3], C = [0, 1, 1]. Solution: at the beginning we have capital 0, so we can
# choose only the first order. After its completion, we have a capital equal to 1, so we can choose either
# order 2 or 3. Order 3 has a bigger profit, so we choose order 3 because we can only choose one
# order (k = 2). We finish with capital of 4.


def orders(P, C, k):
    for i in range(len(P)):
        P[i] = (P[i], C[i])
    P.sort(key=lambda x: x[0])
    max_capital = 0
    for i in range(len(P)):
        max_capital = max(max_capital, P[i][0])
    T = [0] * (max_capital + 1)
    for i in range(len(P)):
        T[P[i][0]] = max(T[P[i][0]], P[i][1])
    total_capital = 0
    for i in range(k):
        total_capital += T[i]
    return total_capital


k = 3
P = [2, 1, 3, 0, 1, 0, 4, 3, 1]
C = [7, 4, 0, 5, 8, 3, 2, 1, 3]
print(orders(P, C, k))
