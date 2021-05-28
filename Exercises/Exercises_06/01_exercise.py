# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las składa
# się z n drzew rosnących na pozycjach 0, ..., n-1. Dla każdego i {0, ..., n-1} znany
# jest zysk c[i], jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce
# uzyskać maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew
# pod rząd. Proszę zaproponować algorytm, dzięki któremu John znajdzie optymalny plan
# wycinki.


def deforestation(C):
    DP = [0]*len(C)
    DP[0] = C[0]
    DP[1] = max(C[0], C[1])
    for i in range(2, len(DP)):
        DP[i] = max(DP[i-2]+C[i], DP[i-1])
    return DP[-1]


C = [5, 1, 2, 4, 5, 9, 1, 3]
print(deforestation(C))
