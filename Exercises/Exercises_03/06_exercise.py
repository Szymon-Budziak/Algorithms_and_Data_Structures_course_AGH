# Dana jest tablica n liczb. Proszę zaproponować algorytm który stwierdza czy pewna liczba
# występuje w ciągu > (więcej niż) n/2 razy.


def leader(T):
    count = 1
    leader = T[0]
    for i in range(1, len(T)):
        if T[i] == leader:
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                leader = T[i]
                count = 1
    count = 0
    for i in range(len(T)):
        if T[i] == leader:
            count += 1
    if count > len(T) // 2:
        return leader
    return None


T = [2, 3, 2, 4, 5, 2, 2, 1, 5, 2, 2]
print(leader(T))
