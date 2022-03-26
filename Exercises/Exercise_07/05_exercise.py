# Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków o wagach w1 , ..., wn. Waga każdego
# z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków wagi mogą wynosić
# 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm który wybiera ładunki
# tak, że przyczepa jest możliwie maksymalnie zapełniona (ale bez przekraczania pojemności)
# i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się np. załadować przyczepę
# do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając jednego ładunku,
# to lepsze jest to pierwsze rozwiązanie).


def load_trailer(T, K):
    T.sort(reverse=True)
    count = 0
    for i in range(len(T)):
        if weights[i] <= K:
            count += 1
            K -= T[i]
    return count


weights = [2, 2, 4, 8, 1, 8, 16]
K = 27
print(load_trailer(weights, K))
