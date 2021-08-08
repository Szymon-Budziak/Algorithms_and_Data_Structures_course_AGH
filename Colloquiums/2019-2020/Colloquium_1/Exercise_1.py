# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna
# to taka, która w liczbie występuje więcej niż jeden raz. Mówimy, że liczba naturalna A jest
# ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B,
# a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr
# wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od
# 114577, a liczby 2344 i 67333 są jednakowo ładne. Dana jest tablica T zawierająca liczby naturalne.
# Proszę zaimplementować funkcję: pretty_sort(T), która sortuje elementy tablicy T od najładniejszych
# do najmniej ładnych. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu
# umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.


def convert_number(number):
    actual_number = number
    digits = [0] * 10
    while number > 0:
        digits[number % 10] += 1
        number //= 10
    single = multiple = 0
    for i in range(10):
        if digits[i] == 1:
            single += 1
        elif digits[i] > 1:
            multiple += 1
    return actual_number, single, multiple


def counting_sort(T, idx):
    count = [0] * 10
    result = [0] * len(T)
    for i in range(len(T)):
        count[T[i][idx]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    j = len(T) - 1
    while j >= 0:
        result[count[T[j][idx]] - 1] = T[j]
        count[T[j][idx]] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = result[i]
    T.reverse()


def pretty_sort(T):
    for i in range(len(T)):
        T[i] = convert_number(T[i])
    # We go through the array nd convert number. If length of number is k
    # the complexity of this operation is O(k*n)
    single_index = 1
    multiple_index = 2
    counting_sort(T, multiple_index)
    counting_sort(T, single_index)
    for i in range(len(T)):
        T[i] = T[i][0]
    # We go through the array and replace element of original array with
    # the element from additional A list
    # Total complexity of algorithm should be O(n*k) + O(n)
    return T


T = [123, 455, 1266, 114577, 2344, 6733]
print(pretty_sort(T))
