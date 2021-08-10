# Dany jest zbiór klocków K = [K1, ..., Kn]. Każdy klocek K[i] opisany jest jako jednostronnie
# domknięty przedział (a[i], b[i]], gdzie a[i], b[i] ∈ N, i ma wysokość 1 (należy założyć, że żadne
# dwa klocki nie zaczynają się w tym samym punkcie, czyli wartości a[i] są parami różne). Klocki
# są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający klocek dotyka innego klocka
# (powierzchnią poziomą), to jest do niego trwale doczepiany i przestaje spadać. Kolejność spadania
# klocków jest poprawna jeśli każdy klocek albo w całości ląduje na osi liczbowej, albo w całości
# ląduje na innych klockach. Rozważmy przykładowy zbiór klocków K = [K1, K2, K3, K4], gdzie:
# K1 = (2,4], K2 = (5,7], K3 = (3,6], K4 = (4,5].
# Kolejność K1, K4, K2, K3 jest poprawna (choć są też inne poprawne kolejności) podczas gdy
# kolejność K1, K2, K3, K4 poprawna nie jest (K3 nie leży w całości na innych klockach).
# Proszę podać algorytm, który sprawdza czy dla danego zbioru klocków istnieje poprawna kolejność
# spadania. Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność. Proszę także
# odpowiedzieć na następujące pytanie:
# Czy jeśli początki klocków nie muszą być parami różne to algorytm dalej działa poprawnie?
# Jeśli tak, proszę to uzasadnić. Jeśli nie, to proszę podać kontrprzykład.


def place_bricks(bricks, visited, full_range, height, result):
    check = False
    for i in range(len(bricks)):
        flag = True
        if not visited[i]:
            for j in range(bricks[i][0] + 1, bricks[i][1] + 1):
                if full_range[j] == height:
                    continue
                else:
                    flag = False
                    check = False
                    break
            if flag:
                for j in range(bricks[i][0] + 1, bricks[i][1] + 1):
                    full_range[j] = height + 1
                visited[i] = True
                check = True
                result.append(bricks[i][2])
    return check


def falling_blocks(bricks):
    for i in range(len(bricks)):
        bricks[i].append(i + 1)
    bricks.sort(key=lambda x: x[0])
    visited = [False] * len(bricks)
    max_range = 0
    for i in range(len(bricks)):
        max_range = max(max_range, bricks[i][1])
    full_range = [0] * (max_range + 1)
    height = 0
    result = []
    for i in range(len(bricks)):
        check = place_bricks(bricks, visited, full_range, height, result)
        if check:
            height += 1
    return result


bricks = [[2, 4], [5, 7], [3, 6], [4, 5]]
print(falling_blocks(bricks))
