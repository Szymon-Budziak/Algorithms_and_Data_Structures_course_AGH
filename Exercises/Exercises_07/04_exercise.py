# Mamy dany zbiór zadań T = {t1 , ..., tn}. Każde zadanie t[i] dodatkowo posiada:
# (a) termin wykonania d(t[i]) (liczba naturalna) oraz (b) zysk g(t[i]) za wykonanie
# w terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli
# zadanie t[i] zostanie wykonane przed przekroczeniem swojego terminu d(t[i]), to dostajemy
# za nie nagrodę g(t[i]) (pierwsze wybrane zadanie jest wykonywane w chwili 0, drugie wybrane
# zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który
# prowadzi do maksymalnego zysku.


def job_sequencing(T, time_limit):
    T.sort(key=lambda x: x[2], reverse=True)
    jobs = [-1] * time_limit
    result = [-1] * time_limit
    max_profit = 0
    for i in range(len(T)):
        for j in range(T[i][1] - 1, -1, -1):
            if result[j] == -1 and j < len(T):
                result[j] = 1
                jobs[j] = T[i][0]
                max_profit += T[i][2]
                break
    for i in range(len(jobs)):
        if jobs[i] != -1:
            print(jobs[i], end=" ")
    print()
    return max_profit


def find_deadline(T):
    time_limit = 0
    for i in range(len(T)):
        if time_limit < T[i][1]:
            time_limit = T[i][1]
    return time_limit


T = [(1, 20, 2), (2, 15, 2), (3, 10, 1), (4, 5, 3), (5, 1, 3)]
deadline = find_deadline(T)
print(job_sequencing(T, deadline))
